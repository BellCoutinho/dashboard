import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';
import { Image } from './image.model';


@Injectable({
  providedIn: 'root'
})
export class ImageService {
  baseImageUrl = 'http://localhost:5000/patient/image'
  constructor(private http: HttpClient) { }

  processing(id: string): Observable<Image> {
    return this.http.get<Image>(this.baseImageUrl + '/processing/' + id)
  }

  fetch_by_patient(patientId: string): Observable<Image> {
    return this.http.get<Image>(this.baseImageUrl + '/find/' + patientId)
  }

}
