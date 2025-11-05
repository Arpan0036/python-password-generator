# Python Password Generator

This is a beginner friendly Python project that generates strong random passwords using the built-in `random` module.

You choose how many letters, numbers and symbols you want in your password — and the program randomly builds and shuffles the characters to create a secure password every time.

## How it works

1. Python asks for user input:
   - number of letters
   - number of numbers
   - number of symbols

2. It picks random characters from pre-built lists

3. It mixes the characters using `random.shuffle()` for maximum randomness

4. Finally it prints the generated password

## Requirements

- Python 3.x

No external libraries are required. Only the built-in `random` module is used.
