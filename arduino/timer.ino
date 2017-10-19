// Simple strand test for Adafruit Dot Star RGB LED strip.
// This is a basic diagnostic tool, NOT a graphics demo...helps confirm
// correct wiring and tests each pixel's ability to display red, green
// and blue and to forward data down the line.  By limiting the number
// and color of LEDs, it's reasonably safe to power a couple meters off
// the Arduino's 5V pin.  DON'T try that with other code!

#include <Adafruit_DotStar.h>
// Because conditional #includes don't work w/Arduino sketches...
#include <SPI.h>         // COMMENT OUT THIS LINE FOR GEMMA OR TRINKET
//#include <avr/power.h> // ENABLE THIS LINE FOR GEMMA OR TRINKET

#define NUMPIXELS 72 // Number of LEDs in strip

// Here's how to control the LEDs from any two pins:
#define DATAPIN    4
#define CLOCKPIN   5
Adafruit_DotStar strip = Adafruit_DotStar(
                           NUMPIXELS, DATAPIN, CLOCKPIN, DOTSTAR_BRG);
// The last parameter is optional -- this is the color data order of the
// DotStar strip, which has changed over time in different production runs.
// Your code just uses R,G,B colors, the library then reassigns as needed.
// Default is DOTSTAR_BRG, so change this if you have an earlier strip.

// Hardware SPI is a little faster, but must be wired to specific pins
// (Arduino Uno = pin 11 for data, 13 for clock, other boards are different).
//Adafruit_DotStar strip = Adafruit_DotStar(NUMPIXELS, DOTSTAR_BRG);

void setup() {

#if defined(__AVR_ATtiny85__) && (F_CPU == 16000000L)
  clock_prescale_set(clock_div_1); // Enable 16 MHz on Trinket                            
#endif
  Serial.begin(9600);
  strip.begin();                                           
  strip.show(); 
  strip.setBrightness(64);                                               
}
            
// This requires about 200 mA for all the 'on' pixels + 1 mA per 'off' pixel.             

#define  LIGHTS 73                            

unsigned long lightDelay(int seconds);


void loop() {
  int seconds = 1;  
  uint32_t color = 0xFF0000;      // 'On' color (starts green) 
  
  while(seconds != 0) {
    unsigned long timerDelay;
    int head = 73;

    Serial.println("How many seconds to set the timer to?\t");
    while (Serial.available() == 0);
  
    int seconds = Serial.parseInt();
    timerDelay = lightDelay(seconds); 
                                                              
    while(head--) {   
      if (head < 5) {
        color = 0x00FF00;
      } 
      strip.setPixelColor(head, color);                                                  
      strip.show();
      delay(timerDelay);
    }
    
    delay(5000);
    head = 73;

    while (head--) {
      strip.setPixelColor(head, 0);
      strip.show();
    }
  }
}

unsigned long lightDelay(int seconds) {
  unsigned long converted = seconds * 1000 / 72;
  return converted;
}

