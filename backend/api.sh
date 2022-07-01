#!/bin/bash

# Patient
curl --request POST http://localhost:5000/patient/register\
     --header 'Content-Type: application/json'\
     --data '{"name":"Natália Giovanna Bárbara Fernandes", "phone_number": "996073355",
              "cpf":"92753242712"}'

curl --request POST http://localhost:5000/patient/register\
     --header 'Content-Type: application/json'\
     --data '{"name":"Barbara", "phone_number": "40028922", "cpf":"70532017403"}'

# Doctor
curl --request POST http://localhost:5000/doctor/register\
     --header 'Content-Type: application/json'\
     --data '{"name": "Dr. Daniel Ferreira", "crm": "PB7070"}'

curl --request POST http://localhost:5000/doctor/register\
     --header 'Content-Type: application/json'\
     --data '{"name": "Maria", "crm": "123453-SP"}'

# Medical Record
curl --request POST http://localhost:5000/record/register\
     --header 'Content-Type: application/json'\
     --data '{"medical_notes": "paciente doente", "doctor": 1, "patient": 1}'
