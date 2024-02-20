def find_chessboard_pos(pawn):
    horizontal = {0: "a", 1: "b", 2: "c", 3: "d", 4: "e", 5: "f", 6: "g", 7: "h"}
    vertical = {0: "8", 1: "7", 2: "6", 3: "5", 4: "4", 5: "3", 6: "2", 7: "1"}
    return f"{horizontal[pawn[1]]}{vertical[pawn[0]]}"


chessboard = []
white_pawn = []
black_pawn = []

for i in range(8):
    row = input().split()
    chessboard.append(row)
    if "w" in row:
        white_pawn = [i, row.index("w")]
    if "b" in row:
        black_pawn = [i, row.index("b")]

directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "up_left": (-1, -1),
    "up_right": (-1, 1),
    "down_left": (1, -1),
    "down_right": (1, 1),
}
while white_pawn[0] > 0 and black_pawn[0] < 7:
    up_left_row, up_left_col = white_pawn[0] + directions["up_left"][0], white_pawn[1] + directions["up_left"][1]
    up_right_row, up_right_col = white_pawn[0] + directions["up_right"][0], white_pawn[1] + directions["up_right"][1]
    up_row, up_col = white_pawn[0] + directions["up"][0], white_pawn[1] + directions["up"][1]

    down_left_row, down_left_col = black_pawn[0] + directions["down_left"][0], black_pawn[1] + directions["down_left"][
        1]
    down_right_row, down_right_col = black_pawn[0] + directions["down_right"][0], black_pawn[1] + \
                                     directions["down_right"][1]
    down_row, down_col = black_pawn[0] + directions["down"][0], black_pawn[1] + directions["down"][1]

    if 0 <= up_left_row < len(chessboard) and 0 <= up_left_col < len(chessboard):
        if chessboard[up_left_row][up_left_col] == "b":
            white_pawn = [up_left_row, up_left_col]
            print(f"Game over! White win, capture on {find_chessboard_pos(white_pawn)}.")
            break

    if 0 <= up_right_row < len(chessboard) and 0 <= up_right_col < len(chessboard):
        if chessboard[up_right_row][up_right_col] == "b":
            white_pawn = [up_right_row, up_right_col]
            print(f"Game over! White win, capture on {find_chessboard_pos(white_pawn)}.")
            break

    chessboard[white_pawn[0]][white_pawn[1]] = "-"
    white_pawn = [up_row, up_col]
    chessboard[up_row][up_col] = "w"

    if up_row == 0:
        print(f"Game over! White pawn is promoted to a queen at {find_chessboard_pos(white_pawn)}.")
        break

    if 0 <= down_left_row < len(chessboard) and 0 <= down_left_col < len(chessboard):
        if chessboard[down_left_row][down_left_col] == "w":
            black_pawn = [down_left_row, down_left_col]
            print(f"Game over! Black win, capture on {find_chessboard_pos(black_pawn)}.")
            break

    if 0 <= down_right_row < len(chessboard) and 0 <= down_right_col < len(chessboard):
        if chessboard[down_right_row][down_right_col] == "w":
            black_pawn = [down_right_row, down_right_col]
            print(f"Game over! Black win, capture on {find_chessboard_pos(black_pawn)}.")
            break

    chessboard[black_pawn[0]][black_pawn[1]] = "-"
    black_pawn = [down_row, down_col]
    chessboard[down_row][down_col] = "b"

    if down_row == 7:
        print(f"Game over! Black pawn is promoted to a queen at {find_chessboard_pos(black_pawn)}.")
        break
