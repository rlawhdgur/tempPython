# -*- coding : utf-8 -*-

# 핵심 주제 : Decorator
# 중첩 함수, 함수를 객체처럼 사용 배움

# 사칙연산을 만들 예정 (중첩함수, 객체)

def math_functions(func_name):
    """더하기, 빼기, 곱하기, 몫을 구하는 함수입니다.
    Args:
        func_name(str) : 함수 이름 기입

    Returns:
        int

    Raises:
        ValueError : 만약 Return 값이 문자면 에러를 발생시킨다.
    """

    if func_name == "add":
        def add(a, b):
            return a + b
        return add
    elif func_name == "subtract":
        def subtract(a, b):
            return a - b
        return subtract
    elif func_name == "multiple":
        def multiple(a, b):
            return a * b
        return multiple
    elif func_name == "divide":
        def divide(a, b):
            return a // b # 몫 구하는 ==> //
        return divide
    else:
        print("....")






if __name__ == "__main__":
    docstring = math_functions.__doc__
    border = '#' * 50
    print('{}\n{}\n{}\n' .format(border, docstring, border))

    x = 100
    y = 2

    add = math_functions("add")
    print("100 + 2 = {}" .format(add(x, y)))
    
    multiple = math_functions("multiple")
    print("100 * 2 = {}" .format(multiple(x, y)))

    subtract = math_functions("subtract")
    print("100 - 2 = {}" .format(subtract(x, y)))

    divide = math_functions("divide")
    print("100 // 2 = {}" .format(divide(x, y)))
    