import json 

def load_data_json(file_name):
        with open(file_name, "r") as file:
            nfa_data = json.load(file)

        states = nfa_data["states"]
        alphabet = nfa_data["alphabet"]
        initial_state = nfa_data["initial_state"][0]
        final_states = set(nfa_data["final_state"])

        transitions = {}

        for state_form in states:
             for symbol in alphabet:
                  transitions[(state_form, symbol)] = set()

        for t in nfa_data["transitions"]:
            start_state = t["start"]
            symbol = t["state"]
            end_states = t["ends"]
            if (start_state, symbol) not in transitions:
                 transitions[(start_state, symbol)] = set()
            for end in end_states:
                 transitions[(start_state, symbol)].add(end)

        print(f"States: {states}")
        print(f"Alphabet {alphabet}")
        print(f"Initial state {initial_state}")
        print(f"Final states {final_states}")
        print(f"Number of transitions {len(transitions)}")

        return states, alphabet, initial_state, final_states, transitions

def emulate_nfa(input, initial_state, final_states, transitions, alphabet):
    current_states = {initial_state}

    for  symbol in input:
            if symbol not in alphabet:
               print(f"Errors: {symbol} not in alphabet. String rejected.")
               return False
            next_states = set()
            for state in current_states:
                 key = (state, symbol)
                 if key in transitions:
                      next_states.update(transitions[key])
                      print(f"{symbol} : {state} -- ({symbol}) -- {transitions[key]}")
                 else:                       
                      print(f"{symbol} : {state} -- ({symbol}) -- No transition found. Dead end")
            current_states = next_states
            if not current_states:
                print(f"No possible states left after processing {symbol}")
                return False
            else:
                print(f"Next possible states : {current_states}")

    if any(state in final_states for state in current_states):
         print(f"String {input} ACCEPTED")
         return True
    else:
         print(f"String {input} REJECTED")
         return False

json_file_path = 'nfa_input.json'
states, alphabet, intial_state, final_states, transitions = load_data_json(json_file_path)

if intial_state is not None:
     emulate_nfa("1", intial_state, final_states, transitions, alphabet)
     emulate_nfa("01", intial_state, final_states, transitions, alphabet)
     emulate_nfa("11", intial_state, final_states, transitions, alphabet)
     emulate_nfa("111", intial_state, final_states, transitions, alphabet)
     emulate_nfa("000", intial_state, final_states, transitions, alphabet)
     emulate_nfa("012", intial_state, final_states, transitions, alphabet)
