
# Q2) 숫자 카드 게임

size_of_card_by_user = input()
size_of_card = list(map(int, size_of_card_by_user.split()))

# maek size_of_card[0] x size_of_card[1]
set_of_card = [[0] * size_of_card[0] for i in range(size_of_card[1])]

for i in range(len(size_of_card[1])):
    row = input()
    row_card = list(map(int, row.split()))

    set_of_card[] = 