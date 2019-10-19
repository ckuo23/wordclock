import datetime as dt
import time
import numpy as np

# Returns current hour according to system time
def getHour():
    if (dt.datetime.now().hour == 0):
        hour = 12;
    elif (dt.datetime.now().hour > 12):
        hour = dt.datetime.now().hour - 12;
    else:
        hour = dt.datetime.now().hour;
    return hour;

# Returns current minute according to system time
def getMinutes():
    return dt.datetime.now().minute;

def setValidMatrix(hour, minutes): # decodes time and sets valid matrix
    set_matrix([0,0,2]);
    set_matrix([0,3,2]);
    set_matrix([9,6,6]);
    if (minutes > 35):
        if (hour == 12):
            set_matrix(get_location(hour));
        else:
            set_matrix(get_location(hour + 1));
        set_matrix([4,1,2]);
        if (minutes < 40):
            set_matrix([3,1,10]);
        elif (minutes < 45):
            set_matrix([3,1,6]);
        elif (minutes < 50):
            set_matrix([2,2,7]);
        elif (minutes < 55):
            set_matrix([1,6,3]);
        elif (minutes < 60):
            set_matrix([3,7,4]);
    else:
        set_matrix(get_location(hour));
        set_matrix([4,3,4]);
        if (minutes < 10):
            set_matrix([3,7,4]);
        elif (minutes < 15):
            set_matrix([1,6,3]);
        elif (minutes < 20):
            set_matrix([2,2,7]);
        elif (minutes < 25):
            set_matrix([3,1,6]);
        elif (minutes < 30):
            set_matrix([3,1,10]);
        elif (minutes < 35):
            set_matrix([1,2,4]);

# returns X location of hour in matrix
# X IS DOWN, Y IS ACROSS
def get_location(hour):
    if hour == 1:
        return [4,8,3]
    elif hour == 2:
        return [8,0,3]
    elif hour == 3:
        return [6,7,5]
    elif hour == 4:
        return [5,0,4]
    elif hour == 5:
        return [5,4,4]
    elif hour == 6:
        return [5,8,3]
    elif hour == 7:
        return [7,1,5]
    elif hour == 8:
        return [7,6,5]
    elif hour == 9:
        return [9,0,4]
    elif hour == 10:
        return [1,6,3]
    elif hour == 11:
        return [6,1,6]
    else:
        return [8,3,6]

Matrix = np.zeros((12,12)) #letter matrix

def set_matrix(loc):
    for n in range(loc[2]):
        Matrix[loc[0]][loc[1] + n] = 1; # matrix indexing in python is 'backwards'