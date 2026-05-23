import sys

file = open(sys.argv[1], "r") 
words = file.read().split() 

def newword(word): 
    if len(word) > 4: 
        return word[:4] + "-" 
    else: 
        return word 

sentence = "" 

for word in words: 
    sentence += newword(word) + " "

file.close()

new_file_name = sys.argv[2]

total_char = len(sys.argv[2])

before_ex = total_char - 5

last_5 = sys.argv[2][before_ex:]

if last_5 == ".yktr":
    pass
else:
    new_file_name += ".yktr"




newfile = open(new_file_name, "w")
newfile.write(sentence)