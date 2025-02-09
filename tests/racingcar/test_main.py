import pytest
from unittest.mock import patch
from racingcar.main import main

# 상수 정의
MOVING_FORWARD = 4
STOP = 3

# 전진 및 정지 동작 테스트
def test_전진_및_정지(capsys):
    """
    자동차가 전진하거나 정지하는 동작을 테스트합니다.
    'random.randint' 값을 모의하여, 전진 또는 정지 여부를 제어합니다.
    'capsys'를 이용하여 출력값을 캡처하여 검증합니다.
    """
    with patch('random.randint', side_effect=[MOVING_FORWARD, STOP]):  # 상수 사용
        # 자동차 이름과 시도 횟수에 대한 사용자 입력을 모의 처리
        with patch('builtins.input', side_effect=["pobi,woni", "1"]):
            main()  # 프로그램 실행

        # 출력값을 캡처한 후 검증
        캡처된_출력 = capsys.readouterr().out
        assert all(예상_출력 in 캡처된_출력 for 예상_출력 in ["pobi : -", "woni : ", "최종 우승자 : pobi"])


# 이름에 대한 예외 처리 테스트
def test_이름에_대한_예외():
    """
    자동차 이름에 대한 예외 처리를 테스트합니다.
    'pytest.raises'를 사용해 IllegalArgumentException과 유사한 ValueError를 발생시키는지 검증합니다.
    """
    with pytest.raises(ValueError):
        # 자동차 이름이 잘못된 경우에 대한 입력을 모의 처리
        with patch('builtins.input', side_effect=["pobi,javaji", "1"]):
            main()  # 프로그램 실행

# 추가적인 시나리오에 대한 테스트를 필요에 따라 작성할 수 있습니다.

# 이름에 대한 예외 처리 테스트
def test_시도에_대한_예외():
    """
    시도 횟수에 대한 예외 처리를 테스트합니다.
    'pytest.raises'를 사용해 IllegalArgumentException과 유사한 ValueError를 발생시키는지 검증합니다.
    """
    with pytest.raises(ValueError):
        # 자동차 이름이 잘못된 경우에 대한 입력을 모의 처리
        with patch('builtins.input', side_effect=["pobi,javaji", "0"]):
            main()  # 프로그램 실행

# 이름의 중복에 대한 예외 처리 테스트
def test_중복에_대한_예외():
    """
    이름 중복에 대한 예외 처리를 테스트합니다.
    'pytest.raises'를 사용해 IllegalArgumentException과 유사한 ValueError를 발생시키는지 검증합니다.
    """
    with pytest.raises(ValueError):
        # 자동차 이름이 잘못된 경우에 대한 입력을 모의 처리
        with patch('builtins.input', side_effect=["pobi,javaji,pobi", "1"]):
            main()  # 프로그램 실행
