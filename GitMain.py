def talking(worda, wordb):
    # type: (str, str) -> str
    c = worda + wordb
    return c

print talking("Sunnie", " sky")

print talking(worda="Baking", wordb=" cookies")
talking("cool", "off")

def divby2(a):
    if a%2 == 0:
        print "%d is a multiple of 2" %a
    else:
        print "%d is not a multiple of 2" %a


divby2(101)