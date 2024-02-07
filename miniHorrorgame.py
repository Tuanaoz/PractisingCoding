import random
sanity = 0

print("After getting married with your parter you two moved into a new house that turned out to be a haunted house and your parter has been possesed in order to survive you need to escape all of the rooms. The more sanity you gain the better the resultsssss......")
while True :
    choose=input("choose the first room you want to get in (a)Kitchen,b)Living room,c)Bedroom or d)Bathroom)")
    try :
        str(choose)
    except ValueError :
            continue
    choose = str(choose)
    ################################# KITCHEN ROOM #####################################
    if choose=="a":
        while True:
            print("both of you go to the kitchen, and your partner grabs the knife")
            K1=input("what will you do? a) Sacrifice, b) Take the other knife, c) Run away")
       
            if K1=="b":
                while True:
                    t=["Left","Right"]
                    Wife1=random.choice(t)
                    K2=input("congrats now your partner is attacking you choose your next move Left or Right?")
                    if K2 == "left" and Wife1 == "Right":
                        print("congrats you survive")
                        break
                    elif K2 == "right" and Wife1 == "Right":
                        print("you both die")
                    elif K2 == "left" and Wife1 == "left" :
                        print("you both die")
                    elif K2 == "Right" and Wife1 == "left" :
                        print("congrats you survive")
                        break
                    else:
                        print("Thats not an option - try again")
                break
                break
            elif K1 == "a":
                print("you sacrifice yourself game over try again")
                continue
            elif K1 == "c":
                print("You run back to the hallway and safety but your wife chases you and you lose some sanity")
                sanity -= 10
                break
            else:
                print("your death made your partner happy")
                continue
            break
        break
        ################################################Bathroom################################################################
           
    elif choose=="d":
        while True:
            print("You are getting ready to take your bath and suddenly your head is underwater and your partner is the reason")
            Ba1=input("what will you do? a) Drown your partner,b) Drown Together, c ) Wait for your DEATH")
            while True:
                    if Ba1=="a":
                        print("You killed your partner :) , congrats.")
                        sanity -=10
                        break
                    elif Ba1=="b" :
                        print("your partner slipped over and fall you got the chance to run away")
                        sanity += 10
                        continue
                   
                    elif Ba1=="c":
                        print("your death made your partner happy")
                        print("you died try again")
                        continue
                        sanity -= 10
                    else:
                        continue
######################################################BEDROOM#################################################################
        elif Choose=="c":
                    while True:
                        print("You are smoking by the window and you feel two hands behind your back, realizing it is your partner being murderous once again")
                        Be1=input("what will you do? a) try to run away ,b) Calm them down, c ) let it happen")
                            while True:
                                if Be1=="a":
                                    print("Your partner started to chase you, you tried to go upstairs but you strangled now your arm is broken but you manage to survive ")
                                    sanity -=10
                                 break
                                     elif Be1=="b" :
                                         print("Both of you survive romantically")
                                            sanity += 10
                                        continue
                   
        elif Ba1=="c":
                        print("your death made your partner happy")
                        continue
                        sanity -= 10
                    else:
                        continue
         ###############################################LIVING ROOM################################################################
             elif Choose=="b"
             while True:
            print("Wife trying to strangle you while you are trying to sleeping")
            L1=input("what will you do? a) Make her unhappy by staying alive,b) Enjoy it, c ) RUN")
            while True:
                    if L1=="a":
                        print("OMG you killed your wife...")
                        sanity -=10
                        break
                    elif L1=="b" :
                        print("You died happily")
                        sanity += 10
                        continue
                   
                    elif Ba1=="c":
                        print("You are out of the house")
                        continue
                        sanity += 5
                    else:
                        break
