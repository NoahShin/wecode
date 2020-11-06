even_numbers = []
def even():
    for num in range(1,51):
        if num % 2 == 0:
            even_numbers.append(num)
    print(even_numbers)
    return even_numbers
even()
