int button[]={2,3,4,5};//can be added more as per need.//2 for enter
                                                       //3 for mouse toggle
                                                       //4 for s as keyboard and left click as mouse
                                                       //5 for space as keyboard and right click as mouse
long int instant1;
bool signalSent[]={false,false,false};


void setup() {
for (int i=0;i<4;i++){
  pinMode(button[i], INPUT);
}
  Serial.begin(115200); 
}

void loop() {
while(digitalRead(button[3])){
  instant1= millis();
  
  label :
    send_button_signals();
    if((millis()-instant1)<=1){
       send_joystick_signals();  
       goto label;
     }
    else if(((millis()-instant1)>1) && ((millis()-instant1)<15)){
        Serial.print(1);
        Serial.println(1);
        goto label;
      }
     else if(((millis()-instant1)>=15)){
        Serial.print(1);
        Serial.println(1);
      }
  }

  
     if(!(digitalRead(button[3]))){
       send_button_signals();
       send_joystick_signals();
      }

}

void send_joystick_signals(){
       if(analogRead(A1)<250){
       Serial.print(0);//down_button_press
          }
       else if(analogRead(A1)>750){
       Serial.print(2);//up_button_press
          }
       else
       Serial.print(1);//up/down_button_release
    
       if(analogRead(A0)<250){
       Serial.println(0);//left_button_press
        }
       else if(analogRead(A0)>750){
       Serial.println(2);//right_button_press
            }
       else 
       Serial.println(1);//left/right_button_release
  }

  void send_button_signals(){
    Serial.print("m");//tells that the packet of "signals" starts here.
    for(int i=0;i<3;i++){
        if (digitalRead(button[i]) == HIGH && signalSent[i]) {
        Serial.print(0);
         }
       if (digitalRead(button[i]) == HIGH && !signalSent[i]) {
        Serial.print(1);
           signalSent[i] = true;
         }
       if (digitalRead(button[i]) == LOW) {
           Serial.print(0);
           signalSent[i] = false;
         }    
    }
    Serial.print(digitalRead(button[3]));
}
