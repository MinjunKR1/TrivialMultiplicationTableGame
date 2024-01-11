import random

n1 = 0
n2 = 0

p = 0

c1 = 0
c2 = 0

print("===================")
print("개 하찮은 구구단 게임")
print("===================")
s1 = str(input("하/중/상 > "))

if s1 == "하":
    print("===================")
    print("난이도 : 하")
    p1 = 5
    p2 = 1
    while True:
        if p1+1 == p2:
            break
        elif p1 > 0:
            print("===================")
            print(f"{p2}번 문제 ({p1-p2} 문제 남음)")
            n1 = (random.randint(1,9))
            n2 = (random.randint(1,9))
            print(f"문제 : {n1} x {n2}")
            e = int(input("답 > "))
            if n1*n2 == e:
                print("===================")
                print(f"정답입니다. ( 답 : {n1*n2} )")
                n1 = 0
                n2 = 0
                c1 = int(c1) + 1
            else:
                print("===================")
                print("틀렸습니다 애송이 더 강해져서 와라 ㅋ")
                print("===================")
                c2 =  int(c2) + 1
                n1 = 0
                n2 = 0
            p2 = p2+1
        else:
            print("오류 발생")
            break
    print(f"게임이 끝났습니다 문제수 : {p1}개 , 정답수 : {c1}, 오답수 : {c2}")
elif s1 == "중":
    print("===================")
    print("난이도 : 중")
    p1 = 10
    p2 = 1
    while True:
        if p1+1 == p2:
            break
        elif p1 > 0:
            print("===================")
            print(f"{p2}번 문제 ({p1-p2} 문제 남음)")
            n1 = (random.randint(1,30))
            n2 = (random.randint(1,30))
            print(f"문제 : {n1} x {n2}")
            e = int(input("답 > "))
            if n1*n2 == e:
                print("===================")
                print(f"정답입니다. ( 답 : {n1*n2} )")
                n1 = 0
                n2 = 0
                c1 = int(c1) + 1
            else:
                print("===================")
                print("틀렸습니다 애송이 더 강해져서 와라 ㅋ")
                n1 = 0
                n2 = 0
                c2 = int(c2) + 1
            p2 = p2+1
        else:
            print("오류 발생")
            break
    print(f"게임이 끝났습니다 문제수 : {p1}개 , 정답수 : {c1}, 오답수 : {c2}")
elif s1 == "상":
    print("===================")
    print("난이도 : 상")
    p1 = 20
    p2 = 1
    while True:
        if p1+1 == p2:
            break
        elif p1 > 0:
            print("===================")
            print(f"{p2}번 문제 ({p1-p2} 문제 남음)")
            n1 = (random.randint(1,99))
            n2 = (random.randint(1,99))
            print(f"문제 : {n1} x {n2}")
            e = int(input("답 > "))
            if n1*n2 == e:
                print("===================")
                print(f"정답입니다. ( 답 : {n1*n2} )")
                n1 = 0
                n2 = 0
                c1 = int(c1) + 1
            else:
                print("===================")
                print("틀렸습니다 애송이 더 강해져서 와라 ㅋ")
                print("===================")
                n1 = 0
                n2 = 0
                c2 = int(c2) + 1
            p2 = p2+1
        else:
            print("오류 발생")
            break
    print(f"게임이 끝났습니다 문제수 : {p1}개 , 정답수 : {c1}, 오답수 : {c2}")