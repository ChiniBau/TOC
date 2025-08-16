class PDA:
    def __init__(self):
        self.stack = []
        self.state = 'q0'

    def transition(self, symbol, half_done=False):
        if not half_done:
            # First half w: push symbols onto stack
            if symbol in ['a', 'b']:
                self.stack.append(symbol)
            elif symbol == 'c':
                self.state = 'q1'  # Transition to second half
            else:
                self.state = 'reject'
        else:
            # Second half w^R: pop and compare
            if self.stack and symbol == self.stack[-1]:
                self.stack.pop()
            else:
                self.state = 'reject'

    def process_string(self, input_string):
        half_done = False
        for symbol in input_string:
            if symbol == 'c':
                half_done = True
                self.transition(symbol, half_done=False)  # Just switch state
            else:
                self.transition(symbol, half_done=half_done)
            if self.state == 'reject':
                return False

        # Accept by final state if stack is empty and state is q1
        if not self.stack and self.state == 'q1':
            return True
        return False


# Example usage
if __name__ == "__main__":
    user_input = input("Enter a string of the form w c w^R with w ∈ {a,b}: ")
    pda = PDA()
    if pda.process_string(user_input):
        print(f"String '{user_input}' is accepted by final state.")
    else:
        print(f"String '{user_input}' is rejected.")
