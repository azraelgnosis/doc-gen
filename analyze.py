import os

dir_path = os.path.dirname(__file__)
filename = "sample.py"

file_path = os.path.join(dir_path, filename)

class Module:
    __slots__ = ["name", "classes", "functions"]

    def __init__(self, name):
        self.name = name

    def __repr__(self): f"{self.name}"

with open(file_path) as f:
    module_name = f.name.split("\\")[-1].split(".")[0]

module = Module(module_name)