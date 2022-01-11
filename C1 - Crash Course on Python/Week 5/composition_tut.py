
class CPU:

    def __init__(self, cores, speed):
        self.cores = cores
        self.speed = speed

    def cpu_start(self):
        print(f"CPU has {self.cores} cores and {self.speed}GHz speed ")


class RAM:

    def __init__(self, capacity, speed):
        self.capacity = capacity
        self.speed = speed

    def ram_initialize(self):
        print(
            f'RAM initialized with {self.capacity} memory and {self.speed}GHz speed')


class Motherboard:

    def __init__(self, slot, iopins):
        self.slot = slot
        self.iopins = iopins

    def motherboard_initialize(self):
        print(
            f'Motherboard switched on with {self.iopins} pins and {self.slot} RAMs')


class Computer:

    def __init__(self, cpu, ram, motherboard):
        self.cpu = cpu
        self.ram = ram
        self.motherboard = motherboard

    def computer_ON(self):
        print(f'Computer powering ON')


meralaptop = Computer(CPU(4, 3), RAM(8, 2), Motherboard(2, 10))


meralaptop.computer_ON()
meralaptop.cpu.cpu_start()
meralaptop.ram.ram_initialize()
meralaptop.motherboard.motherboard_initialize()
