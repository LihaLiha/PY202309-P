import csv

def save_to_csv(expense_name, amount, date, category):
    # CSV 파일에 저장할 데이터
    data = [[expense_name, str(amount), date, category]]

    # CSV 파일에 데이터 추가 또는 생성
    with open('가계부.csv', 'a', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerows(data)

# 사용자로부터 정보 입력 받기
expense_name = input("지출 항목을 입력하세요: ")
amount = float(input("금액을 입력하세요: "))
date = input("날짜를 입력하세요 (YYYY-MM-DD 형식): ")
category = input("카테고리를 입력하세요: ")

# CSV 파일에 정보 저장
save_to_csv(expense_name, amount, date, category)
print("정보가 저장되었습니다.")