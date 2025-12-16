print("Welcom to computer quiz game ")
quiz=input("Do u want to play? ")
  
if quiz.lower()!="yes":
    quit()

print("okay! lets play a easy quiz game")
score=0

answer=input("what is CPU stands for? ")
if answer.lower()=="central processing unit":
    print("Corrrect!")
    score+=1
else:
    print("You are wrong!")

answer=input("what is RAM stands for? ")
if answer.lower()=="random access memory":
    print("Correct!")
    score+=1
else:
    print("You are wrong!")

answer=input("What is GPU stands for? ")
if answer.lower()=="graphic processing unit":
    print("Correct!")
    score+=1
else:
    print("You are wrong!")

answer=input("What is ROM stands for? ")
if answer.lower()=="read only memory":
    print("Correct")
    score+=1
else:
    print("You are wrong")

answer=input("What is PSU stands for? ")
if answer.lower()=="power supply unit":
    print("Correct!")
    score+=1
else:
    print("You are wrong!")

print("You got",str(score),"correct")
print("You got",str(score/5*100),"percentage")