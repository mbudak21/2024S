#include <stdio.h>
#include <unistd.h>

int main(){
  for (int i=0; i<10000; i++){
    fork();
    sleep(1);
    printf("%d\n", getpid());
  }
}
