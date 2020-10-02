list_of_ages = [2,12,12,14,15,16,16,17,18,14,20,20]
max(list_of_ages)
print(max(list_of_ages))
set(list_of_ages)
print(set(list_of_ages))






def compare_lists(list1,list2):
    for num in list1:
        if num in list2:
            return True
        return False
list1 = [2,12,12,14,15,16,16,17,18,14,20,20]
list2 = [2,4,12,14,15,16,16,17,18,14,20,20]

if compare_lists(list1,list2):
    print("They have common members. ")
else:
    print("They have no common members ")






# Tuples
def tuple_exercise():
    number = int(input("How many numbers would like to add: "))

    my_tuple = tuple()
    tmp_list = []
    while number > 0:
        num = "Please enter a number (again): "
        tmp_list.append(num)
    my_tuple = tuple(tmp_list)

    print("Max: ", max(my_tuple))
    print("Sum: ", sum(my_tuple))
    print("Min: ", min(my_tuple))


    new_list = list(my_tuple)
    new_list.append(45)
    new_list.append(56)
    new_tuple = tuple(new_list)

    print("Initial tuple: ", my_tuple)
    print("New tuple: ", new_tuple)
