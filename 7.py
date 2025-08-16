def nfa_ends_with_01(string):
    current_states = {'q0'}
    
    for char in string:
        next_states = set()
        for state in current_states:
            if state == 'q0':
                if char == '0':
                    next_states.update({'q0', 'q1'})
                elif char == '1':
                    next_states.add('q0')
            elif state == 'q1':
                if char == '1':
                    next_states.add('q2')
        current_states = next_states
    
    return 'q2' in current_states

def main():
    print("\n---- NFA Menu ----")
    while True:
        print("1. Input a string to check")
        print("2. Exit")
        choice = input("Enter your choice (1 or 2): ")
        
        if choice == '1':
            string = input("Enter a binary string (end with 01): ")
            if all(ch in '01' for ch in string):
                if nfa_ends_with_01(string):
                    print(" String is ACCEPTED by the NFA (ends with '01').\n")
                else:
                    print(" String is REJECTED by the NFA (does not end with '01').\n")
            else:
                print(" Invalid input. Please enter only binary characters (0 or 1).\n")
        elif choice == '2':
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 1 or 2.")

if __name__ == "__main__":
    main()
