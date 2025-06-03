import json

def load_data_json(file_name):
    with open(file_name, "r") as file:
        pda_data = json.load(file)

    states = pda_data["states"]
    alphabet = pda_data["alphabet"]
    stack_alphabet = pda_data["stack_alphabet"]
    initial_state = pda_data["initial_state"][0]
    stack_start = pda_data["initial_stack_symbol"]
    final_states = pda_data["final_states"]
    transitions = pda_data["transitions"]

    print("States:", states)
    print("Alphabet:", alphabet)
    print("Stack alphabet:", stack_alphabet)
    print("Initial state:", initial_state)
    print("Stack starts with:", stack_start)
    print("Final states:", final_states)
    print("Transitions:", len(transitions))

    return states, alphabet, initial_state, stack_start, final_states, transitions

def apply_epsilon(state, stack, transitions):
    changed = True
    while changed:
        changed = False
        for t in transitions:
            if t["start"] != state or t["input"] != "epsilon":
                continue

            pop_req = t["pop"]
            if pop_req != "epsilon" and (not stack or stack[-1] != pop_req):
                continue

            if pop_req != "epsilon":
                stack.pop()

            if t["push"] != "epsilon":
                for sym in reversed(t["push"]):
                    stack.append(sym)

            state = t["top"]
            changed = True
            break

    return state, stack

def pda_emulate(input_str, start_state, stack_start, final_states, transitions, alphabet):
    state = start_state
    stack = [stack_start]

    if input_str == "":
        state, stack = apply_epsilon(state, stack, transitions)

    for ch in input_str:
        if ch not in alphabet:
            return False
        moved = False
        for t in transitions:
            if t["start"] != state or t["input"] != ch:
                continue
            pop_req = t["pop"]
            if pop_req != "epsilon" and (not stack or stack[-1] != pop_req):
                continue
            if pop_req != "epsilon":
                stack.pop()
            if t["push"] != "epsilon":
                for sym in reversed(t["push"]):
                    stack.append(sym)
            state = t["top"]
            moved = True
            break

        if not moved:
            return False

        state, stack = apply_epsilon(state, stack, transitions)

    state, stack = apply_epsilon(state, stack, transitions)
    return state in final_states


json_file_path = 'pda_input.json'
states, alphabet, initial_state, stack_start, final_states, transitions = load_data_json(json_file_path)
tests = ["", "ab", "aabb", "aaabbb", "a", "b", "abb"]
for s in tests:
    result = pda_emulate(s, initial_state, stack_start, final_states, transitions, alphabet)
    print(f"Input = '{s}': {'ACCEPT' if result else 'REJECT'}")
