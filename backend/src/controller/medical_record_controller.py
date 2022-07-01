from datetime import datetime, date
from flask import Blueprint, request, jsonify
from src.infra.db.postgres import postgres_connection
from src.infra.db.config import Db
from src.domain.medical_record import MedicalRecord
import src.repository.medical_record_repository as repository
import json

medical_record_bp = Blueprint('medical_record', __name__, url_prefix='/record')

@medical_record_bp.post('/register')
def register():
    if not request.is_json:
        return jsonify({'msg': 'invalid input'})
    medical_record = MedicalRecord(date = date.today(),
                                   time = datetime.now().strftime("%H:%M:%S"),
                                   medical_notes = request.json.get('medical_notes'),
                                   doctor = request.json.get('doctor'),
                                   patient = request.json.get('patient'))

    for key, value in medical_record.__dict__.items():
        if not value:
            return jsonify({'msg': f'Missing {key} parameter'})

    repository.save(medical_record)
    return jsonify({'msg': 'Success register'})

@medical_record_bp.get('/find/<id>')
def find_one(id):
    if not id and id < 0:
        return jsonify({'msg': 'invalid id'})
    medical_record = repository.find_by_id(id)

    if not medical_record:
        return jsonify({'msg': 'Medical record not found'})

    return json.dumps(medical_record, default=str)

@medical_record_bp.get('/find/patient/<id>')
def find_one_by_patient(id):
    if not id and id < 0:
        return jsonify({'msg': 'invalid id'})
    medical_record = repository.find_by_patient_id(id)

    if not medical_record:
        return jsonify({'msg': 'Medical record not found'})

    print(medical_record)
    return json.dumps({
        'id':  medical_record[0],
        'date': medical_record[1],
        'time': medical_record[2],
        'medical_notes': medical_record[3]
    }, default=str)


@medical_record_bp.get('/find')
def find_all():
    result = repository.find_all()
    if len(result) == 0:
        return jsonify({'msg':'Medical record not found'})
    return json.dumps(result, default=str)

@medical_record_bp.put('/update/<id>')
def update(id):
    if not id and id < 0:
        return jsonify({'msg': 'invalid id'})
    if not request.is_json:
        return jsonify({'msg': 'invalid input'})
    medical_record = repository.find_by_id(id)
    if not medical_record:
        return jsonify({'msg': 'Medical record not fond'})
    record_updated = MedicalRecord(date = request.json.get('date'),
                                   time = request.json.get('time'),
                                   medical_notes = request.json.get('medical_notes'),
                                   doctor = request.json.get('doctor'),
                                   patient = request.json.get('patient'))
    for i, (key, value) in enumerate(record_updated.__dict__.items()):
        if not value:
            setattr(record_updated, key, medical_record[i+1])
            continue
        setattr(record_updated, key, value)
    repository.update(record_updated, id)
    return json.dumps(record_updated.__dict__, default=str)

@medical_record_bp.get('/exists/<id>')
def exists(id):
    if not id and id < 0:
        return jsonify({'msg': 'invalid id'})
    medical_record = repository.exists_by_id(id)
    if not medical_record[0]:
        return jsonify({'msg': 'Medical record not found'})
    return jsonify({'msg': 'Medical record found'})

@medical_record_bp.delete('/delete/<id>')
def delete(id):
    if not id and id < 0:
        return jsonify({'msg': 'invalid id'})
    medical_record = repository.exists_by_id(id)
    if not medical_record[0]:
        return jsonify({'msg': 'Doctor not found'})
    repository.delete(id)
    return jsonify({'msg': 'Successfully delete'})


