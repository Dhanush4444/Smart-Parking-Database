int lightSensor = A0;
int rainSensor  = A1;
int lightRelay = 4;
int speed1Relay = 5;
int speed2Relay = 6;
void setup() {
  Serial.begin(9600);
pinMode(A0,INPUT);
pinMode(A1,INPUT);
for(int i=4;i<=6;i++)
pinMode(i,OUTPUT);
}
int lightIn=0;
int rainIn=0;

void loop() {
lightIn = analogRead(lightSensor);
rainIn = analogRead(rainSensor);

Serial.print("Light : ");
Serial.println(analogRead(A0));
Serial.print("Rain : ");
Serial.println(analogRead(A1));

if(lightIn > 700){
  digitalWrite(lightRelay,HIGH);
}
else
  digitalWrite(lightRelay,LOW);

if(rainIn> 700){
digitalWrite(speed1Relay,LOW);  
digitalWrite(speed2Relay,LOW);
}
else if(rainIn < 500){
  digitalWrite(speed1Relay,LOW);
  digitalWrite(speed2Relay,HIGH);
}

else{
  digitalWrite(speed1Relay,LOW);
  digitalWrite(speed2Relay,LOW); 
}

delay(300);

}
