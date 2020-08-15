
def create_cast_list(filename):
    cast_list = []
    file = open('flying_circus_cast.txt', 'r')
    
    for line in file.readlines():
        values = line.split(',')
        cast_list.append(values[0])
   
    return cast_list

cast_list = create_cast_list('flying_circus_cast.txt')
for actor in cast_list:
    print(actor)