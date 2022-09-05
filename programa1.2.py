letter = { 
        'A' : True,
        'B' : True,
        'C' : None,
        'D' : True,
        'E' : True,
        'F' : True,
        'G' : None,
        'H' : True,
        'I' : True,
        'J' : None,
        'K' : True,
        'L' : None,
        'M' : False,
        }

target_letter = 'M'

new_fact = True

rules_fired = ['facts']

while new_fact == True:
    new_fact = False
    
    # Rule 1
    if letter['A'] is True and letter['B'] is True:
        letter['C'] = True
        new_fact = True
        rules_fired.append('R1')
    
    # Rule 2
    if letter['D'] is True and letter['E'] is True and letter['F'] is True:
        letter['G'] = True
        new_fact = True
        rules_fired.append('R2')
        
    # Rule 3
    if letter['H'] is True and letter['I'] is True:
        letter['J'] = True
        new_fact = True
        rules_fired.append('R3')
        
    # Rule 4
    if letter['C'] is True and letter['G'] is True:
        letter['K'] = True
        new_fact = True
        rules_fired.append('R4')
        
    # Rule 5
    if letter['G'] is True and letter['J'] is True:
        letter['L'] = True
        new_fact = True
        rules_fired.append('R5')
        
    # Rule 6
    if letter['K'] is True and letter['L'] is True:
        letter['M'] = True
        new_fact = True
        rules_fired.append('R6')
    
    

    if letter['M'] is True:
        print(f'El objetivo {target_letter} es TRUE\n')
        print('Rules fired: ')
        print(rules_fired)
        new_fact = False

        
        


        
