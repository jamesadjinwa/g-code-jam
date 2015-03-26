#code Jam Africa 2011

fhand = open('B-small-practice.in')
fout = open('output.txt', 'w')
i = 0

# Calculate number of lines in file
#with open('B-small-practice.in') as f:
#    print(sum(1 for _ in f))

for line in fhand :
    i += 1
    words = line.split()
    if len(words) == 0 : continue
    else :
        words.reverse()
    fout.write("Case #"+str(i)+": ")
    fout.write(" ".join(str(x) for x in words)) # Convert list to string and write to file
    fout.write('\n')


with open('output.txt', 'r') as fin:
    data = fin.read().splitlines(True)
with open('output.txt', 'w') as fout:
    fout.writelines(data[1:])
    
fout.close()
fhand.close()
