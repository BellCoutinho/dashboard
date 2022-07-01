class Doctor:
    def __init__(self, name, crm):
        self.name = name
        self.crm = crm

    def __str__(self):
        return f'Doctor({self.name}, {self.crm})'
