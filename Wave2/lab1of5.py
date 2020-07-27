elements = {'hydrogen': {'number': 1, 'weight': 1.00794, 'symbol': 'H'},
            'helium': {'number': 2, 'weight': 4.002602, 'symbol': 'He'}}


#adding is_noble_gas key to hydrogen and helium
elements['hydrogen']['is_noble_gas'] = False

elements['helium']['is_noble_gas'] = True


#print, print, print!!!
print(elements['hydrogen']['is_noble_gas'])
print(elements['helium']['is_noble_gas'])