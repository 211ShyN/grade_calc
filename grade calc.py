#평점변환함수
def convert_score(grade):
    match grade:
        case 'A+':
            gpa = 4.5
        case 'A0':
            gpa = 4.0
        case 'B+':
            gpa = 3.5
        case 'B0':
            gpa = 3.0
        case 'C+':
            gpa = 2.5
        case 'C0':
            gpa = 2.0
        case 'D+:
            gpa = 1.5
        case 'D':
            gpa = 1.0
        case 'F':
            gpa = 0.0
            

while True:
    print("작업을 선택하세요.")
    print("     1. 입력")
    print("     2. 계산")

    user_value = input()
    
    match value:
        #연산
        case 1:
            user_value = input("학점을 입력하세요: ")
            credit = int(user_value)

            user_value = input("평점을 입력하세요: ")
            gpa = convert_score(user_value)

            if gpa = 0
