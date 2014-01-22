int red=9;
int green=10;
int blue=11;

int length=3; //buffer length
byte byteCount;
char endCmd='\n';


void setup(){
  pinMode(red,OUTPUT);
  pinMode(green,OUTPUT);
  pinMode(blue,OUTPUT);
  Serial.begin(9600);
  
   analogWrite(red,0);
   analogWrite(green,0);
   analogWrite(blue,0);
}

void loop(){
 char buffer[length];
 byteCount=-1;
 byteCount=Serial.readBytesUntil(endCmd, buffer, length); //read length char or until endCmd
 if(byteCount==3){
   analogWrite(red,buffer[0]);
   analogWrite(green,buffer[1]);
   analogWrite(blue,buffer[2]);
   Serial.print(buffer[0]);
   Serial.print(buffer[1]);
   Serial.print(buffer[2]);
 } 
 
 
}
