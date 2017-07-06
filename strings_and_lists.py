#find and replace
words = "It's thanksgiving day. It's my birthday,too!"

print words.index("day")

words = words.replace("day", "month", 1)

print words

#printing min and max
x = [2,54,-2,7,12,98]

print min(x)
print max(x)

#printing first and last
x = ["hello",2,54,-2,7,12,98,"world"]

x[:len(x)-1]

print [x[0], x[-1]]

#new list
x = [19,2,54,-2,7,12,98,32,10,-3,6]

x.sort()
print x

first_list = x[:len(x)/2]
second_list = x[len(x)/2:]

print first_list
print second_list

second_list.insert(0,first_list)
print second_list
