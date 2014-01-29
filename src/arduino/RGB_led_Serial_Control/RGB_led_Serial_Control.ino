int red=9;
int green=10;
int blue=11;

int length=4; //buffer length
byte byteCount;
char endCmd='\n';

long time=0;
int periode = 10000;
int value;
boolean fading=false;
char color;

void setup(){
  pinMode(red,OUTPUT);
  pinMode(green,OUTPUT);
  pinMode(blue,OUTPUT);
  Serial.begin(9600);
  Serial.setTimeout(10);
   analogWrite(red,0);
   analogWrite(green,0);
   analogWrite(blue,0);
}

void loop(){
 char buffer[length];
 byteCount=-1;
 byteCount=Serial.readBytesUntil(endCmd, buffer, length); //read length char or until endCmd
 if(byteCount==4 && buffer[0]=='l'){
   analogWrite(red,buffer[1]);
   analogWrite(green,buffer[2]);
   analogWrite(blue,buffer[3]);
   fading=false;
 }
 if(byteCount==3 && buffer[0]=='f')
 {
   fading=true;
   color=buffer[1];
   periode=buffer[2]*100;
   analogWrite(red,0);
   analogWrite(green,0);
   analogWrite(blue,0);
 }
 if(fading){
   time = millis();
   value = 128+127*cos(2*PI/periode*time);   
   if(color=='r'){
     analogWrite(red,value);
   }else if (color=='g'){
     analogWrite(green,value);
   }else if (color=='b'){
     analogWrite(blue,value);
   }
 }
 
}
