from f_translate_cambrigde import cambrigde_translate
import enchant,csv


word_list2 = []
with open("600-892.csv","r",encoding="utf-8") as file2:
    for line in file2:
        word = line.strip().split(",")[0]
        word_list2.append(word)


with open("600-892.json","w") as file:
    file.write("{\n")
    for word in word_list2:
        d = enchant.Dict("en_US")
        if d.check(word) == "False":
            word = d.suggest(word)[0]
            eng,thai = cambrigde_translate(word)
        else:
            eng,thai = cambrigde_translate(word)

        file.write('"'+str(eng)+'"'+":"+'"'+str(thai)+'",\n')
    file.write("\n}")    



