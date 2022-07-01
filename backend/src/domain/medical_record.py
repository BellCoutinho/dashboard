
class MedicalRecord:

    def __init__(self, date, time, medical_notes, doctor, patient):
        self.date = date
        self.time = time
        self.medical_notes = medical_notes
        self.doctor = doctor
        self.patient = patient

    def __str__(self):
        return f'MedicalRecord({self.date},{self.time},{self.patient},{self.doctor})'

