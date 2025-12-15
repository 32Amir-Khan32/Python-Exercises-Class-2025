class Computer:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
        self.cpu = self.CPU()  # Create CPU object
        self.ram = self.RAM()  # Create RAM object
    
    class CPU:
        def __init__(self):
            self.cores = 4
            self.speed = "3.2 GHz"
        
        def process(self, task):
            print(f"CPU processing: {task}")
    
    class RAM:
        def __init__(self):
            self.capacity = "16 GB"
            self.type = "DDR4"
        
        def allocate(self, amount):
            print(f"RAM allocating: {amount} GB")
        
        def free(self, amount):
            print(f"RAM freeing: {amount} GB")
    
    def display_specs(self):
        print(f"Computer: {self.brand} {self.model}")
        print(f"CPU: {self.cpu.cores} cores @ {self.cpu.speed}")
        print(f"RAM: {self.ram.capacity} {self.ram.type}")
    
    def run_program(self, program_name):
        print(f"\nRunning {program_name}...")
        self.ram.allocate(4)
        self.cpu.process(program_name)
        self.ram.free(4)

# Create computer
my_pc = Computer("Dell", "XPS 15")
my_pc.display_specs()
my_pc.run_program("Python IDE")