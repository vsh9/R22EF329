# Number Classification API

## Overview
This project provides an API to classify numbers based on different criteria such as:
- Checking if a number is prime.
- Checking if a number is even.
- Generating Fibonacci sequences.
- Generating random numbers within a specified range.
- Managing a sliding window of previously fetched numbers.

The API integrates with external services to fetch and classify numbers.

## Features
- Implements a sliding window (max size = 10) to store recently processed numbers.
- Uses external APIs to classify numbers as prime, even, Fibonacci, or random.
- Filters and removes duplicate numbers before updating the sliding window.

## Technologies Used
- Python
- Django Ninja (FastAPI alternative for Django)
- Collections (Deque for sliding window)
- External API integrations

## Installation
1. Clone the repository:
   ```sh
   git clone https://github.com/vsh9/R22EF329.git
   ```
2. Navigate to the project directory:
   ```sh
   cd R22EF329
   ```

## API Endpoints

### 1. Generate Fibonacci Sequence
- **Endpoint**: `GET /fibonacci/{count}`
- **Description**: Returns a Fibonacci sequence of the given count.
- **Example Request**:
  ```sh
  GET /fibonacci/5
  ```
- **Example Response**:
  ```json
  {
    "sequence": [0, 1, 1, 2, 3]
  }
  ```

### 2. Generate Random Number
- **Endpoint**: `GET /random/{min_val}/{max_val}`
- **Description**: Returns a random number within the specified range.
- **Example Request**:
  ```sh
  GET /random/10/100
  ```
- **Example Response**:
  ```json
  {
    "random_number": 42
  }
  ```

### 3. Check Even Number
- **Endpoint**: `GET /even/{number}`
- **Description**: Checks if a given number is even.
- **Example Request**:
  ```sh
  GET /even/8
  ```
- **Example Response**:
  ```json
  {
    "is_even": true
  }
  ```

### 4. Fetch Numbers by ID
- **Endpoint**: `GET /numbers/{number_id}`
- **Description**: Fetches numbers from external APIs based on the given ID (p, f, e, r).
- **Example Request**:
  ```sh
  GET /numbers/p
  ```
- **Example Response**:
  ```json
  {
    "windowPrevState": [2, 3, 5],
    "windowCurrState": [2, 3, 5, 7, 11],
    "numbers": [7, 11]
  }
  ```

## Sliding Window Implementation
- The project maintains a **sliding window of the last 10 numbers** fetched from external sources.
- This ensures that duplicates are not reprocessed and provides an efficient number tracking mechanism.

## External APIs Used
- **Prime Number API**: `http://20.224.56.144/test/primes`
- **Fibonacci API**: `http://20.224.56.144/test/fibo`
- **Even Number API**: `http://20.224.56.144/test/fibo`
- **Random Number API**: `http://20.224.56.144/test/rand`

