class PDA:
    def __init__(self):
        self.stack = []
        self.state = 'q0'

    def transition(self, symbol):
        if self.state == 'q0':
            if symbol == 'a':
                self.stack.append('A')  # Push A for every a
            elif symbol == 'b':
                self.state = 'q1'
            else:
                self.state = 'reject'

        elif self.state == 'q1':
            if symbol == 'b':
                self.stack.append('B')  # Push B for every b
            elif symbol == 'c':
                self.state = 'q2'
            else:
                self.state = 'reject'

        elif self.state == 'q2':
            if symbol == 'c':
                if self.stack:
                    top = self.stack.pop()
                    if top not in ['A', 'B']:
                        self.state = 'reject'
                else:
                    self.state = 'reject'
            else:
                self.state = 'reject'

    def process_string(self, input_string):
        for symbol in input_string:
            self.transition(symbol)
            if self.state == 'reject':
                return False

        # Accept by final state if stack is empty and last state is q2
        if not self.stack and self.state == 'q2':
            return True
        return False


# Example usage
if __name__ == "__main__":
    user_input = input("Enter a string of the form a^n b^m c^n with n,m >= 1: ")
    pda = PDA()
    if pda.process_string(user_input):
        print(f"String '{user_input}' is accepted by final state.")
    else:
        print(f"String '{user_input}' is rejected.")
