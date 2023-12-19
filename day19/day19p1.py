from typing import Dict

def process_part(part: Dict[str, int], workflow_id: str):
    global workflows
    if workflow_id == 'A':
        return True
    if workflow_id == 'R':
        return False
    
    rules, second_workflow_id = workflows[workflow_id]

    for key, operator, val, result in rules:
        if operator == '>':
            if part[key] > val:
                return process_part(part, result)
        elif operator == '<':
            if part[key] < val:
                return process_part(part, result)
        else:
            print('ERROR: Invalid operator')
            exit(1)
    return process_part(part, second_workflow_id)
    

raw_workflows, raw_parts = open('input.txt','r').read().split('\n\n')

raw_workflows = raw_workflows.split('\n')
raw_parts = raw_parts.split('\n')

workflows = {}

for workflow in raw_workflows:
    workflow_id, workflow_rules = workflow[:-1].split('{')
    workflow_rules = workflow_rules.split(',')

    workflows[workflow_id] = ([], workflow_rules.pop())

    for rule in workflow_rules:
        comp, result = rule.split(':')
        key = comp[0]
        operator = comp[1]
        val = int(comp[2:])
        workflows[workflow_id][0].append((key, operator, val, result))


total = 0
for raw_part in raw_parts:
    part = {}
    for key_val in raw_part[1:-1].split(','):
        key, val = key_val.split('=')
        part[key] = int(val)
    if process_part(part, 'in'):
        total += sum(part.values())

print(total)