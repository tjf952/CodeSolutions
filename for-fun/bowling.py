"""
Given the number of bowling pins, the sum of those pin values,
and the product of those pin values, find the exact pins that
were knocked down

Example:
    size = number of pins
    psum = sum of pins
    ppro = product of the pins
    n=3, psum=15, ppro=105 > 3,5,7
"""

import numpy


def bowling(size, psum, ppro):
    nums = list(range(1, 11))

    def dfs(idx, path, cur):
        if cur > psum or len(path) > size:
            return
        if cur == psum and len(path) == size:
            if numpy.prod(path) == ppro:
                print(path)
                return path
        for i in nums[idx:]:
            dfs(i, path + [i], cur + i)

    return dfs(0, [], 0)


if __name__ == "__main__":
    option = input("Automatic [1] or manual [2] : ")
    answer = None
    try:
        if option == "2":
            size = int(input("Enter the number of pins: "))
            psum = int(input("Enter the sum of the pins: "))
            ppro = int(input("Enter the product of the pins: "))
            print(f"Calling bowling({size}, {psum}, {ppro})")
            answer = bowling(size, psum, ppro)
        else:
            print("Default size is 10, enter numbers 1-10 only.")
            li = input("Enter a list of numbers split by spaces: ")
            li = list(map(int, li.split()))
            psum = sum(li)
            ppro = 1
            for x in li:
                ppro *= x
            print(f"Calling bowling({len(li)}, {psum}, {ppro})")
            answer = bowling(len(li), psum, ppro)
    except:
        print("Invalid input, closing...")
