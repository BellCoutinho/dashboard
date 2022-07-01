import requests
import base64

payload = {"name":"Natália Giovanna Bárbara Fernandes", "phone_number": "996073355", "cpf":"92753242712"}
requests.post('http://localhost:5000/patient/register', json=payload)


payload = {"name":"João Theo Renato Almeida", "phone_number": "992399207", "cpf":"83717972650"}
requests.post('http://localhost:5000/patient/register', json=payload)

payload = {"name":"Diego Yago Nelson Pires", "phone_number": "991953049", "cpf":"07610818011"}
requests.post('http://localhost:5000/patient/register', json=payload)


payload = {"name":"Dra. Mariáh Grossi", "crm":"SP161352"}
requests.post('http://localhost:5000/doctor/register', json=payload)

payload = {"name":"Ruan Carlos Lopes Cavalcante", "crm":"PA8970"}
requests.post('http://localhost:5000/doctor/register', json=payload)

payload = {"medical_notes":"""Paciente recorre ao P.A relatando hematoquezia
(Sangue vivo), no mês de julho sem dor associada e nenhuma irradiação.
Não aumentava ou diminuía o volume de acordo com a alimentação, essa
hematoquezia era constante. Além disso, não havia fator de melhora ou de
piora desse sangramento. Paciente relata não ter reparado outras
alterações nas regiões anal e pélvica durante esse tempo. Atualmente, se
encontra internado para receber quimioterapia por um câncer de
colorretal.""", "doctor": 1, "patient": 1}
requests.post('http://localhost:5000/record/register', json=payload)


payload = {"medical_notes":"""Paciente recorre ao P.A relatando hematoquezia
(Sangue vivo), no mês de julho sem dor associada e nenhuma irradiação.
Não aumentava ou diminuía o volume de acordo com a alimentação, essa
hematoquezia era constante. Além disso, não havia fator de melhora ou de
piora desse sangramento. Paciente relata não ter reparado outras
alterações nas regiões anal e pélvica durante esse tempo. Atualmente, se
encontra internado para receber quimioterapia por um câncer de
colorretal.""", "doctor": 1, "patient": 1}
requests.post('http://localhost:5000/record/register', json=payload)


with open('./store/inu1.jpg', 'rb') as f:
    image64 = base64.b64encode(f.read())

payload = {'filename': 'inu1.jpg', 'image64': str(image64)}
requests.post('http://localhost:5000/patient/image/1', json=payload)

with open('./store/inu2.jpg', 'rb') as f:
    image64 = base64.b64encode(f.read())

payload = {'filename': 'inu2.jpg', 'image64': str(image64)}
requests.post('http://localhost:5000/patient/image/1', json=payload)

with open('./store/inu3.jpg', 'rb') as f:
    image64 = base64.b64encode(f.read())

payload = {'filename': 'inu3.jpg', 'image64': str(image64)}
requests.post('http://localhost:5000/patient/image/1', json=payload)
