import datetime
import csv
import pandas as pd
import shutil
from tabulate import tabulate
import re, os
import numpy as np

# tabulate 한글 출력을 위한 코드
tabulate.WIDE_CHARS_MODE = False


# csv 저장 함수
def save_to_csv(expense_name, amount, date, category):
    # CSV 파일에 저장할 데이터
    data = [[expense_name, str(amount), date, category]]

    #CSV 파일에 데이터 추가
    with open("가계부.csv", "a", newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerows(data)
    

# 지출 입력, 저장 함수
def enter_expense():
    # 사용자로부터 지출 정보 입력 받기
    expense_name = input("지출 항목을 입력하세요: ")
    print("\n")
    amount = float(input("금액을 입력하세요: "))
    print("\n")
    date = input("날짜를 입력하세요 (YYYY-MM-DD 형식): ")
    print("\n")
    category = input("카테고리를 입력하세요: ")
    print("\n")

    # 입력된 정보 파일에 저장
    save_to_csv(expense_name, amount, date, category)
    print("지출 정보가 저장되었습니다.\n")

    # 데이터 정리를 위해 csv 카피
    shutil.copy('가계부.csv', '가계부정리.csv')



# 특정 달의 지출 내역
# 능력 부족으로 연도는 지정 불가합니다.(현재 csv 파일에 2023 데이터만 있습니다.)
def show_expenses_month():
    df = pd.read_csv('가계부정리.csv')
    month = int(input("지출 내역을 조회할 달을 입력해주세요. \n예시) 8월 --> 8: "))
    
    # 입력받은 month만 추출
    filtered_month = df.loc[df['월'] == month]

    # 카테고리까지만 범위로 지정하여 중복되는 정보 출력 X
    filtered_index = filtered_month.loc[:, :'카테고리']
    print(tabulate(filtered_index, headers='keys', tablefmt='grid', showindex=False, stralign='center'))
    


# pandas를 이용해서 데이터 날짜 변환
def date_conversion():
    df = pd.read_csv('가계부정리.csv')
    df['날짜(2023MMDD)'] = pd.to_datetime(df['날짜(2023MMDD)'], format='%Y%m%d')
    df['날짜_datetime'] = pd.to_datetime(df['날짜(2023MMDD)'])
    df['연도'] = df['날짜_datetime'].dt.year
    df['월'] = df['날짜_datetime'].dt.month
    df['일'] = df['날짜_datetime'].dt.day
    df['요일'] = df['날짜_datetime'].dt.day_name()
    df.to_csv('가계부정리.csv', index=False)


# 각 달의 지출 합계 출력 함수
def average_expense():
    df = pd.read_csv('가계부정리.csv')

    # 년,월을 추출하여 각 기간의 합을 출력
    newtable = pd.pivot_table(data=df,index= ['연도', '월'], values='지출액', aggfunc='sum')
    print(tabulate(newtable, headers='keys', tablefmt='grid', stralign='center'))
    print("(년, 월) 지출액")





while True:
    ## 메인 메뉴
    print(":::::::::::::::::")
    print("지출 관리 프로그램")
    print(":::::::::::::::::")
    print(":::::::메뉴:::::::")
    print("1. 지출 내용 입력")
    print("2. 지출 상세")
    print("3. 나의 한달 지출")
    print("4. 종료")
    menu_num = int(input("번호를 입력해주세요: "))
    print("\n")

    if menu_num == 1:
        # 지출 저장      
        enter_expense()

        # 날짜 데이터로 변환
        date_conversion()

    elif menu_num == 2:
        show_expenses_month()
            
    elif menu_num == 3:
        average_expense()

    elif menu_num == 4:
        # 종료
        print("종료합니다.")
        break

    else:
        # 외 문자 입력 시
        print("올바른 번호를 입력해주세요.\n")
        continue









# 사용자로부터 기간 입력 받기


# 입력한 기간 내의 지출 내역 출력


## 고정 지출 저장 기능  <-- 후순위
# 1. 일 선택
# 2. 고정 지출 금액 입력 (+ 메모)
# 3. 매달 지출에 고정


## 해당 달의 지출액
# 1. 연도, 달 입력
# 2. 해당 달의 지출액 합산
# 3. 지출액 출력


## 날, 달마다 지출 평균액 계산
# 날, 달의 지출액 평균 구하기
# 평균 출력







