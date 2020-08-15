import random

word_file = "words.txt"
word_list = []

with open(word_file,'r') as words:
	for line in words:
		word = line.strip().lower()
		if 3 < len(word) < 8:
			word_list.append(word)

def generate_password():
    words = word_list
    a = random.choice(words)
    b = random.choice(words)
    c = random.choice(words)
    print(a+b+c)
    

print(generate_password())
