def dfa_transition_based(string):
    state = 'q0'

    for ch in string:
        if ch not in {'a', 'b'}:
            return False  # Invalid character

        if state == 'q0':
            state = 'q1'
        elif state == 'q1':
            state = 'q2' if ch == 'a' else 'q_dead'
        elif state == 'q2':
            state = 'q3'
        elif state == 'q3':
            state = 'q4' if ch == 'b' else 'q_dead'
        elif state == 'q4':
            state = 'q4'
        elif state == 'q_dead':
            state = 'q_dead'

    return state == 'q4'

def main():
    print("\n---- DFA: 2nd='a' and 4th='b' ----")
    while True:
        print("1. Input a string to check")
        print("2. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            string = input("Enter a string using only 'a' and 'b': ")
            if all(c in 'ab' for c in string):
                if dfa_transition_based(string):
                    print(" String is ACCEPTED by the DFA (2nd='a' and 4th='b').\n")
                else:
                    print(" String is REJECTED by the DFA.\n")
            else:
                print(" Invalid input. Only 'a' and 'b' allowed.\n")
        elif choice == '2':
            print("Exiting. Goodbye!")
            break
        else:
            print("Invalid choice.\n")

if __name__ == "__main__":
    main()
