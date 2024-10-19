class VM:
    def __init__(self):
        self.regs = {'A': 0, 'B': 0, 'C': 0, 'D': 0}
        self.pc = 0
        self.prog = []

    def load(self, program):
        self.prog = program
        self.pc = 0

    def run(self):
        while self.pc < len(self.prog):
            inst = self.prog[self.pc]
            self.execute(inst)
            self.pc += 1

    def execute(self, inst):
        opcode, *operands = inst.split()

        if opcode == 'SET':
            register, value = operands
            self.regs[register] = int(value)
        elif opcode == 'ADD':
            dest, s1, s2 = operands
            self.regs[dest] = self.regs[s1] + self.regs[s2]
        elif opcode == 'SUB':
            dest, s1, s2 = operands
            self.regs[dest] = self.regs[s1] - self.regs[s2]
        elif opcode == 'MUL':
            dest, s1, s2 = operands
            self.regs[dest] = self.regs[s1] * self.regs[s2]
        elif opcode == 'DIV':
            dest, s1, s2 = operands
            if self.regs[s2] == 0:
                raise ValueError("division by zero")
            self.regs[dest] = self.regs[s1] // self.regs[s2]
        elif opcode == 'PRINT':
            register = operands[0]
            print(f"register {register} value: {self.regs[register]}")
        else:
            raise ValueError(f"unknown opcode: {opcode}")
        
vm = VM()

program = [
    "SET A 3",
    "SET B 4",
    "ADD C A B",
    "PRINT C"
]

vm.load(program)
vm.run()
