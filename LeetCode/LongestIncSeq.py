def longest_substring(list_of_ints):
    dp = [0] * len(list_of_ints)
    dp[0] = 1
    left = right = 0
    max_len = 0
    curr_start = 0
    for i in range(1, len(list_of_ints)):
        if list_of_ints[i - 1] < list_of_ints[i]:
            dp[i] = dp[i - 1] + 1
        else:
            dp[i] = 1
            curr_start = 1
        if dp[i] > max_len:
            max_len = dp[i]
            left = curr_start
            right = i
    sub_arr = []
    for i in range(left, right + 1):
        sub_arr.append(list_of_ints[i])
    return sub_arr
print(longest_substring([1, 2, 3, 4, 5, 4, 7, 8, 9]))
