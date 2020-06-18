
class StackFsm(object):
    __state = []
    __iterations = 0

    def push_state(self, state):
        self.__state.append(state)

    def pop_state(self):
        self.__state.pop()

    def update(self):
        if len(self.__state) > 0:
            self.__iterations += 1
            self.__state[-1]()
        else:
            raise ValueError("empty state")

    @property
    def iterations(self):
        return self.__iterations

    @property
    def state(self):
        if len(self.__state) > 0:
            self.__iterations += 1
            return self.__state[-1].__name__
        else:
            raise ValueError("empty state")




