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

    def __init__(self, states_passed, accepts_passed, alphabet_passed, q0_passed, func):
        self.set_states(states_passed)
        self.set_accepts(accepts_passed)
        self.alphabet = alphabet_passed
        self.q0 = State(q0_passed)
        self.set_func(func)

    def set_states(self, states_passed):
        for state in states_passed:
            self.states = states.append(State(states))

    def set_accepts(self, accepts_passed):
        for accept in accepts_passed:
            accept_temp = states[states.index(accept)]
            accept_temp.isAccept = True
            self.accepts.append()

    def set_func(self, func):
        for i in range(0,int(len(func)/3)):
            src = func[i]
            dest = func[i + 1]
            alph = func[i + 2]
            states[states.index(src)].set_transition(dest,alph)
    
    def is_string_valid(self, string):
        
        inputs = list(string)
        current_state = self.q0
        for letter in inputs :
            try:
                if letter in self.set_transitions[current_state]:
                    current_state = self.set_transitions[current_state][letter]
                else:
                    return False
            except KeyError as e :
                return False
        if current_state in self.accepts:
            return True
        
        return False

states = input('Enter states:')
accept = input('Enter accepting states:')
alphabet = input('Enter alphabet:')
q0 = input('Enter first state:')
func = input('Enter transition functions. From state i to state j by alphabet a -> i j a:')
automata = Automata(states, accept, alphabet, q0, func)
