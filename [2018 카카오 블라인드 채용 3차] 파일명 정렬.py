import re
def solution(files):
    answer = []
    # head, number, tail로 구분한다. 정규식을 사용하여 number기준 분리함
    fileList = []
    for file in files:
        fileList.append(re.split("([0-9]+)", file))

    # head는 대문자 기준, number는 Int로 변환하여 정렬함
    sortList = sorted(fileList, key = lambda x: (x[0].upper(), int(x[1])))

    for i in range(len(sortList)):
        s = ""
        for j in range(len(sortList[i])):
            s += sortList[i][j]
        answer.append(s)
    return answer


f = [["img12.png", "img10.png", "img02.png", "img1.png", "IMG01.GIF", "img2.JPG"], ["F-5 Freedom Fighter", "B-50 Superfortress", "A-10 Thunderbolt II", "F-14 Tomcat"]]
for fi in f:
    print(solution(fi))