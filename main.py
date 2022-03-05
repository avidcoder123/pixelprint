from blessed import Terminal

term = Terminal()

#Half block unicode constant
PIXEL = "▀"

def pairwise(data):
    return zip(data[0::2], data[1::2])

testfile: list[str] = open("testfile", "r").readlines()

#If testfile has an odd number of lines, add a line full of k equal to the length of the last line
if len(testfile) % 2 != 0:
    testfile.append("k" * len(testfile[-1]))

#Take the lists in testfile by twos. If one line is longer than the other, make them the same length by filling the shorter line with k
for i in range(len(testfile)):
    if i == len(testfile) - 1:
        break
    if len(testfile[i]) > len(testfile[i+1]):
        testfile[i+1] += "k" * (len(testfile[i]) - len(testfile[i+1]))
    elif len(testfile[i]) < len(testfile[i+1]):
        testfile[i] += "k" * (len(testfile[i+1]) - len(testfile[i]))

def charToColor(c):
    if c == "r":
        return "red"
    elif c == "b":
        return "blue"
    else:
        return "black"

for topline, bottomline in pairwise(testfile):
    for top, bottom in zip(topline, bottomline):
        topcolor = charToColor(top)
        bottomcolor = charToColor(bottom)

        color = f"{topcolor}_on_{bottomcolor}"

        if bottom in ["\n", "k"] and top in ["\n", "k"]:
            continue
        elif top in ["\n", "k"]:
            color= f"black_on_{bottomcolor}"
        elif bottom in ["\n", "k"]:
            color = topcolor
        #Get the blessed function that will print the correct pixel.
        fn = getattr(term, color)
        print(fn(PIXEL), end="")
    print("")
