def find_the_highest(mylist):
    my_dict = {}
    for val in mylist:
        if val not in my_dict.keys():
            my_dict[val] = 1
        elif val in  my_dict.keys():
            previous_valu = my_dict.get(val)
            my_dict[val] += 1
    print(my_dict.items())
    max_key_value = max(my_dict, key=my_dict.get)
    dict_values = list(my_dict.values())
    max_value = max(my_dict.values())
    print(dict_values)
    if not dict_values.count(max_value) == 1:
                    print(max_key_value)
    else:
        print(max_value)            
data = "12,13,12,13,4"
mylist = data.split(",")
find_the_highest(mylist)