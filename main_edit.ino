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
int d1 = 0;
int d2 = 0;
int d3 = 0;
int d4 = 0;
int d5 = 0;


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

  /*for (int n=0;n<5;n++){
    if (ADCflexn == 0){
    dn = 0;}
    else{
    dn = 1;
  } 
  }*/
  int CV = 100; //CV - Critical Value
  if (ADCflex1 < CV){
    d1 = 0;}
    else{
    d1 = 1;
  }
  if (ADCflex2 < CV){
    d2 = 0;}
    else{
    d2 = 1;
  }
  if (ADCflex3 < CV){
    d3 = 0;}
    else{
    d3 = 1;
  }
  if (ADCflex4 < CV){
    d4 = 0;}
    else{
    d4 = 1;
  }
  if (ADCflex5 < CV){
    d5 = 0;}
    else{
    d5 = 1;
  }
 
  //int MatA[1][5] = {{ADCflex1, ADCflex2, ADCflex3, ADCflex4, ADCflex5}};
  int MatB[1][5] = {{d1, d2, d3, d4, d5}};

  //  Serial.println(ADCflex1);
  //  Serial.println(ADCflex2);
  //  Serial.println(ADCflex3);
  //  Serial.println(ADCflex4);
  //  Serial.println(ADCflex5);
  //  //Serial.println(MatA);
  //  Serial.println("");

    /*for(int k=0;k<5;k++){
      Serial.print(MatA[0][k]);
      Serial.print("\t");
    }
    Serial.println(" ");*/
    
    for(int k=0;k<5;k++){
      Serial.print(MatB[0][k]);
      Serial.print("\t");
    }
    Serial.println(" ");
  delay(1000);
}
