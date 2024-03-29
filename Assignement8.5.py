
#8.5 Open the file mbox-short.txt and read it line by line. When you find a line that starts with 'From ' like the following line:
#From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
#You will parse the From line using split() and print out the second word in the line (i.e. the entire address of the person who sent the message). Then print out a count at the end.
#Hint: make sure not to include the lines that start with 'From:'.

#You can download the sample data at http://www.pythonlearn.com/code/mbox-short.txt

fname = raw_input("Enter file name: ")
try:
    if len(fname) < 1 : fname = "mbox-short.txt"
    fh = open(fname,'r')
except:
    print " No such file exist"
    quit()

count = 0

for lineitem in fh:
    lineitem = lineitem.rstrip()
    if lineitem.startswith('From') and not lineitem.startswith('From:'):
        words = lineitem.split()
        count = count+1
        print words[1]

print "There were", count, "Lines in the file with From as the first word"