#Write a program that prompts for a file name, then opens that file and reads through the file, looking for lines of the form:

# X-DSPAM-Confidence:    0.8475

#Count these lines and extract the floating point values from each of the lines and compute the average of those values and produce an output as shown below.

#You can download the sample data at http://www.pythonlearn.com/code/mbox-short.txt when you are testing below enter mbox-short.txt as the file name.

# Use the file name mbox-short.txt as the file name

fname = raw_input("Enter file name: ")
try:
    fh = open(fname,'r')
except:
    print " No such file exist"
    quit()

count = 0
summing_up = 0

for line in fh:
    if not line.startswith("X-DSPAM-Confidence:") :
        continue
    count = count+1
    position = line.find(':')
    number_string = line[position+1:]
    number_float = float(number_string)
    summing_up = number_float + summing_up
    print count ,number_float , summing_up
avg = summing_up/count
print 'Average spam confidence:',avg