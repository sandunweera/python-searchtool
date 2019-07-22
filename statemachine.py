class StateMachine:

    def __init__(self):
        self.handlers = {}
        self.start_state = None
        self.end_states = []

    def add_state(self, name, handler, end_state=0, message=""):

        self.handlers[name] = handler, message
        if end_state:
            self.end_states.append(name)

    def set_start(self, name):
        self.start_state = name

    def run(self):
        try:
            handler, message = self.handlers[self.start_state]
        except:
            raise RuntimeError("No start state found")
        if not self.end_states:
            raise RuntimeError("No end state found")

        while True:
            uin = input(message)

            new_state = handler(self, input=uin)
            if new_state in self.end_states:
                break
            else:
                handler, message = self.handlers[new_state]
