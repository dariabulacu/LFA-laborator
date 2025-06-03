# Palindrome-Checking Turing Machine

This repository contains a simple Turing machine emulator in Python that decides whether a given input string (over the alphabet `{a, b}`) is a palindrome. The Turing machine is specified via a JSON configuration file, and the Python script reads this file, runs the machine on test inputs, and prints whether each string is accepted or rejected.

---

## Repository Structure


```plaintext
.
├── palindrome_tm.json     
├── tm_emulator.py           
└── README.md               
```

- **palindrome_tm.json**  
  Contains the list of states, alphabet, blank symbol, initial/final states, and transition rules for the palindrome-checking TM.

- **tm_emulator.py**  
  A minimal Python script that:  
  1. Loads the JSON configuration.  
  2. Emulates the Turing machine (dynamically expanding the tape).  
  3. Tests example strings (e.g., `"aba"`, `"abba"`, etc.).  
  4. Prints `ACCEPT` if the input is recognized as a palindrome, or `REJECT` otherwise.

---

## Prerequisites

- Python 3.6 or higher  
- No additional third-party libraries required (uses only Python’s built-in `json` module).
