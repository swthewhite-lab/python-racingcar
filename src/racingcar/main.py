def main():
    def check_carname(x):
        for i in x :
            if len(i)>5:
                raise ValueError
    
    
    car_name=input("경주할 자동차 이름을 입력하세요.(이름은 쉼표로 구분)").split(',')
    check_carname(car_name)
    
    Cars=dict.fromkeys(car_name,"")

    print(Cars)


    
    print("프로그램이 시작되었습니다.")


if __name__ == "__main__":
    # 프로그램이 직접 실행될 때만 main() 함수를 호출
    main()
