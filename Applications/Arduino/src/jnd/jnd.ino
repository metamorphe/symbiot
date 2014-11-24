// Open a serial connection and flash LED when input is received

void setup(){
  // Open serial connection.
  Serial.begin(9600);
  pinMode(13, OUTPUT);
  pinMode(3, OUTPUT);
  pinMode(5, OUTPUT);
  pinMode(6, OUTPUT);

}

// 12 is the maximum length of a decimal representation of a 32-bit integer,
// including space for a leading minus sign and terminating null byte
char buffer[12];
String keyData = "";
String valueData = "";
int delimiter = (int) '\n';
int comma = (int) ',';
bool key = true;

void process(String keyData, String valueData){
    unsigned int n = keyData.length() + 1;
    keyData.toCharArray(buffer, n);
   
    int key = atoi(buffer);

    // Convert ASCII-encoded integer to an int
    n = valueData.length() + 1;
    valueData.toCharArray(buffer, n);
    int value = atoi(buffer);


    value = map(value, 0, 1000, 0, 255);
    analogWrite(key, value);
}
void loop() {
    while (Serial.available()) {
        int ch = Serial.read();
        if (ch == -1) {
            // Handle error
        }
        else if (ch == comma){
            key = false;
            break;
        }
        else if (ch == delimiter) {
            key = true;
            process(keyData, valueData);
            keyData = "";
            valueData = "";
            break;
        }
        else if (key){
            keyData += (char) ch;
        }
        else if(!key){
            valueData += (char) ch;
        }
    }
}
