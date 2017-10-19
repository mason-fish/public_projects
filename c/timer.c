#include <stdio.h>
#include <time.h>

#define LIGHTS 72

void delay(int milliseconds);
int lightDelay(int seconds); 

int main() {
  int seconds;
  int timerDelay;
  int count = LIGHTS;

  puts("How many seconds to set the timer to?\t");
  scanf("%d", &seconds);
  timerDelay = lightDelay(seconds);
  do {
    printf("%d/%d\n", count, LIGHTS);
    delay(timerDelay);
  } while(--count);

  printf("\n\t*****TIME IS UP!*****\n\t%d seconds have passed!\t\n", seconds);
  
  return(0);
}

void delay(int milliseconds) {
  long pause;
  clock_t now,then;

  pause = milliseconds*(CLOCKS_PER_SEC/1000);
  now = then = clock();
  while( (now-then) < pause )
    now = clock();
}

int lightDelay(int seconds) {
  int converted = seconds * 1000 / 72;
  return converted;
}

