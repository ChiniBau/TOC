class PDA:
    def __init__(self):
        self.stack = []
        self.state = 'q0'

    def transition(self, symbol):
        if self.state == 'q0':
            if symbol == '0':
                self.stack.append('X')  # Push X for every 0
                self.state = 'q1'
            elif symbol == '1':
                self.stack.append('Y')  # Push Y for every 1
                self.state = 'q2'

        elif self.state == 'q1':
            if symbol == '0':
                self.stack.append('X')
            elif symbol == '1':
                if self.stack and self.stack[-1] == 'X':
                    self.stack.pop()
                else:
                    self.state = 'reject'

        elif self.state == 'q2':
            if symbol == '1':
                self.stack.append('Y')
            elif symbol == '0':
                if self.stack and self.stack[-1] == 'Y':
                    self.stack.pop()
                else:
                    self.state = 'reject'

    def process_string(self, input_string):
        for symbol in input_string:
            self.transition(symbol)
            if self.state == 'reject':
                return False

        # Accept if stack is empty (empty stack acceptance)
        if not self.stack and '0' in input_string and '1' in input_string:
            return True
        return False


def main():
    print("\n---- PDA Menu ----")
    while True:
        print("1. Input a string to check")
        print("2. Exit")
        choice = input("Enter your choice (1 or 2): ")

        if choice == '1':
            string = input("Enter a binary string (equal number of 0’s and 1’s): ")
            if all(ch in '01' for ch in string):
                pda = PDA()
                if pda.process_string(string):
                    print("String is ACCEPTED by the PDA (empty stack acceptance).\n")
                else:
                    print("String is REJECTED by the PDA.\n")
            else:
                print("Invalid input. Please enter a string containing only 0 and 1.\n")
        elif choice == '2':
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 1 or 2.\n")


if __name__ == "__main__":
    main()
