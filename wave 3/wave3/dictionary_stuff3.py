
fruit_count, not_fruit_count = 0, 0
basket_items = {'apples': 4, 'oranges': 19, 'kites': 3, 'sandwiches': 8}
fruits = ['apples', 'oranges', 'pears', 'peaches', 'grapes', 'bananas']

#Iterating through the dictionary
for fruit in basket_items:
    if fruit in fruits:
        fruit_count += basket_items[fruit]
    elif fruit not in fruits:
        not_fruit_count += basket_items[fruit]


print(fruit_count, not_fruit_count)