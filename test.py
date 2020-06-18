from fsm import StackFsm
from unittest import TestCase

class EatWhenHungry(StackFsm):
    hunger = 1

    def __init__(self):
        self.push_state(self.full)

    def hungry(self):
        self.hunger += 1
        if self.hunger >= 1:
            self.pop_state()
            self.push_state(self.full)

    def full(self):
        self.hunger -= 1
        if self.hunger < 1:
            self.pop_state()
            self.push_state(self.hungry)


class StackFsmTestCase(TestCase):
    def test_fsm(self):
        fsm = EatWhenHungry()
        self.assertEqual(1, fsm.hunger)
        self.assertEqual('full', fsm.state)
        fsm.update()
        self.assertEqual(0, fsm.hunger)
        self.assertEqual('hungry', fsm.state)
        fsm.update()
        self.assertEqual(1, fsm.hunger)
        self.assertEqual('full', fsm.state)
