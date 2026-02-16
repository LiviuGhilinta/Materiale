#include <SevSeg.h>

#define PIN_TRIG 0
#define PIN_ECHO 23

int interval = 0, durata = 0;
float distanta = 0;
unsigned long previousMillis = 0;  
const long intervalBuzzer = 200;   
bool buzzerState = false;
SevSeg sevseg;

void setup() {
  pinMode(18, OUTPUT);  
  pinMode(PIN_TRIG, OUTPUT);
  pinMode(PIN_ECHO, INPUT);
  pinMode(13, OUTPUT);  
  pinMode(25, OUTPUT);  
  pinMode(26, OUTPUT);  

  byte numDigits = 2;
  byte digitPins[] = {15, 2, 0, 0};
  byte segmentPins[] = {4, 16, 17, 5, 27, 19, 21, 22};
  bool resistorsOnSegments = false;
  byte hardwareConfig = COMMON_CATHODE;
  bool updateWithDelays = false;
  bool leadingZeros = false;
  bool disableDecPoint = false;

  sevseg.begin(hardwareConfig, numDigits, digitPins, segmentPins, resistorsOnSegments,
               updateWithDelays, leadingZeros, disableDecPoint);
  sevseg.setBrightness(90);
  Serial.begin(115200);
}

void loop() {
  if (millis() - interval >= 100) {
    interval += 100;
    digitalWrite(PIN_TRIG, LOW);
    delayMicroseconds(5);
    digitalWrite(PIN_TRIG, HIGH);
    delayMicroseconds(10);
    digitalWrite(PIN_TRIG, LOW);
    durata = pulseIn(PIN_ECHO, HIGH);
    distanta = durata / 58.0;

    
    unsigned long currentMillis = millis();
    if (currentMillis - previousMillis >= intervalBuzzer) {
      previousMillis = currentMillis;
      buzzerState = !buzzerState;

      if (distanta <= 20 && distanta >= 15) {
        if (buzzerState) tone(18, 500);
        else noTone(18);
        digitalWrite(13, HIGH);
        digitalWrite(25, LOW);
        digitalWrite(26, LOW);
      } else if (distanta < 15 && distanta >= 10) {
        if (buzzerState) tone(18, 550);
        else noTone(18);
        digitalWrite(13, HIGH);
        digitalWrite(25, HIGH);
        digitalWrite(26, LOW);
      }  else {
        noTone(18);
        digitalWrite(13, LOW);
        digitalWrite(25, LOW);
        digitalWrite(26, LOW);
      }
    }
        if (distanta < 10 && distanta >= 2) {
         tone(18, 580);
        digitalWrite(13, HIGH);
        digitalWrite(25, HIGH);
        digitalWrite(26, HIGH);
      }
    sevseg.setNumber(distanta);
  }
  sevseg.refreshDisplay();
}