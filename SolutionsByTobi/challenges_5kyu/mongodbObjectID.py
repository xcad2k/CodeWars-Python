########################################################################
#                                                                      #
#   NAME:     Mongodb ObjectID                                         #
#   RANK:     5kyu                                                     #
#   URL:      https://www.codewars.com/kata/52fefe6cb0091856db00030e   #
#                                                                      #
########################################################################

from datetime import datetime
import re


class Mongo(object):

    @classmethod
    def is_valid(cls, s):
        """returns True if s is a valid MongoID; otherwise False"""
        return re.match(r"[a-f0-9]", s)

    @classmethod
    def get_timestamp(cls, s):
        """if s is a MongoID, returns a datetime object for the timestamp; otherwise False"""
        pass