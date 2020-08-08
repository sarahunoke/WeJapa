# Write a for loop using range() to print out multiples of 5 up to 30 inclusive
multiples = []
for i in range(1, 31):
    if i % 5 == 0:
        multiples.append(i)
        
print(multiples)

