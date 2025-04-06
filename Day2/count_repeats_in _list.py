
user_input = input("Enter numbers separated by spaces: ")

lst = user_input.split()  
numbers = [] 
for num in lst:
    numbers.append(int(num))  
count_dict = {}
for num in numbers:
    if num in count_dict:
        count_dict[num] += 1  
    else:
        count_dict[num] = 1  
print("Repeated values and their counts:")
for key in count_dict:
    if count_dict[key] > 1: 
        print(key, ":", count_dict[key])
