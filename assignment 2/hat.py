number_list = [1,2,3,4,5]
user_input = int(input("please enter")) 
#len shows the size of the list
number_list[len(number_list)//2] = user_input
print(number_list)
#pop deletes the last item in the list
number_list.pop(-1)
print(len(number_list))
