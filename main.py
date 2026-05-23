file = open("test.txt", "r")

words = file.read().split()

words_but_short = [n[:4] for n in words]

print("- ".join(words_but_short)+"-")