from typing import List

def func(a: str, b: float = 3.5) -> int:

    return a+b

value = func(3)
print(value)

Vector = List[float]

#fixme inches, pounds, yesars
height_weight_age = [79, 170, 40]

grades = [95, 80, 75, 62]

def add(v: Vector, w: Vector) -> Vector:

    assert len(v) == len(w), "Vectors must be the same length"

    return [v_i + w_i for v_i, w_i in zip(v, w)]

assert add([1, 2, 3], [4, 5, 6]) == [5, 7, 9]

def subtract(v: Vector, w: Vector) -> Vector:

    assert len(v) == len(w), "Vectors must be the same length"

    return [v_i - w_i for v_i, w_i in zip(v, w)]

assert subtract([5, 7, 9], [4, 5, 6]) == [1, 2, 3]

def vector_sum(vectors: List[Vector]) -> Vector:
    answer = vectors.pop()
    while(len(vectors)>0):
        answer = add(answer, vectors.pop())

    return answer

assert vector_sum([[1, 2], [3, 4], [5, 6], [7, 8]]) == [16, 20], "vector_sum error"


