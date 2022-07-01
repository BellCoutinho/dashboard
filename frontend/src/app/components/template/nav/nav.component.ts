import { Component, OnInit, AfterViewInit, ViewChild } from '@angular/core';
import { MatSidenav } from '@angular/material/sidenav';
import { ButtonMenuService} from '../button-menu.service';

@Component({
  selector: 'app-nav',
  templateUrl: './nav.component.html',
  styleUrls: ['./nav.component.css']
})
export class NavComponent implements OnInit, AfterViewInit {
  @ViewChild(MatSidenav)
  sidenav!: MatSidenav;

  constructor(private buttonMenuService: ButtonMenuService) { }

  ngOnInit(): void {
    this.buttonMenuService.isButtonMenuOpen.subscribe((isOpen: boolean) => {
      if (isOpen) {
        this.sidenav.open()
      } else {
        this.sidenav.close()
      }
    })
  }

  ngAfterViewInit() {
    console.log(this.sidenav)
  }
}
