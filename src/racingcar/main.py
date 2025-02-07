def main():
    print("프로그램이 시작되었습니다.")

    car_names = input("경주할 자동차 이름을 입력하세요.(이름은 쉼표로 구분)\n")
    cars = car_names.split(",")

    print(cars)

    attempts = input("시도할 횟수는 몇 회인가요?\n")

    print("실행 결과\n")


if __name__ == "__main__":
    # 프로그램이 직접 실행될 때만 main() 함수를 호출
    main()
