import random  #because we are going to use random numbers and letters
import string  # with the help of this we can access uppercase,lowercase, digitd, hexadigits, punctuations etc.
import PySimpleGUI as sg
#for theme
sg.theme('DarkTeal7') #provide the theme
sg.set_options(font='verdana, 15')
# will make 6 lists as follow
layout = [
    #key is used here to get the access to the value of this input for the uppercase
    [sg.Text('Uppercase: '), sg.Push(), sg.Input(size=15,key='-UP-' )], # sg.push for puttin them in a line
    [sg.Text('Lowercase: '),sg.Push(),  sg.Input(size=15,key='-LOW-')],
    [sg.Text('Digits: '),sg.Push(),  sg.Input(size=15,key='-DIG-')],
    [sg.Text('Symbols: '),sg.Push(),  sg.Input(size=15,key='-SYM-')],
    [sg.Button('OK'), sg.Button('Cancel')],
    [sg.Text('Password'),sg.Push(),  sg.Multiline(size=15, no_scrollbar=True, disabled=True,key='-PASS-')]
]
#will create a Window and it has 2 basic arguments title and layout
window = sg.Window('Password Generator', layout)

# to get access to the events and values by reading the window
while True:
    events, values = window.read()
    if events == 'Cancel'or events == sg.WIN_CLOSED:
        break

    if events == 'OK' :
        try:
            u_upper = int(values['-UP-'])
            # make variable that stores uppercase, lowercase, digits , puntuations
            # random.sample() is for selecting the random numbers
            upper = random.sample(string.ascii_uppercase, u_upper)
            u_lower = int(values['-LOW-'])
            lower = random.sample(string.ascii_lowercase,u_lower)
            u_digits = int(values['-DIG-'])
            digits = random.sample(string.digits, u_digits)
            u_symbols = int(values['-SYM-'])
            symbols = random.sample(string.punctuation, u_symbols)

            total = upper+ lower+ digits+ symbols
            total = random.sample(total , len(total)) # random letters like digits ,lowercase, puntuations,uppercase
            total = ''.join(total) # to eliminate the space between the password's letters
            # INSTEAD OF PRINTING THE TOTAL
           #use key of the window i.e PASS and update the value of the total
            window['-PASS-'].update(total)
        except ValueError:  # when there is value error the is there is no number(error handling)
             window['-PASS-'].update("No Valid Number")
            
window.close()

