class Patient:

    def __init__(self, name, phone_number, cpf):
        self.name = name
        self.phone_number = phone_number
        self.cpf = cpf

    def __str__(self):
        return f'Patient({self.name},{self.phone_number},{self.cpf})'

