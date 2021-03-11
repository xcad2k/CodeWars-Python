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
        if isinstance(s, str) and re.match('^([0-9a-f]){24}$', s):
            return True
        return False

    @classmethod
    def get_timestamp(cls, s):
        """if s is a MongoID, returns a datetime object for the timestamp; otherwise False"""
        if cls.is_valid(s):
            return datetime.fromtimestamp(int(s[:8], 16))
        return False


print(Mongo.get_timestamp('507f1f77bcf86cd799439011'))
print(Mongo.is_valid('507f1f77bcf86cz799439011'))
print(Mongo.is_valid(3333333333333333333333334))
