#10일간 24시 동안 온도와 습도 계산
#텍스트파일: 0번 째 리스트:일, 첫 번째 리스트: 시간, 두 번째 리스트: 온도, 세 번째 리스트: 습도 -> 한 행에 일, 시간, 온도, 습도

def main():
    NUMBER_OF_DAYS = 10
    NUMBER_OF_HOURS = 24
    f = open("weather.txt", "r")

    data = []

    for i in range(NUMBER_OF_DAYS):
        data.append([])                      #리스트 생성
        for j in range(NUMBER_OF_HOURS):
            data[i].append([])               #리스트 하나 더 추가 하고 밑의 hour를 추가한 리스트에 넣음
            data[i][j].append(0)            #온도 들어갈 공간
            data[i][j].append(0)          #습도 들어갈 공간

# 파일 입출력 넣기
    for k in range(NUMBER_OF_DAYS * NUMBER_OF_HOURS):              # 0~239까지의 데이터
        line = f.readline().strip().split()
        day = eval(line[0])
        hour = eval(line[1])
        temperature = eval(line[2])
        humidity = eval(line[3])

        data[day - 1][hour - 1][0] = temperature
        data[day - 1][hour - 1][1] = humidity

#온도와 습도의 평균을 구하는 코드를 작성

    for i in range(NUMBER_OF_DAYS):
        dta = 0
        dha = 0
        for j in range(NUMBER_OF_HOURS):
            dta = data[i][j][0] + dta
            dha = data[i][j][1] + dha
        dta2 = dta / 24
        dha2 = dha / 24
        print(str(i) + '일의 평균 온도는' + str(dta2) + '입니다.')
        print(str(i) + '일의 평균 습도는' + str(dha2) + '입니다.')
        print('')

main()
