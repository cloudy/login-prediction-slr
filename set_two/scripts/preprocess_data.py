#!/usr/bin/env python3

# This performs necessary pre-processing for raw data from 'last' command

FILE_NAME = "../data/session_time.txt"
#FILE_NAME = "../data/connect_time.txt"


def main():
   
    f = open(FILE_NAME, 'r')
    data = f.readlines()

    
    data_conved = sessionConvToHours(data)
    #data_conved = convToHours(data)
    

    print(data_conved)

    outfile = open("session_time.csv", 'w')
    #outfile = open("connect_time.csv", 'w')

    
    for val in data_conved:
        outfile.write('%s\n' % float('%.5g' % val))


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
