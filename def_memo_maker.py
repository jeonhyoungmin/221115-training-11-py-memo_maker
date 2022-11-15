import datetime

def memo_maker(title, text):
    get_time_data = datetime.datetime.now()
    # 자바스크립트의 new Date()처럼 시간에 대한 객체가 마련되어있다.
    # 연월일에 대한 데이터를 추출하고 문자열로 변환해주는 작업을 진행했다.
    change_time_string = str(get_time_data.year) + "-" + str(get_time_data.month) + "-" + str(get_time_data.day)
    # 자바스크립트는 숫자와 문자가 + (덧셈) 기호로 결합하면, 자동으로 문자열로 바뀌는 현상이 일어나는데, 이것은 자바스크립트 특유의 특징이며 일반적으로 데이터타입이 다르면 에러가 발생한다.
    # 따라서 필요한 연월일 데이터를 str() 함수로 데이터타입을 변환하였다.

    temp_file_name = change_time_string + "-" + title + ".txt"
    # 파일명과 확장자를 결정하는 변수 temp_file_name


    # open -> write -> close 트랜잭션 패턴
    # 마치 서버 구축할 때 GET 요청으로 페이지를 응답하는 것과 비슷하다.
    make_open_txt_file = open("./" + temp_file_name, "w", encoding="utf-8")
    make_open_txt_file.write(text)
    make_open_txt_file.close()

    print("메모장 제목 :", temp_file_name)
    print("메모장 내용:", text)