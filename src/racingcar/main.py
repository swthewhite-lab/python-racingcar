import random


def main():
    """
    프로그램을 실행하고, 자동차 경주의 시뮬레이션을 수행하는 함수
    사용자로부터 자동차 이름과 시도 횟수를 입력받고, 각 시도마다
    경주를 진행하여 최종 우승자를 출력.
    """
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
    """
    각 자동차가 0에서 9 사이의 랜덤 숫자를 생성하여, 
    4 이상의 숫자가 나오면 해당 자동차의 위치를 1 증가시키는 함수
    """
    for car in cars :
        if random.randint(0,9) >= 4 :
            car_positions[car] += 1

def get_winner(cars, car_positions):
    """
    경주에서 우승한 자동차를 구하는 함수
    """
    max_value = max(car_positions.values())
    return [car for car in cars if car_positions[car] == max_value]

def print_winner(cars, car_positions):
    """
    최종 우승자를 출력하는 함수
    """
    winner = get_winner(cars, car_positions)
    print(f"최종 우승자 : {', '.join(winner)}")

if __name__ == "__main__":
    main()