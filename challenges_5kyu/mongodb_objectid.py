########################################################################
#                                                                      #
#   NAME:     Mongodb ObjectID                                         #
#   RANK:     5kyu                                                     #
#   URL:      https://www.codewars.com/kata/52fefe6cb0091856db00030e   #
#                                                                      #
########################################################################

from datetime import datetime


class Mongo(object):

    @classmethod
    def is_valid(cls, s):
        """returns True if s is a valid MongoID; otherwise False"""
        try:
            inputbytes = bytes(s)
        except TypeError as e:
            print(e)
            return False

        return True

    @classmethod
    def get_timestamp(cls, s):
        """if s is a MongoID, returns a datetime object for the timestamp; otherwise False"""
        return True


print(Mongo.is_valid('507f1f77bcf86cd799439011'))
print(Mongo.is_valid('507f1f77bcf86cz799439011'))
