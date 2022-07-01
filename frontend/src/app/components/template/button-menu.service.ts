import { Injectable, EventEmitter } from '@angular/core';

@Injectable({
  providedIn: 'root'
})
export class ButtonMenuService {
  isButtonMenuOpen = new EventEmitter<boolean>();
  constructor() { }

  changeNavbar(isOpen: boolean) {
    this.isButtonMenuOpen.emit(isOpen)
  }

}
