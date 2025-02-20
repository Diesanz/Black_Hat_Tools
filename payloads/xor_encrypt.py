
def xor_encrypt(data, key):
	return bytes([b ^key for b in data])

def xor_decrypt(data, key):
	return xor_encrypt(data, key)
	
# Ejemplo con shellcode
shellcode = b"\xfc\x48\x83\xe4\xf0\xe8\xc8\x00\x00\x00"  # Shellcode de ejemplo
key = 0x55  # Clave XOR

encrypted_shell = xor_encrypt(shellcode, key)
print("Shellcode XOR encrypt: ", encrypted_shell.hex())

decrypted_shell = xor_decrypt(encrypted_shell, key)
print("Shellcode XOR descrypt:", decrypted_shell.hex())
