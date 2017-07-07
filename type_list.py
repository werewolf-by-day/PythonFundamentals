l = ['magical unicorns',19,'hello',98.98,'world']
l = [2,3,1,7,4,12]
l = ['magical','unicorns']

if l is int:
sum = 0
    for i in l:
        sum += i
    print "Sum: " + sum
    print "The array you entered is of integer type"
elif l is str:
    print "String: " + "".join(l)
    print "The array you entered is of string type:"
else:
sum = 0
    l is int && l is str:
    print "String: " + "".join(str(l))
    for int in l:
        sum += int
    print "Sum: " + sum
    print "The array you entered is of mixed type"
