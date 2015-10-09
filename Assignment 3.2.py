#Write a program to prompt for a score between 0.0 and 1.0. If the score is out of range, print an error. If the score is between 0.0 and 1.0, print a grade using the following table:
#Score Grade
#>= 0.9 A
#>= 0.8 B
#>= 0.7 C
#>= 0.6 D
#< 0.6 F
#If the user enters a value out of range, print a suitable error message and exit. For the test, enter a score of 0.85.

try :
    grade = raw_input("Enter Score: ")
    g = float(grade)
except :
    print "Please Enter score between 0.0 and 1.0"
    quit()

if g < 0.6 and g >= 0.0:
    print "F"
elif g >=0.6 and g < 0.7:
    print "D"
elif g >=0.7 and g < 0.8 :
    print "C"
elif g >=0.8 and g < 0.9 :
    print "B"
elif g>0.9 and g<=1.0:
    print "A"
else:
    print "Number out of range"

