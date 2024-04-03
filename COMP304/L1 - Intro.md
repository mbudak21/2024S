## What is an Operating System?
Intermediary between user and hardware resources.
1) Provide resource abstraction 
2) Manage and coordinate resources
3) Provide security and protection via system calls (lets the process transition from usermode to kernel mode)
4) Provide fairness among users (or programs), multiprogramming:= CPU scheduling

## Computer Startup
- **Bootstrap** program is loaded at power-up or reboot, also known as BIOS/UEFI
	Typically stored in ROM, known as firmware
	Initializes all aspects of a system
	Then, grub loads kernel into main memory and starts execution

- **init** or systemd is the first process in Linux 
- **Process** an active program

## Interrupts
An OS is interrupt driven, it waits for events to occur
1) Device or Hardware interrupts
- I/O device is done or
- Hardware throws exception
1) Software Interrupts
- A trap or exception is a software generated interrupt caused either by an error or a user request (system call)

**Interrupt Vector:** Contains the addresses of all the service routines for interrupt handling

