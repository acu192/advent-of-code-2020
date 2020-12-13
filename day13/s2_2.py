
with open('input', 'rt') as f:
    _, buses = f.read().strip().splitlines()
    buses = [(int(b), r) for r, b in enumerate(buses.split(',')) if b != 'x']
    buses = [(b, r % b) for b, r in buses]         # some remainders need to be further simplified
    buses = [(b, (b - r) % b) for b, r in buses]   # since we want the time t *before* the bus next arrival


print('find t...\n')

for b, r in buses:
    print('t = {} (mod {})'.format(r, b))

print()


a, step = 0, 1
for b, r in buses:
    while a % b != r:
        a += step
    step *= b

print('final answer:', a)

