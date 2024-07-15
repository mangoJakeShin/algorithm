import re

class filename:
    def __init__(self, head, number, tail, ord):
        self.head = head.lower()
        self.number = int(number)
        self.tail = tail
        self.ord = ord

    def sort(files):
        return sorted(files, key=lambda x: (x.head, x.number,x.ord))

def solution(files):
    answer = []
    li = []

    for i in range(len(files)) :
        file = files[i]
        fl = re.split(r'\d+',file)
        newname = filename(fl[0],re.findall(r'\d+',file)[0],fl[1], i)
        li.append(newname)

    li2 = filename.sort(li)
    for l in li2 :
        answer.append(files[l.ord])
    return answer

solution(["img12.png", "img10.png", "img02.png", "img1.png", "IMG01.GIF", "img2.JPG"])
