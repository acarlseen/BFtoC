#include <stdio.h>

int registers[10] = {0};
int current_register = 0;

int main()
{
	char output;
	current_register += 1;
	registers[current_register] += 8; 
	while (registers[current_register] > 0) 
 	{
		current_register -= 1;
		registers[current_register] += 9; 
		current_register += 1;
		registers[current_register] -= 1; 
	} 
	current_register -= 1;
	printf("%c", registers[current_register]); 
	current_register += 1;
	registers[current_register] += 4; 
	while (registers[current_register] > 0) 
 	{
		current_register -= 1;
		registers[current_register] += 7; 
		current_register += 1;
		registers[current_register] -= 1; 
	} 
	current_register -= 1;
	registers[current_register] += 1; 
	printf("%c", registers[current_register]); 
	registers[current_register] += 7; 
	printf("%c", registers[current_register]); 
	printf("%c", registers[current_register]); 
	return 0; 
}