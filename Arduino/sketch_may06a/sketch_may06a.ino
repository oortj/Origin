#include <SoftwareSerial.h>

SoftwareSerial btSerial(2, 3); // RX | TX

void setup() {
  Serial.begin(57600);
  Serial.println("Enter AT commands:");
  btSerial.begin(38400);  // HC-05 default speed in AT command more
}

void loop() {
  if (btSerial.available())  Serial.write(btSerial.read());
  if (Serial.available())    btSerial.write(Serial.read());
}
