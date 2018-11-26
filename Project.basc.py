
def fun_chack(a):

        if  ord(a) < 48 or  ord(a) >57:
            return 1
        else:
            return 0    

            


def print_board(board):   
    cut=1

    print('-----------------')
    for k in board:
        print ('|',end=" ")
        print (k,end=" ")
        print ('|',end=" ")
        cut=cut+1
        if cut>3:               
            print()
            print('-----------------')
            cut=1   
          

def rule(board):
    if board[0]=="x" and  board[1]=="x" and  board[2]=="x":
        return 1
    elif board[0]=="o" and  board[1]=="o" and  board[2]=="o":
        return 2   

    if board[3]=="x" and  board[4]=="x" and  board[5]=="x":
        return 1
    elif board[3]=="o" and  board[4]=="o" and  board[5]=="o":
        return 2   


    if board[6]=="x" and  board[7]=="x" and  board[8]=="x":
        return 1
    elif board[6]=="o" and  board[7]=="o" and  board[8]=="o":
        return 2    

    if board[0]=="x" and  board[3]=="x" and  board[6]=="x":
        return 1
    elif board[0]=="o" and  board[3]=="o" and  board[6]=="o":
        return 2    

 


    if  board[1]=="x" and  board[4]=="x" and  board[7]=="x":
        return 1
    elif board[1]=="o" and  board[4]=="o" and  board[7]=="o":
        return 2    
    if  board[2]=="x" and  board[5]=="x" and  board[8]=="x":
        return 1    
    elif board[2]=="o" and  board[5]=="o" and  board[8]=="o":
        return 2   
    if  board[0]=="x" and  board[4]=="x" and  board[8]=="x":
        return 1
    elif  board[0]=="o" and  board[4]=="o" and  board[8]=="o":
        return 2    
    if  board[2]=="x" and  board[4]=="x" and  board[6]=="x":
        return 1  
    elif board[2]=="o" and  board[4]=="o" and  board[6]=="o":
        return 2  


def start_to_play(x,board,fp):
    x=int(x)
    if  'first player'== fp:
        board[x-1]="x"
    elif 'second player'==sp:
        board[x-1]="o"
           
def chack_game(a):
    if  rule(board)==1:
        print('first player won')  
        a=input("for mor game press y else press n  ")

    elif rule(board)==2:
        print('second player won')  
        a=input("for mor game press y else press n  ")  


  
    return a                 

print("Welcome to x and o game")
fp='first player'
sp='second player'

board=[1,2,3,4,5,6,7,8,9]
print_board(board)
a='y'
while a=='y':
    x=input('choose please location you want to mark first player:\n')
     
    while  fun_chack(x):
        x=input('wrong input choose please location you want to mark first player:\n')
        
        
    start_to_play(x,board,fp)
    print_board(board)
    chack_game(a)   
  
    o=input('choose please location you want to mark second player:\n')
    while  fun_chack(o):
        o=input('wrong input choose please location you want to mark first player:\n')
        break
    start_to_play(o,board,sp)
    print_board(board)
    a=chack_game(a)
    print("aaaaaa",a)
    
else:
    print ("winer")
   
    


  

       


   
    



           
              

            
   
       
      
    






