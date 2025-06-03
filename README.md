# Laboratoare Limbaje-Formale-si-Automate

> **Limbaje Formale și Automate** – Implementantion of DFA, NFA, PDA and TM



## ☰ Table of Contents

* [Overview](#overview)
* [Features](#features)
* [Usage Examples](#usage-examples)

  * [DFA sample](#dfa-sample)
  * [NFA sample](#nfa-sample)


---

## Overview

This repository gathers the coursework for the **LFA** module (*Formal  Languages & Automata*). 

---

## Features

| Category       | What you’ll find                                 |
| -------------- | ------------------------------------------------ |
| **Playground** | JSON‑driven emulator for DFAs & NFAs             |
| **Algorithms** | subset‑construction, ε‑closure, DFA minimisation |
| **Pipeline**   | Regex ➜ NFA ➜ DFA converter                      |
| **Visuals**    | Mermaid & Graphviz diagram exporter              |
| **Tooling**    | Typer CLI, pytest + coverage, pre‑commit hooks   |



</details>

### DFA sample

Binary strings with an **odd** number of `1`s:

```mermaid
stateDiagram-v2
    [*] --- q0 : start
    q0 -(1)- q1 
    q0 -(0)- q0 
    q1 -(1)- q0 
    q1 -(0)- q1 
    q1 --- [*] : accept
```


