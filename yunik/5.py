class PDA:
    def __init__(self):
        self.stack = []
        self.state = 'q0'

    def transition(self, symbol):
        if self.state == 'q0':
            # Push 'a' symbols to stack
            if symbol == 'a':
                self.stack.append('a')
            elif symbol == 'b' and self.stack:
                self.state = 'q1'
            else:
                self.state = 'reject'

        elif self.state == 'q1':
            # Read b's without touching stack
            if symbol == 'b':
                pass  # stay in q1
            elif symbol == 'c' and self.stack:
                self.state = 'q2'
                self.stack.pop()  # consume one 'a' immediately when first 'c' comes
            else:
                self.state = 'reject'

        elif self.state == 'q2':
            # Match c's with a's from stack
            if symbol == 'c' and self.stack:
                self.stack.pop()
            else:
                self.state = 'reject'

    def process_string(self, input_string):
        a_seen = False
        b_seen = False
        c_seen = False

        for symbol in input_string:
            if symbol == 'a':
                a_seen = True
            if symbol == 'b':
                b_seen = True
            if symbol == 'c':
                c_seen = True

            self.transition(symbol)
            if self.state == 'reject':
                return False

        # Accept if stack empty, in q2, and at least one 'a','b','c' seen
        if not self.stack and self.state == 'q2' and a_seen and b_seen and c_seen:
            return True
        return False


if __name__ == "__main__":
    while True:
        string = input("Enter a string of the form a^n b^m c^n where n,m>=1 (or 'q' to quit): ")
        if string.lower() == 'q':
            print("Exiting the program. Goodbye!")
            break
        if all(ch in 'abc' for ch in string):
            pda = PDA()
            if pda.process_string(string):
                print(" String is ACCEPTED by the PDA (final state acceptance).\n")
            else:
                print(" String is REJECTED by the PDA.\n")
        else:
            print("Invalid input. Please enter a string containing only a, b, c.\n")
