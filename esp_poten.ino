#define port_pin 34 
int PORT;


void setup() {
Serial.begin(9600);
Serial.println("STARTING");
}

void loop() {
PORT = analogRead(port_pin);
Serial.println("Port_value : ");
Serial.print(PORT);
}
