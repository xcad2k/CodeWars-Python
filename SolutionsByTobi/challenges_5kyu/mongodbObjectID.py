########################################################################
#                                                                      #
#   NAME:     Mongodb ObjectID                                         #
#   RANK:     5kyu                                                     #
#   URL:      https://www.codewars.com/kata/52fefe6cb0091856db00030e   #
#                                                                      #
########################################################################

import re
from datetime import datetime


class Mongo(object):

    @classmethod
    def is_valid(cls, s):
        return type(s) == str and re.match(r"^[a-f0-9]{24}$", s) is not None

    @classmethod
    def get_timestamp(cls, s):
        return False if not Mongo.is_valid(s) else datetime.fromtimestamp(int(f"0x{s[:8]}", 16))
