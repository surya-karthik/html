import webbrowser,sys,pyperclip

sys.argv   #   ['matpit.py','870', 'valencia', 'st.']

#check if command line argument is passed or not
if len(sys.argv)>1:
    #['matpit.py','870', 'valencia', 'st.']...-> '870 valencia st.'

    address= ' '.join (sys.argv[1:])

else:
    address=pyperclip.paste()
    
webbrowser.open('https://www.google.com/maps/place/'+ address)    

    
    
