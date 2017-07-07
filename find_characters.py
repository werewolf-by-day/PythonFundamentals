# input
word_list = ['hello','world','my','name','is','Anna']
new_list = []
for str in word_list:
    for val in str:
        if val == "o":
            new_list.append(str)
print new_list
