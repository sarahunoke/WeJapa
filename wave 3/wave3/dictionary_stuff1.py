
result = 0
basket_items = {'apples': 4, 'oranges': 19, 'kites': 3, 'sandwiches': 8}
fruits = ['apples', 'oranges', 'pears', 'peaches', 'grapes', 'bananas']

#for to add the number of fruits in basket_items
for fruit in basket_items:
    if fruit in fruits:
        result += basket_items[fruit]
    else:
        pass

print(result)