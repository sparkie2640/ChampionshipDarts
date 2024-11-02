int oneD1 = 12; int twoD1 = A1;
int oneD2 = 13; int twoD2 = A5;
int oneD3 = 13; int twoD3 = A0;
int oneD4 = 12; int twoD4 = A2;
int oneD5 = 12; int twoD5 = 2;
int oneD6 = 12; int twoD6 = A3;
int oneD7 = 13; int twoD7 = 5;
int oneD8 = 13; int twoD8 = 4;
int oneD9 = 12; int twoD9 = 3;
int oneD10 = 13; int twoD10 = A4;
int oneD11 = 12; int twoD11 = 4;
int oneD12 = 13; int twoD12 = 2;
int oneD13 = 13; int twoD13 = A3;
int oneD14 = 13; int twoD14 = 3;
int oneD15 = 12; int twoD15 = A4;
int oneD16 = 12; int twoD16 = 5;
int oneD17 = 12; int twoD17 = A5;
int oneD18 = 13; int twoD18 = A2;
int oneD19 = 12; int twoD19 = A0;
int oneD20 = 13; int twoD20 = A1;

int oneO1 = 10; int twoO1 = A1;
int oneO2 = 11; int twoO2 = A5;
int oneO3 = 11; int twoO3 = A0;
int oneO4 = 10; int twoO4 = A2;
int oneO5 = 10; int twoO5 = 2;
int oneO6 = 10; int twoO6 = A3;
int oneO7 = 11; int twoO7 = 5;
int oneO8 = 11; int twoO8 = 4;
int oneO9 = 10; int twoO9 = 3;
int oneO10 = 11; int twoO10 = A4;
int oneO11 = 10; int twoO11 = 4;
int oneO12 = 11; int twoO12 = 2;
int oneO13 = 11; int twoO13 = A3;
int oneO14 = 11; int twoO14 = 3;
int oneO15 = 10; int twoO15 = A4;
int oneO16 = 10; int twoO16 = 5;
int oneO17 = 10; int twoO17 = A5;
int oneO18 = 11; int twoO18 = A2;
int oneO19 = 10; int twoO19 = A0;
int oneO20 = 11; int twoO20 = A1;

int oneT1 = 8; int twoT1 = A1;
int oneT2 = 9; int twoT2 = A5; 
int oneT3 = 9; int twoT3 = A0;
int oneT4 = 8; int twoT4 = A2;
int oneT5 = 8; int twoT5 = 2;
int oneT6 = 8; int twoT6 = A3;
int oneT7 = 9; int twoT7 = 5;
int oneT8 = 9; int twoT8 = 4;
int oneT9 = 8; int twoT9 = 3;
int oneT10 = 9; int twoT10 = A4;
int oneT11 = 8; int twoT11 = 4;
int oneT12 = 9; int twoT12 = 2;
int oneT13 = 9; int twoT13 = A3;
int oneT14 = 9; int twoT14 = 3;
int oneT15 = 8; int twoT15 = A4;
int oneT16 = 8; int twoT16 = 5;
int oneT17 = 8; int twoT17 = A5;
int oneT18 = 9; int twoT18 = A2;
int oneT19 = 8; int twoT19 = A0;
int oneT20 = 9; int twoT20 = A1;

int oneI1 = 6; int twoI1 = A1;
int oneI2 = 7; int twoI2 = A5; 
int oneI3 = 7; int twoI3 = A0;
int oneI4 = 6; int twoI4 = A2;
int oneI5 = 6; int twoI5 = 2;
int oneI6 = 7; int twoI6 = A3;
int oneI7 = 7; int twoI7 = 5;
int oneI8 = 7; int twoI8 = 4;
int oneI9 = 6; int twoI9 = 3;
int oneI10 = 7; int twoI10 = A4;
int oneI11 = 6; int twoI11 = 4;
int oneI12 = 7; int twoI12 = 2;
int oneI13 = 7; int twoI13 = A3;
int oneI14 = 7; int twoI14 = 3;
int oneI15 = 6; int twoI15 = A4;
int oneI16 = 6; int twoI16 = 5;
int oneI17 = 6; int twoI17 = A5; 
int oneI18 = 7; int twoI18 = A2;
int oneI19 = 6; int twoI19 = A0;
int oneI20 = 7; int twoI20 = A1;


int singleBull = A6;
int oneDB = 7;
int twoDB = A6;

int up = 47;
int down = 51;
int left = 45;
int right = 49;
int enter = 53;

int led_light (int pinOne, int pinTwo) {
  pinMode(pinOne, OUTPUT);
  pinMode(pinTwo, OUTPUT);
  digitalWrite(pinOne, LOW);  
  digitalWrite(pinTwo, LOW);    
  delay(500);              
  pinMode(pinOne, INPUT);
  pinMode(pinTwo, INPUT);
  delay(250);
  pinMode(pinOne, OUTPUT);
  pinMode(pinTwo, OUTPUT);
  digitalWrite(pinOne, LOW);  
  digitalWrite(pinTwo, LOW);    
  delay(500);              
  pinMode(pinOne, INPUT);
  pinMode(pinTwo, INPUT);
  delay(250);
  pinMode(pinOne, OUTPUT);
  pinMode(pinTwo, OUTPUT);
  digitalWrite(pinOne, LOW);  
  digitalWrite(pinTwo, LOW);    
  delay(1000);              
  pinMode(pinOne, INPUT);
  pinMode(pinTwo, INPUT);
}

int led_post (int pinOne, int pinTwo) {
  pinMode(pinOne, OUTPUT);
  pinMode(pinTwo, OUTPUT);
  digitalWrite(pinOne, LOW);  
  digitalWrite(pinTwo, LOW);    
  delay(50);              
  pinMode(pinOne, INPUT);
  pinMode(pinTwo, INPUT);
}

int single_bull (int pinTwo) {
  pinMode(9, OUTPUT);
  pinMode(8, OUTPUT);
  pinMode(6, OUTPUT);
  pinMode(pinTwo, OUTPUT);
  digitalWrite(9, LOW);  
  digitalWrite(8, LOW);  
  digitalWrite(6, LOW);  
  digitalWrite(pinTwo, LOW);    
  delay(500);              
  pinMode(9, INPUT);
  pinMode(8, INPUT);
  pinMode(6, INPUT);
  pinMode(pinTwo, INPUT);
  delay(250);
  pinMode(9, OUTPUT);
  pinMode(8, OUTPUT);
  pinMode(6, OUTPUT);
  pinMode(pinTwo, OUTPUT);
  digitalWrite(9, LOW);  
  digitalWrite(8, LOW);
  digitalWrite(6, LOW);
  digitalWrite(pinTwo, LOW);    
  delay(500);              
  pinMode(9, INPUT);
  pinMode(8, INPUT);
  pinMode(6, INPUT);
  pinMode(pinTwo, INPUT);
  delay(250);
  pinMode(9, OUTPUT);
  pinMode(8, OUTPUT);
  pinMode(6, OUTPUT);
  pinMode(pinTwo, OUTPUT);
  digitalWrite(9, LOW);  
  digitalWrite(8, LOW);
  digitalWrite(6, LOW);
  digitalWrite(pinTwo, LOW);    
  delay(1000);              
  pinMode(9, INPUT);
  pinMode(8, INPUT);
  pinMode(6, INPUT);
  pinMode(pinTwo, INPUT);
}

int button_on(int button)
{
  pinMode(button, OUTPUT);  
  digitalWrite(button, HIGH);
}

int button_off(int button)
{
  pinMode(button, INPUT);    
}

int button_blink(int button)
{
  //Clear the pin first just in case it's already on
  pinMode(button, INPUT);
  delay(50);
  //Blnk 3 times
  pinMode(button, OUTPUT);  
  digitalWrite(button, HIGH);
  delay(500);
  pinMode(button, INPUT);    
  delay(250);    
  pinMode(button, OUTPUT);  
  digitalWrite(button, HIGH);
  delay(500);
  pinMode(button, INPUT);    
  delay(250);    
  pinMode(button, OUTPUT);  
  digitalWrite(button, HIGH);
  delay(1000);
  pinMode(button, INPUT);    
}
void setup() {
 Serial.begin(115200);
}
void loop() {
  if (Serial.available() > 0) {
    String ledString = Serial.readStringUntil('\n');
    Serial.print("I received: ");
    Serial.println(ledString);
    if (ledString == "D1") { led_light(oneD1, twoD1); }
    if (ledString == "D2") { led_light(oneD2, twoD2); }
    if (ledString == "D3") { led_light(oneD3, twoD3); }
    if (ledString == "D4") { led_light(oneD4, twoD4); }
    if (ledString == "D5") { led_light(oneD5, twoD5); }
    if (ledString == "D6") { led_light(oneD6, twoD6); }
    if (ledString == "D7") { led_light(oneD7, twoD7); }
    if (ledString == "D8") { led_light(oneD8, twoD8); }
    if (ledString == "D9") { led_light(oneD9, twoD9); }
    if (ledString == "D10") { led_light(oneD10, twoD10); }
    if (ledString == "D11") { led_light(oneD11, twoD11); }
    if (ledString == "D12") { led_light(oneD12, twoD12); }
    if (ledString == "D13") { led_light(oneD13, twoD13); }
    if (ledString == "D14") { led_light(oneD14, twoD14); }
    if (ledString == "D15") { led_light(oneD15, twoD15); }
    if (ledString == "D16") { led_light(oneD16, twoD16); }
    if (ledString == "D17") { led_light(oneD17, twoD17); }
    if (ledString == "D18") { led_light(oneD18, twoD18); }
    if (ledString == "D19") { led_light(oneD19, twoD19); }
    if (ledString == "D20") { led_light(oneD20, twoD20); }
    if (ledString == "O1") { led_light(oneO1, twoO1); }
    if (ledString == "O2") { led_light(oneO2, twoO2); }
    if (ledString == "O3") { led_light(oneO3, twoO3); }
    if (ledString == "O4") { led_light(oneO4, twoO4); }
    if (ledString == "O5") { led_light(oneO5, twoO5); }
    if (ledString == "O6") { led_light(oneO6, twoO6); }
    if (ledString == "O7") { led_light(oneO7, twoO7); }
    if (ledString == "O8") { led_light(oneO8, twoO8); }
    if (ledString == "O9") { led_light(oneO9, twoO9); }
    if (ledString == "O10") { led_light(oneO10, twoO10); }
    if (ledString == "O11") { led_light(oneO11, twoO11); }
    if (ledString == "O12") { led_light(oneO12, twoO12); }
    if (ledString == "O13") { led_light(oneO13, twoO13); }
    if (ledString == "O14") { led_light(oneO14, twoO14); }
    if (ledString == "O15") { led_light(oneO15, twoO15); }
    if (ledString == "O16") { led_light(oneO16, twoO16); }
    if (ledString == "O17") { led_light(oneO17, twoO17); }
    if (ledString == "O18") { led_light(oneO18, twoO18); }
    if (ledString == "O19") { led_light(oneO19, twoO19); }
    if (ledString == "O20") { led_light(oneO20, twoO20); }
    if (ledString == "T1") { led_light(oneT1, twoT1); }
    if (ledString == "T2") { led_light(oneT2, twoT2); }
    if (ledString == "T3") { led_light(oneT3, twoT3); }
    if (ledString == "T4") { led_light(oneT4, twoT4); }
    if (ledString == "T5") { led_light(oneT5, twoT5); }
    if (ledString == "T6") { led_light(oneT6, twoT6); }
    if (ledString == "T7") { led_light(oneT7, twoT7); }
    if (ledString == "T8") { led_light(oneT8, twoT8); }
    if (ledString == "T9") { led_light(oneT9, twoT9); }
    if (ledString == "T10") { led_light(oneT10, twoT10); }
    if (ledString == "T11") { led_light(oneT11, twoT11); }
    if (ledString == "T12") { led_light(oneT12, twoT12); }
    if (ledString == "T13") { led_light(oneT13, twoT13); }
    if (ledString == "T14") { led_light(oneT14, twoT14); }
    if (ledString == "T15") { led_light(oneT15, twoT15); }
    if (ledString == "T16") { led_light(oneT16, twoT16); }
    if (ledString == "T17") { led_light(oneT17, twoT17); }
    if (ledString == "T18") { led_light(oneT18, twoT18); }
    if (ledString == "T19") { led_light(oneT19, twoT19); }
    if (ledString == "T20") { led_light(oneT20, twoT20); }
    if (ledString == "I1") { led_light(oneI1, twoI1); }
    if (ledString == "I2") { led_light(oneI2, twoI2); }
    if (ledString == "I3") { led_light(oneI3, twoI3); }
    if (ledString == "I4") { led_light(oneI4, twoI4); }
    if (ledString == "I5") { led_light(oneI5, twoI5); }
    if (ledString == "I6") { led_light(oneI6, twoI6); }
    if (ledString == "I7") { led_light(oneI7, twoI7); }
    if (ledString == "I8") { led_light(oneI8, twoI8); }
    if (ledString == "I9") { led_light(oneI9, twoI9); }
    if (ledString == "I10") { led_light(oneI10, twoI10); }
    if (ledString == "I11") { led_light(oneI11, twoI11); }
    if (ledString == "I12") { led_light(oneI12, twoI12); }
    if (ledString == "I13") { led_light(oneI13, twoI13); }
    if (ledString == "I14") { led_light(oneI14, twoI14); }
    if (ledString == "I15") { led_light(oneI15, twoI15); }
    if (ledString == "I16") { led_light(oneI16, twoI16); }
    if (ledString == "I17") { led_light(oneI17, twoI17); }
    if (ledString == "I18") { led_light(oneI18, twoI18); }
    if (ledString == "I19") { led_light(oneI19, twoI19); }
    if (ledString == "I20") { led_light(oneI20, twoI20); }
    if (ledString == "DB") { led_light(oneDB, twoDB); }
    if (ledString == "SB") { single_bull(singleBull); }
    if (ledString == "UP_ON") { button_on(up); }
    if (ledString == "UP_OFF") { button_off(up); }
    if (ledString == "UP_BLINK") { button_blink(up); }
    if (ledString == "DOWN_ON") { button_on(down); }
    if (ledString == "DOWN_OFF") { button_off(down); }
    if (ledString == "DOWN_BLINK") { button_blink(down); }
    if (ledString == "LEFT_ON") { button_on(left); }
    if (ledString == "LEFT_OFF") { button_off(left); }
    if (ledString == "LEFT_BLINK") { button_blink(left); }
    if (ledString == "RIGHT_ON") { button_on(right); }
    if (ledString == "RIGHT_OFF") { button_off(right); }
    if (ledString == "RIGHT_BLINK") { button_blink(right); }
    if (ledString == "ENTER_ON") { button_on(enter); }
    if (ledString == "ENTER_OFF") { button_off(enter); }
    if (ledString == "ENTER_BLINK") { button_blink(enter); }
    if (ledString == "BUTTON_POST") {
      button_on(up);
      delay(50);
      button_off(up);
      delay(50);
      button_on(down);
      delay(50);
      button_off(down);
      delay(50);
      button_on(left);
      delay(50);
      button_off(left);
      delay(50);
      button_on(right);
      delay(50);
      button_off(right);
      delay(50);
      button_blink(enter);
    }
    if (ledString == "POST") { 
      led_post(oneD20, twoD20); 
      led_post(oneD1, twoD1); 
      led_post(oneD18, twoD18); 
      led_post(oneD4, twoD4); 
      led_post(oneD13, twoD13); 
      led_post(oneD6, twoD6); 
      led_post(oneD10, twoD10); 
      led_post(oneD15, twoD15); 
      led_post(oneD2, twoD2); 
      led_post(oneD17, twoD17); 
      led_post(oneD3, twoD3); 
      led_post(oneD19, twoD19); 
      led_post(oneD7, twoD7); 
      led_post(oneD16, twoD16); 
      led_post(oneD8, twoD8); 
      led_post(oneD11, twoD11); 
      led_post(oneD14, twoD14); 
      led_post(oneD9, twoD9); 
      led_post(oneD12, twoD12); 
      led_post(oneD5, twoD5); 
      led_post(oneO20, twoO20); 
      led_post(oneO1, twoO1); 
      led_post(oneO18, twoO18); 
      led_post(oneO4, twoO4); 
      led_post(oneO13, twoO13); 
      led_post(oneO6, twoO6); 
      led_post(oneO10, twoO10); 
      led_post(oneO15, twoO15); 
      led_post(oneO2, twoO2); 
      led_post(oneO17, twoO17); 
      led_post(oneO3, twoO3); 
      led_post(oneO19, twoO19); 
      led_post(oneO7, twoO7); 
      led_post(oneO16, twoO16); 
      led_post(oneO8, twoO8); 
      led_post(oneO11, twoO11); 
      led_post(oneO14, twoO14); 
      led_post(oneO9, twoO9); 
      led_post(oneO12, twoO12); 
      led_post(oneO5, twoO5); 
      led_post(oneT20, twoT20); 
      led_post(oneT1, twoT1); 
      led_post(oneT18, twoT18); 
      led_post(oneT4, twoT4); 
      led_post(oneT13, twoT13); 
      led_post(oneT6, twoT6); 
      led_post(oneT10, twoT10); 
      led_post(oneT15, twoT15); 
      led_post(oneT2, twoT2); 
      led_post(oneT17, twoT17); 
      led_post(oneT3, twoT3); 
      led_post(oneT19, twoT19); 
      led_post(oneT7, twoT7); 
      led_post(oneT16, twoT16); 
      led_post(oneT8, twoT8); 
      led_post(oneT11, twoT11); 
      led_post(oneT14, twoT14); 
      led_post(oneT9, twoT9); 
      led_post(oneT12, twoT12); 
      led_post(oneT5, twoT5); 
      led_post(oneI20, twoI20); 
      led_post(oneI1, twoI1); 
      led_post(oneI18, twoI18); 
      led_post(oneI4, twoI4); 
      led_post(oneI13, twoI13); 
      led_post(oneI6, twoI6); 
      led_post(oneI10, twoI10); 
      led_post(oneI15, twoI15); 
      led_post(oneI2, twoI2); 
      led_post(oneI17, twoI17); 
      led_post(oneI3, twoI3); 
      led_post(oneI19, twoI19); 
      led_post(oneI7, twoI7); 
      led_post(oneI16, twoI16); 
      led_post(oneI8, twoI8); 
      led_post(oneI11, twoI11); 
      led_post(oneI14, twoI14); 
      led_post(oneI9, twoI9); 
      led_post(oneI12, twoI12); 
      led_post(oneI5, twoI5); 
      led_post(oneDB, twoDB); 
      single_bull(singleBull); 
    }
  }
}
