int masterLines = 9; //Change here to the number of lines of your Master Layer
int slaveLines = 16; //Change here to the number of lines of your Slave Layer
int vibSense = 53;

//2-9 Master Darts
//A0-A10 Slave Darts
//34 Master Buttons
//35-39 Slave Buttons
int matrixMaster[] = {34, 9, 8, 7, 6, 5, 4, 3, 2}; //Put here the pins you connected the lines of your Master Layer (13/12 = Home Button)
int matrixSlave[] = {39, 38, 37, 36, 35, A10, A9, A8, A7, A6, A5, A4, A3, A2, A1, A0}; //Put here the pins you connected the lines of your Slave Layer (14/13 Up, 12/11 Down)
bool vibDetect = false;

void setup() 
{     
    Serial.begin(115200);     
    for(int i = 0; i < slaveLines; i++){         
        pinMode(matrixSlave[i], INPUT_PULLUP);     
    }
   for(int i = 0; i < masterLines; i++){         
       pinMode(matrixMaster[i], OUTPUT);         
       digitalWrite(matrixMaster[i], HIGH);     
   } 

   pinMode(vibSense, INPUT);
}
void loop() 
{     
  
  int one = -1;
  int two = -1;
 
  for(int i = 0; i < masterLines; i++)
  {         
      digitalWrite(matrixMaster[i], LOW);         
      for(int j = 0; j < slaveLines; j++)
      {             
          if(digitalRead(matrixSlave[j]) == LOW)
          {                 
              one = j;
              two = i;
              //Serial.write((j << 4) + i);       
              if (one >= 0 || two >= 0)
              {
                String output = String(one);
                output += ",";
                output += String(two);
                //Serial.print(one);                 
                //Serial.print(",");                 
                Serial.println(output);  
                
              }
              delay(500);                 
              break;             
          }

      }
      digitalWrite(matrixMaster[i], HIGH);
      if (one >= 0 || two >= 0)
      {
        break;
      }
  } 
  if (one < 0 || two < 0)
  {
    if (digitalRead(vibSense) == HIGH)
    {
      if (vibDetect == false)
      {
        vibDetect = true;
        Serial.println("VIB");
        delay(500);
      }
    }
    else
    {
      vibDetect = false;
    }
  }
}
