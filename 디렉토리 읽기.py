import os

path_dir = 'D:\신정규 파일\업무용\진행중\GSC 관련\API 데이터\수질운영일지'

file_list = os.listdir(path_dir)
file_list.sort()
print(file_list)

f = open(path_dir + "\\" + "tot.txt", 'w', encoding='utf-8')
for file in file_list :
    fileline = open(path_dir + "\\" + file, 'rt', encoding='utf-8')
    while True :
        try:
            line = fileline.readline()
        except :
            print(line)
        # line = line.replace("}", "}\n")
        line = line.replace("][", "],\n[")
        if not line :
            break
        f.write(line)
        # print(line)

# f.write("]")

f.close()
#
# print(file_list)