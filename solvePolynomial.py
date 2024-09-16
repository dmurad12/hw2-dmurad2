def solve_polynomial(coefficients, x_value):

    answer = 0
    highest_power_of_x = len(coefficients) - 1 
    for i in range(highest_power_of_x + 1):
        answer += coefficients[i] * (x_value ** (highest_power_of_x - i))

    return answer



coefficients = [5, 12, -3]
x_value = 3
print(solve_polynomial(coefficients, x_value))
