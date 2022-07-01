import { Component, OnInit } from '@angular/core';
import { ActivatedRoute } from '@angular/router';

import { Patient} from '../patient.model';
import { PatientService } from '../patient.service';
import { MedicalRecord } from '../medical-record.model';
import { MedicalRecordService } from '../medical-record.service';
import { Doctor } from '../doctor.model';
import { DoctorService } from '../doctor.service';
import { Image } from '../image.model';
import { ImageService } from '../image.service';

@Component({
  selector: 'app-patient-read',
  templateUrl: './patient-read.component.html',
  styleUrls: ['./patient-read.component.css']
})
export class PatientReadComponent implements OnInit {

  patient: Patient = {
    id: 0,
    name: '',
    phone_number: '',
    cpf: ''
  }
  record: MedicalRecord = {
    id: 0,
    date: '',
    time: '',
    medical_notes: '',
  }
  doctor: Doctor = {
    id: 0,
    name: '',
    crm: ''
  }

  lastImage: Image = {
    id: 0,
    filename: '',
    date: '',
    image64: ''
  }

  processingImage: Image = {
    id: 0,
    filename: '',
    date: '',
    image64: ''
  }

  constructor(
      private patientService: PatientService,
      private medicalRecordService: MedicalRecordService,
      private doctorService: DoctorService,
      private imageService: ImageService,
      private route: ActivatedRoute
  ) { }

  ngOnInit(): void {
    var id = this.route.snapshot.paramMap.get('id')
    if (id == null) {
      id = ''
    }
    this.patientService.fetch(id).subscribe(patient => {
      this.patient = patient
    })
    this.medicalRecordService.fetch_by_patient(id).subscribe(record => {
      this.record = record
    })
    this.doctorService.fetch_by_patient(id).subscribe(doctor => {
      this.doctor = doctor
    })

    this.imageService.fetch_by_patient(id).subscribe(image => {
      this.lastImage = image
      this.lastImage.image64 = this.lastImage.image64.slice(2,-1)
    })
    /*
    this.imageService.processing(this.lastImage.id.toString()).subscribe(image => {
      this.processingImage = image
      console.log(this.processingImage)
    })
    */
  }
}
