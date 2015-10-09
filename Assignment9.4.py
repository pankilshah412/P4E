#Write a program to read through the mbox-short.txt and figure out who has the sent the greatest number of mail messages. The program looks for 'From ' lines and takes the second word of those lines as the person who sent the mail. The program creates a Python dictionary that maps the sender's mail address to a count of the number of times they appear in the file. After the dictionary is produced, the program reads through the dictionary using a maximum loop to find the most prolific committer.


fname = raw_input("Enter file name: ")
try:
    if len(fname) < 1 : fname = "mbox-short.txt"
    fhand = open(fname,'r')
except:
    print " No such file exist"
    quit()

counts = dict()
for lineitem1 in fhand:
    lineitem1 = lineitem1.rstrip()
    if lineitem1.startswith('From') and not lineitem1.startswith('From:'):
        words = lineitem1.split()
        counts[words[1]]= counts.get(words[1],0)+1
#print counts

bigcount = None
bigword = None
for word,count in counts.items():
    #print word, count
    if bigcount is None or count > bigcount:
        bigword = word
        bigcount = count

print bigword, bigcount
