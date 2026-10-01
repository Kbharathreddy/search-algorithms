def f(x):
    return -(x-3)**2+9
def hill_climbing(start):
    current=start
    while True:
        left=current-1
        right=current+1
        best=current
        if f(left)>f(best):
            best=left
        if f(right)>f(best):
            best=right
        print("current:",current,"value:",f(current))

        if f(best)<=f(current):
            break
        current=best

    print("Best State:",current)
    print("Best Value:",f(current))

hill_climbing(0)