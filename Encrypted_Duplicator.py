import csv

str2 = "~^SKjnk:e9cQyVOwLs5I0R`g>4XN!=23x6<a8+T_zvpioCW%J@DUY,Fd;?rfZ1lBqm$&EPG7-/bt*|#.AuhMH"
str1 = "A>lTMgzKpkvnt/%UPFqVN|2rw&$DQj.08-4<d=;J1?u~@+W:sbHCef5x3iZBS_c`6,hXym9Ia^!7EoY#LRGO*"
duplicate_list = []

def read_csv(csv):
    for row in csv:
        duplicate_row = []
        for element in row:
            duplicate_string = ""
            for letter in element:
                if letter in str1:
                    x = str1.index(letter)
                    duplicate_string += str2[x]
                else:
                    duplicate_string += letter
            duplicate_row.append(duplicate_string)
        duplicate_list.append(duplicate_row)

with open("tobeobliterated copy.csv") as file:
    f = csv.reader(file)
    reader = list(f)
    read_csv(reader)

with open("tobeobliterated copy.csv", "w", newline = "") as file:
    f  = csv.writer(file)
    f.writerow(duplicate_list[0])
    f.writerows(duplicate_list[1:])
