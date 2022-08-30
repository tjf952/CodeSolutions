# WEB > BYE > YEP > SPY
# JAW > AWE > WET > TOE
# KITE > EDIT > DOTE > OWED > DOWN

import re

words = [word.strip() for word in open("words.txt", "r").readlines()]


def shift_switch():
    start = input("Enter the starting word: ").lower()
    end = input("Enter the ending word: ").lower()
    length = len(end)
    stack = [(start, end, [])]
    while stack:
        start, sub, path = stack.pop()
        print("STACK:", start, "|", sub, "|", path)
        if start == end:
            print(f"Valid path found: {path + [end]}")
            ans = ", ".join(path[1:])
            print(f"Answer: {ans.upper()}")
            return
        shift = [start[i + 1 :] + start[: i + 1] for i in range(len(start) - 1)]
        print("\tSHIFT:", shift)
        search = []
        for word in shift:
            for i in range(len(word)):
                search.append(word[:i] + f"[{sub}]" + word[i + 1 :])
        search = "^" + "$|^".join(search) + "$"
        r = re.compile(search)
        wordlist = list(filter(r.match, words))
        print("\tWORDLIST RESULT:", wordlist)
        if sub:
            for word in wordlist:
                for letter in word:
                    if letter not in start:
                        new_sub = sub.replace(letter, "", 1)
                        break
                stack.append((word, new_sub, path + [start]))

    print("Failed to find a valid path!")


shift_switch()
