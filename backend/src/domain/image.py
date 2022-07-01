class Image:
    def __init__(self, filename, date, image64):
        self.filename = filename
        self.date = date,
        self.image64 = image64
    def __str__(self):
        return f'Image({self.filename}, {self.date}, {self.image64})'

