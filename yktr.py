import sys

file = open(sys.argv[1], "r")

lines = file.readlines()

file.close()

fullfile = ""

for line in lines:
    #print(line)
    file = line 
    words = file.split() 
    
    cutoff = 5

    def newword(word): 
        if len(word) > cutoff: 
            return word[:cutoff] + "-" 
        else: 
            return word 

    sentence = "" 

    for word in words: 
        sentence += newword(word) + " "

  
    fullfile += "\n"+sentence


new_file_name = sys.argv[2]

total_char = len(sys.argv[2])

before_ex = total_char - 5

last_5 = sys.argv[2][before_ex:]

if last_5 == ".yktr":
    pass
else:
    new_file_name += ".yktr"


newfile = open(new_file_name, "w")
newfile.write(fullfile)
