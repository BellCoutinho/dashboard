from datetime import date
from flask import Blueprint, request, jsonify
from src.infra.db.postgres import postgres_connection
from src.infra.db.config import Db
from src.domain.patient import Patient
from src.domain.image import Image
import src.repository.patient_repository as repository
import src.repository.image_repository as image_repository
import json
import base64
import os

patient_bp = Blueprint('patient', __name__, url_prefix='/patient')

@patient_bp.post('/register')
def register():
    if not request.is_json:
        return jsonify({'msg': 'invalid input'})

    patient = Patient(name = request.json.get('name'),
                      phone_number = request.json.get('phone_number'),
                      cpf = request.json.get('cpf'))
    for key, value in patient.__dict__.items():
        if not value:
            return jsonify({'msg': f'Missing {key} parameter'})

    repository.save(patient)
    return jsonify({'msg': 'Successfully registered'})

@patient_bp.get('/find')
def find_all():
    patients = repository.find_all()
    if len(patients) == 0:
        return jsonify({'msg': 'Patient not found'})
    result = []
    for patient in patients:
        result.append({
            'id': patient[0],
            'name': patient[1],
            'phone_number': patient[2],
            'cpf': patient[3]
        })
    return jsonify(result)


@patient_bp.get('/find/<id>')
def find_one(id):
    if not id and id < 0:
        return jsonify({'msg': 'invalid input'})

    patient = repository.find_by_id(id)

    if not patient:
        return jsonify({'msg': 'Patient not found'})

    return jsonify({
        'id': patient[0],
        'name': patient[1],
        'phone_number': patient[2],
        'cpf': patient[3]
    })

@patient_bp.put('/update/<id>')
def update(id):
    if not id and id < 0:
        return jsonify({'msg': 'invalid id'})
    if not request.is_json:
        return jsonify({'msg': 'invalid input'})

    patient = repository.find_by_id(id)

    if not patient:
        return jsonify({'msg': 'Patient not found'})

    patient_updated = Patient(name = request.json.get('name'),
                              phone_number = request.json.get('phone_number'),
                              cpf = request.json.get('cpf'))
    for i, (key, value) in enumerate(patient_updated.__dict__.items()):
        if not value:
            setattr(patient_updated, key, patient.index(i))
            continue
        setattr(patient_updated, key, value)
    repository.update(patient_updated, id)
    return json.dumps(patient_updated.__dict__)


@patient_bp.delete('/delete/<id>')
def delete(id):
    if not id and id < 0:
        return jsonify({'msg': 'invalid input'})

    patient = repository.exists_by_id(id)
    if not patient:
        return jsonify({'msg': 'Patient not found'})

    repository.delete(id)
    return jsonify({'msg': 'Successfully deleted'})


@patient_bp.get('/exists/<id>')
def exists(id):
    if not id and id < 0:
        return jsonify({'msg': 'invalid input'})

    patient = repository.exists_by_id(id)
    if not patient:
        return jsonify({'msg': 'Patient not found'})

    return jsonify({'msg': 'Patient found'})

@patient_bp.post('/image/<id>')
def register_encoded_image(id):
    if not id and id < 0:
        return jsonify({'msg': 'invalid input'})

    if not request.is_json:
        return jsonify({'msg': 'invalid input'})

    patient = repository.exists_by_id(id)
    if not patient:
        return jsonify({'msg': 'Patient not found'})

    image = Image(filename = request.json.get('filename'),
                  date = date.today(),
                  image64 = request.json.get('image64'))

    for key, value in image.__dict__.items():
        if not value:
            return jsonify({'msg': f'Missing {key} parameter'})

    image_repository.save(image, id)
    return jsonify({'msg': 'Successfully registered'})

@patient_bp.get('/image/find/<id>')
def find_last_image(id):
    if not id and id < 0:
        return jsonify({'msg': 'invalid input'})

    patient = repository.exists_by_id(id)
    if not patient:
        return jsonify({'msg': 'Patient not found'})

    image = image_repository.find_last(id)

    if not image:
        return jsonify({'msg': 'Image not found'})

    return json.dumps({
        'id': image[0],
        'filename': image[1],
        'date': image[2],
        'image64': image[3]
    }, default=str)

@patient_bp.get('/image/findall/<id>')
def find_all_image(id):
    if not id and id < 0:
        return jsonify({'msg': 'invalid input'})

    patient = repository.exists_by_id(id)
    if not patient:
        return jsonify({'msg': 'Patient not found'})

    images = image_repository.find_all(id)

    if len(images) == 0:
        return jsonify({'msg': 'Image not found'})

    result = []
    for image in images:
        result.append({
            'id': image[0],
            'filename': image[1],
            'date': image[2],
            'image64': image[3]
        })
    return jsonify(result)


    #return json.dumps({
    #    'id': image[0],
    #    'filename': image[1],
    #    'date': image[2],
    #    'image64': image[3]
    #}, default=str)

@patient_bp.get('/image/processing/<id>')
def image_processing(id):
    with open(os.getcwd() + 'siamese.jpg', 'rb') as f:
        image64 = base64.b64encode(f.read())

    return json.dumps({
        'id': image['id'],
        'filename': image['filename'],
        'date': image['date'],
        'image64': str(image64)
    }, default=str)
