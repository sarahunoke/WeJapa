#create a function that calculates the amount of tiles needed

def num_of_tiles(width, length):
    num_of_tiles = width * length
    return num_of_tiles

#calculate the no of tiles needed
    
total_num_of_tiles  = num_of_tiles(9, 7)  + num_of_tiles(5, 7)


#create a function that calculates tiles remaining

def remainder(num_of_packages, total_no_of_tiles):
    tiles_bought = num_of_packages * 6
    remainder = tiles_bought - total_no_of_tiles
    return remainder

#calculate the no of tiles remaining
    
remainder = remainder(17, total_no_of_tiles = total_num_of_tiles)
 

#print results
print(total_num_of_tiles)

print(remainder)