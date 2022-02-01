"""https://ibb.co/QpW3hVD - задание"""
class Nvidia:
    def __init__(self):
        super().__init__()

class GeForce:
    def __init__(self):
        super().__init__()

class AMD:
    def __init__(self):
        super().__init__()

class Intel:
    def __init__(self):
        super().__init__()

class Memory:
    def __init__(self):
        super().__init__()


class GPU(Nvidia, GeForce):
    def __init__(self):
        super().__init__()

class CPU(AMD, Intel):
    def __init__(self):
        super().__init__()

class Motherboard(CPU, GPU, Memory):
    def __init__(self, model_nvidia, model_gf, model_amd, model_intel, memory, type_gpu, type_cpu):
        self.model_nvidia = model_nvidia
        self.model_gf = model_gf
        self.model_amd = model_amd
        self.model_Intel = model_intel
        self.model_memory = memory
        self.type_gpu = type_gpu
        self.type_cpu = type_cpu
        super().__init__()

ex = Motherboard(model_nvidia="model_nvidia 123", model_gf="model_gf 132", model_amd="model_amd 7896", model_intel="model_intel 798", memory="memory 789456", type_gpu="type_gpu 45646", type_cpu="type_cpu asdas")
print(ex.__dict__)
print(CPU.__dict__)

