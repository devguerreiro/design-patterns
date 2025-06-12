class CPU:
    def turn_on(self):
        return "CPU ok!"


class Memory:
    def load(self):
        return "Memory ok!"


class Disk:
    def read(self):
        return "Disk ok!"


class Computer:
    def boot(self):
        cpu = CPU()
        memory = Memory()
        disk = Disk()

        return [cpu.turn_on(), memory.load(), disk.read(), "System started!"]


computer = Computer()

assert computer.boot() == [
    "CPU ok!",
    "Memory ok!",
    "Disk ok!",
    "System started!",
]
