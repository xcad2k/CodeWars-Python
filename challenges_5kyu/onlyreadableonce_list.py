########################################################################
#                                                                      #
#   NAME:     OnlyReadableOnce list                                    #
#   RANK:     5kyu                                                     #
#   URL:      https://www.codewars.com/kata/53f17f5b59c3fcd589000390   #
#                                                                      #
########################################################################

class SecureList():
    def __init__(self, inputlist):
        # We need to insert all elements from inputlist into a new
        # variable. Otherwise it accesses the parent declared variable
        self._inputlist = [*inputlist]

    def __getitem__(self, index):
        try:
            return self._inputlist.pop(index)
        except Exception as e:
            print(f"Error: {e}")
            pass

    def __str__(self):
        tmp = self._inputlist
        self._inputlist = []
        return str(tmp)

    def __len__(self):
        return len(self._inputlist)

    def __repr__(self):
        return str(self)


newlist = SecureList([1, 2, 3, 4])

print(newlist[2])
print(newlist)
