def lines(file):
    for line in file:
        yield line
        yield '\n'

def blocks(file):
    block = []

    for line in lines(file):
        if line.strip():
            block.append(line)
        elif block:
            yield ''.join(block).strip()
            block = []

'''f = open(r'test.txt')
file = f.readlines()
for b in blocks(file):
    print(b)'''