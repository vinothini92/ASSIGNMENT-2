#State-Machine program for modelling pronunciation of words for speech recognition
#set of words {cat,cot,cab,cob}
#At the end of input,this return whether it has or hasnt reached succesfully end state

State_Machines = { 'One'  :   {'Found':False,'event': ('Two',None,None,None,None)},
                   'Two'  :   {'Found':False,'event': ('None','Three','Three',None,None)},
                   'Three':   {'Found':False,'event': (None,None,None,'Four','Four')},
                   'Four' :   {'Found':True,'event':  (None,None,None,'Four','Four')}  
    }

def phone_lattice():
    word = []
    while(1):
        print "enter the each letter and 'q' to exit"
        letter = raw_input()
        if (letter == 'q'):
            break
        word.append(letter)
    current_state = State_Machines['One']
    for char in word:
        if char == 'c':
            current_state = State_Machines[current_state['event'][0]]
        elif char == 'a':
            current_state = State_Machines[current_state['event'][1]]
        elif char == 'o':
            current_state = State_Machines[current_state['event'][2]]
        elif char == 't':
            current_state = State_Machines[current_state['event'][3]]
        elif char == 'b':
            current_state = State_Machines[current_state['event'][4]]
        if current_state == None:
            print "not end"
    if current_state['Found']:
        print "End state"
    else:
        print "Not End"                                    
    

if __name__ == '__main__':
    phone_lattice()
