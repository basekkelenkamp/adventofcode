import ast
import csv
from pprint import pprint

# ADD EXTRA WHITESPACE AT END OF INPUT DATA

list_of_boards = []
new_board = []
with open('4.csv', newline='') as inputfile:
    for index, row in enumerate(csv.reader(inputfile)):
        if index == 0:
            list_draw_numbers = [int(x) for x in row]
            continue

        if len(row) == 0:
            if new_board:
                list_of_boards.append(new_board)
            new_board = []

        if len(row) == 1:
            row_stripped = row[0].replace("  ", " ").replace(" ", ",")
            if row_stripped[0] == ",":
                row_stripped = row_stripped[1:]
            new_board.append(list(ast.literal_eval(row_stripped)))


vertical_list_of_boards = []
for board in list_of_boards:
    vertical_list_of_boards.append([list(x) for x in zip(*board)])

pprint(list_of_boards)
print("\n\n")
pprint(vertical_list_of_boards)

combined_boards = [[[[z, False] for z in y] for y in x] for x in list_of_boards]
vertical_combined_boards = [[[[z, False] for z in y] for y in x] for x in vertical_list_of_boards]

bingo = False
for draw_number in list_draw_numbers:

    for index0, (board, vertical_board) in enumerate(zip(combined_boards, vertical_combined_boards)):
        for index1, (row, v_row) in enumerate(zip(board, vertical_board)):

            for index2, (value, vertical_value) in enumerate(zip(row, v_row)):
                if value[0] is draw_number:
                    value[1] = True
                    combined_boards[index0][index1][index2][1] = True

                if vertical_value[0] is draw_number:
                    value[1] = True
                    vertical_combined_boards[index0][index1][index2][1] = True

            print(row)

            # BINGO
            if sum([x[1] for x in row]) is len(row) or sum([x[1] for x in v_row]) is len(v_row):
                # board_sum = 0
                bingo = {
                    "drawn_number": draw_number,
                    "board_winner": index0
                }

                # for _row in board:
                #     for x in _row:
                #         if not x[1]:
                #             board_sum = board_sum + x[0]

print(bingo["board_winner"])
breakpoint()
board_sum = 0
for _row in combined_boards[bingo["board_winner"]]:
    for x in _row:
        if not x[1]:
            board_sum = board_sum + x[0]

print(board_sum, bingo["drawn_number"])
breakpoint()
