import { TestBed } from '@angular/core/testing';

import { ButtonMenuService } from './button-menu.service';

describe('ButtonMenuService', () => {
  let service: ButtonMenuService;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(ButtonMenuService);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
