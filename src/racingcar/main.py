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
    except ValueError:
        raise ValueError("올바른 횟수를 입력하세요. (양의 정수)")