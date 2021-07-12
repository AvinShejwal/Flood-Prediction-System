
#include <DHT.h>
#define dht_1 2
#define trigPin 5
#define echoPin 4
#define DHTTYPE DHT11
DHT dht(dht_1,DHTTYPE);
int X;
int Y;
float TIME = 0;
float FREQUENCY = 0;
float WATER = 0;
const int input = 3;

void setup()
{
  Serial.begin (9600);
  pinMode(trigPin, OUTPUT);
  pinMode(echoPin, INPUT);
  pinMode(6,INPUT);
  pinMode(input,INPUT);
  dht.begin();
}

void loop()
{
  Serial.begin(9600);

  float temp = dht.readTemperature();
  float humid = dht.readHumidity();

  int rain = digitalRead(6);
  
  X = pulseIn(input, HIGH);
  Y = pulseIn(input, LOW);
  TIME = X + Y;
  FREQUENCY = 1000000/TIME;
  WATER = FREQUENCY/7.5;

  long duration,inches, cm;
  digitalWrite(trigPin, LOW);
  delay(2);
  digitalWrite(trigPin, HIGH);
  delay(10);
  digitalWrite(trigPin, LOW);
  duration = pulseIn(echoPin, HIGH);
  inches = microsecondsToInches(duration);
  
  Serial.println("T ="+ String(temp)+", H ="+String(humid)+", R="+String(rain)+", F ="+String(WATER)+", D ="+String(inches));
  
  delay (1000);
}

long microsecondsToInches(long microseconds)
{
  return microseconds / 74 / 2;
}
