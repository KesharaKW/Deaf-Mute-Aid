const int flex1 = A0;
const int flex2 = A1;
const int flex3 = A2;
const int flex4 = A3;
const int flex5 = A4;
int ADCflex1 = 0;
int ADCflex2 = 0;
int ADCflex3 = 0;
int ADCflex4 = 0;
int ADCflex5 = 0;

void setup() {
  Serial.begin(9600);
  pinMode(flex1, INPUT);
  pinMode(flex2, INPUT);
  pinMode(flex3, INPUT);
  pinMode(flex4, INPUT);
  pinMode(flex5, INPUT);
}

void loop() {
  ADCflex1 = analogRead(flex1);
  ADCflex2 = analogRead(flex2);
  ADCflex3 = analogRead(flex3);
  ADCflex4 = analogRead(flex4);
  ADCflex5 = analogRead(flex5);

  int MatA[1][5] = {{ADCflex1, ADCflex2, ADCflex3, ADCflex4, ADCflex5}};

  for(int k=0;k<5;k++){
     Serial.print(MatA[0][k]);
     Serial.print("\t");
    }
    
     Serial.println(" ");
     delay(100);
}
