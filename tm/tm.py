import json

def load_data_json(file_name):
    
    with open(file_name, "r") as file:
        tm_data = json.load(file)

    states = tm_data["states"]
    alphabet = tm_data["alphabet"]
    blank_symbol = tm_data["initial_stack_symbol"] 
    initial_state = tm_data["initial_state"][0]
    final_states = tm_data["final_states"]
    transitions = tm_data["transitions"]

    print("States:", states)
    print("Alphabet:", alphabet, "+", blank_symbol)
    print("Initial state:", initial_state)
    print("Blank symbol:", blank_symbol)
    print("Final states:", final_states)
    print("Transitions:", len(transitions))
    return states, alphabet, initial_state, blank_symbol, final_states, transitions

def tm_emulate(input_str, start_state, blank_symbol, final_states, transitions, alphabet):
   
    tape = list(input_str)
    head = 0
    state = start_state

    while True:
        if state in final_states:
            return True
        if head < 0:
            tape.insert(0, blank_symbol)
            head = 0
        elif head >= len(tape):
            tape.append(blank_symbol)

        current_symbol = tape[head]
        moved = False
        for t in transitions:
            if t["start"] == state and t["input"] == current_symbol:
                tape[head] = t["push"]
                direction = t.get("direction", "R").upper()
                if direction == "R":
                    head += 1
                elif direction == "L":
                    head -= 1
                state = t["top"]
                moved = True
                break
        if not moved:
            return False

   
states, alphabet, initial_state, blank_symbol, final_states, transitions = load_data_json("palindrome_tm.json")
tests = ["aba", "abba", "a", "aa", "abc", "abcba", ""]
for s in tests:
    accepted = tm_emulate(s, initial_state, blank_symbol, final_states, transitions, alphabet)
    print(f"Input = '{s}': {'ACCEPT' if accepted else 'REJECT'}")