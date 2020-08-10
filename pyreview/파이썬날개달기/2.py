class Calculator:
    def __init__(self):
        self.value = 0

    def add(self, val):
        self.value += val





cal = MaxLimitCalculator()
cal.add(50) # 50 더하기
cal.add(60) # 60 더하기

print(cal.value) # 100 출력