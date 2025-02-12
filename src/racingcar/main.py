<<<<<<< HEAD
"""자동차 경주 게임 메인 스크립트"""
=======
""" 자동차 경주 게임 메인 스크립트 """
>>>>>>> a8f68ff7178f271a24793fe592b609c29719c4aa

import random


<<<<<<< HEAD
# 상수 정의
MOVE_THRESHOLD = 4  # 자동차가 전진할 최소 랜덤 값
MIN_RAND = 1  # 랜덤 숫자의 최소값
MAX_RAND = 9  # 랜덤 숫자의 최대값
MAX_NAME_LENGTH = 5  # 자동차 이름 최대 길이


def move_cars(car_positions):
    """자동차 이동 로직 (랜덤 숫자가 MOVE_THRESHOLD 이상이면 이동)"""

    for name in car_positions:
        if random.randint(MIN_RAND, MAX_RAND) >= MOVE_THRESHOLD:
=======
def move_cars(car_positions):
    """자동차 이동 로직 (랜덤 숫자가 4 이상이면 이동)"""

    for name in car_positions:
        if random.randint(1, 9) >= 4:
>>>>>>> a8f68ff7178f271a24793fe592b609c29719c4aa
            car_positions[name] += 1


def print_race(car_positions):
    """현재 경주 상태 출력"""

    for name, pos in car_positions.items():
        if pos > 0:
            print(f"{name} : {'-' * pos}")
        else:
            print(f"{name} : {' '.rstrip()}")  # Trailing whitespace 제거
    print()


def get_winners(car_positions):
    """최종 우승자 결정"""

    max_pos = max(car_positions.values())
<<<<<<< HEAD
    return [
        name for name, pos in car_positions.items() if pos == max_pos
    ]  # ✅ 긴 줄 개행 처리
=======
    return [name for name, pos in car_positions.items() if pos == max_pos]
>>>>>>> a8f68ff7178f271a24793fe592b609c29719c4aa


def main():
    """메인 함수"""

<<<<<<< HEAD
    car_names = input("경주할 자동차 이름을 입력하세요. (이름은 쉼표로 구분): ").split(
        ","
    )  # ✅ 긴 문자열 개행 처리

    car_names = list(
        dict.fromkeys(name.strip() for name in car_names if name.strip())
    )  # ✅ 중복 제거 및 공백 제거 (가독성 향상)

    for name in car_names:
        if len(name) > MAX_NAME_LENGTH:
            raise ValueError(
                f"⚠ 자동차 이름은 {MAX_NAME_LENGTH}자 이하만 가능합니다!"
            )  # ✅ 긴 문자열 개행 처리

    try:
        num_attempts = int(input("시도할 횟수는 몇 회인가요? "))  # 시도 횟수 입력
=======
    car_names = input("경주할 자동차 이름을 입력하세요."
                      "(이름은 쉼표로 구분): ").split(",")
    car_names = list(dict.fromkeys(
        name.strip() for name in car_names if name.strip()
    ))  # ✅ 올바른 들여쓰기 수정

    for name in car_names:
        if len(name) > 5:
            raise ValueError("⚠ 자동차 이름은 5자 이하만 가능합니다!")

    try:
        num_attempts = int(input("시도할 횟수는 몇 회인가요? "))  # 변수명 수정
>>>>>>> a8f68ff7178f271a24793fe592b609c29719c4aa
        if num_attempts <= 0:
            raise ValueError("⚠ 시도 횟수는 1 이상이어야 합니다!")
    except ValueError:
        print("⚠ 잘못된 입력입니다. 숫자를 입력하세요.")
        return

    car_positions = {name: 0 for name in car_names}  # 자동차 위치 초기화

<<<<<<< HEAD
    for _ in range(num_attempts):
=======
    for _ in range(num_attempts):  # 변수명 수정
>>>>>>> a8f68ff7178f271a24793fe592b609c29719c4aa
        move_cars(car_positions)  # 자동차 이동
        print_race(car_positions)  # 현재 상태 출력

    winners = get_winners(car_positions)  # 우승자 결정
    print(f"\n최종 우승자 : {', '.join(winners)}")


if __name__ == "__main__":
    main()  # ✅ 마지막 빈 줄 제거 (W391 해결) 현재 코드에서 """자동차 경주 게임 메인 스크립트"""

import random


# 상수 정의
MOVE_THRESHOLD = 4  # 자동차가 전진할 최소 랜덤 값
MIN_RAND = 1  # 랜덤 숫자의 최소값
MAX_RAND = 9  # 랜덤 숫자의 최대값
MAX_NAME_LENGTH = 5  # 자동차 이름 최대 길이


def move_cars(car_positions):
    """자동차 이동 로직 (랜덤 숫자가 MOVE_THRESHOLD 이상이면 이동)"""

    for name in car_positions:
        if random.randint(MIN_RAND, MAX_RAND) >= MOVE_THRESHOLD:
            car_positions[name] += 1


def print_race(car_positions):
    """현재 경주 상태 출력"""

    for name, pos in car_positions.items():
        if pos > 0:
            print(f"{name} : {'-' * pos}")
        else:
            print(f"{name} : {' '.rstrip()}")  # Trailing whitespace 제거
    print()


def get_winners(car_positions):
    """최종 우승자 결정"""

    max_pos = max(car_positions.values())
    return [
        name for name, pos in car_positions.items() if pos == max_pos
    ]  # ✅ 긴 줄 개행 처리


def main():
    """메인 함수"""

    car_names = input("경주할 자동차 이름을 입력하세요. (이름은 쉼표로 구분): ").split(
        ","
    )  # ✅ 긴 문자열 개행 처리

    car_names = list(
        dict.fromkeys(name.strip() for name in car_names if name.strip())
    )  # ✅ 중복 제거 및 공백 제거 (가독성 향상)

    for name in car_names:
        if len(name) > MAX_NAME_LENGTH:
            raise ValueError(
                f"⚠ 자동차 이름은 {MAX_NAME_LENGTH}자 이하만 가능합니다!"
            )  # ✅ 긴 문자열 개행 처리

    try:
        num_attempts = int(input("시도할 횟수는 몇 회인가요? "))  # 시도 횟수 입력
        if num_attempts <= 0:
            raise ValueError("⚠ 시도 횟수는 1 이상이어야 합니다!")
    except ValueError:
        print("⚠ 잘못된 입력입니다. 숫자를 입력하세요.")
        return

    car_positions = {name: 0 for name in car_names}  # 자동차 위치 초기화

    for _ in range(num_attempts):
        move_cars(car_positions)  # 자동차 이동
        print_race(car_positions)  # 현재 상태 출력

    winners = get_winners(car_positions)  # 우승자 결정
    print(f"\n최종 우승자 : {', '.join(winners)}")


if __name__ == "__main__":
    main()  # ✅ 마지막 빈 줄 제거 (W391 해결)