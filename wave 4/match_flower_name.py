

def read_text():
    flower_dic = []
    flower_name = []
    file = open('flowers.txt', 'r')
    for line in file.readlines():
        flower_dic.append(line[0])
        flower_name.append(line[3:])
    flower = zip(flower_dic, flower_name)
    flower = dict(flower)
    return(flower)


def main():
    reply = input("Enter your First [space] Last name only: ")
    letter = reply[0]
    dictionary = read_text()
    print(f"Unique flower name with the first letter: {dictionary[letter]}")
    
main()
