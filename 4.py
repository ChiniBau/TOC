def dfa_contains_001(string):
    state = 'q0'
    
    for char in string:
        if state == 'q0':
            if char == '0':
                state = 'q1'
            elif char == '1':
                state = 'q0'
        elif state == 'q1':
            if char == '0':
                state = 'q2'
            elif char == '1':
                state = 'q0'
        elif state == 'q2':
            if char == '0':
                state = 'q2'
            elif char == '1':
                state = 'q3'
        elif state == 'q3':
            state = 'q3'
    
    return state == 'q3'

def main():
    print("\n---- DFA Menu ----")
    while True:
        print("1. Input a string to check")
        print("2. Exit")
        choice = input("Enter your choice (1 or 2): ")
        
        if choice == '1':
            string = input("Enter a binary string (substring 001): ")
            if all(ch in '01' for ch in string):
                if dfa_contains_001(string):
                    print(" String is ACCEPTED by the DFA (contains substring '001').\n")
                else:
                    print(" String is REJECTED by the DFA (does not contain '001').\n")
            else:
                print(" Invalid input. Please enter only binary characters (0 or 1).\n")
        elif choice == '2':
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 1 or 2.\n")

if __name__ == "__main__":
    main()
