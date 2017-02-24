int x = 0; 

void setup() {
  Serial.begin(115200);      // open the serial port at 115200 bps:    
}

void loop() { 
  int measure = 0; 
  for(x=0; x< 8; x++){
    measure = analogRead(x);
    Serial.print(measure);
    Serial.print(" ");
  }
  Serial.println("");      // prints another carriage return
  delay(200);            // delay 200 milliseconds
}
