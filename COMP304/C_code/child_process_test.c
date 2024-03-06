#include <threads.h>
int mypid;

if( (mypid = fork() == 0) ){
  execve("childProgram.out", argv, 0);
  printf("Error in the exec, killing child");
  exit(0);
}


