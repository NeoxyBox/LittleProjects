#define led1 7
#define pot A0

int potVal;

void setup() {
  // put your setup code here, to run once:
  pinMode(led1, OUTPUT);
  Serial.begin(9600);
}

void loop() {
  potVal = analogRead(pot);
  Serial.println(potVal);

  if (potVal == 0)
  {
    digitalWrite(led1, LOW);
  }
  if (potVal == 1023)
  {
    digitalWrite(led1, HIGH);
    delay(200);
    digitalWrite(led1, LOW);
    delay(200);
    digitalWrite(led1, HIGH);
    delay(200);
    digitalWrite(led1, LOW);
    delay(200);
    digitalWrite(led1, HIGH);
  }

  delay(20);
}
