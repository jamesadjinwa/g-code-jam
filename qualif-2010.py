#code Qualification round Jam Africa 2010

j = 0
newwords = list()
fhand = open('B-small-practice.in')
fout = open('output.txt', 'w')

# Calculate number of lines in file
#with open('B-small-practice.in') as f:
#    print(sum(1 for _ in f))

for line in fhand :
    newwords = []
    words = line.split()
    if len(words) == 0 : continue
    else :
        n = len(words)
        i = 1
        for word in words :
            j = n - i
            newwords.append(words[j])
            i += 1
    print(" ".join(str(x) for x in newwords)) # Convert list to string

    fout.write(" ".join(str(x) for x in newwords))
    fout.write('\n')


with open('output.txt', 'r') as fin:
    data = fin.read().splitlines(True)
with open('output.txt', 'w') as fout:
    fout.writelines(data[1:])
    
fout.close()
fhand.close()
    
