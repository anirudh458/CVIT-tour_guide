
from runtime.objects.session.session import Session
from runtime.objects.role.role import Role
from runtime.objects.session.tests.test_harness import TestHarness

class TestCreateSessionExc(TestHarness):

    # session's user has no roles.  
    # This should raise an exception.

    def test_user_with_no_roles(self):
        print "test_session_user_with_no_roles"

        with self.assertRaises(Exception):
            Session(user=self.user_with_no_roles, key=self.key, role=Role.admin)



    # session's user has role [user].
    # Session's role is admin.  
    # This should raise an exception

    def test_user_role_mismatch(self):
        print "test_user_role_mismatch"

        with self.assertRaises(Exception):
            Session(user=self.user_with_user_role, key=self.key, role=Role.admin)
