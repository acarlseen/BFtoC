registers = [0 for x in range(10)]
current_register = 0
current_register += 1
registers[current_register] += 8 
for x in range(registers[current_register]): 
	current_register -= 1
	registers[current_register] += 9 
	current_register += 1
	registers[current_register] -= 1 
current_register -= 1
print(chr(registers[current_register])) 
current_register += 1
registers[current_register] += 4 
for x in range(registers[current_register]): 
	current_register -= 1
	registers[current_register] += 7 
	current_register += 1
	registers[current_register] -= 1 
current_register -= 1
registers[current_register] += 1 
print(chr(registers[current_register])) 
registers[current_register] += 7 
print(chr(registers[current_register])) 
print(chr(registers[current_register])) 
