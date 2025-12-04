import sys

N = int(sys.stdin.readline())

tree = {}

for _ in range(N):
    root, left, right = sys.stdin.readline().split()
    tree[root] = [left, right] #{'A' = ['B', 'C'], 'B': ['D',...]}

def order1(node):
    if node == '.':
        return
    print(node, end='') #루트
    order1(tree[node][0]) #왼쪽
    order1(tree[node][1]) #오른쪽

def order2(node):
    if node == '.':
        return
    order2(tree[node][0]) #왼쪽
    print(node, end='') #루트
    order2(tree[node][1]) #오른쪽


def order3(node):
    if node == '.':
        return
    order3(tree[node][0]) #왼쪽
    order3(tree[node][1]) #오른쪽
    print(node, end='') #루트

order1('A')
print()
order2('A')
print()
order3('A')