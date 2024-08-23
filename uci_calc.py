# UK UCI Calculator #
# Copyright (c) Nathan Gill 2024 #
# under Mozilla Public License 2.0 #
# https://www.jcq.org.uk/wp-content/uploads/2020/01/Unique-Candidate-Identifiers.pdf #

print("-------UK UCI Calculator--------")
print("    (c) Nathan Gill 2024")
print("under Mozilla Public License 2.0\n")

ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
CHECK_DIGITS = "ABCDEFGHKLMRTVWXY"

# Converts any character to its integer equivalent
def to_int(n):
    try:
        return int(n)
    except:
        return ALPHABET.index(n) + 1

while True:
    centre_num = input("Centre Number: ").upper()
    if len(centre_num) != 5:
        print("Invalid centre number!")
        quit()
    
    candidate_num = input("Candidate Number: ").upper()
    if len(candidate_num) != 4:
        print("Invalid candidate number!")
        quit()
    
    reg_year = input("Registration Year: ").upper()
    if len(reg_year) != 4:
        print("Invalid registration year!")
        quit()

    print("Board:")
    print(" 0: NCN")
    print(" A: OCR")
    print(" B: Pearson")
    print(" C: AQA")
    print(" E: WJEC")
    print(" G: CCEA")
    print("Or any other")
    board = input("Board: ").upper()
    if len(board) != 1:
        print("Invalid board number!")
        quit()

    uci = centre_num[:5] + board[:1] + reg_year[2:] + candidate_num[:4]

    total = 0
    mul = 16
    for c in uci:
        total += to_int(c) * mul
        mul -= 1

    uci += CHECK_DIGITS[total % 17]

    print("\nUCI: ", uci)
    if len(uci) != 13:
        print("UCI corrupt!")

    n = input("\nGenerate another (Y/n)? ")
    if n.upper() == "N":
        break
