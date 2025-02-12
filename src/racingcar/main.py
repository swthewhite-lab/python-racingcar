import random


def is_number(Data):
    """
    Data가 숫자인지 확인하는 함수.
    숫자가 아니면 ValueError를 발생시킴.
    """
    try:
        int(Data)  # Data가 int 형식인지 확인
    except ValueError as e:
        raise ValueError("숫자만 입력해주세요.") from e  # 숫자가 아닌 값 입력시 예외 처리


def validate_input(Data):
    for i in range(len(Data)):
        if len(Data[i]) > 5:
            raise ValueError("이름은 5자 이하만 가능합니다.")
        Data[i] = [Data[i], 0]
    return Data


def try_input():
    print("시도할 횟수는 몇 회인가요?")
    n = input()
    is_number(n)
    return int(n)


def play_1set_of_game(Data):
    for i in range(len(Data)):
        value = random.randint(0, 10)
        if value >= 4:
            Data[i][1] += 1
    return Data


def check_winner(Data):
    win_list, winner_count = list(), 0
    for i in range(len(Data)):
        if Data[i][1] > winner_count:
            win_list, winner_count = [Data[i][0]], Data[i][1]
        elif Data[i][1] == winner_count:
            win_list.append(Data[i][0])
    return win_list


def print_game_play_result(Data, n):
    for i in range(n):
        Data = play_1set_of_game(Data)
        for i in range(len(Data)):
            print("{0} : {1}".format(Data[i][0], "-" * Data[i][1]))
        print()
    return Data


def main():
    """
    프로그램의 진입점 함수.
    여기에서 전체 프로그램 로직을 시작합니다.
    """
    # 프로그램의 메인 로직을 여기에 구현
    print("경주할 자동차 이름을 입력하세요.(이름은 쉼표로 구분)")
    name_list = validate_input(list(map(str, input().split(","))))
    n = try_input()
    print()
    print("실행 결과")

    win_list = check_winner(print_game_play_result(name_list, n))

    print("최종 우승자 : {0}".format(', '.join(win_list)))


if __name__ == "__main__":
    # 프로그램이 직접 실행될 때만 main() 함수를 호출
    main()
