
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

  strip.begin(); // Initialize pins for output
  strip.show();  // Turn all LEDs off ASAP
}

// Runs 10 LEDs at a time along strip, cycling through red, green and blue.
// This requires about 200 mA for all the 'on' pixels + 1 mA per 'off' pixel.

int      head  = 0, tail = -1; // Index of first 'on' and 'off' pixels
uint32_t color = 0xFF0000;      // 'On' color (starts red)
int Hdir = 1; // 1 l2r, -1 r2l
int Tdir = 1;
int runs = 5;
void loop() {
  while (runs) {
    strip.setPixelColor(head, color); // 'On' pixel at head
    strip.setPixelColor(tail, 0);     // 'Off' pixel at tail
    strip.show();                     // Refresh strip
    delay(3);                        // Pause 20 milliseconds (~50 FPS)

    head += Hdir;
    tail += Tdir;

    if (head >= NUMPIXELS) {        // Increment head index.  Off end of strip?
      Hdir = -1;                       //  Yes, reset head index to start
      //if((color >>= 8) == 0)          //  Next color (R->G->B) ... past blue now?
      //  color = 0xFF0000;             //   Yes, reset to red
      runs = runs - 1;
    }
    if (head <= 0) {        // Increment head index.  Off end of strip?
      Hdir = 1;                       //  Yes, reset head index to start
      //if((color >>= 8) == 0)          //  Next color (R->G->B) ... past blue now?
      //  color = 0xFF0000;             //   Yes, reset to red
    }
    if (tail >= NUMPIXELS) {
      Tdir = -1;   
    }
    if (tail <= 0) {
      Tdir = 1;
    }
  }
}
