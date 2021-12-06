# First thing that popped into my head was a sliding dictionary...
# Probably should make a scalable solution at some point ¯\_(ツ)_/¯

fishes = []
eff_fishes = {'0':0,'1':0,'2':0,'3':0,'4':0,'5':0,'6':0,'7':0,'8':0}

def calc_fishes():

    return(sum(eff_fishes.values()))


def main():
    f = open("input.txt", "r")
    for x in f:
        fishes = x.split(",")
    
    for fish in fishes:
        eff_fishes[fish] = eff_fishes[fish] + 1

    print(eff_fishes)

    for day in range(0,257):
        print("DAY {0}: {1} fishes roam about!".format(day, calc_fishes()))
        
        # Theres probably a wayyyyyy better way to do this...
        tmp = eff_fishes['0']
        eff_fishes['0'] = eff_fishes['1']
        eff_fishes['1'] = eff_fishes['2']
        eff_fishes['2'] = eff_fishes['3']
        eff_fishes['3'] = eff_fishes['4']
        eff_fishes['4'] = eff_fishes['5']
        eff_fishes['5'] = eff_fishes['6']
        eff_fishes['6'] = eff_fishes['7']
        eff_fishes['7'] = eff_fishes['8']
        eff_fishes['8'] = tmp
        eff_fishes['6'] = eff_fishes['6'] + tmp
        
    calc_fishes()

if __name__ == "__main__":
    main()
