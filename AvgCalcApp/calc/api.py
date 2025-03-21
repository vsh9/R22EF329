from ninja import NinjaAPI
from collections import deque
from .utils import is_prime, fetch_numbers, fibonacci, random_number, is_even
from .schemas import output

api = NinjaAPI()

# Sliding window storage (max size = 10)
window_size = 10
window = deque(maxlen=window_size)

# Mapping for third-party APIs
NUMBER_APIS = {
    "p": "http://20.224.56.144/test/primes",
    "f": "http://20.224.56.144/test/fibo",
    "e": "http://20.224.56.144/test/fibo",
    "r": "http://20.224.56.144/test/rand"
}

# Generate Fibonacci numbers up to the specified count
@api.get("/fibonacci/{count}", response=output)
def get_fibonacci(request, count: int):
    return fibonacci(count)

# Generate a random number between min_val and max_val.
@api.get("/random/{min_val}/{max_val}", response=output)
def get_random_number(request, min_val: int, max_val: int):
    return random_number(min_val, max_val)

# Check if the specified number is even
@api.get("/even/{number}", response=output)
def check_even(request, number: int):
    return {"is_even": is_even(number)}

# Handle incoming requests for numbers by ID
@api.get("/numbers/{number_id}", response=output)
def get_numbers(request, number_id: str):
    if number_id not in NUMBER_APIS:
        return {"error": "Invalid number ID"}

    # Get previous window state
    window_prev_state = list(window)

    # Fetch numbers
    new_numbers = fetch_numbers(number_id)
    if not new_numbers:
        return {"error": "Failed to fetch numbers"}

    # Remove duplicates and update the sliding window
    unique_numbers = [num for num in new_numbers if num not in window]

    # Filter only primes if number_id is 'p'
    if number_id == "p":
        unique_numbers = [num for num in unique_numbers if is_prime(num)]

    window.extend(unique_numbers)

    # Get current window state
    window_curr_state = list(window)

    # Return response
    return {
        "windowPrevState": window_prev_state,
        "windowCurrState": window_curr_state,
        "numbers": unique_numbers,
    }