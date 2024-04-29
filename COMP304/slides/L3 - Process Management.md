![[Pasted image 20240429111856.png]]

**Multiprogramming** enables N programs to be space-muxed in executable memory, and time-muxed across the CPU.

## Process States
As a process executes, it changes its state
- **new**: The process is being created
- **running**: Instructions are being executed
 - **waiting**: The process is waiting for some event (e.g., IO) to occur
 - **ready**: The process is waiting to be assigned to a CPU
 - **terminated**: The process has finished execution

## Process Control Block (PCB)

