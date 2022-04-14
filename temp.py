with open("y.txt", 'r') as f:
    with open("cotas.txt", 'w') as f1:
        i = 0
        for x in f:
            f1.write(f"{i} {x}")
            i += 0.5