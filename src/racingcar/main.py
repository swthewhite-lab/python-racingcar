import random

"""
자동차 경주 프로그램

이 모듈은 간단한 자동차 경주 게임을 구현합니다. 사용자로부터 자동차 이름을 입력받고,
정해진 횟수만큼 자동차가 전진하는 시뮬레이션을 진행하여 최종 우승자를 출력합니다.
"""


def get_car_names():
    names = input("경주할 자동차 이름을 입력하세요.(이름은 쉼표로 구분)").split(',')
    check_carname(names)
    return names


def get_try_count():
    count = int(input("시도할 횟수는 몇 회인가요?"))
    if count == 0:
        raise ValueError("시도 횟수는 0보다 커야 합니다.")
    return count


def check_carname(x):
    """
    자동차 이름을 검증하는 함수.
    이름이 5자를 초과할 경우 예외를 발생시킨다.
    """
    if not x:
        raise ValueError("자동차 이름은 비어있을 수 없습니다.")
    for i in x:
        if not i.strip():
            raise ValueError("자동차 이름은 공백일 수 없습니다.")
        elif len(i) > 5:
            raise ValueError("자동차 이름은 5자를 초과할 수 없습니다.")
    if len(x) != len(set(x)):
        raise ValueError("자동차 이름은 중복될 수 없습니다.")


def carfoward():
    """
    자동차를 전진시키는 함수.
    0에서 9까지 랜덤값을 생성하여 4 이상이면 1을 반환, 그렇지 않으면 0을 반환한다.
    """
    random_number = random.randint(0, 9)
    if random_number >= 4:
        return 1
    return 0


def status(cars):
    """
    각 자동차의 진행 상태를 출력하는 함수.
    각 자동차의 진행 상태를 '-'로 나타낸다.
    """
    for key, value in cars.items():
        print(f"{key} : {value * '-'}")


def winner(cars):
    """
    최종 우승자를 출력하는 함수.
    가장 많은 전진을 한 자동차들을 우승자로 표시한다.
    """
    maxfoward = max(cars.values())
    winners = [key for key, value in cars.items() if value == maxfoward]
    print(f"\n최종 우승자 : {', '.join(winners)}")


def main():
    """
    프로그램의 메인 함수.
    자동차 이름과 시도할 횟수를 입력받고, 경주를 진행한 후 우승자를 출력한다.
    """
    try:
        car_names = get_car_names()
        cars = dict.fromkeys(car_names, 0)
        try_count = get_try_count()
        
        for _ in range(try_count):
            for name in car_names:
                cars[name] += carfoward()
            status(cars)
            print()
        
        winner(cars)
    except ValueError as e:
        print(f"오류: {str(e)}")
        raise


if __name__ == "__main__":
    # 프로그램이 직접 실행될 때만 main() 함수를 호출
    main()
