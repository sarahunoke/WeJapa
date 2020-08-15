user_list = []
list_sum = 0

for i in range(10):
    userInput = input("Enter any 2-digit number: ")
    
    if userInput.isdigit() == False:
        print("Incorrect value")
        break
    else:
        number = int(userInput)
        if number % 2 == 0:
            user_list.append(number)
            list_sum += number
   

print("user_list: {}".format(user_list))
print("The sum of the even numbers in user_list is: {}.".format(list_sum))


