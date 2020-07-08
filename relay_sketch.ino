#define PIN_RELAY   5
#define ON_STATE   '0'
#define OFF_STATE  '1'
 
void serialEvent() {
  char serial_input;
  
  while (Serial.available())
    serial_input = Serial.read();
    
  switch(serial_input) {
    case ON_STATE: 
      digitalWrite(5, HIGH); 
      Serial.println("RELAY ACTIVATED");
      break;
      
    case OFF_STATE: 
      digitalWrite(5, LOW);
      Serial.println("RELAY DE-ACTIVATED"); 
      break;
  }
}

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  pinMode(5, OUTPUT);
}

void loop() {
  // put your main code here, to run repeatedly:
}
