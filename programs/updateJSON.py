
import json
from sys import getsizeof





def add_dict_to_json(jsonfile,newDicts):
    oldDicts = json.load(open(jsonfile,encoding='utf-8'))
    oldDicts.update(newDicts)
    with open(jsonfile, 'w') as json_file:
        json.dump(oldDicts, json_file)


# TEST
# 1WRITE
word_dicts = {"site1":"word1","seite1":"word2"}

jsonfile = "try.json"
with open(jsonfile, 'w') as json_file:
    json.dump(word_dicts, json_file)

# 2UPDATE
new_word_dicts = {"site2":"word21","seite2":"word22"}
add_dict_to_json(jsonfile,new_word_dicts)

