class Graph():
    def __init__(self, size):
        self.SIZE = size
        self.graph = [[0 for _ in range(size)] for _ in range(size)]


def print_graph(g):
    print('%9s'% '', end=' ')
    for v in range(g.SIZE):
        print("{0:^9}".format(name_ary[v][0]), end=' ')
    print()
    for row in range(g.SIZE):
        print("%8s" % name_ary[row][0], end=' ')
        for col in range(g.SIZE):
            print("{0:^9}".format(g.graph[row][col]), end=' ')
        print()
    print()


G1 = None
stack = []
visited_ary = []
num = []
name_ary = [['GS25', 30], ['CU', 60], ['Seven11', 10], ['MiniStop', 90], ['Emart24', 40]]
for i in range(0, len(name_ary) - 1):
    i = name_ary[i]

gSize = 5
G1 = Graph(gSize)
G1.graph[0][1] = 1; G1.graph[0][2] = 1
G1.graph[1][0] = 1; G1.graph[1][2] = 1; G1.graph[1][3] = 1
G1.graph[2][0] = 1; G1.graph[2][1] = 1; G1.graph[2][3] = 1
G1.graph[3][1] = 1; G1.graph[3][2] = 1; G1.graph[3][4] = 1
G1.graph[4][3] = 1

current = 0
stack.append(current)
visited_ary.append(current)
num.append(name_ary[current])

while (len(stack) != 0):
    next = None
    for vertex in range(5):
        if G1.graph[current][vertex] == 1:
            if vertex in visited_ary:
                pass
            else:
                next = vertex
                break

    if next != None:
        current = next
        stack.append(current)
        visited_ary.append(current)
        num.append(name_ary[current])
    else:
        current = stack.pop()


print_graph(G1)
print('허니버터칩 최대 보유 편의점(개수) --> ', end='')

maxValue = num[0]

for i in range(1, len(num) - 1):
    if maxValue[1] < num[i][1]:
        maxValue = num[i]
print(f'{maxValue[0]} ( {maxValue[1]} )', end='   ')
