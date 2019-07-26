def hanota_move(n, source, dest, intermediate):
    if n >= 1:
        hanota_move(n-1, source, intermediate, dest)
        print("Move %s -> %s" % (source, dest))
        hanota_move(n-1, intermediate,  dest, source)

hanota_move(5, 'A', 'B', 'C')
