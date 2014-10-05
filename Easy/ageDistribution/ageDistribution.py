import sys

lines = file(sys.argv[1], 'r')

for line in lines:
    age = int(line.rstrip())
    if age >= 0 and age <= 2:
        print "Still in Mama's arms"
    elif age >= 3 and age <= 4:
        print 'Preschool Maniac'
    elif age >= 5 and age <= 11:
        print 'Elementary school'
    elif age >= 12 and age <= 14:
        print 'Middle school'
    elif age >= 15 and age <= 18:
        print 'High school'
    elif age >= 19 and age <= 22:
        print 'College'
    elif age >= 23 and age <= 65:
        print 'Working for the man'
    elif age >= 66 and age <= 100:
        print 'The Golden Years'
    else:
        print 'This program is for humans'
