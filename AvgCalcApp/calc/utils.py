import httpx
import requests
import time
from collections import deque
import random

# Sliding window storage (max size = 10)
window_size = 10
window = deque(maxlen=window_size)

# Mapping for third-party APIs
NUMBER_APIS = {
    "p": "http://20.224.56.144/test/primes",
    "f": "http://20.224.56.144/test/fibo",
    "e": "http://20.224.56.144/test/even",
    "r": "http://20.224.56.144/test/rand"
}

#Fetch numbers from the third-party API with a timeout of 500ms
def fetch_numbers(number_id):
    if number_id not in NUMBER_APIS:
        return None

    url = NUMBER_APIS[number_id]
    try:
        start_time = time.time()
        response = httpx.get(url, timeout=0.5)  # 500ms timeout
        elapsed_time = (time.time() - start_time) * 1000  # Convert to ms

        if elapsed_time > 500 or response.status_code != 200:
            return None

        return response.json().get("numbers", [])

    except requests.exceptions.RequestException:
        return None

#Generate a list of Fibonacci numbers up to n
def fibonacci(n):
    fib_sequence = [0, 1]
    while len(fib_sequence) < n:
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
    return fib_sequence[:n]

#Generate a random number between min_val and max_val
def random_number(min_val, max_val):
    return random.randint(min_val, max_val)

#Generate a random number between min_val and max_val.
def is_even(n):
    return n % 2 == 0

#Check if a number is prime
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True
