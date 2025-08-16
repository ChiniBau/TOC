def nfa_contains_001(string):
    current_states = {'q0'}

    for char in string:
        next_states = set()
        for state in current_states:
            if state == 'q0':
                if char == '0':
                    next_states.update(['q0', 'q1'])  # non-deterministic: stay or move
                elif char == '1':
                    next_states.add('q0')
            elif state == 'q1':
                if char == '0':
                    next_states.add('q2')
            elif state == 'q2':
                if char == '1':
                    next_states.add('q3')
            elif state == 'q3':
                next_states.add('q3')  # once accepted, stay accepted
        current_states = next_states

    return 'q3' in current_states

def main():
    print("\n--- NFA: Accepts Strings Containing '001' ---")
    while True:
        print("1. Enter a binary string")
        print("2. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            string = input("Enter a string over {0,1}: ")
            if all(c in '01' for c in string):
                if nfa_contains_001(string):
                    print(" String is ACCEPTED by the NFA (contains '001').\n")
                else:
                    print(" String is REJECTED by the NFA (does not contain '001').\n")
            else:
                print("Invalid input: Only 0 and 1 are allowed.\n")
        elif choice == '2':
            print("Exiting. Goodbye!")
            break
        else:
            print("Invalid choice! Please select 1 or 2.")

if __name__ == "__main__":
    main()
