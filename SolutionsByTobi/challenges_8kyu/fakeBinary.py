#####################################################################################
#                                                                                   #
#   NAME:     Fake Binary                                                           #
#   RANK:     8kyu                                                                  #
#   URL:      https://www.codewars.com/kata/57eae65a4321032ce000002d/train/python   #
#                                                                                   #
#####################################################################################

def fake_bin(x):
    return "".join("0" if int(a) < 5 else "1" for a in x)


fake_bin("45385593107843568")