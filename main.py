'''
Initial "hello world" test case written in BrainFuck
>++++++++[<+++++++++>-]<.
>++++[<+++++++>-]<+.
+++++++..
+++.
>>++++++[<+++++++>-]<++.
------------.
>++++++[<+++++++++>-]<+.
<.
+++.
------.
--------.
>>>++++[<++++++++>-]<+.

What does it all mean?!
> shifts to the right one cell
< shifts to the left one cell
+ increments the value of the current cell
- decrements the value of the current cell
[ begins a loop using value of current cell as the case, decrease to NULL
] ends a loop
. ends a "line" of code
, read a character from input and store to memory
'''

'''
Things to add:
Parenthesis counter/matching
Process counter
For loop func, include int k for loop condition. Pass value of register through for writing loop.
'''

class BFtoPy:
    registers = [0 for x in range(30000)]

    def __init__(self, text: str):
        self.bf_code = text

    def loop(self, loop_func: str, current_register: int):
        condition = current_register
        print(f'current_register = {current_register} and the value is {self.registers[current_register]}')
        while self.registers[condition] > 0:
            for i, elem in enumerate(loop_func):
                if elem == '+':
                    self.registers[current_register] += 1
                    print(f'Counting Up {self.registers[current_register]} in register {current_register}')

                elif elem == '-':
                    self.registers[current_register] -= 1
                    #print(f'Counting Down {self.registers[current_register]} in register {current_register}')

                elif elem == '>':
                    current_register += 1
                elif elem == '<':
                    current_register -= 1
            #print(self.registers[0])
            #self.registers[condition] -= 1


    '''error here: looping through [code], but reading and executing [code] after passing it to self.loop()
    might mean unpacking string in a different way... 
    while loop?'''
    def interpretBF(self, bf_code: str):
        reg_manip = 0
        for i, elem in enumerate(bf_code):
            #print(elem)
            if elem == '>':
                reg_manip += 1
            elif elem == '<':
                reg_manip -= 1
            elif elem == '+':
                self.registers[reg_manip] += 1
                #print(f'Counting Up {self.registers[reg_manip]}')

            elif elem == '-':
                self.registers[reg_manip] -= 1
                #print(f'Counting Down {self.registers[reg_manip]}')
            elif elem == '[':
                right_sq = self.matchBracket(i)
                self.loop(bf_code[i+1:right_sq:], reg_manip)
            elif elem == '.':
                print(self.registers[reg_manip])
                print(chr(self.registers[reg_manip]))

    '''returns an index value for matching parenthesis/bracket'''
    def matchBracket(self, bf_code_index) -> int:
        bracket_count = 1
        while bracket_count > 0:
            if self.bf_code[bf_code_index] == '[':
                bracket_count += 1
            elif self.bf_code[bf_code_index] == ']':
                bracket_count -= 1
            bf_code_index += 1
        return bf_code_index



text = open('./hell.bf', 'r')
data = text.read()
print(ord('e'))

answer = BFtoPy(data)
answer.interpretBF(data)
#print(answer.registers)
#print(len(answer.registers))