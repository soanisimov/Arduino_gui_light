int red = 3; //check your connections
int green = 5; //check your connections
int blue = 6; //check your connections
int netural = 11; //check your connections
char message;

void setup() {
Serial.begin(9600); //check
pinMode(red,OUTPUT);
pinMode(green,OUTPUT);
pinMode(blue,OUTPUT);
pinMode(netural,OUTPUT);
}

void loop() {
if(Serial.available() > 0){
  message = Serial.read();
  Serial.print(message);
if(message == '1'){
  for(int i=0;i<=255;i++) {
  analogWrite(red, i);
  delay(5);
}
}
else if(message == '4'){
 for(int i=255;i>=0;i--) {
 analogWrite(red, i);
  delay(5); // ставим задержку для эффекта
 }
}
if(message == '2'){
   for(int i=0;i<=255;i++) {
  analogWrite(green, i);
  delay(5);
}
}
else if(message == '5'){
  for(int i=255;i>=0;i--) {
  analogWrite(green, i);
  delay(5); // ставим задержку для эффекта
}
}

if(message == '3'){
   for(int i=0;i<=255;i++) {
  analogWrite(blue, i);
  delay(5);
}
}
else if(message == '6'){
  for(int i=255;i>=0;i--) {
  analogWrite(blue, i);
  delay(5); // ставим задержку для эффекта
}
} 

if(message == '!'){
while(true){
    digitalWrite(green,HIGH);
    delay(100);
    digitalWrite(blue,HIGH);
    delay(100);
    digitalWrite(red,HIGH);
    delay(100);
    digitalWrite(blue,LOW);
    delay(100);
    digitalWrite(red,LOW);
    delay(100);
    digitalWrite(green,LOW);
    delay(100);
    break;
}
}
if(message == '@'){
  digitalWrite(red,HIGH);
  delay(100);
  digitalWrite(red,LOW);
  delay(100);
  digitalWrite(red,HIGH);
  delay(50);
  digitalWrite(red,LOW);
  digitalWrite(blue,HIGH);
  delay(100);
  digitalWrite(blue,LOW);
  delay(100);
  digitalWrite(blue,HIGH);
  delay(100);
  digitalWrite(blue,LOW);
  digitalWrite(red,LOW);
}
if(message == '$'){
  digitalWrite(green,HIGH);
  delay(500);
   digitalWrite(green,LOW);
  digitalWrite(red,HIGH);
  delay(500);
  digitalWrite(red,LOW);
  digitalWrite(blue,HIGH);
  delay(500);
  digitalWrite(blue,LOW);
}
if(message == '%'){
digitalWrite(red,HIGH);
delay(50);
digitalWrite(red,LOW);
digitalWrite(green,HIGH);
digitalWrite(blue,HIGH);
delay(50);
digitalWrite(green,LOW);
digitalWrite(blue,LOW);
}
if(message == '^'){
for(int i=0;i<=255;i++) {
  analogWrite(red, i);
  delay(15);
}
for(int i=0;i<=255;i++) {
  analogWrite(green, i);
  delay(15);
}
for(int i=0;i<=255;i++) {
  analogWrite(blue, i);
  delay(15);
}
for(int i=255;i>=0;i--) {
  analogWrite(red, i);
  delay(15); 
}
for(int i=255;i>=0;i--) {
  analogWrite(green, i);
  delay(15);
}
for(int i=255;i>=0;i--) {
  analogWrite(blue, i);
  delay(15); 
}
}
if(message == '('){
  for(int i=0;i<=255;i++) {
  analogWrite(red, i);
  delay(10);
}
for(int i=255;i>=0;i--) {
  analogWrite(red, i);
  delay(10);
}
for(int i=0;i<=255;i++) {
  analogWrite(green, i);
  delay(10);
}
for(int i=255;i>=0;i--) {
  analogWrite(green, i);
  delay(10); 
}
for(int i=0;i<=255;i++) {
  analogWrite(blue, i);
  delay(10);
}
for(int i=255;i>=0;i--) {
  analogWrite(blue, i);
  delay(10);
}
}
if(message == ')'){
  int randNumber = random(20);
  for(int i=0;i<=255;i++) {
  analogWrite(blue, i);
  analogWrite(red, i);
  delay(randNumber);
}
for(int i=255;i>=0;i--) {
  analogWrite(blue, i);
  analogWrite(red, i);
  delay(randNumber);
}
}
if(message == '*'){
  for(int i=0;i<=255;i++) {
  analogWrite(red, i);
  analogWrite(green, i);
  delay(10);
}
for(int i=255;i>=0;i--) {
  analogWrite(red, i);
  analogWrite(green, i);
  delay(10);
}
  for(int i=0;i<=255;i++) {
  analogWrite(green, i);
  analogWrite(blue, i);
  delay(10);
}
for(int i=255;i>=0;i--) {
  analogWrite(green, i);
  analogWrite(blue, i);
  delay(10);
}
  for(int i=0;i<=255;i++) {
  analogWrite(red, i);
  analogWrite(blue, i);
  delay(10);
}
for(int i=255;i>=0;i--) {
  analogWrite(red, i);
  analogWrite(blue, i);
  delay(10);
}
if(message == "7"){
  digitalWrite(red,HIGH);
}
}
}
}
