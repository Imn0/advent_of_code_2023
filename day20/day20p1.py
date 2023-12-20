from typing import List
from collections import deque


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

low_pulses = 0
high_pulses = 0


for _ in range(1000):
    low_pulses += 1
    queue = deque([("broadcaster", x, 0) for x in broadcast_targets])

    while queue:
        source, target, pulse = queue.popleft()
        low_pulses, high_pulses = (low_pulses + 1, high_pulses) if pulse == 0 else (low_pulses, high_pulses + 1)

        if target not in modules:
            continue

        module = modules[target]

        if module.module_type == '%' and pulse == 0:
            module.memory = 1 if module.memory == 0 else 0
            for output in module.outputs:
                queue.append((target, output, module.memory))
        
        if module.module_type == '&':
            module.memory[source] = pulse
            output = 0 if all(module.memory.values()) else 1
            for x in module.outputs:
                queue.append((module.module_id, x, output))

print(low_pulses * high_pulses)