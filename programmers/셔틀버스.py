#n = 운행횟수
#t = 간격
#m = 정원
#tt = 경쟁자
def solution(n, t, m, timetable):
    answer = ''
    bt = bustable(n,t)
    timetable = sorted(timetable)
    if len(timetable) < m * n :
        return bt[-1]
    elif m * n == len(timetable) :
        return min(bt[-1], calctime(timetable[-1], -1))
    else :

        return timetable[1]
    return answer

def bustable(n,t) :
    table = ["09:00"]
    for i in range(1, n) :
        last = table[-1]
        table.append(calctime(last, t * i))
    return table

def calctime(time, interval) :
    ret = ""
    m = int(time[3:]) + interval
    if m >= 60 :
        h = int(time[:2]) + 1
        m = m % 60
    elif m <= -1 :
        h = int(time[:2]) -1
        m = m + 60
    else : h = int(time[:2])
    return str(h).zfill(2) + ":" + str(m).zfill(2)


# a = "09:45"
# solution(1,1,5,	["09:10", "09:09", "08:00"])
# print(calctime(a,-50))
# print(min("09:00", "18:59"))
a= ["09:10", "09:09", "08:00", "09:09", "09:09"]
a = sorted(a)
print(a.count("09:09"))
