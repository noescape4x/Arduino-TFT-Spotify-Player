#include <MCUFRIEND_kbv.h>
#include <Adafruit_GFX.h>

MCUFRIEND_kbv tft;

#define BLACK   0x0000
#define WHITE   0xFFFF
#define GREEN   0x07E0

void setup() {
  Serial.begin(9600);

  // screen setting
  uint16_t ID = tft.readID();
  tft.begin(ID);
  tft.setRotation(1);
  tft.fillScreen(BLACK);
  tft.setTextColor(WHITE);
  tft.setTextSize(2);

  tft.setCursor(20, 50);
  tft.print("Waiting for song...");
}

void loop() {
  // check 
  if (Serial.available()) {
    String receivedText = Serial.readStringUntil('\n');

    if (receivedText.length() > 1) {
      int separatorIndex = receivedText.indexOf('~');
      
      if (separatorIndex > 0) {
        String songName = receivedText.substring(0, separatorIndex);
        String artistName = receivedText.substring(separatorIndex + 1);

        tft.fillScreen(BLACK);
        tft.setCursor(20, 50);
        tft.print("      Now Playing:");
        
        tft.setCursor(20, 80);
        tft.setTextColor(GREEN);
        tft.print(songName);  // song Name

        tft.setCursor(20, 140);
        tft.setTextColor(WHITE);
        tft.print(artistName);  // artist Name
      }
    }
  }
}
