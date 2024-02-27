## Kernel stuff

### Monolithic Kernel
All the OS services are implemented in the kernel. Fast OS but hard to extend.


### Micro Kernel
Device Driver is outside of the kernel, in the usersapce.
Moves all the nonessential components from the kernel to user level. Smaller kernel, uses messages with system and user-level programs.

I'm guessing these processes are owned by root, therefore somewhat protected from the userspace. In Linux kernel has the PID0 but is not owned by root, systemd however is owned by root.