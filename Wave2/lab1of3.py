# Use this playground to experiment with list methods, using Test Run
fav_edibles = ['parle-g', 'eba and okro', 'rice with stew and big chicken', 'chilled pepsi', 'monster energy drink', 'shawarma', 'pizza', 'roasted chicken']

print(f"""

Number of chicken items on the list: {fav_edibles.count('roasted chicken')}

postition of chilled pepsi: {fav_edibles.index('chilled pepsi')}

""")
#adding peppersoup to the list
fav_edibles.append('peppersoup')

print(fav_edibles)

#sorting the list
fav_edibles.sort()

print(fav_edibles)