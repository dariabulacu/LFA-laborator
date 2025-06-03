import json 

def load_data_json(file_name):
        with open(file_name, "r") as file:
            dfa_data = json.load(file)

        states = dfa_data["states"]
        alphabet = dfa_data["alphabet"]
        initial_state = dfa_data["initial_state"][0]
        final_states = set(dfa_data["final_state"])

        transitions = {}

        for t in dfa_data["transitions"]:
            transitions [(t["start"], t["state"])] = t["end"]
        print(f"States: {states}")
        print(f"Alphabet {alphabet}")
        print(f"Initial state {initial_state}")
        print(f"Final states {final_states}")
        print(f"Number of transitions {len(transitions)}")

        return states, alphabet, initial_state, final_states, transitions

def emulate_dfa(input, initial_state, final_states, transitions, alphabet):
    current_state = initial_state

    for  symbol in input:
            if symbol not in alphabet:
               print(f"Errors: {symbol} not in alphabet. String rejected.")
               return False
            key = (current_state, symbol)
            if key in transitions:
               next_state = transitions[key]
               print(f"{symbol} : {current_state} -- ({symbol}) -- {next_state}")
               current_state = next_state
            else: 
                print(f"No defined transition from {current_state} with input {symbol}. String rejected")
                return False
    if current_state in final_states:
        print(f"String {input} ACCEPTED")
        return True
    else:
        print(f"String {input} REJECTED")
        return False

json_file_path = 'dfa_input.json'
states, alphabet, intial_state, final_states, transitions = load_data_json(json_file_path)

if intial_state is not None:
     emulate_dfa("1", intial_state, final_states, transitions, alphabet)
     emulate_dfa("01", intial_state, final_states, transitions, alphabet)
     emulate_dfa("11", intial_state, final_states, transitions, alphabet)
     emulate_dfa("111", intial_state, final_states, transitions, alphabet)
     emulate_dfa("000", intial_state, final_states, transitions, alphabet)
     emulate_dfa("012", intial_state, final_states, transitions, alphabet)
