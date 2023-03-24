'''


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

Potentially calling interpretBF recursively when encountering a left bracket '['
eliminates use of func loop()?
this might mean moving "current_register" to class variables
Pass a new instance of BFtoPy class with substring for matched right brackets ']' 

Basically something like:
if elem == '[':
    bracket_code = self.bf_code[self.bf_point, self.matchBracket
'''

registers = [0 for x in range(30000)]
class BFtoPy:

    def __init__(self, bf_code: str, current_reg = 0):
        self.bf_code = bf_code
        self.bf_code_len = len(bf_code)
        self.bf_point = 0
        self.current_register = current_reg


    def loop(self, loop_func: str, current_register: int):
        print(loop_func)
        condition = current_register
        print(f'current_register = {current_register} and the value is {registers[current_register]}')
        while registers[condition] > 0:
            for i, elem in enumerate(loop_func):
                if elem == '+':
                    registers[current_register] += 1
                    #print(f'Counting Up {registers[current_register]} in register {current_register}')

                elif elem == '-':
                    registers[current_register] -= 1
                    #print(f'Counting Down {registers[current_register]} in register {current_register}')

                elif elem == '>':
                    current_register += 1
                elif elem == '<':
                    current_register -= 1
            #print(registers[0])
            #registers[condition] -= 1


    '''error here: looping through [code], but reading and executing [code] after passing it to self.loop()
    might mean unpacking string in a different way... 
    while loop?
    add a skip that passes the loop while doing nothing?
    recursion???
    
    '''

    def interpretBF(self):
        while self.bf_point in range(self.bf_code_len):
            elem = self.bf_code[self.bf_point]
            if elem == '>':
                self.current_register += 1
            elif elem == '<':
                self.current_register -= 1

            elif elem == '+':
                #print(f'Adding to register {self.current_register} value is {registers[self.current_register]}')
                registers[self.current_register] += 1

            elif elem == '-':
                registers[self.current_register] -= 1
                #print(f'Counting down register {self.current_register} now at {registers[self.current_register]}')


            elif elem == '[':
                loop_cond = registers[self.current_register]
                loop = self.matchBracket()
                print(loop[1:-1])
                bracket = BFtoPy(loop[1:-1], self.current_register)
                while loop_cond > 0:
                    print(f'loop_cond is {loop_cond}')
                    bracket.interpretBF()
                    print(f'Register 0 is at {registers[0]}')
                    loop_cond -= 1
                self.bf_point += len(loop) - 1
                #self.loop(bf_code[i:right_sq:], reg_manip)

            elif elem == ']':
                pass

            elif elem == '.':
                #print(registers[self.current_register])
                print(chr(registers[self.current_register]))
            self.bf_point += 1

    '''returns an index value for matching parenthesis/bracket'''
    def matchBracket(self) -> str:
        bracket_count = 1
        right_bracket = self.bf_point + 1
        while bracket_count > 0 and right_bracket < self.bf_code_len:
            if self.bf_code[right_bracket] == '[':
                bracket_count += 1
            elif self.bf_code[right_bracket] == ']':
                bracket_count -= 1
            right_bracket += 1
        print(str(self.bf_code[self.bf_point: right_bracket]))
        return str(self.bf_code[self.bf_point: right_bracket])



text = open('./hell.bf', 'r')
data = text.read()
#print(ord('e'))
#print(data)

answer = BFtoPy(data)
answer.interpretBF()

print(f'Register 0 is {registers[0]} \n'
      f'Register 1 is {registers[1]}')
#print(answer.registers)
#print(len(answer.registers))