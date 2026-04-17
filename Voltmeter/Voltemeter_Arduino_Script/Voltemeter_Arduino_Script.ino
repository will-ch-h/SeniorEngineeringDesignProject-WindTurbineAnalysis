int analogInput = A0;
float vout = 0.0;
float   vin = 0.0;
float R1 = 100000.0; // resistance of R1 (100K) -see text!
float   R2 = 10000.0; // resistance of R2 (10K) - see text!
int value = 0;

void   setup() {
Serial.begin(9600);
  delay(5000);

}

void loop() {
      // read the value at analog input
   value = analogRead(analogInput);
   vout = (value * 5.0) / 1024.0; // see text
   vin = vout / (R2/(R1+R2)); 
   delay(4000);
   Serial.println(vin);
}
