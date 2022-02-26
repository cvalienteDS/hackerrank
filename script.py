import os

def cutBamboo(lengths):
    # Write your code here
    pieces = []
    while lengths:
        pieces.append(len(lengths))
        minimum = min(lengths)
        #lengths.remove(min(lengths))
        lengths = [(x-2) for x in lengths if x != minimum]
    return pieces

if __name__ == '__main__':
    lengths = [6, 5, 4, 4, 2, 2, 8]

    result = cutBamboo(lengths)
    print(result)
