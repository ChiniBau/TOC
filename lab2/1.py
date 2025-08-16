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

        # Accept if stack is empty and at least one 0 and 1 were processed
        if not self.stack and '0' in input_string and '1' in input_string:
            self.state = 'accept'
            return True
        return False


# Example usage
if __name__ == "__main__":
    user_input = input("Enter a string of 0s and 1s: ")
    pda = PDA()
    if pda.process_string(user_input):
        print(f"String '{user_input}' is accepted.")
    else:
        print(f"String '{user_input}' is rejected.")
