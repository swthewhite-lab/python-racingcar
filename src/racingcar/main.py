import random


def main():
    print("프로그램이 시작되었습니다.")

    car_names = input("경주할 자동차 이름을 입력하세요.(이름은 쉼표로 구분)\n")
    cars = car_names.split(",")
    for car in cars:
        if len(car) > 5 :
            raise ValueError("이름이 5자를 초과합니다.")

    car_positions = {car : 0 for car in cars}

    attempts = input("시도할 횟수는 몇 회인가요?\n")
    if not attempts.isdigit():
        raise ValueError("시도 횟수는 숫자로 입력하세요.")
    attempts = int(attempts)

    print("\n실행 결과")
    for _ in range(attempts):
        movement(cars, car_positions)
        for car in cars :
            print(car + " : " + '-' * car_positions[car])
        print()

    print_winner(cars, car_positions)

def movement(cars, car_positions):
    for car in cars :
        if random.randint(0,9) >= 4 :
            car_positions[car] += 1

def get_winner(cars, car_positions):
    max_value = max(car_positions.values())
    return [car for car in cars if car_positions[car] == max_value]

def print_winner(cars, car_positions):
    winner = get_winner(cars, car_positions)
    print(f"최종 우승자 : {', '.join(winner)}")

if __name__ == "__main__":
    main()