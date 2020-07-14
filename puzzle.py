from logic import *

AKnight = Symbol("A is a Knight")
AKnave = Symbol("A is a Knave")

BKnight = Symbol("B is a Knight")
BKnave = Symbol("B is a Knave")

CKnight = Symbol("C is a Knight")
CKnave = Symbol("C is a Knave")

# Puzzle 0
# A says "I am both a knight and a knave."
knowledge0 = And(
    # each char is a Knight or Knave
    Or(AKnave, AKnight),
    Not(And(AKnight, AKnave)),

    # Knight will tell the truth, Knave will lie
    # when the Or is true in here(one of them not both)
    # then the statment both of them is wrong
    Implication(Or(AKnight, AKnave), AKnave)

)


# Puzzle 1
# A says "We are both knaves."
# B says nothing.

# A cannot be a knight since by his own testimony he would then be a knave
# A must be a knave, and the only way for his statement to be false
# is for B to be a knight
knowledge1 = And(
    # each char is a Knight or Knave
    Or(AKnave, AKnight),
    Not(And(AKnight, AKnave)),
    Or(BKnave, BKnight),
    Not(And(BKnight, BKnave)),
    AKnave,
    Implication(AKnave, BKnight)
)


# Puzzle 2
# A says "We are the same kind."
# B says "We are of different kinds."

# A is Knave and B is Knight
knowledge2 = And(
    # each char is a Knight or Knave
    Or(AKnave, AKnight),
    Not(And(AKnight, AKnave)),
    Or(BKnave, BKnight),
    Not(And(BKnight, BKnave)),

    Implication(Or(Or(AKnave, BKnight), Or(AKnight, BKnave)), AKnave),

    Implication(Implication(Or(Or(AKnave, BKnight), Or(AKnight, BKnave)), AKnave), BKnight)

)

# Puzzle 3
# A says either "I am a knight." or "I am a knave.", but you don't know which.
# B says "A said 'I am a knave'."
# B says "C is a knave."
# C says "A is a knight."
knowledge3 = And(
    # each char is a Knight or Knave
    Or(AKnave, AKnight),
    Not(And(AKnight, AKnave)),
    Or(BKnave, BKnight),
    Not(And(BKnight, BKnave)),
    Or(CKnave, CKnight),
    Not(And(CKnight, CKnave)),

    # this triggers the following two statments
    Implication(Or(AKnight, AKnave), BKnave),

    Implication(Implication(AKnave, BKnave), CKnight),
    Implication(CKnight, AKnight)

)


def main():
    symbols = [AKnight, AKnave, BKnight, BKnave, CKnight, CKnave]
    puzzles = [
        ("Puzzle 0", knowledge0),
        ("Puzzle 1", knowledge1),
        ("Puzzle 2", knowledge2),
        ("Puzzle 3", knowledge3)
    ]
    for puzzle, knowledge in puzzles:
        print(puzzle)
        if len(knowledge.conjuncts) == 0:
            print("    Not yet implemented.")
        else:
            for symbol in symbols:
                if model_check(knowledge, symbol):
                    print(f"    {symbol}")


if __name__ == "__main__":
    main()
