import argparse

if __name__ == "__main__":

    input_formule = input('Vul de bakkerformule in als volgt: volkorenmeel:70, bloem:30, etc.\n')
    dict_formule = dict(x.split(':') for x in input_formule.split(','))

    input_hoeveelheid = input ('Voer de gewenste hoeveelheid meel in (in grammen):\n')
    
    for key in dict_formule:
        print(key, ':', (float(dict_formule[key]) * int(input_hoeveelheid))/100, 'gr')

    # print(dict_formule)