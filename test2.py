import time

text = "안녕하세요"

for char in text:
    print(char, end='', flush=True)
    time.sleep(0.5)
print()

import random

print("\n간단한 숫자 맞추기 게임을 시작합니다!")
목표숫자 = random.randint(1, 100)
시도횟수 = 0

while True:
    try:
        추측 = int(input("\n1부터 100 사이의 숫자를 맞춰보세요: "))
        시도횟수 += 1

        if 추측 < 목표숫자:
            print("더 큰 숫자입니다!")

        elif 추측 > 목표숫자:
            print("더 작은 숫자입니다!")

        else:
            print(f"\n축하합니다! {시도횟수}번 만에 숫자를 맞추셨습니다!")
            break



