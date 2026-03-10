def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b


def first_word(text):
    text = text.strip()
    return text.split()[0]


def first_word_longer(text):
    words = text.strip().split()
    longest = words[0]
    for word in words:
        if len(word) > len(longest):
            longest = word
    return longest


def is_even(n):
    return n % 2 == 0


def celsius_to_fahrenheit(c):
    return (c * 9/5) + 32


def count_vowels(text):
    vowels = "aeiouAEIOU"
    count = 0
    for char in text:
        if char in vowels:
            count += 1
    return count