import pandas
import random
processsed_list = []
with open("data/french_words.csv", "r") as data:
    words = data.readlines()
    for line in words:
        split_up = line.split(",")
        processsed_list.append({split_up[0]:split_up[1].removesuffix("\n")})
random.shuffle(processsed_list)