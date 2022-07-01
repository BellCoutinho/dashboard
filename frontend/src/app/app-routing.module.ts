import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { HomeComponent } from './view/home/home.component';
import { PatientsComponent } from './view/patients/patients.component';
import { PatientReadComponent } from './components/patient/patient-read/patient-read.component';

const routes: Routes = [
  {
    path: "",
    component: HomeComponent
  },
  {
    path: "patients",
    component: PatientsComponent
  },
  {
    path: "patient/:id",
    component: PatientReadComponent
  }
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
