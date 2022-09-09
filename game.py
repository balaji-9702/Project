"""
MY Logic

manual = 'help'
start = ' ready to drive'
stop = 'stoping the travel'
quit = 'Exited'
exit = 'sorry i cant understand'
#limit = 2
k = 0
i =1
limit = 2


value= input('>' )
if value == manual:

    print('''Start -> To Start drive
             Stop - > To stop the travel
             quit - > To Quit ''' )
            
    while i:         
     command= input('>' )       
     if command == 'start':
        print(start)
     elif command == 'stop':
        print(stop) 
     elif command == 'quit':
        print(quit)
        break
    
 
else:

        print(exit)
 """  


user_value = ''
command ='quit'
help = 'help'
start = ' ready to drive'
stop = 'stoping the travel'
quit = 'Exited'
exit = 'sorry i cant understand'
inputs=['Start -> To Start drive',
             'Stop - > To stop the travel',
             'quit - > To Quit']

print ('Start by typing "help" command ')
while user_value.lower() != 'command':
   user_value = input('> ')
   if user_value == help:
      print(inputs)
   elif   user_value == 'start':
      print (start)
   elif   user_value == 'stop':
      print(stop)   
   elif   user_value == 'quit':
      print (quit)
      break
   else:
      print (exit)      
 

    

    
