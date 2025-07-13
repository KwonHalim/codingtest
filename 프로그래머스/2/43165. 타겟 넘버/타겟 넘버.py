def solution(numbers, target):
    return dfs(numbers, 0, 0, target)


def dfs(numbers, index, value, target):
    if index == len(numbers) and value == target:
        return 1
    elif index == len(numbers):
        return 0

    return dfs(numbers, index + 1, value + numbers[index], target) + dfs(numbers, index + 1, value - numbers[index], target)
    