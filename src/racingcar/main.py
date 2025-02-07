import random
def main():
    print("프로그램이 시작되었습니다.")

    car_names = input("경주할 자동차 이름을 입력하세요.(이름은 쉼표로 구분)\n")
    cars = car_names.split(",")
    car_positions = {car : 0 for car in cars}

    print(cars)
    print(car_positions)

    attempts = int(input("시도할 횟수는 몇 회인가요?\n"))

    print("\n실행 결과")

        
def movement(cars, car_positions) :
    for car in cars :
        if (random.randint(0,9) >= 4) :
            car_positions[car] += 1

if __name__ == "__main__":
    main()
