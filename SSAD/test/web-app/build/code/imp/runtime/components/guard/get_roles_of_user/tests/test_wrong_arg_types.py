
import unittest
from runtime.objects.session.session import Session
from runtime.components.guard.get_roles_of_user.tests.harness import TestHarness
from runtime.datatypes.cmd.cmd import Cmd

class TestWrongArguments(TestHarness):

    def test_pass(self):
        print "test_with_wrong_type_arguments"

        session = self.session
        instr = {'cmd': Cmd.get_roles_of_user, 
                 'session': 'session', 
                 'user': self.d_user}
        guard = self.component
        with self.assertRaises(Exception):
            guard.do(instr)
