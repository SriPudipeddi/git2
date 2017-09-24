def talking(worda, wordb):
    c = worda + wordb
    return c

print talking("Sunny", " sky")
worda = raw_input("Enter a word: ")
wordb = raw_input("Enter another word: ")
print talking(worda, wordb)