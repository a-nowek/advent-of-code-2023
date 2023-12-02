# Part 1
def findCode(text):
    digits = []
    for char in text:
        char.isdigit() and digits.append(char)

    firstDigit, lastDigit = digits[0], digits[-1]
    if not lastDigit:
        return int(firstDigit + firstDigit)
    return int(firstDigit + lastDigit)


def main():
    finalCode = 0
    with open("input.txt") as file:
        for singleLine in file:
            finalCode += findCode(singleLine)

    print(finalCode)


main()
