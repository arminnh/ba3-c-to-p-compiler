#include <stdio.h>

void main() {
   int i = 0;
   char ch;

   for (i = 0; i < 256; i++) {
      printf("%c ", ch);
      ch = (char) ((int) ch + 1);
      //ch = ch + (char) 1;
   }
}
