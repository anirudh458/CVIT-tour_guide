
import unittest
from runtime.objects.session.session import Session
from runtime.components.engine.show_sessions.tests.harness import TestHarness
from runtime.datatypes.cmd.cmd import Cmd

class TestDoPasses(TestHarness):

    def test_do_passes(self):
        print "test_do_passes"
        session = self.session
        instr = {'cmd': Cmd.show_sessions, 'session': session}
        engine = self.component
        result = engine.do(instr)
        self.assertEqual(result['instr'], instr)
        self.assertEqual(result['result'][0], session)
