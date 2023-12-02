spelledNumbers = [
    "zero",
    "one",
    "two",
    "three",
    "four",
    "five",
    "six",
    "seven",
    "eight",
    "nine",
]
numbersDict = {number: spelledNumbers.index(number) for number in spelledNumbers}


def findCode(text: str):
    unsortedList: list[dict[str, int | str]] = []

    for [index, char] in enumerate(text):
        char.isdigit() and unsortedList.append({"v": char, "i": index})

    for spelledNumber in spelledNumbers:
        posL, posH = text.find(spelledNumber), text.rfind(spelledNumber)

        if posL == -1 and posH == -1:
            continue
        if posL == posH:
            unsortedList.append({"v": numbersDict[spelledNumber], "i": posL})
            continue

        for pos in [posL, posH]:
            pos != -1 and unsortedList.append(
                {"v": numbersDict[spelledNumber], "i": pos}
            )

    sortedDigits = sorted(unsortedList, key=lambda obj: obj["i"])

    firstDigit, lastDigit = sortedDigits[0], sortedDigits[-1]
    if not lastDigit:
        return int(str(firstDigit["v"]) + str(firstDigit["v"]))
    return int(str(firstDigit["v"]) + str(lastDigit["v"]))


def main():
    with open("input.txt", "r") as file:
        finalCode = 0
        for singleLine in file:
            finalCode += findCode(singleLine)
        print(finalCode)


main()
