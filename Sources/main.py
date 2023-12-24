import pandas as pd
from tabulate import tabulate
import numpy as np
from function import *

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
        sum_expense()

    elif menu_num == 4:
        # 종료
        print("종료합니다.")
        break

    else:
        # 외 문자 입력 시
        print("올바른 번호를 입력해주세요.\n")
        continue



