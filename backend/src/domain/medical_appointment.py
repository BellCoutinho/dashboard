class MedicalAppointment:
    def __init__(self, date, time, medical_notes):
        self.date = date
        self.time = time
        self.medical_notes = medical_notes

    def __str__(self):
        return f'MedicalAppointment({self.date}, {self.time}, {self.medical_notes})'

    def __repr__(self):
        return self.__str__()
