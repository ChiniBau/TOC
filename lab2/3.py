class PDA:
    def __init__(self):
        self.stack = []
        self.state = 'q0'

    def transition(self, symbol):
        if self.state == 'q0':
            if symbol == '0':
                self.stack.append('X')  # Push X for every 0
            elif symbol == '1':
                if self.stack:
                    self.stack.pop()  # Pop X for each 1
                    self.state = 'q1'
                else:
                    self.state = 'reject'

        elif self.state == 'q1':
            if symbol == '1':
                if self.stack:
                    self.stack.pop()
                else:
                    self.state = 'reject'
            else:
                self.state = 'reject'

    def process_string(self, input_string):
        for symbol in input_string:
            self.transition(symbol)
            if self.state == 'reject':
                return False

        # Accept by final state if stack is empty and last state is q1
        if not self.stack and self.state == 'q1':
            return True
        return False


# Example usage
if __name__ == "__main__":
    user_input = input("Enter a string of the form 0^n1^n: ")
    pda = PDA()
    if pda.process_string(user_input):
        print(f"String '{user_input}' is accepted by final state.")
    else:
        print(f"String '{user_input}' is rejected.")
