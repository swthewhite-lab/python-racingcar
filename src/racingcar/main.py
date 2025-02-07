import random
def main():
    print("프로그램이 시작되었습니다.")

    car_names = input("경주할 자동차 이름을 입력하세요.(이름은 쉼표로 구분)\n")
    cars = car_names.split(",")
    car_positions = {car : 0 for car in cars}

    attempts = int(input("시도할 횟수는 몇 회인가요?\n"))

    print("\n실행 결과")
    for i in range(attempts) :
        movement(cars, car_positions)
        for car in cars :
            print(car + " : " + '-' * car_positions[car])
        print()

    printWinner(cars, car_positions)
        
def movement(cars, car_positions) :
    for car in cars :
        if (random.randint(0,9) >= 4) :
            car_positions[car] += 1

def printWinner(cars, car_positions) :
    winners = []
    max_value = max(car_positions.values())

    for car in cars : 
        if (car_positions[car] == max_value) :
            winners.append(car)
    
    print(f"최종 우승자 : {', '.join(winners)}")

if __name__ == "__main__":
    main()
