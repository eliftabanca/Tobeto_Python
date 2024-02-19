#This bot makes grouping easier for pairs in the lesson.
#It puts 5 different people for each pair, creating a total of 6 pairs.
import random



import random
file_path = "class_members_list.txt"

def get_names_from_file(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        names = file.read().splitlines()
    return names


names = get_names_from_file(file_path)
x = 1
for _ in range(6):
    
    pairs = random.sample(names, 5)
    print(f"{x}. Pair: {', '.join(pairs)}")
    x += 1
    for person in pairs:
        names.remove(person)

