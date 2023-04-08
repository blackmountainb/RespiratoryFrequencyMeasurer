#include "Adafruit_MCP9808.h"
int delay_value = 100;
// Create the MCP9808 temperature sensor object
Adafruit_MCP9808 tempsensor = Adafruit_MCP9808();

void setup() {
  Serial.begin(9600);
  Serial.println("MCP9808 demo by Robojax");
  
  // Make sure the sensor is found, you can also pass in a different i2c
  // address with tempsensor.begin(0x19) for example
  if (!tempsensor.begin()) {
    Serial.println("Couldn't find MCP9808!");
    while (1);
  }
}


void loop() {
  float c = tempsensor.readTempC();
  Serial.println(c);
  delay(delay_value);
  
}// loop end
