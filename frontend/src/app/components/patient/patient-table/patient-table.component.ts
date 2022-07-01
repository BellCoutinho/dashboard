import { Component, OnInit } from '@angular/core';

import { Patient } from '../patient.model';
import { PatientService } from '../patient.service';

@Component({
  selector: 'app-patient-table',
  templateUrl: './patient-table.component.html',
  styleUrls: ['./patient-table.component.css']
})
export class PatientTableComponent implements OnInit {

  displayedColumns: string[] = ['id', 'name', 'phone_number', 'cpf', 'action']
  patients: Patient[]

  constructor(private patientService: PatientService) { 
    this.patients = []
  }

  ngOnInit(): void {
    this.patientService.read().subscribe(patients => {
      this.patients = patients
    })
  }
}
