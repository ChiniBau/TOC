def dfa_starts_with_01(string):
    state = 'q0'
    
    for char in string:
        if state == 'q0':
            if char == '0':
                state = 'q1'
            else:
                return False
        elif state == 'q1':
            if char == '1':
                state = 'q2'
            else:
                return False
        elif state == 'q2':
            if char in ('0', '1'):
                state = 'q2'
            else:
                return False
    return state == 'q2'

def main():
    print("\n---- DFA Menu ----")
    while True:
        print("1. Input a string to check\n2. Exit")
        choice = input("Enter your choice (1 or 2): ")
        
        if choice == '1':
            string = input("Enter a binary string (start with 01): ")
            if all(ch in '01' for ch in string):
                if dfa_starts_with_01(string):
                    print(" String is ACCEPTED by the DFA.\n")
                else:
                    print("String is REJECTED by the DFA.\n")
            else:
                print("Invalid input. Please enter a string containing only 0 and 1.\n")
        elif choice == '2':
            print("Exiting the program. Goodbye!\n")
            break
        else:
            print("Invalid choice. Please enter 1 or 2.\n")

if __name__ == "__main__":
    main()
