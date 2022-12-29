class State:
    name = ''
    isAccept = False
    transitions = {}

    def __init__(self, name):
        self.name = name

    def set_transitions(self, dest, alph):
        self.transitions.update({dest: alph})


class Automata:
    states = []
    accepts = []
    alphabet = []

    def __init__(self, states_passed, accepts_passed, alphabet_passed, q0_passed, function):
        self.set_states(states_passed)
        self.set_accepts(accepts_passed)
        self.alphabet = alphabet_passed
        self.q0 = State(q0_passed)
        self.set_func(function)

    def set_states(self, states_passed):
        for state in states_passed:
            self.states = self.states.append(State(self.states))

    def set_accepts(self, accepts_passed):
        for a in accepts_passed:
            accept_temp = self.states[self.states.index(a)]
            accept_temp.isAccept = True
            self.accepts.append(accept_temp)

    def set_func(self, function):
        for i in range(0, int(len(function)/3)):
            src = function[i*3]
            dest = function[(i * 3) + 1]
            alph = function[(i * 3) + 2]
            self.states[self.states.index(src)].set_transition(dest, alph)


states = input('Enter states:')
accept = input('Enter accepting states:')
alphabet = input('Enter alphabet:')
q0 = input('Enter first state:')
func = input('Enter transition functions. From state i to state j by alphabet a -> i j a:')
automata = Automata(states, accept, alphabet, q0, func)
