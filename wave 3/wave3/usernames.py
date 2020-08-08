

names = ["Joey Tribbiani", "Monica Geller", "Chandler Bing", "Phoebe Buffay"]
usernames = []

# write your for loop here
for i in names:
    usernames.append(i.lower().replace(' ', '_'))


print(usernames)