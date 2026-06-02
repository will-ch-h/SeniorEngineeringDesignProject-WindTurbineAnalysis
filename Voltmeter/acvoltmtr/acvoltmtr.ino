int b;
float a,y=0,ac;
void setup()
{
pinMode(A0,INPUT); // set pin a0 as input pin
Serial.begin(9600);// begin serial communication between arduino and pc
delay(10000);
}
void loop()
{
ac=0;
b=analogRead(A0);// read analog values from pin A0 across capacitor
if (b>15)
{
a=(b*0.0759462759462759);// converts analog value(x) into input ac supply value using this formula ( explained in woeking section)
ac=(a/sqrt(2));
}
//Serial.print(" analog input " ) ; // specify name to the corresponding value to be printed
//Serial.print(b) ; // print input analog value on serial monitor
//Serial.print(" ac voltage ") ; // specify name to the corresponding value to be printed
Serial.print(ac) ; // prints the ac value on Serial monitor
Serial.println();
y=a;
delay(20000);
}
