# Coins: Given an infinite number of quarters (25 cents), dimes (1O cents), nickels (5 cents), and
# pennies (1 cent), write code to calculate the number of ways of representing n cents.

# Most optimized

def coins_dp_iterative(amount, coins = [1,5,10,25]):
    dp = [[0] * (len(coins)+1) for i in range(amount+1)]
    dp[0] = [1] * (len(coins)+1)

    for a in range(1, amount+1):
        for i in range(len(coins)-1,-1,-1):
            dp[a][i] = dp[a][i+1]
            if a - coins[i] >= 0:
                dp[a][i] += dp[a-coins[i]][i]
    return dp[amount][0]

# More optimized 

# def coins_dp_recursive(amount):
#     coins = [1,5,10,25]
#     cache = {}
#     def dfs(i,a):
#         if a == amount:
#             return 1
#         if a > amount:
#             return 0
#         if i ==len(coins):
#             return 0
#         if (i,a) in cache:
#             return cache[(i,a)]

#         cache[(i,a)] = dfs(i, a + coins[i]) + dfs(i+1, a)
#         return cache[(i,a)]
#     return dfs(0,0)

# Not very optimized - exponential

# def coins(n):
#     result = 0
#     paths = []
#     def helper(path, cur_sum):
#         nonlocal result, paths
#         # print(path, cur_sum)
#         if cur_sum == n: 
#             if path not in paths:
#                 paths.append(path)
#                 result += 1
#             return
#         else:
#             if n - cur_sum >= 25:
#                 helper(path + [25], cur_sum+25)
#             if n - cur_sum >= 10:
#                 helper(path + [10], cur_sum+10)
#             if n - cur_sum >= 5:
#                 helper(path + [5], cur_sum+5)
#             if n - cur_sum >= 1:
#                 helper(path + [1], cur_sum+1)
#             return
#     helper([], 0)
#     return result

tests = [5, 10, 15, 20, 25]

for test in tests:
    print(test, ":", coins_dp_iterative(test))