

transitions = [[0, 1, -1],[1, 1, 1]]

def char2code(s):
    if s == '_':
        n = int(input("введите число: "))
        if n == 0:
            return 0
        elif n == 1:
            s = 'm'
        else:
            s = '2'
    elif s >= 'a' and s <= 'z':
        return 1
    elif s >= '0' and s <= '9':
        return 2    

def isIdentifier(line):
    state = 0
    correct = True
    for s in line:
        state = transitions[state][char2code(s)]
        if state == -1:
            correct = False
            break
    return correct and state == 1

def main():
    line = input("введите строку: ")
    for s in line:
        s = char2code(s)

    correct = isIdentifier(line)
    print(correct)

if __name__ == '__main__':
    main()
    
