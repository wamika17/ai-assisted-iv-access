/*
--------------------------------------------------------
Smart AI-Assisted IV Access System

Main Firmware

Author: Wamika Varada
--------------------------------------------------------
*/

void initializeSensors();
void readSensors();
void sendData();

void setup() {

  Serial.begin(115200);

  initializeSensors();

}

void loop() {

  readSensors();

  sendData();

  delay(500);

}

void initializeSensors(){

  Serial.println("Initializing Sensors...");

}

void readSensors(){

  Serial.println("Reading Sensor Data...");

}

void sendData(){

  Serial.println("Sending Data to Dashboard...");

}
