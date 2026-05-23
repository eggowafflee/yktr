file = open(input("file : "), "r")

words = file.read().split()

words_but_short = [n[:4] for n in words]


sentence = " ".join(words_but_short)

file.close

newfile = open(input("new file name : ")+".yktr", "w")
newfile.write(sentence)