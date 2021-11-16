
test_puzzle = [
    0, 2, 4, 0, 0, 0, 0, 9, 3,
    0, 1, 0, 3, 0, 2, 0, 6, 0,
    3, 8, 6, 1, 9, 0, 5, 2, 4,
    0, 6, 7, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 4, 0, 1, 2,
    0, 3, 1, 0, 0, 5, 7, 0, 0,
    1, 0, 0, 9, 2, 0, 4, 3, 0,
    0, 0, 3, 0, 5, 0, 2, 0, 6,
    0, 5, 0, 0, 7, 0, 0, 8, 1
]

test_puzzle_hard = [
    0, 1, 0, 0, 3, 5, 0, 0, 0,
    0, 0, 0, 0, 6, 0, 1, 0, 7,
    0, 2, 3, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 6, 0, 2,
    0, 7, 0, 1, 0, 9, 0, 4, 0,
    4, 0, 2, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 8, 7, 0,
    7, 0, 4, 0, 5, 0, 0, 0, 0,
    0, 0, 0, 3, 4, 0, 0, 9, 0
]


def sudoku_solver(puzzle) -> list:
    notes = init_notes(puzzle)

    cell = 0
    passes = 0
    p_snapshot = puzzle.copy()

    while len(notes) > 0:

        if cell in notes:
            update_cell(cell, notes, puzzle)

        # update cell to check, and exit the solver
        # if no progress was made in the pass
        cell = (cell + 1) % len(puzzle)

        if cell == 0:
            passes += 1

        if cell == 0 and p_snapshot == puzzle:
            print("solver got stuck")
            break
        elif cell == 0:
            p_snapshot = puzzle.copy()

    print("passes: {}".format(passes))
    return puzzle


def init_notes(puzzle: list) -> dict:
    notes = {}

    for index, cell in enumerate(puzzle):
        if cell == 0:
            notes[index] = set(i for i in range(1, 10)) - rcb_set(index, puzzle)

    return notes


def update_cell(index, notes, puzzle):
    if len(notes[index]) == 1:
        puzzle[index] = notes[index].pop()
        del notes[index]

    else:
        notes[index] = notes[index] - rcb_set(index, puzzle)


def rcb_set(index, puzzle) -> set:
    r = index // 9
    c = index % 9
    b = (c // 3) + 3 * (r // 3)  # box column + 3 * box row

    row = set()
    column = set()
    box = set()

    for i, v in enumerate(puzzle):
        if i // 9 == r:
            row.add(v)
        if i % 9 == c:
            column.add(v)
        if (((i % 9) // 3) + (3 * ((i // 9) // 3))) == b:
            box.add(v)

    return set.union(row, box, column) - {0}


if __name__ == "__main__":
    puzzle = sudoku_solver(test_puzzle_hard)

    for i in range(9):
        print(puzzle[i*9:(i+1)*9])