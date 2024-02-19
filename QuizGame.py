print("Welcome to My Quiz Game!")

playing = input("Do You Want To Play? ")

if playing.lower() != "yes":
    quit()

print("Okay! Let's Play :)")
score = 0
answer = input("What Does CPU stand for? ")
if answer.lower() == "central processing unit":
    print('Correct!')
    score += 1
else:
    print('Incorrect!')
    
answer = input("What Does GPU stand for? ")
if answer.lower() == "graphics processing unit":
    print('Correct!')
    score += 1
else:
    print('Incorrect!')
    
answer = input("What Does RAM stand for? ")
if answer.lower() == "random access memory":
    print('Correct!')
    score += 1
else:
    print('Incorrect!')
        
answer = input("What Does PSU stand for? ")
if answer.lower() == "power supply":
    print('Correct!')
    score += 1
else:
    print('Incorrect!')
    
print("You Got "+ str(score)+ " Questions Correct!")
print("You Got "+ str((score / 4) * 100) +" %.")