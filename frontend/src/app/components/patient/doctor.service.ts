import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

import { Doctor } from './doctor.model';
@Injectable({
  providedIn: 'root'
})
export class DoctorService {

  baseDoctorUrl = 'http://localhost:5000/doctor'
  constructor(private http: HttpClient) { }

  fetch_by_patient(patientId: string): Observable<Doctor> {
    return this.http.get<Doctor>(this.baseDoctorUrl + '/find/patient/' + patientId)
  }

}
