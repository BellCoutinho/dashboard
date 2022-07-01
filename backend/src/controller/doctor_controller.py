from flask import Blueprint, request, jsonify
from src.infra.db.postgres import postgres_connection
from src.infra.db.config import Db
from src.domain.doctor import Doctor
import src.repository.doctor_repository as repository
import json


doctor_bp = Blueprint('doctor', __name__, url_prefix='/doctor')

@doctor_bp.post('/register')
def register():
    if not request.is_json:
        return jsonify({'msg': 'invalid input'})
    doctor = Doctor(
        name = request.json.get('name'),
        crm = request.json.get('crm'))
    for key, value in doctor.__dict__.items():
        if not value:
            return jsonify({'msg': f'Missing {key} parameter'})

    repository.save(doctor)
    return jsonify({'msg': 'Success register'})

@doctor_bp.get('/find/<id>')
def find_one(id):
    if not id and id < 0:
        return jsonify({'msg': 'invalid input'})
    doctor = repository.find_by_id(id)

    if not doctor:
        return jsonify({'msg': 'Doctor not fond'})

    return jsonify(doctor)

@doctor_bp.get('/find/patient/<id>')
def find_one_by_patient(id):
    if not id and id < 0:
        return jsonify({'msg': 'invalid input'})
    doctor = repository.find_by_patient_id(id)

    if not doctor:
        return jsonify({'msg': 'Doctor not fond'})

    return jsonify({
        'id': doctor[0],
        'name': doctor[1],
        'crm': doctor[2]
    })


@doctor_bp.get('/find')
def find_all():
    result = repository.find_all()
    if len(result) == 0:
        return jsonify({'msg':'Doctor not fount'})
    return json.dumps(result)


@doctor_bp.put('/update/<id>')
def update(id):
    if not id and id < 0:
        return jsonify({'msg': 'invalid id'})
    if not request.is_json:
        return jsonify({'msg': 'invalid input'})
    doctor = repository.find_by_id(id)
    if not doctor:
        return jsonify({'msg': 'Doctor not found'})
    doctor_updated = Doctor(name = request.json.get('name'),
                            crm = request.json.get('crm'))
    for i, (key, value) in enumerate(doctor_updated.__dict__.items()):
        if not value:
            setattr(doctor_updated, key, doctor.index(i))
            continue
        setattr(doctor_updated, key, value)
    repository.update(doctor_updated, id)

    return json.dumps(doctor_updated.__dict__)

@doctor_bp.get('/exists/<id>')
def exists(id):
    if not id and id < 0:
        return jsonify({'msg': 'invalid id'})
    doctor = repository.exists_by_id(id)
    if not doctor[0]:
        return jsonify({'msg': 'Doctor not found'})
    return jsonify({'msg': 'Doctor found'})

@doctor_bp.delete('/delete/<id>')
def delete(id):
    if not id and id < 0:
        return jsonify({'msg': 'invalid id'})
    doctor = repository.exists_by_id(id)
    if doctor[0] == False:
        return jsonify({'msg': 'Doctor not found'})
    repository.delete(id)
    return jsonify({'msg': 'Successfully delete'})


