
crrct_ans = '0'
wrong_ans = '0'
tot_marks =''
limit = 3
i = 1


qno1 = '''Select the Correct District of TamilNadu ?
            1. iduki  2.palakad    3.tirupur '''
qno2 = '''Select the Correct District which is famous for Textile ?
            1. iduki  2.palakad    3.tirupur  '''  
qno3 = '''Select the Correct District which is called as small Japan ?
            1. iduki  2.palakad    3.tirupur  '''                      




while i <= limit:
 if i == 1:   
  print (qno1)
 elif i == 2:
    print (qno2)  
 elif i == 3:
    print(qno3)   
 user_value = input('> ').lower()
 if user_value == 'iduki' :
    wrong_ans = int(wrong_ans)+1
    i=i+1
 elif user_value == 'palakad' :
    wrong_ans = int(wrong_ans)+1
    i=i+1  
 elif user_value == 'tirupur' :
    crrct_ans = int(crrct_ans)+1 
    i=i+1 
 else :
    wrong_ans = int(wrong_ans)+1
    i=i+1  

print('Total Correct answers ' + str(crrct_ans) ) 
print('Total Wrong answers ' + str(wrong_ans) ) 


