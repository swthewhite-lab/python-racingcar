import random


def check_carname(x):
    '''
    이름 검증 절차
    '''
    for i in x :
        if len(i)>5:
            raise ValueError("자동차 이름은 5자를 초과할 수 없습니다.")

def carfoward():
    """
    자동차 전진시키는 함수수
    """
    a=random.randint(0,9)
    if a>=4 :
        return 1
    else :
        return 0

def status(Cars):
    """
    진행상태를 나타내는 함수
    """
    for key,value in Cars.items():
        print(f"{key} : {value*'-'}")



def winner(Cars):
    """
    최종 우승자를 나타내는 함수
    """
    maxfoward=max(Cars.values())
    winners=[key for key,value in Cars.items() if value==maxfoward]
    print(f"\n최종 우승자 : {', '.join(winners)}")

def main():
    car_name=input("경주할 자동차 이름을 입력하세요.(이름은 쉼표로 구분)").split(',')
    check_carname(car_name)
    
    Cars=dict.fromkeys(car_name,0)
    
    trycount=int(input("시도할 횟수는 몇 회인가요?"))
    if trycount ==0:
        ValueError("시도할 횟수는 0일 수 없습니다")
    
    count=0
    while count<trycount:
        for i in car_name:
            Cars[i]+=carfoward()
        status(Cars)
        print("")
        count+=1
    

    winner(Cars)





    
    


if __name__ == "__main__":
    # 프로그램이 직접 실행될 때만 main() 함수를 호출
    main()
