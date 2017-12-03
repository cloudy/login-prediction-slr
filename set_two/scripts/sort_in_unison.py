#!/usr/bin/env python3

# This performs necessary pre-processing for raw data from 'last' command
import numpy as np


FILE_LOGIN = "../postprocess/connect_time.csv"
FILE_SESSION = "../postprocess/session_time.csv"

def main():
    
    login_data = np.genfromtxt(FILE_LOGIN, delimiter=',')
    session_data = np.genfromtxt(FILE_SESSION, delimiter=',')

    

    login_s, session_s = map(list, zip(*sorted(zip(login_data, session_data), reverse=False)))
    
    
    print("LOGIN")
    for i in range(len(login_s)):
        print(login_s[i], session_s[i])

    x  = int(input("Accept? "))

    if (x == 1):
        outfile_login = open(FILE_LOGIN, 'w')

        
        for val in login_s:
            outfile_login.write('%s\n' % float('%.5g' % val))
            #outfile.write("%s\n" % val)

        outfile_session = open(FILE_SESSION, 'w')
        
        for val in session_s:
            outfile_session.write('%s\n' % float('%.5g' % val))




def sessionConvToHours(data):
    # format: (HH:MM)

    in_hours = []

    for time in data:
        tokenized_time = time.split('(')[1].split(')')[0].split(':')
        print(tokenized_time)
        
        in_hours.append(float(tokenized_time[0]) + float(tokenized_time[1])/60)

    return in_hours


def convToHours(data):

    in_hours = []

    for login in data:
        # Takes value in format HH:MM:SS and tokenizes, adds up each delimited element
        # w/ respective multiplier.
        

        temp_tok = login.split(':')

        print(temp_tok)
        print(login)
        in_hours.append(float(temp_tok[2])/3600+float(temp_tok[1])/60+float(temp_tok[0]))

    return in_hours



def calcInterval(data):
    in_intervals = []
    # Go through and get the difference between T1 and TO to determine login intervals
    # Must abs values bc for ex, TO may be 23:34:46 and T1 00:12:49 where the difference would be negative
    for i in range(0, len(data) - 1):
        in_intervals.append(abs(data[i] - data[i+1]))

    return in_intervals








if __name__ == "__main__":
    main()
