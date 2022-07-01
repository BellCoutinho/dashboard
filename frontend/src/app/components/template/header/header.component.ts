import { Component, OnInit } from '@angular/core';
import { ButtonMenuService } from '../button-menu.service';

@Component({
  selector: 'app-header',
  templateUrl: './header.component.html',
  styleUrls: ['./header.component.css']
})
export class HeaderComponent implements OnInit {
  isOpen: boolean = false
  constructor(private buttonMenuServie: ButtonMenuService) { }

  ngOnInit(): void {
  }

  buttonMenuToggle() {
    this.isOpen = !this.isOpen
    this.buttonMenuServie.changeNavbar(this.isOpen)
  }
}
