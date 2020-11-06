def even(numbers):
    even_numbers = []
    for num in range(1,51):
        if num % 2 == 0:
            even_numbers = even_numbers.append(num)
            return even_numbers
