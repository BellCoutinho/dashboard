import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';
import { Patient } from './patient.model';

@Injectable({
  providedIn: 'root'
})
export class PatientService {

  basePatientUrl = 'http://localhost:5000/patient'

  constructor(private http: HttpClient) { }

  read(): Observable<Patient[]> {
    return this.http.get<Patient[]>(this.basePatientUrl + '/find')
  }

  fetch(id: string): Observable<Patient> {
    return this.http.get<Patient>(this.basePatientUrl + '/find/' + id)
  }
}
