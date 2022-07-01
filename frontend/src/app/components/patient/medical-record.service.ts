import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';
import { MedicalRecord } from './medical-record.model';

@Injectable({
  providedIn: 'root'
})
export class MedicalRecordService {

  baseRecordUrl = 'http://localhost:5000/record'

  constructor(private http: HttpClient) { }

  fetch(id: string): Observable<MedicalRecord> {
    return this.http.get<MedicalRecord>(this.baseRecordUrl + '/find/' + id)
  }
  
  fetch_by_patient(patientId: string): Observable<MedicalRecord> {
    return this.http.get<MedicalRecord>(this.baseRecordUrl + '/find/patient/' + patientId)
  }

}
