// so we can see BlinkM_funcs working
#define BLINKM_FUNCS_DEBUG 1

/* BlinkM dependencies */
#include "Wire.h"
#include "BlinkM_funcs.h"

/* rF dependencies */
#include <SPI.h>
#include "nRF24L01.h"
#include "RF24.h"

/* rF configuration */
RF24 radio(9,10); 

int blinkm_addr = 0x09;
const uint64_t pipes[2] = { 0xF0F0F0F0E1LL, 0xF0F0F0F0D2LL };
typedef enum { role_ping_out = 1, role_pong_back } role_e;
const char* role_friendly_name[] = { "invalid", "Ping out", "Pong back"};
// Set default role
role_e role = role_pong_back;

/* Function Prototypes */
void send_LB(blinkm_script_line *script_lines, uint8_t script_len, uint8_t delay_sec);
void check_receive(void);
uint8_t readSerialString(void);
void realloc_read_buf(blinkm_script_line *orig_ptr, uint8_t script_len);

/* Utility declarations */
const char *ACK = "ACK";
const unsigned int max_script_lines = 255; // max capacity of uint8_t
static void setup_blinkM();
static void setup_radio();

typedef struct _lightscript_header {
  uint8_t num_lines;
  uint8_t delay_sec;
} lightscript_header;

lightscript_header *READ_HEAD_BUF;
blinkm_script_line *READ_BUF;

/* Hard-coded lightscripts for testing purposes */
blinkm_script_line script1_lines[] = {
  { 10, { 'n', 0xfe,0xfe,0xfe}},
  { 5, { 'n', 0x00,0x00,0x00}},
  { 10, { 'n', 0xfe,0xfe,0xfe}},
  { 5, { 'n', 0x00,0x00,0x00}}
};
blinkm_script_line script2_lines[] = {
  { 10, { 'n', 0xfe,0x00,0x00}},
  { 10, { 'n', 0x00,0xfe,0x00}},
  { 10, { 'n', 0x00,0x00,0xfe}},
  { 1, { 'n', 0x00,0x00,0x00}}
};
uint8_t script1_len = 4;
uint8_t script2_len = 4;

// Basic flash-red script for testing
blinkm_script_line flash_red_lines[] = {
  { 10, { 'n', 0xfe,0x00,0x00}},
  { 5, { 'n', 0x00,0x00,0x00}},
  { 10, { 'n', 0xfe,0x00,0x00}},
  { 5, { 'n', 0x00,0x00,0x00}}
};
int flash_red_len = 4;

/* Temporary variables for presentation*/
const int beanNum = 0;
const int buttonInput = 2;
const int delayButtonInput = 3;
static void playback(void);
unsigned long lastPress = 0;

char serInStr[30];  // array that will hold the serial input string


void help()
{
  Serial.println("\r\nBlinkMScriptWriter!\r\n"
                 "'p' to write the script and play once\r\n"
                 "'s' to send the script to nearby nodes\r\n"
                 "'o' to stop script playback\r\n"
                 "'0' to fade to black\r\n"
                 "'f' to flash red\r\n"
                 );
}

/* Main Code */

void setup()
{
  setup_blinkM();
  setup_radio();
  READ_HEAD_BUF = (lightscript_header *) malloc(sizeof(lightscript_header) * 8);
  if (!READ_HEAD_BUF) { Serial.println("ERROR: could not allocate READ_HEAD_BUF"); }
}

void loop()
{
    check_receive();
    
    //temporary: check for button input and send if necessary
    if (digitalRead(buttonInput) == HIGH) {
      unsigned long pressTime = millis();
      if (pressTime - lastPress > 1000) {
        lastPress = pressTime;
        Serial.print("Button pressed. Broadcasting behavior.\r\n");
        BlinkM_writeScript( blinkm_addr, 0, script2_len, 0, script2_lines);
        BlinkM_playScript( blinkm_addr, 0,1,0 );
        send_LB(script2_lines, script2_len, 0);
        Serial.print("\r\ncmd>");
      }
    }
    if (digitalRead(delayButtonInput) == HIGH) {
      unsigned long pressTime = millis();
      if (pressTime - lastPress > 1000) {
        lastPress = pressTime;
        Serial.print("Button pressed. Broadcasting behavior.\r\n");
        BlinkM_writeScript( blinkm_addr, 0, script2_len, 0, script2_lines);
        BlinkM_playScript( blinkm_addr, 0,1,0 );
        send_LB(script2_lines, script2_len, 2);
        Serial.print("\r\ncmd>");
      }
    }
        
  
    //read the serial port and create a string out of what you read
    if( readSerialString() ) {
        Serial.println(serInStr);
        char cmd = serInStr[0];
        int num = atoi(serInStr+1);
        if ( cmd == 'p' ) {
          Serial.println("Sending command on serial to blinkM...");
          BlinkM_writeScript( blinkm_addr, 0, script1_len, 0, script1_lines);
          Serial.println("Sent. Playing script...");
          BlinkM_playScript( blinkm_addr, 0,1,0 );
          Serial.print("\r\ncmd>");
        }
        else if ( cmd == 's') {
          send_LB(script2_lines, script2_len, 0);
          Serial.print("\r\ncmd>");
        }
        else if( cmd == 'o' ) {
          Serial.println("Stopping Script 0");
          BlinkM_stopScript( blinkm_addr );
          Serial.print("\r\ncmd>");
        }
        else if( cmd =='0' ) {
            Serial.println("Fade to black");
            BlinkM_fadeToRGB( blinkm_addr, 0,0,0);
            Serial.print("\r\ncmd>");
        }
        else if( cmd =='f' ) {
            Serial.println("Flash red");
            BlinkM_writeScript( blinkm_addr, 0, flash_red_len, 0, flash_red_lines);
            BlinkM_playScript( blinkm_addr, 0,1,0 );
            Serial.print("\r\ncmd>");
        }
    }
}

//read a string from the serial and store it in an array
//you must supply the array variable
uint8_t readSerialString()
{
  if(!Serial.available()) {
    return 0;
  }
  delay(10);  // wait a little for serial data
  int i = 0;
  while (Serial.available()) {
    serInStr[i] = Serial.read();   // FIXME: doesn't check buffer overrun
    i++;
  }
  serInStr[i] = 0;  // indicate end of read string
  return i;  // return number of chars read
}

static void setup_blinkM()
{
    BlinkM_beginWithPower();

    BlinkM_setAddress( blinkm_addr );
    
    Serial.begin(19200); 
    byte rc = BlinkM_checkAddress( blinkm_addr );
    if( rc == -1 ) 
        Serial.println("\r\nno response");
    else if( rc == 1 ) 
        Serial.println("\r\naddr mismatch");

    help();
    Serial.print("cmd>");
}

static void setup_radio()
{
    radio.begin();
    radio.setRetries(15,15);
    
    // Become the primary receiver (pong back)
    role = role_pong_back;
    radio.openWritingPipe(pipes[1]);
    radio.openReadingPipe(1,pipes[0]);
    radio.startListening();
}


// wait for header first!
void check_receive()
{
  if (!radio.available()) { return; }
  /* Check header */
  bool found_header = false;
  while (!found_header)
  {
    Serial.println("Attempting to read header...");
    found_header = radio.read( READ_HEAD_BUF, sizeof(lightscript_header));
  }
  uint8_t script_len = READ_HEAD_BUF->num_lines;
  uint8_t delay_sec = READ_HEAD_BUF->delay_sec;
  Serial.print("Got header and will malloc read buffer with # lines: ");
  Serial.println(script_len);
  Serial.print("Header dictates playback delay of seconds: ");
  Serial.println(delay_sec);
  realloc_read_buf(READ_BUF, script_len);
  unsigned long temp_buf;
  
  /* Read payload */
  bool done = false;
  uint8_t curr_line = 0;
  while (!done)
  {
    // Fetch the payload, and see if this was the last one.
    if (!radio.available()) {
      continue; // spin if nothing available, does not account for packet loss
    }
    radio.read(&READ_BUF[curr_line], sizeof(blinkm_script_line));
    Serial.print("Got line with dur: ");
    Serial.println(READ_BUF[curr_line].dur, DEC);
    curr_line++;
    if (curr_line >= script_len) {
      done = true;
    }
  }
  
  // Play script TODO: make function
  delay(delay_sec * 1000);
  BlinkM_writeScript( blinkm_addr, 0, script_len, 0, READ_BUF);
  BlinkM_playScript( blinkm_addr, 0,1,0 );
  Serial.print("\r\ncmd>");
}

void send_LB(blinkm_script_line *script_lines, uint8_t script_len,
              uint8_t delay_sec)
{
  Serial.println("Setting this node as transmitter...");
  role = role_ping_out;
  radio.stopListening();
  radio.openWritingPipe(pipes[0]);
  radio.openReadingPipe(1,pipes[1]);
  Serial.println("done.");

  /* Send header */
  lightscript_header header;
  header.num_lines = script_len;
  header.delay_sec = delay_sec;
  Serial.print("Sending header--script len is: ");
  Serial.println(header.num_lines);
  Serial.print("Sending with delay: ");
  Serial.println(header.delay_sec);
  bool ok = radio.write(&header, sizeof(lightscript_header));
  if (ok)
    Serial.println("Send ok... ");
  else
    Serial.println("Send failed.");

  delay(500);
  /* Send main script */
  Serial.println("Now sending: ");
  for (int i = 0; i < script_len; i++)
  {

    ok = radio.write(&script_lines[i], sizeof(blinkm_script_line));
    if (ok)
      Serial.println("Send line ok... ");
    else {
      Serial.println("Send line failed. Trying again...");
      i--;
    }
  }
  
  Serial.println("Setting back as receiver");
  role = role_pong_back;
  radio.openWritingPipe(pipes[1]);
  radio.openReadingPipe(1,pipes[0]);
  radio.startListening();
  Serial.print("done.");
}

void realloc_read_buf(blinkm_script_line *orig_ptr, uint8_t script_len)
{
  READ_BUF = (blinkm_script_line *) realloc(orig_ptr, script_len * sizeof(blinkm_script_line));
  for (int i = 0; i < script_len; i++)
  {
    memset(&READ_BUF[i], 0, sizeof(blinkm_script_line));
  }
}

void free_read_buf(blinkm_script_line *buffer, uint8_t script_len)
{
  free(buffer);
}







