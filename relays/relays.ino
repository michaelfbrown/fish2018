/************************************************
   Name：_2_channel_relay
   Description: control the 2 channel relay module to ON or OFF
   Website: www.sunfounder.com
   Email: service@sunfounder.com
*****************************************************/


//the relays connect to
int IN1 = 4;
int IN2 = 5;

#define ON   0
#define OFF  1
void setup()
{
  relay_init();//initialize the relay
  //begin a serial connection with the computer (optional-- but helpful for debugging)
  Serial.begin(9600);
}

int feeder=0;


//the main loop waits for communication (feeder) from the computer and closes one of two relays when there is a signal
void loop() {


 if (Serial.available()) {
                // read the value for feeder:
                feeder = Serial.read();
                Serial.println(feeder);
                //}

//feeder = Serial.parseInt();  this is function Alex suggested but so far not needed



if (feeder == 1){
  relay_SetStatus(ON, OFF);//turn on RELAY_1
  delay(2000);//delay 2s
  relay_SetStatus(OFF, OFF);//turn off RELAY_1
  feeder =0;
  
}

if (feeder == 2){
  relay_SetStatus(OFF, ON);//turn on RELAY_1
  delay(2000);//delay 2s
  relay_SetStatus(OFF, OFF);//turn off RELAY_1
  feeder=0;
}

if (feeder == 0){
  relay_SetStatus(OFF, OFF);//turn off both relays
}
}
}


//I'm not sure what the code below does.  It was part of the arduino example I started with
void relay_init(void)//initialize the relay
{
  //set all the relays OUTPUT
  pinMode(IN1, OUTPUT);
  pinMode(IN2, OUTPUT);
  relay_SetStatus(OFF, OFF); //turn off all the relay
}
//set the status of relays
void relay_SetStatus( unsigned char status_1,  unsigned char status_2)
{
  digitalWrite(IN1, status_1);
  digitalWrite(IN2, status_2);
}




