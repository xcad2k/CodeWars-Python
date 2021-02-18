########################################################################
#                                                                      #
#   NAME:     OnlyReadableOnce list                                    #
#   RANK:     5kyu                                                     #
#   URL:      https://www.codewars.com/kata/53f17f5b59c3fcd589000390   #
#                                                                      #
########################################################################

class SecureList:
    def __init__(self, data_list):
        # duplicate input to not mutate it
        self._data = [*data_list]

    def __getitem__(self, item):
        return self._data.pop(item)

    def __get__(self, instance, owner):
        return self._data

    def __str__(self):
        d = self._data
        self._data = []
        return str(d)

    def __repr__(self):
        return str(self)

    def __len__(self):
        return len(self._data)


test = SecureList([1, 2, 3])

print(test._data)
