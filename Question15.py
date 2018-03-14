def combinations(x, y):
    xs = []
    ys = []
    diffs = []
    xval = 1
    yval = 1
    diffval = 1
    for i in range(1, x+1):
        xs.append(i)
    print xs
    for e in range(1, y+1):
        ys.append(e)
    print ys
    for u in range(1, (x-y)+1):
        diffs.append(u)
    print diffs
    for a in xs:
        xval = xval * a
    print xval
    for o in ys:
        yval = yval * o
    print yval
    for y in diffs:
        diffval = diffval * y
    print diffval
    super = xval / yval
    super = super / diffval
    return super

print combinations(40, 20)