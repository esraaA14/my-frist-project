
# ملاحظة: الكود دا خاص بلغة Arduino C++، مش Python، لكن هيتحفظ بامتداد .py حسب طلبك

# الكود دا بيتحط في Arduino IDE أو Tinkercad

#include <Keypad.h>
#include <Servo.h>

const byte ROWS = 4;
const byte COLS = 4;
char keys[ROWS][COLS] = {
  {'1','2','3','A'},
  {'4','5','6','B'},
  {'7','8','9','C'},
  {'*','0','#','D'}
};
byte rowPins[ROWS] = {9, 8, 7, 6}; 
byte colPins[COLS] = {5, 4, 3, 2}; 

Keypad keypad = Keypad(makeKeymap(keys), rowPins, colPins, ROWS, COLS);

Servo myServo;
String password = "1234"; // الباسورد
String input = "";

void setup() {
  myServo.attach(10); 
  myServo.write(0); // الباب مقفول
  Serial.begin(9600);
}

void loop() {
  char key = keypad.getKey();
  
  if (key){
    Serial.print(key);
    if(key == '#'){ 
      if(input == password){
        Serial.println(" -> Access Granted");
        myServo.write(90); // فتح الباب
        delay(5000); 
        myServo.write(0); // قفل الباب بعد 5 ثواني
      } else {
        Serial.println(" -> Wrong Password");
      }
      input = "";
    } else if(key == '*'){
      input = ""; // مسح الإدخال
    } else {
      input += key;
    }
  }
}
