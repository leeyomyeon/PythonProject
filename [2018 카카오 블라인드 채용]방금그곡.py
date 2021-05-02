import re
def timeInt(time):  # 시간 정수로 변환
    return int(time[0:2]) * 60 + int(time[3:5])

def Melody(music):  # 샾 제거하고 소문자로변경
    str = ""
    melody = re.compile('[A-G]#?').findall(music)
    for i in range(len(melody)):
        if len(melody[i]) == 2:
            str += melody[i][0].lower()
        else:
            str += melody[i]
    return str

def solution(m, musicinfos):
    answer = ''
    # 재생된 시간만큼 문자열 만들기
    # 샾이 붙은 문자를 소문자로 대치, 정규식 사용
    time = 0
    melody = Melody(m)

    for m in musicinfos:
        music = m.split(",")
        t = timeInt(music[1]) - timeInt(music[0])
        music[3] = Melody(music[3])

        str = ''    # 멜로디 찾기
        for i in range(t):
            str += music[3][i % len(music[3])]

        if str.find(melody) != -1 and time < t:
            time = t
            answer = music[2]

    if time == 0:
        return "(None)"

    return answer


ms = ["ABCDEFG", "CC#BCC#BCC#BCC#B", "ABC"]
minfo = [["12:00,12:14,HELLO,CDEFGAB", "13:00,13:05,WORLD,ABCDEF"], ["03:00,03:30,FOO,CC#B", "04:00,04:08,BAR,CC#BCC#BCC#B"], ["12:00,12:14,HELLO,C#DEFGAB", "13:00,13:05,WORLD,ABCDEF"]]
for i in range(3):
    print(solution(ms[i], minfo[i]))