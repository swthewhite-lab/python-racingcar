def main():
    import random
    car_names = input("경주할 자동차 이름을 입력하세요.(이름은 쉼표로 구분): ").split(",")
    car_names = list(set(name.strip() for name in car_names if name.strip()))
    car_dict = {}

    for name in car_names:
        name = name.strip()
        if len(name) > 5:
            raise ValueError("⚠ 자동차 이름은 5자 이하만 가능합니다!")

        car_dict[name] = 0  

    try:
        N = int(input("시도할 횟수는 몇 회인가요? "))
        if N <= 0:
            raise ValueError("⚠ 시도 횟수는 1 이상이어야 합니다!")
    except ValueError:
        print("⚠ 잘못된 입력입니다. 숫자를 입력하세요.")
        return

    carPos = {name: 0 for name in car_dict}

    for _ in range(N):
        for name in car_dict:
            rand_num = random.randint(1, 9)  
            if rand_num >= 4:  
                carPos[name] += 1

        for name in carPos:
            print(f"{name} : {'-' * carPos[name] if carPos[name] > 0 else ' '}")
        print()  # 줄바꿈 추가

    print()  # 최종 출력과 구분을 위해 개행 추가
    maxPos = max(carPos.values())
    winners = [name for name, pos in carPos.items() if pos == maxPos]

    print(f"최종 우승자 : {', '.join(winners)}")

if __name__ == "__main__":
    main()
