import csv
import pandas as pd
import shutil
from tabulate import tabulate

# tabulate 한글 출력 시 깨짐 현상을 방지하기 위한 코드
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

    # 데이터 정리를 위해 csv 카피 (가계부 정리 파일로 카피 후 데이터를 변환합니다.)
    shutil.copy('가계부.csv', '가계부정리.csv')



# 특정 달의 지출 내역
# 연도는 지정 불가합니다.(현재 csv 파일에 2023 데이터만 있습니다.)
def show_expenses_month():
    df = pd.read_csv('가계부정리.csv')
    month = int(input("지출 내역을 조회할 달을 입력해주세요. \n예시) 8월 --> 8: "))
    
    # 입력받은 month만 추출
    filtered_month = df.loc[df['월'] == month]

    # 카테고리까지만 범위로 지정하여 중복되는 정보 출력 X
    filtered_index = filtered_month.loc[:, :'카테고리']
    print(tabulate(filtered_index, headers='keys', tablefmt='grid', showindex=False, stralign='center'))
    


# pandas를 이용해서 데이터 날짜 변환 (사용자가 입력한 (YYYYMMDD) 데이터를 날짜 데이터로 변환시킵니다.)
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
def sum_expense():
    df = pd.read_csv('가계부정리.csv')

    # 년,월을 추출하여 각 기간의 합을 출력
    newtable = pd.pivot_table(data=df,index= ['연도', '월'], values='지출액', aggfunc='sum')
    print(tabulate(newtable, headers='keys', tablefmt='grid', stralign='center'))
    
    
    # 12월의 소비액을 치킨값으로 표현
    
    dec_expense = newtable.loc[(2023, 12), '지출액']
    price_chiken = float(dec_expense / 20000)

    print(f'12월 지출로 치킨을 {round(price_chiken, 1)}마리 살 수 있어요!')

    

