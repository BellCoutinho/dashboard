from datetime import datetime, date

from flask import Flask

from src.domain.patient import Patient
from src.domain.medical_record import MedicalRecord
from src.domain.doctor import Doctor
from src.domain.medical_appointment import MedicalAppointment
#from src.controller.patient_controller import register
from src.infra.db.postgres import postgres_connection, create_entities
from src.controller.patient_controller import patient_bp
from src.controller.doctor_controller import doctor_bp
from src.controller.medical_record_controller import medical_record_bp
from werkzeug.exceptions import BadRequest

def handle_bad_request(e):
    print(e)
    return 'bad request!', 400

def main():
    app = Flask(__name__)
    app.register_blueprint(patient_bp)
    app.register_blueprint(doctor_bp)
    app.register_blueprint(medical_record_bp)
    app.register_error_handler(400, handle_bad_request)
    return app

if __name__ == '__main__':
    create_entities()
    main().run()
    #bell = Patient('Bell', '88559092', '70532017404')
    #doctor = Doctor('CARLOS ALBERTO MAGNO BACALHAO', '1560-PB')
    #bell_medical_appointment1 = MedicalAppointment(
    #   date.today(),
    #  datetime.now().strftime("%H:%M:%S"),
    #    """
    #    Paciente recorre ao P.A relatando hematoquezia
    #    (Sangue vivo), no mês de julho sem dor associada e nenhuma irradiação.
    #    Não aumentava ou diminuía o volume de acordo com a alimentação, essa
    #    hematoquezia era constante. Além disso, não havia fator de melhora ou de
    #    piora desse sangramento. Paciente relata não ter reparado outras
    #    alterações nas regiões anal e pélvica durante esse tempo. Atualmente, se
    #    encontra internado para receber quimioterapia por um câncer de
    #    colorretal.
    #    """)
    #bell_medical_appointment2 = MedicalAppointment(
    #    date.today(),
    #    datetime.now().strftime("%H:%M:%S"),
    #    """
    #    Relata HAS, Nega Dm e alergias.  Nega outros procedimentos prévios e 
    #    outras internações anteriores à essa.
    #    """)
    #bell_medical_record =  MedicalRecord(bell, doctor, [bell_medical_appointment1, bell_medical_appointment2])
    #print(bell)
    #print(bell_medical_record)
    #print(doctor)
    #print(bell_medical_appointment1)
    #print(bell_medical_appointment2)

