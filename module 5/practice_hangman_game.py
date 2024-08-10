list_of_word = ["apple","ball","cat","cow","camel","cobra","cobalt","nikil","rust","rush","random","pitch","guage","graphite","gun powder","lemon","lichi","leaopard","ocean","ostrich","ugly","umbrella","star","parrot","plug","pillow","shield","summer","winter","rainy","leaves","trees","steam","root","rapidly"]
import random as rd
picked_word = rd.choice(list_of_word)

word_in_list =[]
for i in picked_word:
    word_in_list.append(i)
print(word_in_list)

game_list = []

for i in range(len(list_of_word)):
    if list_of_word[i] == "a" or list_of_word[i] == "e" or list_of_word[i] == "i" or list_of_word[i] == "o" or list_of_word[i] == "u":
        game_list.append(list_of_word[i])
        
    else:
        game_list.append("_")
        continue

print(game_list)