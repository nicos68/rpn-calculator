import { Component, OnInit } from '@angular/core';
import { HttpClient } from '@angular/common/http';

@Component({
  selector: 'app-calculator',
  templateUrl: './calculator.component.html',
  styleUrls: ['./calculator.component.css']
})
export class CalculatorComponent implements OnInit {
  serverUrl = 'http://localhost:8080';
  enteredValue = '';

  stack = [];

  constructor(private httpClient: HttpClient) { }

  ngOnInit(): void {
    this.httpClient.get<Array<string>>(this.serverUrl + '/rpn/stack')
    .subscribe(
        response => this.stack = response
      );
  }

  push(): void {
    this.httpClient.post<Array<string>>(
      this.serverUrl + '/rpn/stack',
      this.enteredValue
    )
    .subscribe(
      (response) => {
        this.stack = response;
        this.enteredValue = '';
      }
    );
  }

  execute(): void {
    this.httpClient.get<Array<string>>(
      this.serverUrl + '/rpn/stack/execute'
    )
    .subscribe(
      (response) => {
        this.stack = response;
        this.enteredValue = '';
      }
    );
  }

}
