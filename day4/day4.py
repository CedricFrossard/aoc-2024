def main():
    characters = []

    with open(file="./input", mode="r") as input_file:
        for line in input_file:
            chars = list(line)
            characters.append(chars)

        solvePart1(characters)
        solvePart2(characters)


def solvePart1(characters):
    validcount = 0
    for i, line in enumerate(characters):
        for j, char in enumerate(line):
            if (char == "X"):
                validcount += search([i,j], ['M','A','S'], characters)


    print(f"part 1 response: {validcount}")

def solvePart2(characters):
    validcount = 0
    for i, line in enumerate(characters):
        for j, char in enumerate(line):
            if (char == "A"):
                if (searchX([i,j], characters)):
                    validcount += 1
    print(f"part 2 response: {validcount}")

    
def search(start, target, characters):
    valid = 0
    directions = [
        [-1, 0],
        [-1, 1],
        [-1, -1],
        [0, 1],
        [0, -1],
        [1, -1],
        [1, 0],
        [1, 1],
    ]
    for i, direction in enumerate(directions):
        isValid = True
        vx = start[0]
        vy = start[1]
        for j, letter in enumerate(target):
            vx += direction[0]
            vy += direction[1]
            if (vx < 0 or vx >= len(characters) or vy < 0 or vy >= len(characters[vx])):
                isValid = False
                break
            if (not letter == characters[vx][vy]):
                isValid = False
        if isValid == True:
            valid = valid + 1
    return valid

def searchX(start, characters):
    valid = 0
    directions = [
        [
            [-1, 1],
            [1, -1],
        ], 
        [
            [-1, -1],
            [1, 1],
        ]
    ]
    for i, direction in enumerate(directions):
        vx = start[0] + direction[0][0]
        vx2 = start[0] + direction[1][0]
        vy = start[1] + direction[0][1]
        vy2 = start[1] + direction[1][1]

        if (vx < 0 or vx >= len(characters) or vy < 0 or vy >= len(characters[vx]) 
            or vx2 < 0 or vx2 >= len(characters) or vy2 < 0 or vy2 >= len(characters[vx])):
            return False
        if (
            ('M' != characters[vx][vy] and 'S' != characters[vx][vy]) or
            ('M' != characters[vx2][vy2] and 'S' != characters[vx2][vy2]) 
        ):
            return False
        if (characters[vx][vy] == characters[vx2][vy2]):
            return False

    return True


if __name__ == "__main__":
    main()