import random


THRESHOLD = 4  # 성공 기준 값
MAX_RANDOM_VALUE = 10  # 랜덤 숫자의 최대값


def is_number(data):
    """
    data가 숫자인지 확인하는 함수.
    숫자가 아니면 ValueError를 발생시킴.
    """
    try:
        return int(data)  # data가 int 형식인지 확인
    except ValueError as e:
        raise ValueError("숫자만 입력해주세요.") from e  # 숫자가 아닌 값 입력시 예외 처리


def validate_name(data):
    for i in range(len(data)):
        if len(data[i]) > 5:
            raise ValueError("이름은 5자 이하만 가능합니다.")
        elif len(data[i]) == 0:
            raise ValueError("이름은 빈칸일 수 없습니다.")
        elif data.count(data[i]) != 1:
            raise ValueError("중복되는 이름이 있습니다.")
        data[i] = [data[i], 0]


def validate_input(data):
    if isinstance(data, int):
        if data <= 0:
            raise ValueError("시도할 횟수는 양의 정수이어야 합니다.")
    elif isinstance(data, list):
        validate_name(data)
    return data


def try_input():
    print("시도할 횟수는 몇 회인가요?")
    try_number = input()
    try_number = is_number(try_number)
    validate_input(try_number)
    return try_number


def play_1set_of_game(data):
    for i in range(len(data)):
        value = random.randint(0, MAX_RANDOM_VALUE)
        if value >= THRESHOLD:
            data[i][1] += 1
    return data


def check_winner(data):
    win_list, winner_count = list(), 0
    for i in range(len(data)):
        if data[i][1] > winner_count:
            win_list, winner_count = [data[i][0]], data[i][1]
        elif data[i][1] == winner_count:
            win_list.append(data[i][0])
    return win_list


def print_game_play_result(data, try_number):
    for i in range(try_number):
        data = play_1set_of_game(data)
        for i in range(len(data)):
            print("{0} : {1}".format(data[i][0], "-" * data[i][1]))
        print()
    return data


def main():
    """
    프로그램의 진입점 함수.
    여기에서 전체 프로그램 로직을 시작합니다.
    """
    # 프로그램의 메인 로직을 여기에 구현
    print("경주할 자동차 이름을 입력하세요.(이름은 쉼표로 구분)")
    get_name = input().replace(" ", "").split(",")
    name_list = validate_input(list(map(str, get_name)))
    try_number = try_input()
    print()
    print("실행 결과")

    win_list = check_winner(print_game_play_result(name_list, try_number))

    print("최종 우승자 : {0}".format(', '.join(win_list)))


if __name__ == "__main__":
    # 프로그램이 직접 실행될 때만 main() 함수를 호출
    main()
