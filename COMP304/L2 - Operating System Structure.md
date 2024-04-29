**Batch User Interface:** All of the `job` is done in a batch, typically inputted to the OS via a punchcard.

## Operating System Services
- User Interface
- Program Execution
- I/O operations
- File-System manipulation
- Communications
- Error Detection
- Resource Allocation
- Accounting
- Protection and Security

**Mode Bit:** if 0, kernel level if 1, user level
**System Call Table:** Stores all of the registered system calls.
**Make System Call:** `syscall(system_call_number, arguments)`

Memory Protection:
- **Base Register:** Holds the smallest physical address for the process
- **Limit Register:** Contains the size of the range
CPU Protection:
- **Timer:** Timer is decremented every tick, when it reaches 0, an interrupt occurs.



## Kernel stuff

### Monolithic Kernel
All the OS services are implemented in the kernel. Fast OS but hard to extend.

### Micro Kernel
Device Driver is outside of the kernel, in the usersapce.
Moves all the nonessential components from the kernel to user level. Smaller kernel, uses messages with system and user-level programs.

I'm guessing these processes are owned by root, therefore somewhat protected from the userspace. In Linux kernel has the PID0 but is not owned by root, systemd however is owned by root.

### Modular Approach
Load kernel modules at boot or runtime, at need.