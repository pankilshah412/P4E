
#Write a program to read through the mbox-short.txt and figure out the distribution by hour of the day for each of the messages. You can pull the hour out from the 'From ' line by finding the time and then splitting the string a second time using a colon.

#From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008

#Once you have accumulated the counts for each hour, print out the counts, sorted by hour as shown below.


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
        time = lineitem1.split()[5]
        hour = time.split(':')[0]
        counts[hour]= counts.get(hour,0)+1

lst = list()
for k,v in counts.items():
    lst.append((k,v))

lst.sort()

for k,v in lst:
    print k,v