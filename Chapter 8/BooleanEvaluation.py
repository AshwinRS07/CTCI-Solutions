# Boolean Evaluation: Given a boolean expression consisting of the symbols 0 (false), 1 (true), &
# (AND), | (OR), and ^ (XOR), and a desired boolean result value result, implement a function to
# count the number of ways of parenthesizing the expression such that it evaluates to result.
# EXAMPLE
# countEval("l /\01011", false) -> 2
# countEval("0&0&0&1/\ ll0", true) -> 10

def boolean_evaluation_helper(expression, result, memo):
    # memo = {}
    if len(expression) == 0:
        return 0
    if len(expression) == 1:
        return 1 if str(expression) == result else 0
    if expression + str(result) in memo:
        return memo[expression + str(result)]
    ways = 0
    for i in range(1, len(expression), 2):
        left = expression[:i]
        right = expression[i+1:]

        left_true = boolean_evaluation_helper(left, True, memo)
        left_false = boolean_evaluation_helper(left, False, memo)
        right_true = boolean_evaluation_helper(right, True, memo)
        right_false = boolean_evaluation_helper(right, False, memo)

        total = (left_true + left_false) * (right_true + right_false)

        total_true = 0
        if expression[i] == "|":
            total_true = left_true * right_true + left_false * right_true + left_true * right_false
        elif expression[i] == '&':
            total_true = left_true * right_true
        elif expression[i] == '^':
            total_true = left_true*right_false + left_false*right_true
        subways = total_true if result else total-total_true
        ways += subways
    
    memo[expression+str(result)] = ways
    return memo[expression+str(result)]

def boolean_evaluation(expression, result):
    memo = {}
    return boolean_evaluation_helper(expression, result, memo)


expression = "1^0|0|1"
result = False

print(boolean_evaluation(expression, result))