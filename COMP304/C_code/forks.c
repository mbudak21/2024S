#include <stdio.h>
#include <unistd.h>

int main(){

  printf("Print1: %d\n", getpid());

  fork();

  printf("%d\n", getpid());
  
}
