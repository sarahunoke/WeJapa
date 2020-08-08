num_list = [422, 136, 524, 85, 96, 719, 85, 92, 10, 17, 312, 542, 87, 23, 86, 191, 116, 35, 173, 45, 149, 59, 84, 69, 113, 166]


odd_no = []

#for loop to append odd numbers to list
for numbers in num_list:
    if numbers % 2 == 1:
        odd_no.append(numbers)
    else:
        pass
print("Odd numbers added successfully to the list")
    
sum_first_five = sum(odd_no[:5])
print(odd_no, sum_first_five)