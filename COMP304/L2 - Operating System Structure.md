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
- 