import sys
from collections import defaultdict, deque

def parse_file(file):
    with open(file, 'r') as f:
        return [line.rstrip() for line in f]

def get_orders(lines):
    order = defaultdict(list)
    for line in lines:
        if '|' not in line:
            continue
        l = line.split('|')
        order[int(l[0])].append(int(l[1]))
    return order

def get_updates(lines):
    updates = []
    for line in lines:
        if not ',' in line:
            continue
        updates.append(list([int(x) for x in line.split(',')]))
    return updates

file_name = sys.argv[1] if len(sys.argv) >= 2 else 'input.txt'
lines = parse_file(file_name)
orders = get_orders(lines)

ordered = get_updates(lines)

for update in get_updates(lines):
    for page in orders.keys():
        if page in update:
            for after in orders[page]:
                try:
                    if not update.index(page) < update.index(after):
                        ordered.remove(update)
                except:
                    pass



total = 0
for update in ordered: total += update[len(update)//2]
print(total)

unordered = [x for x in get_updates(lines) if x not in ordered]

def resolve_order(orders, unordered):
    def dag(nodes, dependencies):
        in_degree = {node: 0 for node in nodes}
        for node, deps in dependencies.items():
            for dep in deps:
                in_degree[dep] += 1
        
        queue = deque([node for node in nodes if in_degree[node] == 0])
        sorted_order = []

        while queue:
            current = queue.popleft()
            sorted_order.append(current)

            for dep in dependencies[current]:
                in_degree[dep] -= 1
                if in_degree[dep] == 0:
                    queue.append(dep)

        return sorted_order

    results = []
    for update in unordered:
        nodes = set(update)
        dependencies = defaultdict(list)
        for page, afters in orders.items():
            if page in nodes:
                dependencies[page].extend(after for after in afters if after in nodes)

        sorted_update = dag(nodes, dependencies)
        results.append(sorted_update)

    return results

 
total2 = 0
for update in resolve_order(orders, unordered): total2 += update[len(update)//2]
print(total2)