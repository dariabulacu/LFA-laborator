# LFA-laborator

A collection of assignments, examples, and implementations for the “Limbaje Formale și Automate” (Formal Languages & Automata) course.  
This repository contains code for (deterministic/non-deterministic) finite automata, pushdown automata, Turing machines

---

## Repository Structure

```plaintext
LFA-laborator
├── DFA/                   
│   ├── dfa_input.json     
│   ├── dfa.py     
│   └── README.md           
│
├── NFA/                    
│   ├── nfa_input.json     
│   ├── nfa.py      
│   └── README.md
│
├── PDA/                    
│   ├── pda_input.json     
│   ├── pda.py   
│   └── README.md
│
├── TM/                     
│   ├── palindrome_tm.json  
│   ├── tm.py       
│   └── README.md
│
└── README.md      
```         

## Overview


- **DFA (Deterministic Finite Automata)**
  - JSON files describing states, alphabet, transitions, initial/final states.  
  - A Python emulator that loads a DFA from JSON and tests input strings.

- **NFA (Non-deterministic Finite Automata)**
  - Similar structure to DFA, but supports multiple transitions per symbol.  
  - A simple Python simulator that handles nondeterminism via recursion or breadth-first search.

- **PDA (Pushdown Automata)**
  - JSON definition of a sample PDA (e.g., recognizing balanced parentheses or `aⁿbⁿ`).  
  - A Python script (emulator) illustrating how to apply transitions, ε-moves, and stack operations.

- **TM (Turing Machines)**
  - JSON definitions for Turing machines (e.g., palindrome checker).  
  - A minimal Python emulator that dynamically expands the tape and follows the JSON transitions.

## Getting Started

### Prerequisites

- Python 3.6 or higher  
- No external dependencies (all scripts use only the standard library, e.g. `json`, `sys`)

---

