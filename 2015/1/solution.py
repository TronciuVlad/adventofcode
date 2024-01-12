f = open("input.in", "r")

count = 0
index = 0
flag = True

for c in f.read():
    if c == '(':
        count += 1
    elif c == ')':
        count -= 1

    index += 1
    if count == -1 and flag:
        print("Hit -1 at: ", index)
        flag = False

print("Final floor: ", count)