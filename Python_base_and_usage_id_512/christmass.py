from random import choice, random


def main():
    SIZE = 15
    print(makeTree(SIZE))


def makeTree(size):
    prob_gr = 0.6
    colours = [31, 33, 34, 35, 36, 37]
    decs = ['@', '&', '*', chr(169), chr(174)]
    blink_col = "\033[5;{0}m{1}\033[0m"
    leaf = "\033[32m#\033[0m"
    tree = "\n{}*\n".format(' ' * (size))
    width = 1

    for pad in range(size - 1, -1, -1):
        width += 2
        temp = ""
        for j in range(width):
            if random() < prob_gr:
                temp += leaf
            else:
                temp += blink_col.format(choice(colours), choice(decs))
        tree += "{0}{1}\n".format(' ' * pad, temp)

    return tree + "{0}{1}\n".format(' ' * (size - 2), "0000") * 4


if __name__ == "__main__":
    main()
