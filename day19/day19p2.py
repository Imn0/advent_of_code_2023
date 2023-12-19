from typing import Tuple


def count(ranges: Tuple[int, int], workflow_id: str):
    global workflows
    if workflow_id == 'A':
        r = 1
        for low, high in ranges.values():
            r *= (high - low + 1)
        return r
    if workflow_id == 'R':
        return 0
    
    total = 0
    rules, second_workflow_id = workflows[workflow_id]

    for key, operator, val, result in rules:
        low, high = ranges[key]
        if operator == '>':
            true_path_range = (val + 1, high)
            false_path_range = (low, val)
        elif operator == '<':
            true_path_range = (low, val - 1)
            false_path_range = (val, high)
        else:
            print('ERROR: Invalid operator')
            exit(1)

        if true_path_range[0] <= true_path_range[1]:
            total += count({**ranges, key: true_path_range}, result)

        if false_path_range[0] <= false_path_range[1]:
            ranges[key] = false_path_range

    else:
        total += count(ranges, second_workflow_id)

    return total

raw_workflows, _ = open('smol.txt','r').read().split('\n\n')

raw_workflows = raw_workflows.split('\n')

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


print(count({'x': (1, 4000), 'm': (1,4000), 'a': (1,4000), 's': (1,4000) },'in'))