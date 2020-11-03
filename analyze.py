import re
import os

dir_path = os.path.dirname(__file__)
filename = "sample.py"

file_path = os.path.join(dir_path, filename)

class Module:
    __slots__ = ["name", "classes", "functions"]

    def __init__(self, name):
        self.name = name

    def __repr__(self): return f"{self.name}"

class_pattern = "class (\w*)(\(.*\))?:$"
function_pattern = "def (\w*)\(.*\).*:$"

with open(file_path) as f:
    module_name = os.path.basename(f.name).split(".")[0]
    file_contents = f.readlines()

module = Module(module_name)

for line in file_contents:
    words = line.strip().split(" ")
    if words[0] == "class":
        classname = words[1].split("")
    elif words[0] == "def":
        pass

print("done")