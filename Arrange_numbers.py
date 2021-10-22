# This fonction is for Arrange the numbers #

def Arrange_numbers():
    list_numbers = [11,19,4,50,8,6,45,1]
    New_list = []
    for i in range(len(list_numbers)):
        min_number = min(list_numbers)
        list_numbers.remove(min_number)
        New_list.append(min_number)
    print(New_list)
Arrange_numbers()
