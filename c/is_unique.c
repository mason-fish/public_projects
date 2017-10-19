#include <stdio.h>

/* 
 * Check if a string has any repeated ascii characters in it
 */
int main(int argc, char **argv)
{
  int i, i2;
  int chars[128];
  for (i = 0; i < 128; i++) {
    chars[i] = 0;
  }

  if (argc != 2) {
    printf("Please provide a string to check! (and only one at a time, please)\n");
    return (1);
  }
  
  for (i = 0; argv[1][i] != '\0'; i++) {}

  if (i > 128) {
    printf("Contains duplicates\n");
    return (0);
  }

  for (i2 = 0; i2 <= i; i2++) {
    if (chars[(int)argv[1][i2]]) {
      printf("Contains duplicates\n");
      return (0);
    }
    chars[(int)argv[1][i2]] = 1;
  }

  printf("Is unique!\n");
  return (0);
}
