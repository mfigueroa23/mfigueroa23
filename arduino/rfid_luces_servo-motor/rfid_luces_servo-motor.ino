// void setup() {
//   // put your setup code here, to run once:

// }

// void loop() {
//   // put your main code here, to run repeatedly:

// }

#include <SPI.h>
#include <MFRC522.h>
#include <Servo.h>

#define SS_PIN 10  // Pin SDA en el módulo RFID
#define RST_PIN 9  // Pin RST en el módulo RFID

Servo servito; //Declaramos un objeto tipo Servo llamado servito

int movIzdo=LOW; //Valdrá HIGH cuando apretemos el pulsador que mueve a 0º
int movDcho=LOW; //Valdrá HIGH cuando apretemos el pulsador que mueve a 180º

const int pinIzdo = 2;

MFRC522 rfid(SS_PIN, RST_PIN);  // Crea un objeto RFID

void setup() {
  Serial.begin(9600);   // Inicia la comunicación serie
  SPI.begin();          // Inicia el bus SPI
  rfid.PCD_Init();      // Inicia el lector RFID
  Serial.println("Acerque una tarjeta o etiqueta RFID...");
  servito.attach(2); //servito está conectado al pin 9
  pinMode(7, OUTPUT);
  pinMode(8, OUTPUT);
  digitalWrite(7, LOW);
  digitalWrite(8, LOW);
}

void loop() {

  digitalWrite(8, HIGH);
  digitalWrite(7, LOW);

  // Verifica si una nueva tarjeta está presente
  if ( !rfid.PICC_IsNewCardPresent() ) {
    return;
  }

  // Selecciona la tarjeta
  if ( !rfid.PICC_ReadCardSerial() ) {
    return;
  }

  // Muestra el UID de la tarjeta
  Serial.print("UID de la tarjeta: ");
  for (byte i = 0; i < rfid.uid.size; i++) {
    Serial.print(rfid.uid.uidByte[i] < 0x10 ? " 0" : " ");
    Serial.print(rfid.uid.uidByte[i], HEX);
  }
  Serial.println();

  digitalWrite(7, HIGH);
  digitalWrite(8, LOW);

  //mueve el servo cuando se lee una tarjeta
  servito.write(180); //mueve el servo a 90 grados
  delay(3000);       // espera el segundo
  servito.write(0);  //regresa el servo a 0 grados

  // Para detener la lectura de la tarjeta
  rfid.PICC_HaltA();
}