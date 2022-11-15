from def_memo_maker import memo_maker

memo_title = input("메모장 이름을 작성하세요 >>> ")
memo_text = input("메모장 내용을 작성하세요 >>> ")

# 자바스크립트 && 논리곱, and 연산자는 파이썬에서 매우 직관적으로 and로 처리한다.

if memo_title != "" and memo_text !="":
      memo_maker(memo_title, memo_text)