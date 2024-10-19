# regvm
A simple register based virtual machine for maths

# usage
```py
vm = VM() # initiate a new virtual machine

# create a program
program = [
  "SET A 4",    # a = 4
  "SET B 20",   # b = 20
  "ADD C A B",  # c = a + b
  "PRINT C"     # print(c)
]

vm.load(program)
vm.run()
```
this is a very basic implementation of a register based VM.
heres a full list of all the instructions which are available.
```
SET
ADD
SUB
MUL
DIV
PRINT
```
