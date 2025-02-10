import random



def get_car_names():
    names = input("경주할 자동차 이름을 입력하세요.(이름은 쉼표로 구분)\n").split(",")
    names = [name.strip() for name in names]

    if not names or any(len(name) > 5 or not name for name in names):
        raise ValueError("자동차 이름은 1~5자의 문자여야 합니다.")

    return names



def get_attempt_count():
    try:
        count = int(input("시도할 횟수는 몇 회인가요?\n"))
        if count <= 0:
            raise ValueError
        return count
    except ValueError as e:
        raise ValueError("올바른 횟수를 입력하세요. (양의 정수)") from e



def move_car():
    if random.randint(0, 9) >= 4:
        return "-"
    return ""



def run_race(cars, attempts):
    results = {car: "" for car in cars}

    print("\n실행 결과")
    for _ in range(attempts):
        for car in cars:
            results[car] += move_car()
        for car, progress in results.items():
            print(f"{car} : {progress}")
        print()
    return results



def get_winners(results):
    max_distance = max(len(progress) for progress in results.values())
    winners = [
        car for car, progress in results.items()
        if len(progress) == max_distance
        ]
    return winners



def main():
    try:
        cars = get_car_names()
        attempts = get_attempt_count()
        results = run_race(cars, attempts)
        winners = get_winners(results)
        print(f"최종 우승자 : {', '.join(winners)}")
    except ValueError as e:
        print(f"입력 오류: {e}")
        raise




if __name__ == "__main__":
    main()
