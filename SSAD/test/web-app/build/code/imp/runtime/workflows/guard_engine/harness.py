
import unittest
from unittest import TestCase
from runtime.workflows.guard_system.wf import GuardSysWf

class TestGuardSysWf(TestCase):

    def setUp(self):
        self.wf = GuardSysWf()
        

    def tearDown(self):
        self.wf = None

    def test_1(self):
        instr = Instr(...)
        ans = self.wf.run(instr)
        self.assertEquals(ans, ...)
