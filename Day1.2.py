# Using python standard libraries
from datetime import datetime
Odds = [1, 3, 5, 7, 9, 11, 13, 15, 17, 29, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41]
CurrentDateTime= datetime.today().minute

if CurrentDateTime in Odds:
    print(" This is an odd time to be here")
else:
    print("This is a good time to be here")
