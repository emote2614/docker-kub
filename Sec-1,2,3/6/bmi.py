def calculate_bmi(weight_kg, height_cm):
    # 키(cm)를 미터로 변환
    height_m = height_cm / 100.0
    # BMI 계산
    bmi = weight_kg / (height_m ** 2)
    return bmi

def bmi_category(bmi):
    if bmi < 18.5:
        return "저체중"
    elif 18.5 <= bmi < 24.9:
        return "정상 체중"
    elif 25 <= bmi < 29.9:
        return "과체중"
    else:
        return "비만"

def main():
    # 사용자 입력
    weight_kg = float(input("몸무게(kg)를 입력하세요: "))
    height_cm = float(input("키(cm)를 입력하세요: "))
    
    # BMI 계산
    bmi = calculate_bmi(weight_kg, height_cm)
    
    # BMI 범주 확인
    category = bmi_category(bmi)
    
    # 결과 출력
    print(f"BMI: {bmi:.2f}")
    print(f"BMI 범주: {category}")

# 프로그램 실행
if __name__ == "__main__":
    main()
