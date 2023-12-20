from typing import List
from collections import deque
import math

def lcm(a, b):
    return abs(a * b) // math.gcd(a, b)

class Module:
    def __init__(self, module_id: str, module_type: chr, outputs: List[str]):
        self.module_id = module_id
        self.module_type = module_type
        self.outputs = outputs
        self.connections = []

        if self.module_type == '%':
            self.memory = 0

        if self.module_type == '&':
            self.memory = {}


modules = {}
broadcast_targets = {}


for line in open("input.txt"):
    l, r = line.strip().split(" -> ")
    out = r.split(", ")
    if l == 'broadcaster':
        broadcast_targets = out
        continue
    modules[l[1:]] = Module(l[1:], l[0], out)


for name, module in modules.items():
    for output in module.outputs:
        if output in modules and modules[output].module_type == '&':
            modules[output].memory[name] = 0

# for name, module in modules.items():
#     print(name, module.module_type, module.outputs, module.memory)
[input_to_rx] = [module_id for module_id, module in modules.items() if 'rx' in module.outputs]
cycles = {module_id: None for module_id, module in modules.items() if input_to_rx in module.outputs}

count = 0
found = False
while not found:

    queue = deque([("broadcaster", x, 0) for x in broadcast_targets])
    count += 1
    
    while queue:
        source, target, pulse = queue.popleft()

        if target not in modules:
            continue

        module = modules[target]

        if module.module_id == input_to_rx and pulse == 1:
            if cycles[source] is None:
                cycles[source] = count

        if all(cycles.values()):
            found = True
            break
            
        if module.module_type == '%' and pulse == 0:
            module.memory = 1 if module.memory == 0 else 0
            for output in module.outputs:
                queue.append((target, output, module.memory))
        
        if module.module_type == '&':
            module.memory[source] = pulse
            output = 0 if all(module.memory.values()) else 1
            for x in module.outputs:
                queue.append((module.module_id, x, output))


result_lcm = 1
for value in cycles.values():
    result_lcm = lcm(result_lcm, value)
print(result_lcm)