#rock paper scissors game with computer
# r=rock.
# s=scissors.
# p=paper.
import random
def winorloss(number,a,n):
    if(number==1):
        number="r"
        if(a=="p"):
            print("you win")
            n+=1
        if(a=="s"):
            print("you loss")   
        if(a=="r"):
            print("draw")    
    if(number==2):
        number="p"
        if(a=="r"):
            print("you loss")   
        if(a=="s"):
            print("you win")
            n+=1 
        if(a=="p"):
            print("draw")     
    if(number==3):
        number="s"
        if(a=="p"):
            print("you loss")   
        if(a=="r"):
            print("you win")
            n+=1
        if(a=="s"):
            print("draw")
    return n            

i=1  
n=0 
k=int(input("how many times u wanna play game=")) 
while(i<=k):
 a=(input()) 
 number=random.randint(1,3)
 d=int(winorloss(number,a,n))
 n=d
 if(number==1):
     print("computers choice is rock")
 if(number==2):
     print("computers choice is paper")
 if(number==3):
      print("computers choice is scisoors")
 print("your choice is",a)
 i+=1     
print(f'you scored      {n} points') 
#print("you scored",n,"points")
print(f'computer scored {k-n} points')
print(end='\n')

if(n>(k-n)):
    print("YOU WON THE GAME")
# else:
#     print("YOU LOSS THE GAME")    
elif(n<(k-n)):
     print("YOU LOSS THE GAME")   
