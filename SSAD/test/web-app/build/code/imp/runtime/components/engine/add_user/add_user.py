
import traceback

from runtime.datatypes.cmd.cmd import Cmd
from runtime.objects.user.user import User

class AddUser:

    @staticmethod 
    def do(obj, instr):
        user = instr['data']['user']
        obj.em.add_user(user)
        return {'instr': instr, 'result': user}
