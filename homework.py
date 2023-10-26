def calculate_safety_cost(base_amount, target_amount, rate):
    total_amount = target_amount * rate + base_amount
    return total_amount

target_amount = float(input("대상액(재료비+노무비)을 입력하세요: "))
rate = float(input("비율을 입력하세요 (0.1은 10%를 나타냅니다): "))
base_amount = float(input("기초액을 입력하세요: "))

safety_cost = calculate_safety_cost(base_amount, target_amount, rate)

print(f"안전관리비는 {safety_cost}원입니다.")
