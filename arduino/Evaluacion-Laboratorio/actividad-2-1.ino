int vocinaPin = 10;                // choose the pin for the vocina
int pirPin = 6;               // choose the input pin (for PIR sensor)
int pirState = LOW;             // we start, assuming no motion detected
int val = 0;                    // variable for reading the pin status
 
void setup() {
  pinMode(vocinaPin, OUTPUT);      // declare Vocina as output
  pinMode(pirPin, INPUT);     // declare sensor as input
}
 
void loop(){
  val = digitalRead(pirPin);  // read input value
  
  // check if the input is HIGH 
  if (val == HIGH){            
    digitalWrite(vocinaPin, HIGH);  // turn Vocina ON
    if (pirState == LOW) {
      Serial.println("Motion detected!");	// print on output change
      pirState = HIGH;
    }
  } 
  else {
    digitalWrite(vocinaPin, LOW); // turn vocina OFF
    if (pirState == HIGH) {
      Serial.println("Motion ended!");	// print on output change
      pirState = LOW;
    }
  }
}
