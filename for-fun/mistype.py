import re

words = [word.strip() for word in open("words.txt", "r").readlines()]


def mistype(puzzle):
    typo = {
        "q": "qaw",
        "w": "wqasde",
        "e": "ewsdfr",
        "r": "redfgt",
        "t": "trfghy",
        "y": "ytghju",
        "u": "uyhjki",
        "i": "iujklo",
        "o": "oiklp",
        "p": "pol",
        "a": "aqwsxz",
        "s": "sqwedcxza",
        "d": "dwerfvcxs",
        "f": "fertgbvcd",
        "g": "grtyhbvcf",
        "h": "htyujmnbg",
        "j": "jyuikmnh",
        "k": "kuiolmj",
        "l": "lopk",
        "z": "zasx",
        "x": "xzasdc",
        "c": "cxsdfv",
        "v": "vcdfgb",
        "b": "bvfghn",
        "n": "nbghjm",
        "m": "mnhjk",
    }
    puzzle = puzzle.split()
    lengths = [len(x) for x in puzzle]
    sol = []
    for _ in puzzle:
        sol.append([])
    for word in words:
        if len(word) in lengths:
            for i, term in enumerate(puzzle):
                if len(word) == len(term):
                    valid = True
                    for j, c in enumerate(term):
                        if word[j] not in typo[c]:
                            valid = False
                            break
                    if valid:
                        sol[i].append(word)
    return sol


puzzle = input("Enter a puzzle to solve: ")
print(mistype(puzzle))