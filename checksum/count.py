
ID_LENGTH = 14

P1 = (
    (0,	1,	1,	1),
    (1,	1,	1,	0),
    (1,	0,	0,	1),
    (0,	1,	1,	1),
    (1,	1,	1,	0),
    (1,	0,	0,	1),
    (0,	1,	1,	1),
    (1,	1,	1,	0),
    (1,	0,	0,	1),
    (0,	1,	1,	1),
    (1,	1,	1,	0),
    (1,	0,	0,	1),
    (0,	1,	1,	1),
    (1,	1,	1,	0),
    (1,	0,	0,	1)
)

P2 = (
    (0,	1,	1,	2),
    (1,	2,	2,	2),
    (2,	2,	2,	0),
    (2,	0,	0,	2),
    (0,	2,	2,	1),
    (2,	1,	1,	1),
    (1,	1,	1,	0),
    (1,	0,	0,	1),
    (0,	1,	1,	2),
    (1,	2,	2,	2),
    (2,	2,	2,	0),
    (2,	0,	0,	2),
    (0,	2,	2,	1),
    (2,	1,	1,	1),
    (1,	1,	1,	0)
)

list_alpha = {
    "0": (0, 0, 0, 0),
    "1": (0, 0, 0, 1),
    "2": (0, 0, 0, 2),
    "3": (0, 0, 1, 0),
    "4": (0, 0, 1, 1),
    "5": (0, 0, 1, 2),
    "6": (0, 0, 2, 0),
    "7": (0, 0, 2, 1),
    "8": (0, 0, 2, 2),
    "9": (0, 1, 0, 0),
    "A": (0, 1, 0, 1),
    "B": (0, 1, 0, 2),
    "C": (0, 1, 1, 0),
    "D": (0, 1, 1, 1),
    "E": (0, 1, 1, 2),
    "F": (0, 1, 2, 0),
    "G": (0, 1, 2, 1),
    "H": (0, 1, 2, 2),
    "I": (1, 0, 0, 0),
    "J": (1, 0, 0, 1),
    "K": (1, 0, 0, 2),
    "L": (1, 0, 1, 0),
    "M": (1, 0, 1, 1),
    "N": (1, 0, 1, 2),
    "O": (1, 0, 2, 0),
    "P": (1, 0, 2, 1),
    "Q": (1, 0, 2, 2),
    "R": (1, 1, 0, 0),
    "S": (1, 1, 0, 1),
    "T": (1, 1, 0, 2),
    "U": (1, 1, 1, 0),
    "V": (1, 1, 1, 1),
    "W": (1, 1, 1, 2),
    "X": (1, 1, 2, 0),
    "Y": (1, 1, 2, 1),
    "Z": (1, 1, 2, 2)
}

list_reverse = {
    0: "0",
    16: "1",
    32: "2",
    4: "3",
    20: "4",
    36: "5",
    8: "6",
    24: "7",
    40: "8",
    2: "9",
    18: "A",
    34: "B",
    6: "C",
    22: "D",
    38: "E",
    10: "F",
    26: "G",
    42: "H",
    1: "I",
    17: "J",
    33: "K",
    5: "L",
    21: "M",
    37: "N",
    9: "O",
    25: "P",
    41: "Q",
    3: "R",
    19: "S",
    35: "T",
    7: "U",
    23: "V",
    39: "W",
    11: "X",
    27: "Y",
    43: "Z"
}


def join_digits_matrices(matrices: list) -> list:
    joined = []
    for matrix in matrices:
        for char in matrix:
            joined.append(char)

    return joined


def _digit_to_matrix(digit: str) -> tuple:
    return list_alpha[digit]


def digits_to_matrices(digits: str) -> list:
    matrices = []

    for digit in digits:
        matrices.append(_digit_to_matrix(digit))

    return matrices


def check_equation(matrices: list) -> list:  # "folding" in Excel file
    #     [c1, c2, c3, c4] in js implementation
    check = [0, 0, 0, 0]

    matrices = join_digits_matrices(matrices)

    for i in range(14):
        check[0] = check[0] + matrices[i*4] * P1[i][0] + matrices[i*4 + 1] * P1[i][2]
        check[1] = check[1] + matrices[i*4] * P1[i][1] + matrices[i*4 + 1] * P1[i][3]
        check[2] = check[2] + matrices[i*4+2] * P2[i][0] + matrices[i*4 + 3] * P2[i][2]
        check[3] = check[3] + matrices[i*4+2] * P2[i][1] + matrices[i*4 + 3] * P2[i][3]

    check[0] = check[0] % 2
    check[1] = check[1] % 2
    check[2] = check[2] % 3
    check[3] = check[3] % 3

    return check


def reverse_digit(check_matrix: list) -> int:
    q1 = check_matrix[0]  # c1 in js implementation
    q2 = check_matrix[1]  # c2 in js implementation
    c3 = check_matrix[2]
    c4 = check_matrix[3]

    r1 = 0
    r2 = 0

    if c4 == 0:
        r1 = 0
    elif c4 == 1:
        r1 = 2
    elif c4 == 2:
        r1 = 1

    if c3 + r1 == 0:
        r2 = 0
    elif c3 + r1 == 1:
        r2 = 2
    elif c3 + r1 == 2:
        r2 = 1
    elif c3 + r1 == 3:
        r2 = 0
    elif c3 + r1 == 4:
        r2 = 2

    print(f"15: {q1} {q2} {r1} {r2}")

    return q1 + q2*2 + r1*4 + r2*16


def check_digit(reverse: int) -> str:
    return list_reverse[reverse]


'''
list_alpha = {
    "0": (0, 0, 0, 0, 0),
    "1": (0, 0, 0, 1, 16),
    "2": (0, 0, 0, 2, 32),
    "3": (0, 0, 1, 0, 4),
    "4": (0, 0, 1, 1, 20),
    "5": (0, 0, 1, 2, 36),
    "6": (0, 0, 2, 0, 8),
    "7": (0, 0, 2, 1, 24),
    "8": (0, 0, 2, 2, 40),
    "9": (0, 1, 0, 0, 2),
    "A": (0, 1, 0, 1, 18),
    "B": (0, 1, 0, 2, 34),
    "C": (0, 1, 1, 0, 6),
    "D": (0, 1, 1, 1, 22),
    "E": (0, 1, 1, 2, 38),
    "F": (0, 1, 2, 0, 10),
    "G": (0, 1, 2, 1, 26),
    "H": (0, 1, 2, 2, 42),
    "I": (1, 0, 0, 0, 1),
    "J": (1, 0, 0, 1, 17),
    "K": (1, 0, 0, 2, 33),
    "L": (1, 0, 1, 0, 5),
    "M": (1, 0, 1, 1, 21),
    "N": (1, 0, 1, 2, 37),
    "O": (1, 0, 2, 0, 9),
    "P": (1, 0, 2, 1, 25),
    "Q": (1, 0, 2, 2, 41),
    "R": (1, 1, 0, 0, 3),
    "S": (1, 1, 0, 1, 19),
    "T": (1, 1, 0, 2, 35),
    "U": (1, 1, 1, 0, 7),
    "V": (1, 1, 1, 1, 23),
    "W": (1, 1, 1, 2, 39),
    "X": (1, 1, 2, 0, 11),
    "Y": (1, 1, 2, 1, 27),
    "Z": (1, 1, 2, 2, 43)
}

'''