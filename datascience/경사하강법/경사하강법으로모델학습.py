from typing import List

Vector = List[float]

# fixme ranges from -50 to 49, y is always 20 * x + 5
inputs = [(x, 20 * x + 5) for x in range(-50, 50)]

def linear_gradient(x: float, y: float, theta: Vector) -> Vector:
    slope, intercept = theta #fixme 기울기, y절편
    predicted = slope * x + intercept #fixme 모델
    error = (predicted - y) #fixme 주어진 함수의 y 값과 input y값 과의 차이
    squared_error = error ** 2 # fixme 그것의 제곱
    grad = [2 * error * x, 2 * error] #fixme 편미분
    return grad

