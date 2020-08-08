
limit = 40
m=1
n=[]


# write your while loop here
while m**2<limit:
    n.append(m**2)
    m += 1

nearest_square = n[-1]

print(nearest_square)