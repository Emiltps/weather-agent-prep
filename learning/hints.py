def total(numbers: list[float]) -> float:
    return sum(numbers)

def average(numbers: list[float]) -> float:
    return sum(numbers) / len(numbers)

def median(numbers: list[float]) -> float:
    numbers = sorted(numbers)
    n = len(numbers)

    if n == 0:
        raise ValueError("List cannot be empty")
    if n % 2 == 0:
        half = n // 2
        return (numbers[half - 1] + numbers[half]) / 2
    else:
        half = n // 2
        return numbers[half]


# Dictionary is a data structure that stores information as a key-value pair
def find_user(users: dict[str, int], name: str) -> int | None:
    return users.get(name)

print(total([1.0, 2.5, 3.0]))

print("Median")
print(median([1.0, 2.5, 3.0]))
print(median([3.0, 2.5, 1.0]))
print(median([3.0, 2.5, 1.0 , 7]))

print(average([1.0, 2.5, 3.0]))

#print(average(["a", "b"]))          # wrong on purpose
print(find_user({"john": 30 }, "john"))
age = find_user({"john": 30}, "anna")
print(age + 1)                       # wrong on purpose: age might be None