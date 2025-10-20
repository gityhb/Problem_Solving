import sys

N = int(sys.stdin.readline())

card_list = list(range(1, N+1))

front_index = 0

while len(card_list) - front_index > 1:
    front_index += 1

    card_move = card_list[front_index]
    front_index += 1

    card_list.append(card_move)

print(card_list[front_index])