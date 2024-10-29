#include <LiquidCrystal.h>

#include <LiquidCrystal.h>
LiquidCrystal lcd(5, 6, 8, 9, 10, 11);

int redled = 2;
int greenled = 3;
int buzzer = 4;
int sensor = A0;
int sensorThresh = 70;

void setup() {
  pinMode(sensor, INPUT);
  pinMode(buzzer, OUTPUT);
  lcd.begin(16, 2);
  pinMode(greenled, OUTPUT);
  Serial.begin(9600);
  pinMode(redled, OUTPUT);
}

void loop() {
  int analogValue = analogRead(sensor);
  Serial.print(analogValue);
  Serial.println();

  if (analogValue > sensorThresh) {
    digitalWrite(greenled, LOW);
    tone(buzzer, 1000, 10000);
    lcd.clear();
    lcd.setCursor(0, 0);
    lcd.print("ALERTA!!!");
    delay(1000);
    digitalWrite(redled, HIGH);
    lcd.clear();
    lcd.setCursor(0, 1);
    lcd.print("CORRE DE AHI!");
    delay(2000); // 
  } else {
    digitalWrite(redled, LOW);
    noTone(buzzer);
    lcd.clear();
    lcd.setCursor(0, 0);
    lcd.print("SECTOR SEGURO");
    digitalWrite(greenled, HIGH);
    delay(1000);
    lcd.clear();
    lcd.setCursor(0, 1);
    lcd.print("AREA LIMPA");
    delay(1000);
  }
}
