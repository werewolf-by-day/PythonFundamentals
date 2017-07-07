l = ['magical unicorns',19,'hello',98.98,'world']
#l = [2,3,1,7,4,12]
#l = ['magical','unicorns']

if all(isinstance(n, int) for n in l):
    sum = 0
    for i in l:
        sum += i
    print "Sum: " + str(sum)
    print "The array you entered is of integer type"
elif all(isinstance(n, str) for n in l):
    print "String: " + " ".join(l)
    print "The array you entered is of string type"
else:
    sum = 0
    new_string = ""
    for i in l:
        if (isinstance(i, (int, float,))):
            sum += i
        else:
            (isinstance(i, str) for i in l)
            new_string = new_string + " " + str(i)
    print "Sum: " + str(sum)
    print "String: " + new_string
    print "The array you entered is of mixed type"
