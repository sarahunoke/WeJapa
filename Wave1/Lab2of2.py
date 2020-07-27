verse = "If you can keep your head when all about you\n  Are losing theirs and blaming it on you,\nIf you can trust yourself when all men doubt you,\n  But make allowance for their doubting too;\nIf you can wait and not be tired by waiting,\n  Or being lied about, don’t deal in lies,\nOr being hated, don’t give way to hating,\n  And yet don’t look too good, nor talk too wise:"
print(verse)

verse_length = len(verse)
first_pos_and = verse.index('and')
last_pos_you = verse.rfind('you')
you_count = verse.count('you')

print(verse_length)
print(f'Index of the first occurrence of the word "and" in verse: {first_pos_and}')
print(f'Index of the last occurrence of the word "you" in verse: {last_pos_you}')
print(f'count of occurrences of the word "you" in the verse: {you_count}')
