import os
import sys
import time
import random
import cmd
with open("Intro//Intro.txt", "r") as o:
    print(o.read())
def menu():
    print("1.Start")
    time.sleep(1)
    print("2.Help")
    time.sleep(1)
    print("3.Exit")
    choice = input("Save earth or coward away? : ")
    if choice == "1":
        print("Start.")
        def start():   #Start
            print("Welcome to the Middle Earth.")
            print("1.Story Mode.")
            print("2.Mini Games.")
            print("3.Back")
            play = input("Story Mode or Mini Games : ")
            while play != "1" and play != "2" and play != "3":
                play = input("Choose from 1 , 2  or 3 : ")
            if play in "1":
                print("A story you should know !")
                time.sleep(2)
                with open("Start//Start.txt","r") as p:
                    print(p.read())
                    time.sleep(8)
                    os.system('cls')
                characterselection()
            elif play in "2":
                print("Play some mini games.")
                miniepisodes()
            else:
                menu()
        start()  
    elif choice == "2":
        print("Help")
        def help(): #Help
            print("1.Know about the game.")
            print("2.Useful tips.")
            print("3.Locations.")
            print("4.Back.")
            option = input("Select one:")
            if option == "1":
                print("Summary :")
                def summary():
                    print("About the game :")
                    time.sleep(1)
                summary()
                with open("Help//Summary//Summary.txt","r") as k:
                    print(k.read())
                    help()
            elif option == "2":
                print("Usefultips :")
                def usefultips():
                    print("Some tips.")
                    time.sleep(1)
                usefultips()
                print()
                time.sleep(1)
                with open("Help//Usefultips//Usefultips.txt","r") as g:
                    print(g.read())
                    help()
            elif option == "3":
                print("Locations :")
                def locations():
                    print("Information about the Lands.")
                locations()
                with open("Help//Locations//Locations.txt","r") as j:
                    print(j.read())
                    help()
            elif option == "4":
                menu()
            elif option >= "5" or option <= "0":
                print("Invalid Option.")
                print("Choose from 1 to 4.")
                help()
        help()
    elif choice == "3":
        print("End")
        sys.exit()
    else:
        print("Invalid Option")
        print("Choose from 1,2 or 3")
        menu()
        os.system('cls')
def characterselection():
    print("Select Character : ")
    print("1.Frodo")
    time.sleep(1)
    print("2.Aragorn")
    time.sleep(1)
    selection = input("Saviour of Middle Earth : ")
    if selection == "1":
        print("Ring Bearer ! Your Journey starts. ")
        time.sleep(1)
        frodo()
    elif selection == "2":
        print("I will lend my sword towards Frodo's journey. \n By my life or death, I will protect him.")
        time.sleep(1)
        Aragorn()
    elif selection >= "3" or selection <= "0":
        print("Choose from given options.")
        time.sleep(1)
        characterselection()
def Aragorn():
    print("A Ranger from the north \nDangerous Folk.")
    print("You've got two choices")
    time.sleep(1)
    x = "Help Frodo."
    y = "Take ring of power for yourself."
    print(x)
    print(y)
    Arga = input("x or y :")
    if Arga == "x":
        print("Are you frightened? Not frightened enough.")
        print("Taking Frodo to Riverdale")
        time.sleep(1)
        riverdale()
    elif Arga == "y":
        print("Give me the ring.")
        print("I will kill you if i have to to get the ring.")
        time.sleep(1)
        fight1()
    else :
        print("Choose from x or y")
        time.sleep(1)
        Aragorn()
def riverdale():
    print("I am taking you to the Land of the Elves, Riverdale")
    time.sleep(1)
    print("Kingdom of Lord Elrond")
    time.sleep(1)
    fire = "eating" 
    Hobbits = "talking"
    jour = input("Choose from eating or talking : ")
    if jour in fire :
        print("Great watch tower of Amon sul")
        time.sleep(1)
        print("We shall rest here tonight.")
        time.sleep(1)
        print("The ring wraiths catch up to you.")
        time.sleep(1)
        fight2()
    elif jour in Hobbits :
        print("We talk rest at Amon sul.\nStay close \nAs Hobbits lit the fire for eating and started taling, the wraiths caught the light.")
        time.sleep(1)
        print("Night Wraiths are here.\nThey Stab Frodo with an ancient morgul blade.\nA deadly weapon.")
        fight2()
    else:
        print("Invalid type.")
        time.sleep(1)
        print("Type correctly")
        riverdale()
def fight1():
      Frodo = 70
      Aragorn = 100
      time.sleep(1)
      print("Frodo Health", Frodo)
      print("Aragorn Health", Aragorn)
      time.sleep(1)
      while Frodo >= 0 and Aragorn >=0 :
          a=input("Press to any key to attact: ")
          p=random.randint(3,5)
          l=random.randint(2,5)
          print("You hits Frodo",p,"times")
          print("Frodo hits Aragon",l,"times")
          time.sleep(1)
          if p>l:
              Frodo=Frodo-30
              if Frodo>0:
                  print("He won't let you take the ring easy.Frodo has ",Frodo,"energy left")
              else:
                  print("Frodo is dead. \nYou snatched the ring. \nThe night riders are here")
                  print("Leave Bree")
                  power()
          elif l>p:
              Aragorn=Aragorn-15
              if Aragorn>0:
                  print("Frodo is putting up a fight, You have ",Aragorn,"energy left")
              elif Aragorn == 0:
                  print("Frodo ran away \nNight Riders are after him")
              else:
                  again1()
def fight2():
    Aragorn = 100
    NightWraiths = 25
    time.sleep(1)
    while Aragorn >=0 and NightWraiths >=0:
        g=input("Try to ward off the wraiths with fire : \n Press an key : ")
        z=random.randint(2,5)
        o=random.randint(2,3)
        print("Aragorn draws fire rear the Wraiths",z,"times")
        print("They are neither living nor dead.Keep the fire going and let in near the Wraiths",o,"times")
        time.sleep(1)
        if z>o :
            NightWraiths = NightWraiths - 12.5
            if NightWraiths>0:
                print("They answer the call of Sauron \nThey desired power above everthhing else \nSlaves to the dark lord's will")
                print("They have",NightWraiths,"energy left.")
            else:
                print("The Ringwraits are retreating.")
                print("Lets take him to Riverdale fast")
                time.sleep(1)
                os.system('cls')
                arewn()        #Someotherfunction
        elif z<o :
            Aragorn = Aragorn - 25
            if Aragorn > 0:
                print("Wraiths are returning")
                print("Aragorn has",Aragorn,"energy left.")
            else:
                again3()
def power():
    print("You have the ring of power ")
    print("What will you do? ")
    Use = "rule"
    fight = "conquer"
    po = input("rule or conquer : ")
    while po != "rule" and  po != "conquer":
        po = input (" type rule or conquer : ")
    if po in Use:
        print("I will rule the world of men.")
        rule()
    elif po in fight:
        print("Your Heart is being corrupted, the desire to gain power is incresing.")
        dead()
    else:
        print("type correctly: ")
        power()
def rule():
    print("I will reclaim my name and my birth right.")
    time.sleep(1)
    print("You march toward Gondor, to the city of Minas Traith. \nCity of kings.")
    fight3()
def dead():
    print("While you have the ring, the ring wraiths are after you now. \nThey are getting stronger as the day passes.")
    print("They have caught your scent.")
    fight3()
def fight3():
    print("On you journey to Gondor,You infer fear in to the hearts of people as the ring has corrupted your heart.")
    print("While being hunted by the wraiths")
    print("The wraiths are all over you. \nThere is no place to run but the only option that is to fight ")
    Aragorn = 100
    Ringwraiths = 100
    time.sleep(1)
    while Aragorn >=0 and Ringwraiths >=0:
        qw=input("Press any key to defend or attack : ")
        s=random.randint(1,2)
        b=random.randint(3,5)
        print("Aragorn hits ringwraiths",s,"times.")
        print("ringwraiths hit Aragorn",b,"times.")
        time.sleep(1)
        if s>b:
            Ringwraiths = Ringwraiths - 5
            if Ringwraiths>0:
                print("They did not even feel you attacking.")
            else:
                print("You are going to die.")
        elif b>s:
            Aragorn = Aragorn - 40
            if Aragorn >0:
                print("In Hevy voice : Do you know death when you see it? ")
                print("Aragorn gets frizzled.")
            else :
                print("You got killed by the ringwraiths.")
                again5()
def arewn():
    print("While going towards riverdale a lady elf friend of your's lends you help and takes Frodo to riverdale. ")
    Water = "water"
    Healing = "heal"
    jo = input("water or heal : ")
    while jo != "water" and jo != "heal":
        print("Type again:")
        jo = input("water or heal : ")
    if jo in Water :
        print("Wraiths are after her.")
        time.sleep(1)
        print("Lady Arewn calls upon the water for help.")
        time.sleep(1)
        print("If you want him come and claim him.")
        time.sleep(1)
        water()
    elif jo in Healing :
        print("He is fading.")
        print("Lady Arewn heals him just to keep him alive so that he could get to riverdale and get treatment. ")
        time.sleep(1)
        heal()
def water():
    print("Arewn Chants : ") 
    with open("Arewn//Water//Water.txt","r") as c:
        print(c.read())
        print()
        fellowship()
def heal():
    print("Arewn Chants : ")
    with open("Arewn//Grace//Grace.txt","r") as l:
        print(l.read())
        print()
        fellowship()
def again1():
    again=input("Want to fight again? (Enter yes, no or continue ): ")
    while again.lower()!="yes" and again.lower()!="no" and again.lower()!="continue":
        again=input("\n Please enter \"yes\" , \"no\  or \"continue: ")
    if again.lower()=="yes":
        fight1()
    elif again.lower()=="no":
        again2()
    else :
        power()
def again2():
    again=input("Want to go back to the menu or start with Aragorn again (Enter yes or y): ")
    while again.lower()!="yes" and again.lower()!="y":
        again=input("\n Please enter \"yes\" or \"y : ")
    if again.lower()=="yes":
       Aragorn()
    else:
        menu()
def again3():
    again=input("Want to fight again? (Enter yes, no or continue ): ")
    while again.lower()!="yes" and again.lower()!="no" and again.lower()!="continue":
        again=input("\n Please enter \"yes\" , \"no\  or \"continue: ")
    if again.lower()=="yes":
       fight2()
    elif again.lower()=="no":
        again4()
    else :
        power()
def again4():
    again=input("Want to go back to the menu or start with Aragorn again?(Enter yes or y): ")
    while again.lower()!="yes" and again.lower()!="y":
        again=input("\n Please enter \"yes\" or \"y: ")
    if again.lower()=="yes":
        print("Choose wisely this time.")
        menu()
    else:
        Aragorn()
def again5():
    again=input("Want to fight again? (Enter yes, no or continue ): ")
    while again.lower()!="yes" and again.lower()!="no" and again.lower()!="continue":
        again=input("\n Please enter \"yes\" , \"no\  or \"continue: ")
    if again.lower()=="yes":
       fight3()
    elif again.lower()=="no":
        again6()
    else :
        power()
def again6():
    again=input("Want to go back to the menu or start with Aragorn again?(Enter yes or y): ")
    while again.lower()!="yes" and again.lower()!="y":
        again=input("\n Please enter \"yes\" or \"y: ")
    if again.lower()=="yes":
        print("Choose wisely this time.")
        menu()
    else:
        Aragorn()
def fellowship():
    print("Frodo get's in time to riverdale. \nLord Elrond heals him and he get's better in a few days. \nYou get there also.")
    time.sleep(1)
    print("Meeting for the fate of the middle earth has ben summoned.")
    time.sleep(1)
    members()
def members():
    print("People who came to the meeting : ")
    Members= ["Aragorn","Legolas","Gimli","Boromir","Frodo","Gandalf","Samwise","Peragrin","Merdidoc"]
    for i in Members:
        print(i)
        print()
    with open("Lord//lord.txt","r") as v:
        print(v.read())
        time.sleep(6)
    os.system('cls')
    mistymountains()
def mistymountains():
	print("We must take this path for 40 days and hope that the gap of rohan is open for is open for us. ")
	path1= "moria"
	path2= "Pass of charadas"
	path3= "Gap of rohan"
	pathsec=input("Moria,Charadas or Gap of rohan : ")
	while pathsec.lower()!= "moria" and pathsec.lower()!= "charadas"and pathsec.lower()!= "rohan":
		print("Invalid input")
		pathsec = input("type again? : ")
	if pathsec in path1:
		print("We go through the mines of moria.")
		moria()
	if pathsec in path2:
		print("let's take the pass of charadas as our way.")
		charadas()
	if pathsec in path3:
		print("We must take the road to rohan.")
		rohan()

def charadas():
	print("A mountainous way that brings near to rohan but a little away from isengard.")
	path2sec = input("Duck or Hide : ")
	while path2sec.lower() != "duck" and path2sec.lower()!="hide":
		path2sec=input ("Choose one (duck or hide) : ")
	if path2sec in "duck" :
            Aragorn = 100
            Frodo = 100
            Legolas = 100
            Gandalf = 100
            Hobbits = 100
            Gimli = 100
            Boromir = 100
            while Aragorn>0 and Gimli>0 and Legolas>0 and Gandalf>0 and Hobbits>0 and Boromir>0 and Frodo>0:
                snow=input("Press to get down : ")
                dk=random.randint(3,4)
                gk=random.randint(1,2)
                print("Snow is falling hard","Health is dropping",Frodo,Hobbits,Gimli)
                if dk>gk:
                    Frodo=Frodo-20
                    Hobbits= Hobbits-20
                    Gimli=Gimli-20
                    if Frodo<= 75 and Gimli<=75 and Hobbits<=75:
                        print("We must take another path : the gap of rohan or mines of moria.")
                        moria()
                    else:
                        print("We must make through this path.")
                else :
                     Aragorn = Aragorn-10
                     Legolas = Legolas-10
                     Gandalf = Gandalf-10
                     Boromir = Boromir-10
                     if Aragorn<=85 and Gandalf<=85 and Legolas<=85 and Boromir<=85:
                         print("We should go another path. The little one's cannot survive this.")
                         print("It's upto the ring bearer to decide.")
                         fro = input("Which path must we choose? Rohan or Moria")
                         while fro.lower() != "rohan" and fro.lower()!="moria":
                             print("Invalid. type again.")
                             fro = input("rohan or moria : ")
                         if fro in "rohan":
                             rohan()
                         else:
                             moria()
                     else:
                         print("We must go this path.\nThough difficult we move through the traverse path.")
                         rohan()
                         
           
	else:
            print("The Spies of Saruman")
            spi = input ("go behind the rock : ")
            while spi != "rock":
                spi = input ("type rock : ")
            if spi in "rock":
                print("We hide under a rock from spies of Saruman.")
                charadas()
            else:
                moria()
def rohan():
	print("Theodin King's domain.")
	print("Close to Isengard. Saruman's white tower. ")
	ro = input ("Want to go this path? Yes or No : ")
	while ro != "yes" and ro != "no":
            ro = input ("yes or no : ")
	if ro in "yes":
	    print("we must pass through the dark forest.")
	    darkforest()
	else:
            isengard()
def moria():
    print("We fear going through the mines of moria. \nBut if frodo wants it we'll go through the mines.")
    mo = input("yes or no : ")
    while mo != "yes" and mo != "no":
        mo=input("yes or no : ")
    if mo in "yes":
        print("We reached to the secret gate that gives entry.")
        print("Speak friend and enter. ")
        pas = input("Melon or friend : ")
        while pas!="melon":
            print("Wrong word")
            pas = input("Try again : ")
        if pas in "melon":
            print("The gate opens.")
            mines()
        else:
            moria()
    else:
        rohan()
def isengard():
    print("Land of the white wizard.")
    print("While passing through the gap of rohan, Saruman scout see you.")
    print("You are under attack.")
    fight4()
def fight4():
    Aragorn = 100
    Orcs = 100
    print("Aragorn Health", Aragorn)
    print("Orcs Health", Orcs)
    while Aragorn>=0 and Orcs>=0:
        h=input("Press any key to attack : ")
        d=random.randint(3,4)
        f=random.randint(3,6)
        print("You battle them. You have",Aragorn,"Health left.")
        print("Orcs are gaining on you.They have",Orcs,"Health left.")
        if d>f:
            Orcs = Orcs - 15
            if Orcs>0:
                print("You are holding your ground.\nThey have",Orcs,"Health left.")
            else:
                print("You managed to kill all of them.\n Go to Rohan now.")
                darkforest()
        elif f>d:
            Aragorn = Aragorn - 25
            if Aragorn>0:
                print("They are too many in number. You have",Aragorn,"Health left.")
            else:
                print("You have been killed by the Orcs.")
                again7()
def again7():
    again=input("Want to fight again? (Enter yes or no): ")
    while again.lower()!="yes" and again.lower()!="no":
        again=input("\n Please enter \"yes\" or \"no : ")
    if again.lower()=="yes":
       fight4()
    else:
        print("You are dead again.")
        again8()
def again8():
    again=input("Want to go back to the menu or continue from Rohan?(Enter yes or y): ")
    while again.lower()!="yes" and again.lower()!="y":
        again=input("\n Please enter \"yes\" or \"y: ")
    if again.lower()=="yes":
        print("Choose wisely this time.")
        menu()
    else:
        rohan()
def mines():
    print("You have Entered the mines of moria.")
    print("You have two paths")
    pathsec3 = input("Left or right :")
    while pathsec3!="right" and pathsec3!="left":
        pathsec3 = input("Select path : ")
    if pathsec3 in "left":
        print("Orcs are neatby. Be vilgilent.")
        ph=input("go down or go up :")
        while ph != "go down" and ph != "go up":
            ph =input("type again : ")
        if ph in "go down":
            print("Orcs found you.\nGet ready to run.")
            print("Kill orcs that are in your way.")
            fight5()
        else:
            print("The way out is just few steps away.")
            print("The Balrog appers, Gandalf fight's him. Giving you the time to getout.")
            darkforest()
    else:
         print("You are going deep into the mines.\nMithral was the jewel of these mines.")
         print("The stairs ahead are broken.")
         jump1()
def jump1():
    df = input("Jump or run junp :")
    while df != "jump" and df != "run jump":
        df = input("Choose again : ")
    if df in "jump":
        print("Jump to move to the next stair.")
        kp = input("Press an key to jump : ")
        c=random.randint(2,5)
        print("You have to make jumps to get through the stairs.")
        if c<2:
            print("Small jump")
            againq()
        elif c==4:
            print("Long jump")
            againq()
        else:
            print("You passed the stairs.")
            print("You've reached to the way out.")
            darkforest()
    else:
        print("You need to make a jump to pass the stairs.")
        pk = input("Press an key to jump : ")
        g=random.randint(1,2)
        print("Jump ! ")
        if g>=2:
            print("You've made it.")
        else:
            print("You go down the mines.")
            print("You hit hard on the ground")
            print("You are dead")
            againj()
def againq():
    again=input("Jump Again or start from moria?(Enter yes or y): ")
    while again.lower()!="yes" and again.lower()!="y":
        again=input("\n Please enter \"yes\" or \"y: ")
    if again.lower()=="yes":
        print("Choose wisely this time.")
        againj()
    else:
        mines()
def againj():
    again=input("Want to go back to the menu or continue from mines?(Enter yes or y): ")
    while again.lower()!="yes" and again.lower()!="y":
        again=input("\n Please enter \"yes\" or \"y: ")
    if again.lower()=="yes":
        print("Choose wisely this time.")
        menu()
    else:
        mines()
def fight5():
    Aragorn = 100
    Orcs = 100
    print("Aragorn Health", Aragorn)
    print("Orcs Health", Orcs)
    while Aragorn>=0 and Orcs>=0:
        h=input("Press any key to attack : ")
        d=random.randint(3,6)
        f=random.randint(2,4)
        print("They are onto you. You have",Aragorn,"Health left.")
        print("Filthy Anoying creatures.They have",Orcs,"Health left.")
        if d>f:
            Orcs = Orcs - 35
            if Orcs>0:
                print("They keep coming. \nThey must have settled in the mines.\nThey have",Orcs,"Health left.")
            else:
                print("They got scared from the beast of showdow and fire that was awakened a long time ago.\nSwifly move out of the caves. \n Go to Rohan now.")
                darkforest()
        elif f>d:
            Aragorn= Aragorn -15
            if Aragorn>0:
                print("They are too many in number. You have",Aragorn,"Health left.")
            else:
                print("You have been killed by the Orcs.")
                again9()
def again9():
    again=input("Want to fight again? (Enter yes or no): ")
    while again.lower()!="yes" and again.lower()!="no":
        again=input("\n Please enter \"yes\" or \"no : ")
        if again.lower()=="yes":
            fight5()
        else:
            print("You are dead again.")
            again10()
        
def again10():
    again=input("Want to go back to the menu or continue from mines?(Enter yes or y): ")
    while again.lower()!="yes" and again.lower()!="y":
        again=input("\n Please enter \"yes\" or \"y: ")
        if again.lower()=="yes":
            print("Choose wisely this time.")
            menu()
        else:
            mines()
def darkforest():
    print("The fellowship has lost gandalf to the Balrog.")
    ds= "1.Follow the steep path."
    sd= "2.Collect woods."
    cv= "3.Go to forest"
    sp=input("1,2 or 3 : ")
    while sp != "1" and sp != "2" and sp !="3":
        sp = input("Choose from 1,2 or 3 : ")
    if sp in "1":
        print("You've traveled many miles through the way and are near Rohan.")
        theoden()
    elif sp in "2":
        print("The Orcs attacked you and took the Hobbits, except Frodo and Samwise. \nThey are on there way to mount doom.")
        boromir()
    else:
        print("The trees of the darkforest are alive and talking. They are full of memories.")
        print("We are not alone.\nThe white wizard apporaches.")
        gandalfwhite()

##def meeting():
##    with open("Lord//lord.txt","r") as v:
##        print(v.read())
        
def boromir():
    print("Protect the Hobbits. \nFight with the Urakai")
    Boromir = 100
    Urakai = 100
    print("Urakai Health", Urakai)
    print("Boromir Health", Boromir)
    while Urakai >= 0 and Boromir >=0 :
          a=input("Press to any key to attact: ")
          p=random.randint(2,4)
          l=random.randint(3,6)
          print("Boromir hits Urakai",p,"times")
          print("Urakai shot's an arrow towards Boromir",l,"times")
          if p>l:
              Urakai=Urakai-15
              if Urakai>0:
                  print("Resilient in defence. Urakai have ",Urakai,"energy left")
                
              else:
                  print("Urakai is dead. \nYou defended the Hobbits.")
                  darkforest()
          elif l>p:
              Boromir=Boromir-30
              if Boromir>0:
                  print("Urakai shot's another fierce arrow at you, Boromir have ",Boromir,"energy left")
              elif Boromir == 0:
                  print("Urakai Killed you \nIt took 3 arrow's to get ypu down.")
              else:
                  again11()

def again11():
    again=input("Want to fight again? (Enter yes or no): ")
    while again.lower()!="yes" and again.lower()!="no":
        again=input("\n Please enter \"yes\" or \"no : ")
    if again.lower()=="yes":
       boromir()
    else:
        print("You are dead again.")
        again12()
        

def again12():
    again=input("Want to go back to the menu or continue from darkforest?(Enter yes or y): ")
    while again.lower()!="yes" and again.lower()!="y":
        again=input("\n Please enter \"yes\" or \"y: ")
    if again.lower()=="yes":
        print("Choose wisely this time.")
        menu()
    else:
        darkforest()
        
def gandalfwhite():
    print("You must be quick to attack or he will put a smell.")
    kj= input("Sword, Arrow, Axe : ")
    while kj != "sword" and kj != "arrow" and kj != "axe":
        kj = input("again :")
    if kj in "sword":
        print("My Sword got blazed by the wizard.")
        vc=input("throw sword or burn yourself :")
        d=random.randint(1,3)
        if d>=2:
            print("Sword Thrown")
            theoden()
        elif d<2:
            print("You burned yourself.")
            print("The while wizard reveals himself to be Gandalf and heals you.")
            theoden()
        else:
            gandalfwhite()
    elif kj in "axe":
        zs=input("yes or no : ")
        while zs != "yes" and zs != "no":
            zs = input("yes or no : ")
        v=random.randint(2,4)
        if v>=3:
            print("My axe got sliced.")
            theoden()
        elif v<2:
            print("I hit the wizard")
            print("Nothing happened to him")
            theoden()
        else:
            gandalfwhite()
    else:
        xc=input("Fire an arrow:")
        m=random.randint(2,3)
        if m>=3:
            print("Arrow Shot but countered by the wizard.")
            theoden()
        elif m<2:
            print("Arrow passes through the wizard but nothing happened to him.")
            theoden()
        else:
            gandalfwhite()

def theoden():
    with open("White//white.txt","r") as x:
        print(x.read())
    print("You've reached Rohan!")
    print("The Hall of Meduseld. \nWhere king of rohan dwells. ")
    print("Are you armed? ")
    Swords = "Armed"
    swo = input("Swords : ")
    while swo != "yes" and swo != "no":
        swo = input("yes or no : ")
    if swo in "yes":
        print("Guard : I can't let you pass so armed.")
        print("Leave all your weapons outside.")
        remove()
    if swo in "no":
        print("You can pass through.")
        hall()

def remove():
    pla = input("Submit weapons : ")
    while pla != "yes" and pla != "no":
        pla=input(" yes or no : ")
    if pla in "yes":
        print("You can go inside.")
        hall()
    else:
        print("I've hidden the weapons.")
        search()

def search():
    ipo=input("Getting Checked,press c to get Checked :")
    while ipo != "c":
        ipo= input("press c for checking .")
    kvc=random.randint(2,4)
    if kvc == 3:
        print("Checking again : ")
        search()
    else:
        print("You are clear. \nGo inside.")
        hall()
        
def hall():
    print("You are with Gandalf who is there to release Theoden King From Saruman's Spell.")
    pka= input("Hearken or fight : ")
    while pka != "hearken" and pka != "fight":
        pka=input("type again : ")
    if pka in "hearken":
        print("Gandalf")
        helmsdeep()
    else:
        fight6()
def fight6():
    print("You have no power here. Gandalf Greyhame.")
    Gandalf = 10 
    Saruman = 10
    while Gandalf>=0 and Saruman>=0:
        hbl=input("Press any key to remove spell :")
        pi=random.randint(1,2)
        zi=random.randint(3,4)
        print("Gandalf uses a spell to break the spell",pi,"times.")
        print("Saruman counters by a spell",zi,"times.")
        if pi>zi:
            Gandalf = Gandalf - 2
            if Gandalf >0:
                print("Saruman is still strong and has strenght")
            else:
                print("You get defeated.\nSaruman kills Theoden King.")
                againl()
        else:
            Saruman = Saruman - 4
            if Saruman>0:
                print("He is Still resistive.")
            else:
                print("Theoden King is free of his spell.")
                helmsdeep()
def againl():
    again=input("Want to fight again? (Enter yes or no): ")
    while again.lower()!="yes" and again.lower()!="no":
        again=input("\n Please enter \"yes\" or \"no : ")
    if again.lower()=="yes":
       fight6()
    else:
        print("You are dead agian.")
        againl2()
def againl2():
    again=input("Want to go back to the menu or restart from hall of Meduseld again?(Enter yes or no): ")
    while again.lower()!="yes" and again.lower()!="no":
        again=input("\n Please enter \"yes\" or \"no: ")
    if again.lower()=="yes":
        print("Choose wisely this time.")
        menu()
    else:
        hall()
def helmsdeep():
    print("The enemy has shown his hand and started its attact from westfold coming to towards Rohan.")
    westfold()
def westfold():
    print("The whole of westfold burns through the wrath of the enemy")
    print("Next is Rohan.")
    print("Aragorn : What will you do?\n I will ")
    gik = input ("Stronghold or Refuge : ")
    while gik != "stronghold" and gik != "refuge":
        gik = input("type correctly : ")
    if gik in "stronghold":
        print("We fight ")
        print("Gather all the men. ")
        war1()
    else:
        print("We must take refuge in Helms deep.")
        print("While on your way to helms deep lady Ewoyn offers you some stew.")
        eat()
def eat():
    print("Do you want some stew :")
    ghk = input ("yes or no : ")
    while ghk != "yes" and ghk != "no":
        ghk = input("yes or no : ")
    if ghk in "yes":
        print("Thankyou. Yes Please")
        print("Okay. Can I ask you question. \nMy Uncle told me the Strangest thing, he said that you rode to war with Thengal my grandfather.")
        print("Is that true?")
        bvh = input("Yes or No?")
        while bvh != "yes" and bvh != "no":
            bvh = input("yes or no : ")
        if bvh in "yes":
            print("King Theoden has a good memory. \n He was only a small child at that time.")
            guessage()
        else:
            deep()
    else:
        print("Okay. Can I ask you question. \nMy Uncle told me the Strangest thing, he said that you rode to war with Thengal my grandfather.")
        print("Is that true?")
        bvh = input("Yes or No?")
        while bvh != "yes" and bvh != "no":
            bvh = input("yes or no : ")
        if bvh in "yes":
            print("King Theoden has a good memory. \n He was only a small child at that time.")
            guessage()
        else:
            deep()
def guessage():
    number=87
    print("Guess age from 77, 83, 87, 90")
    x=int(input("Maybe : "))
##    if x>number :
##        print("No less ")
##        x=int(input("less : "))
##    elif x<number :
##        print("No Older.")
##        x=int(input("Older : "))
    while x!=number:
        x=int(input(" again :"))
        if x == number :
            print("Your right.")
            time.sleep(1)
            print("Your one of the dunedain. \nDesecdant of Numenor, blessed with long life.")
            time.sleep(1)
            deep()
        else:
            print("No. Older")
def deep():
    print("Close to helmsdeep you get attacked by Orcs and Urakai. ")
    fight7()
def fight7():
    Aragorn = 100
    Orcs = 100
    Urakai = 100
    print("Aragorn Health", Aragorn)
    print("Orcs Health", Orcs)
    print("Urakai Health",Urakai)
    while Aragorn>=0 and Orcs>=0 or Urakai>=0:
        h=input("Press any key and then enter to attack : ")
        d=random.randint(2,4)
        f=random.randint(3,6)
        print("They are onto you. You have",Aragorn,"Health left.")
        print("Filthy Anoying creatures.They have",Orcs,"Health left.")
        if d>f:
            Orcs = Orcs - 15
            Urakai = Urakai -15
            if Orcs>0:
                print("They are in numbers.\nProtect the people.\nThey have",Orcs,"Health left.")
            else:
                print("You managed to survive the attact.")
                print("Get To Helms Deep.")
                alive()
        elif f>d:
            Aragorn= Aragorn - 30
            if Aragorn>0:
                print("They are too many in number. You have",Aragorn,"Health left.")
            else:
                print("Your belt get's stuck with a wolf and he ran down the cliff with you.")
                again13()
def again13():
    again=input("Want to go back to the menu or continue from battle?(Enter yes or y): ")
    while again.lower()!="yes" and again.lower()!="y":
        again=input("\n Please enter \"yes\" or \"y: ")
    if again.lower()=="yes":
        print("Choose wisely this time.")
        menu()
    else:
        alive()
def alive():
    print("You fell of the cliff.")
    ko = input("Get on the horse (yes or no) :")
    while ko != "yes" and ko != "no":
        ko = input("yes or no :")
    if ko in "yes":
        zs=input("Press any key to get on the horse : ")
        o = random.randint(2,5)
        if o>=3:
            print("You've got on the horse.")
            helm()
        else:
            print("The horse move nears you and helps you.")
            helm()
    else:
        print("Lady Arewn : May the grace of valar protect")
        print("You get on the horse.")
        helm()
def helm():
    print("You arrive at helmsdeep.")
    print("Everybody is happy to see you. \nYou tell about the great army marching towards helmsdeep. ")
    war1()
def helpwar():
    print("Elven Army reaches helmsdeep, the man says : \nI bring word from lord Elrond from Riverdale.\nAn Alliance existed between men and elves.\nWe fought once before.\n We came to honor that allegiance.")
    ar= input(" ShakeHand or Hug : ")
    while ar!="shake hand" and ar!="hug":
        ar=input("Type again (Shake hand or hug): ")
    if ar in "hug":
        print("You are most welcome.")
        war1()
    else:
        print("shake hand.")
        print("We appreciate your help.")
        war1()
def war1():
	print("The army of orcs are at our door.")
	print("Get ready for war.")
	Aragorn = 100
	Gandalf = 100
	Legolas = 100
	Gimli = 100
	Haldir = 100
	Elven_Army = 5000
	Orcs_Army = 5000
	Urakai_Army = 5000
	while Urakai_Army >=0 and Orcs_Army >= 0 and Aragorn >=0 and Legolas>= 0 and Gimli>=0 and Gandalf>=0 and Haldir>=0:
            paw = input("Press any key to attack : ")
            a=random.randint(4,8)
            g=random.randint(3,6)
            l=random.randint(3,6)
            m=random.randint(4,6)
            h=random.randint(3,4)
            o=random.randint(3,7)
            u=random.randint(5,9)
            x=a+g+l+m+h
            print("Aragorn has",a,"hits, Gandalf Uses",g,"Spells, Legolas shots",l,"Arrows, Gimli kills",m,"Orcs in a go and Haldir has",h,"kills.")
            print("Orcs and Urakai kill",x,"Rohanain troops")
            if a>u or a>o:
                Urakai_Army = Urakai_Army - 250
                Orcs_Army = Orcs_Army - 250
                if Urakai_Army>0 and Orcs_Army>0:
                    print("Hope is not lost. \nWe fill fight till the end.\nUrakai_Army has",Urakai_Army,"Stenght Left and Orcs_Army has",Orcs_Army,"Stenght left.")
                else :
                    print("We are pushing them back.\nWe can win this.\nFight for the middle earth !\nLoud Roars.")
                    rohan2()
            elif g>u or g>o:
                if Urakai_Army>0 or Orcs_Army>0:
                    print("Hope is not lost. \nWe fill fight till the end.\nUrakai_Army has",Urakai_Army,"Stenght Left and Orcs_Army has",Orcs_Army,"Stenght left.")
                elif Urakai_Army <= 0 and Orcs_Army <= 0:
                    rohan2()
                else :
                    print("We are pushing them back.\nWe can win this.\nFight for the middle earth !\nLoud Roars.")
                    rohan2()
            elif l>u or l>o :
                Urakai_Army = Urakai_Army - 400
                Orcs_Army = Orcs_Army - 250
                if Urakai_Army>0 and Orcs_Army>0:
                    print("Let's see how many I get.")
                    print("Gimli has",m,"Kills and Legolas has",l,"Kills.")
                    print("Urakai_Army has",Urakai_Army,"Stenght Left. and Orcs_Army has",Orcs_Army,"Stenght left.")
##                elif Urakai_Army <= 0 or Orcs_Army <= 0:
##                    rohan2()    
                else:
                    print("Urakai_Army and Orcs_Army have depleted in numbers.\nLet's finsih them off.")
                    print("The war is one.")
                    rohan2()
            elif m>o or m>u:
                Urakai_Army = Urakai_Army - 400
                Orcs_Army = Orcs_Army - 250
                if Urakai_Army>0 and Orcs_Army>0:
                    print("Let's see how many I get.")
                    print("Gimli has",m,"Kills and Legolas has",l,"Kills.")
                    print("Urakai_Army has",Urakai_Army,"Stenght Left. and Orcs_Army has",Orcs_Army,"Stenght left.")
##                elif Urakai_Army <= 0 or Orcs_Army <= 0:
##                    rohan2()    
                else:
                    print("Urakai_Army and Orcs_Army have depleted in numbers.\nLet's finsih them off.")
                    rohan2()
            elif h>o or h>u :
                Urakai_Army = Urakai_Army - 400
                Orcs_Army = Orcs_Army - 300
                if Urakai_Army>0 and Orcs_Army>0:
                    print("Hold you ground.\nBe Brave and fight for the survial of middle earth.")
                    print("Urakai_Army has",Urakai_Army,"Stenght Left. and Orcs_Army has",Orcs_Army,"Stenght left.")
##                elif Urakai_Army <= 0 or Orcs_Army <= 0:
##                    rohan2()
                else:
                    print("Near to Victory.")
                    rohan2()
            elif o>a or u>a:
                Aragorn = Aragorn - 10
                if Aragorn>0 :
                    print("You are getting pushed back.")
                    print("You have",Aragorn,"Health.")
                else :
                    print("You are being gained on.\nYou have been killed by the Urakai.")
                    againwar1()
            elif o>g or u>g:
                Aragorn = Aragorn - 10
                if  Gandalf>0:
                    print("You are getting pushed back.")
                    print("You have",Aragorn,"Health.")
                else :
                    print("You are being gained on.\nYou have been killed by the Urakai.")
                    againwar1()
            elif o>l or u>l :
                Legolas = Legolas - 10
                if Legolas>0 :
                    print("They are too many. We are getting alot of damage.")
                    print("Legolas has",Legolas,"Energy left and Gimli has",Gimli,"Energy left.")
                else:
                    print("Orcs and Urakaiwon the war.")
                    againwar1()
            elif o>m or u>m:
                Gimli = Gimli - 15
                if  Gimli>0:
                    print("They are too many. We are getting alot of damage.")
                    print("Legolas has",Legolas,"Energy left and Gimli has",Gimli,"Energy left.")
                else:
                    print("Orcs and Urakai,won the war.")
                    againwar1()
            elif o>h or u>h:
                Haldir = Haldir - 15
                if Haldir>0:
                    print("A arrow pierced through Haldir's Chest.")
                    print("Haldir has",Haldir,"Health")
                else :
                    againwar1()
            else :
                print("You've won the war.")
                rohan2()
def againwar1():
    again=input("Want to fight again? (Enter yes or no): ")
    while again.lower()!="yes" and again.lower()!="no":
        again=input("\n Please enter \"yes\" or \"no : ")
    if again.lower()=="yes":
       war1()
    else:
        print("You are dead agian.")
        againwar11()
def againwar11():
    again=input("Want to go back to the menu or continue from westfold again?(Enter yes or no): ")
    while again.lower()!="yes" and again.lower()!="no":
        again=input("\n Please enter \"yes\" or \"no: ")
    if again.lower()=="yes":
        print("Choose wisely this time.")
        menu()
    else:
        westfold()
def rohan2():
    print("We won the war.")
    print("Now we look forward towards ending the enemies plan.")
    saruman()
def saruman():
    print("We move to Isengard.\nTo get knowledge of the enimes attact from Saruman as he was deep in the dark lord's counsel.")
    Questions = ["1.What does the enemy plan?,2.Who is this ranger?"]
    for i in Questions:
        print(i)
        print()
        time.sleep(2)
        question = input("What do you want to ask about?\n(Plan or Ranger?) : ")
        while question != "plan" and question != "ranger":
            question = input("What? type again : (plan or ranger) : ")
        if question in "plan":
            print("You come here for information?")
            dfc=input("yes or no : ")
            while dfc != "yes" and dfc != "no":
                dfc = input("type yes or no : ")
            if dfc in "yes":
                print("I will give some information\nSomething festers in the heart of the middle earth that you were blind to see but the graet eye has seen it.")
                print("Even now he press his advantage against you.")
                gondor()
            else:
                print("You are all going to die.\nYou cannot fight against the dark lord.")
                Gandalf = 10
                Saruman = 5
                while Gandalf > 0 and Saruman >0:
                    jkl= input("Press enter to break staff :")
                    a=random.randint(1,3)
                    if a>=2:
                        Saruman = Saruman - 5
                        print("Saruman your staff is broken into",a,"pices")
                        print("Saruman got thrown of the cliff by grima.")
                        gondor()
                    else:
                        print("Saruman got thrown of the cliff by grima.")
                        gondor()
        else :
            print("Do you really think this ranger will ever sit upon the throne of Gondor?")
            fdc =  input("Yes or Y : ")
            while fdc != "yes" and fdc != "y" :
                fdc = input("type yes or y :")
            if fdc in "y":
                print("You are a bigger fool than i thought.")
                print("Saruman got thrown of the cliff by grima.")
                gondor()
            else :
                print("Die")
                Gandalf = 10
                Saruman = 5
                while Gandalf > 0 and Saruman >0:
                    jkl= input("Press enter to break staff :")
                    a=random.randint(1,2)
                    if a>=2:
                        Saruman = Saruman - 5
                        print("Saruman your staff is broken into",a,"pices")
                        gondor()
                    else:
                        print("Saruman got thrown of the cliff by grima.")
                        gondor()
def gondor():
    print("City of Minas Tirath.")
    path = input("Left or right : ")
    while path != "left" and path != "right":
        path = input("type left or right : ")
    if path in "left":
        print("You reavhed the Staircase.")
        path2 = input("Go_up or Go_down : ")
        while path2 != "go up" and path2 != "go down":
            path2=input("type go up or go down : ")
        if path2 in "go down":
            print("You have enter the great hall.")
            x="Confront Sauron"
            print(x)
            print("Lond have you hunted me and I have eluded you.\nBut no more.\nBe Hold The Sword of Elendi.")
            print("I am ready fot you.")
            battleS()
        else :
             print("You've entered the room of kings.\nWhere the throne is set.")
             print("look around more motivation for the battle with sauron.")
             battleS()
    else :
        print("You see the white tree of gondor.\nThe tree of the king.")
        print("You look at the city from above and then prepare for battle.")
        battleS()
def battleS():
    print("You meet Sauron in battle to give frodo the time to destroy the ring.")
    print("The Enemy is almost at his full power")
    Aragorn = 70
    Sauron = 70
    print("Aragorn's Health",Aragorn)
    print("Sauron's Health",Sauron)
    while Aragorn >=0 and Sauron >=0 :
        Sword=input(" blow or cut : ")
        while Sword != "blow" and Sword != "cut":
            Sword = input("blow or cut : ")
        a=6
        b=7
        d=9
        asd=random.randint(a,d)
        das=random.randint(a,b)
        print("Aragorn hits Sauron",asd,"times.")
        print("Sauron hits Aragorn",das,"times.")
        if asd>das:
            Sauron = Sauron - 20
            if Sauron>0:
                print("You grazed Sauron.\nSauron's health is depleted a bit")
                print("You are fighting well.\nThe enemy is shakened.Enemy's ")
                print("You are winning.\nJust keep fighting,for all middle earth.\nSauron's Health",Sauron)
            else :
                print("You defeated Sauron.")
                print("Gained enough time for frodo to destroy the ring of power in mount doom.")
                end()
        else:
             Aragorn = Aragorn - 25
             if Aragorn>0:
                 print("You can feel the wraith of the dark lord.\nHis attacks are swift and heavy.")
                 print("You understand the power of the eye and the darkness.\nYou got a deep wound on your hand.\nYour Health",Aragorn)
             else :
                 print("Do you not know death when you see it? King of men. Breathing Heavily, You barely can stand up,\nYour health",Aragorn)
                 print("Sauron is winning.")
                 print("Sauron killed you and took over the middle earth")
                 againlast()
def againlast():
    again=input("Do you want to fight again.(Enter yes or no): ")
    while again.lower()!="yes" and again.lower()!="no":
        again=input("\n Please enter \"yes\" or \"no : ")
    if again.lower()=="yes":
       battleS()
    else:
       againlast2()
def again2():
    again=input("Want to go back to the menu or continue from gondor (Enter yes or no): ")
    while again.lower()!="yes" and again.lower()!="no":
        again=input("\n Please enter \"yes\" or \"no : ")
    if again.lower()=="yes":
        menu()
    else:
        gondor()

def end():
    print("The Dark Lord has been defeated and the ring of power destroyed.")
    print("I hope the game was fun.")
    print("Play again")
    time.sleep(5)
    menu()
def miniepisodes():
    print("1.Training")
    print("2.Finding Mithral")
    print("3.Saving Foromir")
    print("4.Back")
    select = input("Choose one : ")
    while select != "1" and select != "2" and select != "3" and select != "4":
        select = input("Choose from 1-4 : ")
    if select in "1":
        print("training")
        train()
    elif select in "2":
        print("Finding mithral in mines of moria.")
        print("It is like maze inside.")
        mithral()
    elif select in "3":
        foromir()
    else:
        menu()
def mithral():
    print("You Enter the mines")
    jh =input("left or right : ")
    while jh != "left" and jh != "right":
        jh = input("type correctly left or right : ")
    if jh in "left":
        print("There are stairs going up and down.")
        hj= input("up or down : ")
        while hj != "up" and hj != "down":
            hj = input("up or down : ")
        if hj in "up":
                print("You've encountered orcs.\nRun? \nFight?")
                lop=input(" Run or fight : ")
                while lop!= "run" and lop != "fight":
                    lop= input("run or fight : ")
                if lop in "run":
                    print("Into the cave or the near room?")
                    pol=input("cave or room : ")
                    while pol != "cave" and pol != "room":
                        pol = input("cave or room : ")
                    if pol in "cave":
                        print("The Enterance to the cave get's smashed.\nYou get stuck there.\nYou die.")
                        againm()
                    else:
                        print("You've found a bunch load of mithral.\n now to get of the mines.")
                        print("Get out of the room.\nGo left or right?")
                        ion= input("left or right : ")
                        while ion != "left" and ion != "right":
                            ion = input("(left or right : )")
                        if ion in "left":
                            print("You got to the orcs.")
                            print("You got killed.")
                            print("Try again")
                            againm()
                        else:
                            print("You got out of the mines with a lot of mithral.")
                            print("find more mithral next time.")
                            miniepisode()
                else:
                     fightm()
        else:
                  print("You went down.")
                  print("You've found mithral.")
                  print("Find more mithral someother time.")
                  againm()
    else:
        print("You turned right.")
        print("There is a huge hall way. A flame appears from the side. It's a belrog.")
        print("fight it or leave the mines.")
        jko = input("fight or leave : ")
        while jko!="fight" and jko != "leave":
            jko= input("type fight or leave :")
        if jko in "fight":
            print("there is a rare chance of defeating the belrog but mithral is more important.")
            fightb()
        else:
            againm()
def fightm():
    You = 100
    Orcs = 100
    print("Your Health", You)
    print("Orcs Health", Orcs)
    while You>=0 and Orcs>=0:
        h=input("Press enter to attack : ")
        d=random.randint(3,6)
        f=random.randint(3,6)
        print("You battle them. You have",You,"Health left.")
        print("Orcs are gaining on you.They have",Orcs,"Health left.")
        if d>f:
            Orcs = Orcs - 15
            if Orcs>0:
                print("You are holding your ground.\nThey have",Orcs,"Health left.")
            else:
                print("You managed to kill all of them.\nContinue Searching mithral.")
                conti()
        elif f>d:
            You = You - 15
            if You>0:
                print("They are too many in number. You have",You,"Health left.")
            else:
                print("You have been killed by the Orcs.")
                againmf()
def againm():
    again=input("Want to go back to the miniepisodes or find mithral again (Enter yes or y): ")
    while again.lower()!="yes" and again.lower()!="y":
        again=input("\n Please enter \"yes\" or \"y : ")
    if again.lower()=="yes":
        miniepisodes()
    else:
        mithral()
def againmf():
    again=input("Want to fight again or go to miniepisodes? (Enter yes or y): ")
    while again.lower()!="yes" and again.lower()!="y":
        again=input("\n Please enter \"yes\" or \"y : ")
    if again.lower()=="yes":
        fightm()
    else:
      miniepisodes()
def train():
    morale1 = 100
    morale2 = 100
    time.sleep(1)
    print("Peragrin's Morale",morale1)
    print("Meridoc's Morale",morale2)
    time.sleep(1)
    while morale1 >= 0 and morale2 >=0 :
          a=input("Press Enter to learn ")
          p=(random.randint(3,5))
          l=(random.randint(2,6))
          print("Peragrin learns",p,"Sword moves")
          print("Meridoc learns",l,"Sword moves")
          time.sleep(1)
          if p>l:
            morale1=morale1-20
            if morale1>0:
                  print("It's not easy to weild a sword.Peragrin ",morale1,"morale left")
            else:
                  print("You managed to learn quite a few moves.")
                  print("this is enough for now.")
                  print("train again sometime.")
                  againt()
          elif l>p:
              morale2= morale2 - 20
              if morale2>0:
                  print("You are getting a hang of this.Meridoc",morale2,"morale left")
              else:
                  print("You managed to learn quite a few moves.")
                  print("this is enough for now.")
                  print("train again sometime.")
                  againt()
##              elif morale2 == 0:
##                  print("try again somethere time.")
##                  againt()
          else:
              print("You managed to learn quite a few moves.")
              print("this is enough for now.")
              print("train again sometime.")
              againt()
def againt():
    again=input("Want to go back to the miniepisodes or train again (Enter yes or y): ")
    while again.lower()!="yes" and again.lower()!="y":
        again=input("\n Please enter \"yes\" or \"y : ")
    if again.lower()=="yes":
        miniepisodes()
    else:
        train()
def fightb():
    You = 100
    Belrog = 100
    print("Your Health", You)
    print("Belrog's Health", Belrog)
    while You>=0 and Belrog>=0:
        h=input("Press enter to attack : ")
        d=random.randint(3,6)
        f=random.randint(3,6)
        print("You battle it. You have",You,"Health left.")
        print("He is hammering you.He has",Belrog,"Health left.")
        if d>f:
            Belrog = Belrog - 15
            if Belrog>0:
                print("You are holding your ground.\nIt has",Belrog,"Health left.")
            else:
                print("You managed to kill belrog.\nContinue Searching mithral.")
                conti()
        elif f>d:
            You = You - 10
            if You>0:
                print("He is very powerfull. You have",You,"Health left.")
            else:
                print("You have been killed by the Belrog.")
                againm()
def conti():
    print("You have fought of the belrog.\nContinue finding the mithral.")
    pli = input("Go down or up : ")
    while pli != "down" and pli != "up":
        pli = input("up or down : ")
    if pli in "down":
        print("There are two paths.")
        ipl = input("Steep or narrow : ")
        while ipl != "steep" and ipl != "narrow":
            ipl = input("type again? steep or narrow")
        if ipl in "steep":
            print("You try to go this path but fall hard many times.")
            print("You give up finding mithral.")
            againm()
        else:
            print("It's a very narrow path. You barely can move through.The path ends.")
            print("You see a water pond, a chest. ")
            see = input ("drink water or open chest :")
            while see != "drink" and see != "open":
                see = input("drink or open : ")
            if see in "drink":
                print("While drinking water, someone drags you by your feet.\nYou look at your feet, it's a octopus.\nYou are being dragged into the pond.")
                print("run or cut the hand with sword")
                ad= input("Cut or run")
                while ad != "cut" and ad != "run":
                    ad = input("run or cut : ")
                if ad in "run":
                    print("You see a way out. You ran out of the mines.")
                    print("Do you want to back in to find mithral or it is enough.")
                    mithral()
                        
                else:
                    print("You take out your sword.")
                    cutm = input("press enter to cut :")
                    a=random.randint(3,5)
                    if a>=4:
                        print("You sliced its tail.\nYou get afraid and get out of the mines.\nYou take a breath and go back inside from the other way.")
                        time.sleep(2)
                        mithral()
                            
                    else:
                        print("You got dragged into the pond.")
                        print("You died.")
                        miniepisodes()
            else:
                print("You open the chest. There are alot of jewels in there and some mithtral.")
                print("It was productive day.\nYou get out of the mines but you become greedy an want more mithral.\nfind more mithral or not?")
                eq = input("yes or no : ")
                while eq != "yes" and eq != "no":
                    eq = input("yes or no : ")
                if eq in "yes":
                    mithral()
                else:
                    miniepisodes()
    else:
        print("You see the grave of the drawf lord of the mines.\nThere is secret passage below the grave\nYou here orcs from below.")
        open = input("Go through the passage or not : ")
        while open != "yes" and open != "no":
            open = input("yes or no : ")
        if open in "yes":
            print("You find a cave that is filled with refined mithral.")
            print("You collect as mush as you can and leave.")
            againm()
        else:
            print("You waited and over sighted the passage.\nOrcs moving through the way they see you and attack.")
            fightm()
def foromir():
    print("Save foromir.\nLord Denothor is burning him alive.")
    print("You must save him.")
    print("You are in the Courtyard.\nYou have go to the burial room")
    path = input("Left or right : ")
    while path != "left" and path != "right":
        path = input("type left or right :")
    if path in "left":
        left()
    else :
        right()
def left():
    print("You've reached the ground level of city.\nThe burial room  next to the hall of kings.")
    move = input("Go up or down : ")
    while move != "up" and move != "down":
        move = input("enter up or down : ")
    if move in "down":
        print("The way down is full of orcs.\nGo through the tunnel or up the stairs.")
        pi= input("Tunnel or stairs : ")
        if pi == "tunnel":
            print("There are 3 paths")
            path2=input("North,South,West : ")
            while path2 != "north" and path2 != "south" and path2 != "west":
                path2=input("choose : north, south or west :")
            if path2 in "north":
                print("You ran into Orcs.")
                orcs = random.randint(0,30)
                print("There are about",orcs,"in our way.")
                if orcs < 15:
                    print("Out of my way.\nKill the orcs to move Ahead.")
                    fighto()
                else:
                    print("run the other way and get to the burial room to save foromir.")
                    east()
            elif path2 in "south":
                print("You've are on the middle level of the city, the burial room is on the top.\nOne more level left.")
                right()
            else:
                print("You are going west.")
                west()
        else:
            print("The Stairs of Minas Tirath.")
            print("You run through the stairs but there is a giant rock blocking the way.\nThere are two ways.")
            way = input("left or right : ")
            if way == "left":
                print("The way up has broken stairs.\nUrakai are behind you. There is way that goes down.")
                way1=input("Do you want to fight or go down : ")
                while way1 != "yes" and way != "y":
                    way1 = input(" type yes or y : ")
                if way1 in "yes":
                    fightuk()
                else:
                    left()
            else:
                  east()   
    else:
        print("This is short secret waythat open's up near to the hall of kings.")
        kinghall()
def right():
    print("You are pacing through the enimes.")
    ilo=input("Go through the corridor or westside : ")
    while ilo != "corridor" and ilo != "westside" :
        ilo = input("type corridor or westside : ")
    if ilo in "corridor":
        print("The way seems clear.\nYou move ahead to see the corridor is blocked and there is narrow opening.")
        rem = input("Want to go through the narrow opening?")
        while rem != "yes" and rem != "no":
            rem = input("type yes or no : ")
        if rem in "yes":
            print("You got clear.\nThe burial room is in front of you.\nGo save Foromir. ")
            kinghall()
        else:
            print("Witch king of Angmar, the Leader of the enimes's army has spotted you.")
            print("You got killed. Foromir died as you could not save him.")
            fightwitch()
    else:
        print("Moving to east.")
        east()
def fighto():
    You = 100
    Orcs = 100
    print("Your Health", You)
    print("Orcs Health", Orcs)
    while You>=0 and Orcs>=0:
        h=input("Press enter to attack : ")
        d=random.randint(4,8)
        f=random.randint(3,6)
        print("You battle them. You have",You,"Health left.")
        print("Orcs are gaining on you.They have",Orcs,"Health left.")
        if d>f:
            Orcs = Orcs - 20
            if Orcs>0:
                print("You are holding your ground.\nThey have",Orcs,"Health left.")
            else:
                print("You managed to kill all of them.\nMove forward.")
                right()
        elif f>d:
            You = You - 15
            if You>0:
                print("They are too many in number. You have",You,"Health left.")
            else:
                print("You have been killed by the Orcs.")
                againfo()
def againfo():
    again=input("Want to go back to the miniepisodes or fight again. (Enter yes or y): ")
    while again.lower()!="yes" and again.lower()!="y":
        again=input("\n Please enter \"yes\" or \"y : ")
    if again.lower()=="yes":
        miniepisodes()
    else:
        fighto()
def east():
    print("You are being tailed by orcs.\nYou see a way up through a tall ladder. ")
    halt=input("climb ladder or keep running : ")
    while halt != "climb" and halt != "running":
        halt=input("climb or running : ")
    if halt in "climb":
        print("You've got just one level left.")
        right()
    else:
        print("Goblins are coming from the other side.\nGo up the ladder.")
        east()
def west():
    print("You encounter the witch king of angmar.\nDo you not know death when you see it.")
    print("He kills you in a blink.\nForomir died as you could reach the burial room.")
    miniepisodes()
def fightuk():
    You = 100
    Urakai = 100
    print("Your Health", You)
    print("Urakai Health", Urakai)
    while You>=0 and Urakai>=0:
        h=input("Press enter to attack : ")
        d=random.randint(4,8)
        f=random.randint(3,6)
        print("You battle them. You have",You,"Health left.")
        print("Urakai are gaining on you.They have",Urakai,"Health left.")
        if d>f:
            Urakai = Urakai - 20
            if Urakai>0:
                print("You are holding your ground.\nThey have",Urakai,"Health left.")
            else:
                print("You managed to kill all of them.\nMove forward.")
                right()
        elif f>d:
            You = You - 15
            if You>0:
                print("They are too many in number. You have",You,"Health left.")
            else:
                print("You have been killed by the Urakai.")
                againuk()
def againuk():
    again=input("Want to go back to the miniepisodes or fight again. (Enter yes or y): ")
    while again.lower()!="yes" and again.lower()!="y":
        again=input("\n Please enter \"yes\" or \"y : ")
    if again.lower()=="yes":
        miniepisodes()
    else:
        fightuk()
def kinghall():
    print("You've reached the hall of kings.\nRun to the burial room.\nYou enter the room and see the lord putting the fire up.")
    print("Kill lord Denothor")
    kill = input("Use sword :")
    if kill in "yes":
        print("You killed the lord and saved Foromir.")
        time.sleep(5)
        miniepisodes()
    else:
        print("What are you waiting for ? while you thinking through Foromir got burned alive.")
        againforo()
def againforo():
    again=input("Want to go back to the miniepisodes or kinghall. (Enter yes or y): ")
    while again.lower()!="yes" and again.lower()!="y":
        again=input("\n Please enter \"yes\" or \"y : ")
    if again.lower()=="yes":
        miniepisodes()
    else:
        kinghall()
def fightwitch():
    You = 100
    WitchKing = 100
    print("Your Health", You)
    print("Urakai Health", WitchKing)
    while You>=0 and WitchKing>=0:
        h=input("Press enter to attack : ")
        d=random.randint(4,8)
        f=random.randint(3,6)
        print("You battle him. You have",You,"Health left.")
        print("He is strong and has no effect of your attacks.He",WitchKing,"Health left.")
        if d>f:
            WitchgKing = WitchKing - 20
            if WitchKing>0:
                print("You are holding your ground.\nThey have",WitchKing,"Health left.")
            else:
                print("You managed to kill him.\nMove forward.")
                right()
        elif f>d:
            You = You - 15
            if You>0:
                print("He has tremendous power. You have",You,"Health left.")
            else:
                print("You have been killed by the Witch King.")
                againuk()
def againwk():
    again=input("Want to go back to the miniepisodes or fight again. (Enter yes or y): ")
    while again.lower()!="yes" and again.lower()!="y":
        again=input("\n Please enter \"yes\" or \"y : ")
    if again.lower()=="yes":
        miniepisodes()
    else:
        fightwitch()
        
#Ali's Part Frodo Function

def frodo():
    print("\n  I am Gandalf the grey wizard, and I will help you Destroy the ring to save the middle earth ")
    time.sleep(2)
    print("\n The ring you got is strongest ring of all..... ")
    time.sleep(1)
    print(" The evil powers are in search of this ring to destroy the makind and capture the world. ")
    time.sleep(1)
    print(" \n They have a sense that the ring is in the  shire \n If they  reach here they  will destroy the shire and can do anything to get the ring ")
    time.sleep(2)
    print(" \n \n Now it's all upon you whether you will take the Ring away from here .... \n Or see everyone destroying along with yourself ")
    t()
def t():
    think= input("\n   Will you go ? ")
    if think.lower() =='yes' or think.lower()=='y' :
        bree()
    elif think.lower()== 'no' or think.lower()=='n':
        print(" \n You're a coward person . Did'nt expected that from you .")
        time.sleep(2)
        print(" Game ended \n \n Returning to menu.....")
        time.sleep(1)
        menu()
    else:
        print(" \n incorrect entry \n write Yes or NO ? ")
        t()
def bree():
    print("\n  The Knights of Saruman will be reaching here anytime.... \n You must go .... \n ")
    time.sleep(1)
    print("     - But where Will I go Gandalf ? ")
    time.sleep(1)
    print("\n Just pack your bags and Run and Run towards Bree. I will meet you there .")
    time.sleep(2)
    print("\n Remember ! Keep the ring in the pocket \n Not to wear the ring at any time or the Knights will see you and smell you and chase you and you may get killed ")
    time.sleep(1)
    print(" Hurry !!! \n Hurry !!! you've got no time ")
    c()
def run():
    print("\n \n  ***********  You are going through forests !!! Towards Breee !! \n     Feeling hungry ? Lets have something to eat ! **********")
    time.sleep(2)
    food=input(" There is a hotel near the roadside , wanna go ?  ")
    if food.lower()=='yes' or food.lower()=='y' or food.lower()=='sure' or food.lower()=='yeah' :
        print(" \n Alright \n ")
        time.sleep(2)
        order()
    elif food.lower()=='no' or food.lower()=='n' :
        print(" \n Alright Lets continue the journey \n \n \n ")
        hotel()
    else:
        print(" invalid Entry \n Choose again ")
        time.sleep(1)
        run()
def c():
    check=input(" \n Check the ring \n Is it in the pocket ? ")
    if check.lower()=='yes' or check.lower()=='y':
        print(" \n Great , now do it fast ")
        time.sleep(3)
        run()
    elif check.lower()=='no' or check.lower()=='n':
        print("\n  What? You must have the ring , there is no other option .")
        time.sleep(1)
        c()
    else:
        print(" \n incorrect entry \n ")
        c()
def order():
    print(" \n  Welcome you litte hobbit.... \n what would you like to eat ?")
    time.sleep(1)
    choose=input("We got bread , tea , cake and beer... \n            ")
    if choose.lower()== 'bread' or choose.lower()== 'b' or choose.lower()== '1':
        print(" Alright !! come sit here while your order gets ready ")
        time.sleep(2)
        hotel()
    elif choose.lower()=='tea' or choose.lower()=='t' or choose.lower()=='2':
        print(" Alright !! come sit here while your order gets ready ")
        time.sleep(2)
        hotel()
    elif choose.lower()=='cake' or choose.lower()=='c' or choose.lower()=='3':
        print(" Alright !! That will take some time please come sit here and wait ")
        time.sleep(2)
        hotel()
    elif choose.lower()=='beer' or choose.lower()=='4':
        print(" Alright !! That will take some time please come sit here and wait ")
        time.sleep(2)
        hotel()
    else:
        print(" \n \n we donot have that ")
        order()
def hotel():
    with open("import files//hotel.txt","r") as o:
        print(o.read())
    print(" What to do ? ")
    time.sleep(2)
    hot()
def hot():
    x=input(" Reply with YES to take Sam along. You will Need him:  ")
    if x.lower()=='yes' or x.lower()=='y' or x.lower()=='okay':
        print('''\n  " Thankyou Frodo !! I will be with you at all times !! I promise " ''')
        time.sleep(2)
        print(" \n     - I know and I trust you Sam !!! \n       ")
        time.sleep(1)
        sam()
    elif x.lower()=='no' or x.lower()=='n':
        print(''' " \n No Frodo !! I will go with you at any cost ! \nYou cannot stop me \n I'm your closest friend ! " ''')
        time.sleep(2)
        print("\n      - Okay sam !! But you will do as I say at all the journey ")
        time.sleep(1)
        print('''\n  Okay Frodo ! I promise I will do as you say \n ''')
        sam()
    else:
        print("\n Incorrect Entry \n Try again !!! \n ")
        hot()
def sam():
    with open("import files//ara.txt","r") as o:
          print(o.read())
          c=input("\n \n Press any key to continue ! ")
          ara()
def ara():
    time.sleep(2)
    print(''' \n       - Don't try to touch me . Who are you ? ''')
    time.sleep(2)
    print('''\n  " I am Aragorn , just  come with me. I know you got the ring. I've got a sword .....
        and I will protect you through all this . ''')
    time.sleep(3)
    print('''  \n     - But why should I trust you ? You could be a theif or something.... ''')
    time.sleep(2)
    print(''' \n " I am the heir of the person who destroyed the ring from evil hands.....  " ''')
    time.sleep(1)
    print('''    " and now I am the one who will help you destroy it... " \n \n ''')
    time.sleep(2)
    b()
def b():
    think=input(" \n Trust Aragorn ?  ")
    if think.lower()=='yes' or think.lower()=='y' :
        time.sleep(1)
        guide()
    elif think.lower()=='no' or think.lower()=='n' :
        time.sleep(2)
        no()
    else:
        print(" Invalid entry ! choose the correct option ")
        b()
def no():
    print('''\n \n  " Shut up ! and listen to me \n
  I am not here to play  games . You cannot go without me .
  the spies are already chasing and hunting you . If they find you , you can get killed . ''')
    time.sleep(2)
    guide()
def guide():
    print('''\n  \n  " Wait , did you hear that ! The voice of Evils ? The knights of Sauron are here !
   Come ! Lets hide or they will see us..... "
   ''')
    time.sleep(2)
    print(''' " Here Frodo ! Come here fast !!!!! " ''')
    hide()
def hide():
    time.sleep(2)
    think=input(''' \n \n  What  to Do ?

press "h" to hide
press "r" to run
press "s' to stay
''')
    if think.lower()=='h' or think.lower()=='hide' :
        trunk()
    elif think.lower()=='r' or think.lower()=='run'  :
        time.sleep(2)
        print("\n  No Frodo ! you cannot run from them ! \n Quick !! Come here Please .... We should hide behind the tree !! ")
        hide()
        
    elif think.lower()=='s' or think.lower()=='stay':
        time.sleep(3)
        print(''' *************** YOU GOT KKILLED BY THE KNIGHTS OF SAURON***************
\n                *************************GAME OVER**************************** "
''')
        over()
    else :
        print(" Invalid Entry \n  Try again ")
        time.sleep(1)
        hide()
def over():
    x=input('''\n \n press "1" to Continue from checkpoint 
 \n press "2" to return to main menu       ''')
    if x=='1' or x.lower()=='c' or x.lower()=='continue':
        time.sleep(1)
        sam()
    elif x=='2' or x.lower()=='menu':
        time.sleep(1)
        print( " Loading..... ")
        time.sleep(3)
        menu()
    else :
        print(" incorrect Entry Try again ")
        over()
        
def trunk():
    print('''\n  " Shhh ! Just stay quiet !
  And remember not to wear the ring !!!
 or the could easily see you and locate you where you are "
 ''')
    time.sleep(3)
    print(" \n \n          *****Your mindic powers are enforcing you to wear the ring ***** \n \n ")
    r()
def r():
    wear=input(''' Press "1" to wear the ring
 press "2" to NOT wear the ring ''')
    if wear=='1' :
        print("\n  your eyes are closed and you are not in senses \n   ")
        time.sleep(2)
        print(''' \n \n " Frodo ! Shit !! Frodo, what have you done.....
 Wake up !
 Frodo Wake up !!"
 ''')
        time.sleep(2)
        print( " Aragorn - The knight riders must be reaching us ")
        time.sleep(2)
        faint()
    elif wear=='2' :
        print(" \n \n Great control Frodo ")
        time.sleep(1)
        faint()
    else:
        print(" \n Invalid Entry ...... Choose again")
        time.sleep(2)
        r()
def faint():
    print( '''\n \n  " HERE THEY COME !  " ''')
    time.sleep(2)
    print(" \n Sam , you go and cover Frodo while I fight with them")
    time.sleep(3)
    print(' ***** The Knights are reaching towards you ***** ')
    a=input("\n \n  Press any key to start fight ")
    fi()
def fi():
    Aragorn = 100

    NightWraiths = 25

    time.sleep(1)

    while Aragorn >=0 and NightWraiths >=0:

        g=input("Try to ward off the wraiths with fire : \n Press any key : ")

        z=random.randint(2,5)

        o=random.randint(2,3)

        print("\n Aragorn draws fire rear the Wraiths",z,"times \n ")

        print("They are neither living nor dead.Keep the fire going and let in near the Wraiths",o,"times \n")

        time.sleep(1)

        if z>o :
            NightWraiths = NightWraiths - 12.5
            if NightWraiths>0:
                print("\n They answer the call of Sauron \n \n They desired power above everthhing else \n Slaves to the dark lord's will")

                print("They have",NightWraiths,"energy left.")

            else:
                print("\n The Ringwraits are retreating.")

                print("\n Lets take him to Riverdale fast")

                time.sleep(1)

                os.system('cls')
                fro()

        else  :
             Aragorn = Aragorn - 25
             if Aragorn > 0:
                 print("\n Wraiths are returning")
                 print("\n Aragorn has",Aragorn,"energy left.")

             else:
                 again50()
                
def again50():
    tro=input("\n \n Do you want to Continue or quit the  game ?  ")
    while tro != "continue" and tro != "quit":
        print("\n  Wrong entry.... REwrite ")
        tro=input("\n \n Do you want to Continue or quit the  game ?  ")
    if tro.lower()=='continue':
        fi()
    elif tro.lower()=='quit':
        menu() 
    
    
def fro():
    time.sleep(2)
    print(' \n \n  " Ahh , Mr.Frodo.... " ')
    time.sleep(1)
    print('\n  " Sam? what happened to him ?" ')
    time.sleep(1)
    print("\n     Sam- I don't know whats happening ! ...")
    time.sleep(1)
    print( '\n  "Oh look  he got a wound !! He must be taken away to someone or he may die " ')
    time.sleep(2)
    print("\n    Sam- But.....But what happened to him ?")
    time.sleep(1)
    print("\n  He is attacked by the knights and he struck him with a sword ")
    time.sleep(2)
    print("\n Now we ain't got no time we should take him to riverdale")
    th()
def th():
    print("Carry Frodo to the riverdale \n      OR     \n Leave him here ")
    take=input('''
press "1" to carry Frodo
press "2" to leave him here dying
''')
    if take=='1' :
        tke()
    elif take=='2':
        time.sleep(2)
        print("    \n SAM- what do you think of yourself Man !!! \n       I will not let you go !! Come on take him !\n  ")
        time.sleep(2)
        th()
    else:
        print(" invalid Entry .... Retry !! ")
        th()
def tke():
    time.sleep(1)
    print('''\n    " Frodo ! don't loose hope Frodo " ''')
    time.sleep(2)
    print('''  \n      Aragorn- let's take him to riverdale .... These he will get fine  "  ''')
    time.sleep(1)
    print(''' \n  " As you say Ara'   " ''')
    time.sleep(2)
    x=input("\n \n  press any key to continue : ")
    riven()
def riven():
    print(" \n  ********** The Rivendale is in the east ************ \n ")
    time.sleep(1)
    b=input('''  press "e" to move towards EAST
  press "s" to move towards South
  press "n" to move towards North
  press "w" to move towards WEST
  ''')
    if b.lower()=='e' or b.lower()=='east' :
        print(" \n \n *****moving towards rivendale ***** \n \n ")
        time.sleep(2)
        hunger()
    elif b.lower()=='s' or  b.lower()=='south':
        print(" \n *****WRONG DIRECTION***** ")
        riven()
    elif b.lower()=='n' or b.lower()=='north' :
        print(" \n *****WRONG DIRECTION ***** ")
        riven()
    elif b.lower()=='w' or b.lower()=='west' :
        print(" \n *****WRONG DIRECTION*****")
        riven()
    else:
        print(" invalid entry .... Retry ")
        riven()
def hunger():
    print('''    " I am feeling Hungry Ara' \n     You got something ? "   ''')
    time.sleep(2)
    print(" \n       Aragorn- Tell me a time when you're not.... Fatty ")
    time.sleep(1)
    print('''\n   " Whom you called Fatty ? "    ''')
    time.sleep(1)
    print("\n        Aragorn- Hahahaha....Okay ....Okay Relax .... was just kidding ")
    time.sleep(2)
    g=input("\n Press any key to give Sam a Sandwich ")
    time.sleep(1)
    print('''\n   "Thanks , Ara' , I love you ... " ''')
    time.sleep(1)
    print("\n        Aragorn- Yeah , Yeah ... Okay !! ")
    time.sleep(2)
    print("\n        Aragorn- Look we got no chill now ! \n \n             We gotta save Froodo and wake him up ")
    time.sleep(1)
    print('''\n        " Alright ! lets Go ! "  ''')
    time.sleep(2)
    m=input(" \n \n        *****PRESS ANY KEY TO CONTINUE***** ")
    time.sleep(3)
    dale()
    
def dale():
    print("\n \n \n                                            >>>>>>RIVENDALE<<<<<<    ")
    time.sleep(3)
    print(''' \n \n \n    Elrond: Hey this is Elrond !! What has happened to him  \n ''')
    time.sleep(2)
    a=input("press any  key to talk to Elrond")
    print('''\n     Aragorn: This is Frodo . The knights of Sauron Attacked him and now he is here    ''')
    time.sleep(2)
    print(''' \n          Elrond: But why ? ''')
    time.sleep(1)
    print("\n       Aragorn: I will  tell that later ...... wake him up first ")
    time.sleep(1)
    print("\n        Elrond: okay !lemme see  ")
    time.sleep(2)
    print("\n        Elrond: This is a severe wound ! ")
    time.sleep(1)
    print("          Elrond:I am Putting a spell on him that will wake him up and he will recover soon ")
    time.sleep(2)
    x=input(" \n \n Press any key to enter spell \n \n ")
    time.sleep(4)
    print(''' \n \n \n \n             AABRA KADABRAAAA OUSAAA OUSAAAA LAVIOUUUUUSSAAAAAAAA \n \n \n ''')
    time.sleep(3)
    print("  *******FRODO WAKES UP********* ")
    wake()
def wake():
    print("         Frodo - Where Am I    \n     ")
    time.sleep(1)
    print("  In Rivendale ..... The knights attacked you and you were infected will  evil poison ")
    time.sleep(2)
    print("         Frodo - Where is the ring ? ")
    ri()
def ri():
    a=input(" \n Press 'R' to check the ring in the pocket ")
    if a.lower()=='r' :
        time.sleep(2)
        chek()
    else:
        print(" Invalid Entry .... ")
        time.sleep(2)
        ri()
def chek():
    b=input("\n \n  Is the ring in the pocket ? ")
    if b.lower()=='yes' or b.lower()=='y':
        print("\n          Frodo- Oh ! Thankgod it is there !! ")
        time.sleep(1)
        gan()
        
    elif b.lower()=='no' or b.lower()=='n':
        time.sleep(2)
        print(" \n \n       Frodo- Where is the ring Aragorn ? ")
        time.sleep(1)
        print('''\n    " Oh the ring .... Here it is mr.Frodo "  ''')
        time.sleep(1)
        gan()
    else:
        print(" Incorrect Entry ..... Retry ")
        chek()
def gan():
    print("\n \n                       *************** A BIRD CAME WITH A LETTER*************** \n \n ")
    time.sleep(1)
    a=input(" Press and key to take the letter :")
    time.sleep(1)
    print("    \n    Frodo- Aragorn , what is written in that  ? ")
    time.sleep(2)
    print(''' \n    Aragorn-This a letter from Gandalf
    Saruman has kidnapped him ...
    He know you are here Frodo.
    He is saying .... ''')
    time.sleep(2)
    with open("import files//letter.txt","r") as o:
        print(o.read())
    any=input(" Press any key to continue.... ")
    print("\n \n     Frodo- Oh Shit !! Now what we do Aragorn? Elrond ? " )
    time.sleep(2)
    print(" \n \n       Elrond- We all will go with you and help you to destroy the ring  ! ")
    time.sleep(1)
    print('''\n          Frodo- No , I will go alone ! \n while I was fainted I saw no one can help me ... ''')
    time.sleep(2)
    print(''' \n Only I can help myself ! No one can ever help me in doing this   ''')
    time.sleep(2)
    print("\n \n        Aragorn- No , We will not leave you alone we will go anywhere where you will go ! \n                The way is far too dangerous and we cannot risk your life ")
    time.sleep(2)
    thi_90()
def thi_90():
    think=input("\n  Do you Agree ? Say yes or no : ")
    if think.lower()=='yes' or think.lower()=='y' :
        print(" \n Good decision Frodo " )
        time.sleep(1)
        print(" \n We have got no time....  we should move. ")
        mov_90()
    elif think.lower()=='no' or think.lower()=='n':
        print(" \n Dont do that Froodo ... You really needs us .. \n  Gandalf also want us to go with  you Mr.frodo ...\n please change your decision or we will not let you go ... \n ")
        thi_90()
    else:
        print(" \n                                >>>>>>Incorrect Entry !! Retry ! <<<<<<<")
        thi_90()
def mov_90():
    time.sleep(2)
    print(" \n      Aragorn - There's a long way to go !! \n Lets start moving ! ")
    time.sleep(1)
    a=input(" Press 'any' key to start moving ")
    dre()
def dre():
    time.sleep(2)
    print(" ******************** MOVE SOUTH TO START MOVING TO GONDOR ********************** ")
    time.sleep(1)
    print("\n \n In which direction to move? \n \n ")
    time.sleep(1)
    choi()
def choi():
    d=input('''
press "n" to move NORTH
press "s" to move SOUTH
press "e" to move EAST
press "w" to move WEST         ''')
    if d.lower()=='n' or d.lower()=='north':
        print("\n  Wrong Direction ... choose the right one \n ")
        choi()
    elif d.lower()=='s' or d.lower()=='south':
        print(" \n ALright , Let's go!! ")
        time.sleep(2)
        gon_70()
    elif d.lower()=='e' or d.lower()=='east':
        print("\n  Wrong Direction ... choose the right one \n")
        choi()
    elif d.lower()=='w' or d.lower()=='west':
        print("\n  Wrong Direction ... choose the right one \n")
        choi()
    else:
        print(" Invalid Entry ..... Retry ! ")
        time.sleep(2)
        choi()
def gon_70():
    a=input(" Press any key  to continue..... ")
    time.sleep(2)
    print("\n         aragorn- Froodo , i need to talk to you in separate ! ")
    time.sleep(1)
    print("   \n             Frodo- What's the matter Aragorn ? ")
    time.sleep(1)
    print("      \n     Aragorn- Do as I say.... It is important !")
    time.sleep(2)
    b=input(" Press RETURN KEY to Listen to Aragorn ")
    time.sleep(1)
    print(''' \n Remember ! Not to give the ring to anyone ....
 Even if you trust him !
 The ring you got has Greed in it !
 it makes the person wear it and then his mind start thinking evil ! ''')
    time.sleep(3)
    print('''\n \n       Frodo- Okay as you say Aragorn  ''')
    c=input("\n  press any key to check the ring :   ")
    rin()
def rin():
    d=input("\n  Is the ring in the  pocket ? ")
    if d.lower()=='yes' or d.lower()=='y' :
        print("\n     >>>>>>>>>Great , now you are good to go.... <<<<<<<<< ")
        time.sleep(2)
        wha()
    elif d.lower()=='no' or d.lower()=='n':
        print(" \n \n WHAT ? find the ring Frodo it must be here somewhere ")
        time.sleep(1)
        rin()
    else:
        print(" \n \n incorrect entry ..... RETRY ")
        rin()
def wha():
    a=input(" \n \n Press any key to continue ")
    time.sleep(2)
    print(" \n \n \n         Sam- Frodo , what's  up ? ")
    time.sleep(1)
    print('\n \n "I feel like the knights the coming ....... I think we should hide again "   ')
    time.sleep(2)
    print("               Sam- Come on , Quick ,This way ... we can hide ")
    time.sleep(1)
    hid()
def hid():
    c=input("\n \n press any key to follow sam ")
    time.sleep(2)
    hide=input('''
press "h" to hide

press "r" to run

press "s" to stay           ''')
    if hide.lower()=='h' :
        time.sleep(2)
        print("\n \n           Aragorn- I guess we will be safe in these bushes ")
        time.sleep(1)
        bush()
    elif hide.lower()=='r' :
        time.sleep(2)
        print ("\n \n              Sam- Froodo .... NOOOOOOOO !!!!! " )
        time.sleep(1)
        print(" \n.\n.\n.\n.\n.\n  ********************YOU ARE KILLED************************ \n \n \n ")
        time.sleep(1)
        kille()
    elif hide.lower()=='s' :
        print ("\n \n              Sam- Froodo .... NOOOOOOOO !!!!! " )
        time.sleep(1)
        print(" \n.\n.\n.\n.\n.\n  ********************YOU ARE KILLED************************ \n \n \n ")
        time.sleep(1)
        kille()
    else :
        print(" Invalid Entry .......RETRY ")
        hid()
def kille():
    a=input('''
Press "c" to continue from check point
press "e" to exit to main menu
''')
    if a.lower()=='c' :
        time.sleep(1)
        print("  \n \n    ************* LOADING **************** \n \n ")
        time.sleep(4)
        wha()
    elif a.lower()=='e':
        print("\n \n            ***********RETURNING TO MAIN MENU*********** \n \n ")
        time.sleep(4)
        menu()
    else:
        print(" Invalid Entry .... RETRY ")
        kille()
def bush():
    print("\n \n             SAM- Shh! Stay quiet .... They are just above us ")
    time.sleep(2)
    a=input('\n        Press "a" Three times in a row to stay quiet \n ')
    if a.lower()=='aaa':
        time.sleep(2)
        print("             Aragorn- Oh Thankgod ...They are gone ")
        get()
    else :
        print( "       SAM- I said Donnot speak ")
        time.sleep(2)
        bush()
def get():
    time.sleep(2)
    print("\n \n       Sam- Yeah that was close ......   ")
    time.sleep(1)
    a=input(" \n   \n \n Press any button to check the ring : ")
    time.sleep(1)
    chck3()
def chck3():
    b=input(" \n Is the ring in the pocket : ")
    if b.lower()=='yes' or b.lower()=='y':
        print(" Great !! Now back to the task ")
        time.sleep(1)
        back1()
    elif b.lower()=='no' or b.lower()=='n':
        print("\n                 aragorn- WHAT? You should have the ring !! Go find it back ")
        chck3()
    else:
        print( " Incorrect Entry ... Retry ")
        time.sleep(1)
        chck3()
def back1():
    time.sleep(2)
    choose= input(" Choose the direction ! The Gondor is towards North ! ")
    if choose.lower()=='n' or choose.lower()=='north':
        print("\n Right path !! ")
        time.sleep(1)
        cont1()
    else :
        print("\n  Wrong Path Entered .... Choose the right one ")
        back1()
def cont1():
    a=input("\n \n  Press any key to continue   ")
    time.sleep(3)
    print( '''\n \n        Aragorn- This is Dunland
          The city of the devil... ''')
    time.sleep(1)
    print(" \n               The evil minded Sauron has closed all the other paths \n               We'veno other option than to cross this place to reach the other side ")
    time.sleep(1)
    print("\n \n             Sam- But I am afraid to go through this place ... \n                 What If something happens to us ")
    time.sleep(1)
    print("\n                 Aragorn- As I told you , we have no other chance ... we must cross through this place or Sauron could reach us .. ")
    time.sleep(1)
    print(" Now Get ready to go through this..... ")
    time.sleep(1)
    print("\n                  Sam- I will ask Frodo and do as he says      ")
    time.sleep(1)
    print( "\n                      Frodo ? What do you say !")
    time.sleep(1)
    think4()
def think4():
    a=input( '''\n Press "y" to go \n
 Press "n" to change the way ''')
    if a.lower()=='y' :
        print("\n               Sam-Okay Frodo... I will Do as you say ")
        time.sleep(1)
        cave()
    elif a.lower()=='n' :
        print("              Aragorn- Frodo there is no other way ....\n             We must go from here ")
        time.sleep(2)
        thi_nk()
    else :
        print("\n     Invalid Entry.... Retry !! ")
        time.sleep(1)
        think4()
def thi_nk():
    b=input('''
 press "c" to change your mind
\n press "e" to quit the game ''')
    if b.lower()=='c':
        print("\n            Aragorn- Great Frodo ! I knew you will agree ")
        time.sleep(1)
        cave()
    elif b.lower()=='e' :
        print(" \n     ****************That was a Coward move ********* ")
        time.sleep(2)
        print("\n \n    ************RETURNING BACK TO MENU************** ")
        time.sleep(1)
        print("\n       ******************LOADING****************** ")
        time.sleep(3)
        menu()
    else:
        print(" Invalid Entry .... Retry !! ")
        time.sleep(1)
        thi_nk()
def cave():
    a=input(" \n \n Press any key to continue  ")
    time.sleep(2)
    print("                 Aragorn- This Cave is one of the deadliest caves in the world ")
    time.sleep(1)
    print("\n                         Remember not to touch anything aur say something loudly or it can wake up the devils living here ")
    time.sleep(2)
    print("\n                         It's better to  stay quiet and stay together ")
    time.sleep(2)
    fir()
def fir():
    b=input("\n  Press 'f' to help Aragorn Light the fire ")
    if b.lower()=='f':
        print("\n     ***** Aragorn lights up the fire *****   ")
        time.sleep(1)
        walk1()
    else :
        print( " Incorrect  Entry ....Retry !!! ")
        time.sleep(1)
        fir()
def walk1():
    print("\n              Sam- This is a bright Place !! " )
    time.sleep(1)
    print(" \n                       Aragorn-Shutup Sam!!!! I told you , to stay low !! ")
    time.sleep(2)
    print("\n              Sam- OHKAAAY !!! OHKAAAY !!! Misterr.....Aragorn ")
    time.sleep(1)
    wal=input("\n \n \n                 ............press any  key to move........         ")
    time.sleep(1)
    print("\n                  Frodo- I wish I have never taken this responsibility ... ")
    time.sleep(1)
    print("\n                       Aragorn- Don't Lose hope Frodo ..... Don't say like that ")
    time.sleep(1)
    print("\n             Frodo- Or what should I say Aragorn ?")
    time.sleep(2)
    print("\n                       Aragorn- Remember Mr.Frodo , You cannot change what is gone, but you can change that has yet to come.... ")
    time.sleep(1)
    print(" \n                                 Be Patient and struggle hard , everything will be fine my dear ")
    time.sleep(1)
    print(" \n       **************************************************************************************************************************************** ")
    c=input("\n \n      Press any key to continue !    ")
    time.sleep(2)
    os.system('cls')
    foot()
def foot():
    print ("                 Sam- Ahhh ! I cannot Move my foot ! Pick me up ")
    time.sleep(1)
    print("\n                        Aragorn- What have you done to yourself Sam lemme pick you up")
    time.sleep(1)
    pich()
def pich():
    pick=input("\n \n  Press 'p' three times to pick sam up :  ")
    if pick.lower()=='ppp':
        print("\n.\n.\n.\n.")
        time.sleep(2)
        print("\n \n                       Aragorn- Ahh! here you go sam ! " )
        figh()
    else :
        print(" \n                   Aragorn- You  are a heavy person Sam ")
        time.sleep(1)
        pich()
def figh():
    time.sleep(2)
    with open("import files//scenario1.txt","r") as o:
        print(o.read())
    time.sleep(2)
    print(" \n \n         Aragorn-Look here they come..... The  devils of the Dunland !!! ")
    time.sleep(1)
    swor_d()
def swor_d():
    a=input("\n \n  Press any key to continue ")
    time.sleep(2)
    choice=input('''\n  >>>>What to do ?
press "f"  to start the fight
press "r"  to run away
press "s" to stay ''')
    if choice.lower()=='f':
        print("\n \n  Loading..... ")
        time.sleep(3)
        fihgt()
    elif choice.lower()=='r' :
        print("\n         RUN RUN RUN RUN     ")
        time.sleep(1)
        print('\n \n  """""""" the skulls are now in front of you .... """"""""" ')
        time.sleep(2)
        phight()
    elif choice.lower()=='s':
        print(''' \n \n """"""""""""""YOu're Dead ...The devils Killed you """""""""""""""" ''')
        time.sleep(2)
        n_ow()
    else :
        print(" Invalid Entry.... Retry ")
        swor_d()
def n_ow():
    now=input( '''
press "c" to continue from checkpoint
press "e" to exit to main menu ''')
    if now.lower()=='c':
        time.sleep(2)
        print(" \n \n Loading....... ")
        figh()
    elif now.lower()=='e':
        print(" \n \n >>>RETURNING TO MAIN MENU<<< \n \n ")
        time.sleep(2)
        menu()
    else:
        print("\n \n  Invalid Command .... Retry ")
        n_ow()
def phight():
    fi=input('''\n \n There is no other way  now .... Fight or die
press "f" to fight
press "d" to die ''')
    if fi.lower()=='f':
        time.sleep(2)
        fihgt()
    elif fi.lower()=='d':
        time.sleep(2)
        print("\n \n     >>>>>You died<<<<< ")
        n_ow()
    else:
        print("\n \n Invalid Entry ... ")
        time.sleep(1)
        phight()
def fihgt():
    a=input(" Press any key to continue :    ")
    time.sleep(2)
    print("\n               >>>>> The Skull Devils are infront of you<<<<< ")
    time.sleep(2)
    dev()
def dev():
        fight=input('''\n \n 
Press "a" two times to swing the sword
press "s" to shield
press "a" and "s" for a Combo ''')
        if fight.lower()=='aa' :
            time.sleep(2)
            print("\n \n  Great Move.... You killed them all")
            nw()
        elif fight.lower()=='s' :
            print(" \n \n Now Press 'aa' to attack ")
            time.sleep(1)
            dev()
        elif fight.lower()=='a' :
            print(" \n \n Now Press 'aa' to attack ")
            time.sleep(1)
            dev()
        elif fight.lower()=='as':
            print("\n \n \n            >>>>>>COMBO ATTACK<<<<<<<      \n \n \n ")
            time.sleep(2)
            print("\n \n What a  power attack \n  Great Move.... You killed them all")
            nw()
        else:
            print(" Invalid Command .... Start again ")
            dev()
def nw():
    print("\n \n              Sam- That was a cool move Aragorn...")
    time.sleep(2)
    print("\n \n          Aragorn-We should move now or more of them will be coming our way ")
    time.sleep(1)
    a=input("\n \n Press any key to continue... ")
    time.sleep(1)
    dirc___1()
def dirc___1():
    print( "\n \n You are Standing in the middle of the Dunland Cave , the Gondor is in the towards the SOUTH ")
    time.sleep(1)
    move=input("\n  Choose the direction to move :  ")
    if move.lower()=='south':
        print("\n  Great !! Lets start moving now ")
        time.sleep(1)
        mov_s()
    elif move.lower()=='north':
        print("\n There is nothing in that direction in a cave ! ")
        time.sleep(1)
        dirc___1()
    elif move.lower()=='east' :
        print("  \n    No Frodo ! we cannot back .... We already  did a lot of suffer ")
        time.sleep(1)
        chang()
    elif move.lower()=='west' :
        print(" \n  There is nothing in that direction in a cave ! ")
        time.sleep(1)
        dirc___1()
    else:
        print(" \n \n Incorrect Entry ....Try again ")
        dirc___1()
 
def mov_s():
    a=input("\n \n  Press any key to continue   ")
    time.sleep(1)
    print(" \n \n     Aragorn- Frodo ! Where is the ring ?")
    reng()
def chang():
    choose=input("\n \n  what do you say ?   Choose Again or Quit ?")
    if choose.lower()=='again' and choose.lower()=='choose' and choose.lower()=='choose again':
          time.sleep(1)
          dirc()
    elif choose.lower()=='quit':
          qu_it()
    else:
          print(" Invalid Entry.....Retry ")
          chang()
def qu_it():
    sure=input(" \n Are you sure , you want to quit ? ")
    if sure.lower()=='yes':
        time.sleep()
        print(" \n      >>>>>>>>>LOADING<<<<<<<<<")
        print(" \n  >>>>>>>Returning to Main Menu<<<<<<<<<")
        time.sleep(3)
        menu()
    elif sure.lower()=='n' :
        chang()
    else:
        print("\n \n  incorrect entry ... Retry ")
        time.sleep(2)
        qu_it()
def reng():
    check=input("\n \n Write Check to check the ring : ")
    if check.lower()=='check':
        print(" \n *****CHECKING***** ")
        time.sleep(2)
        poc()
    else:
        print(" Invalid Entry ... Retry ")
        time.sleep(1)
        reng()
def poc():
    iss=input("\n \n Is the ring in the pocket ? ")
    if iss.lower()=='yes' :
        time.sleep(1)
        print(" \n \n           Aragorn- Great !! Check Regularly , the thing is so precious and we cannot risk it ")
        move_3()
    elif iss.lower()=='no':
        time.sleep(1)
        print("\n \n             Aragorn , You must be kidding Frodo ! Check it again ")
        poc_1()
    else:
        print(" Incorrect Entry..... RETRY ")
        time.sleep(1)
        poc()

def poc_1():
    again=input("\n \n Is the ring in the pocket ? ")
    if again.lower()=='yes' :
        time.sleep(1)
        print(" \n \n           Aragorn- Great !! Check Regularly , the thing is so precious and we cannot risk it ")
        move_1()
    elif again.lower()=='no' :
        time.sleep(1)
        print(''' \n
                           Aragorn- Frodo !! What have you done ? we must find the ring until it is found !
                                    There is no other chance Frodo !! ''')
        time.sleep(2)
        print("\n \n                Frodo- But where will we find the ring Aragorn ?")
        time.sleep(1)
        poc_2()
    else:
        print(" Invalid Command .... RETRY ")
        time.sleep(2)
        poc_1()
def poc_2():
    print("\n \n                Aragorn- Close your eyes and see Frodo ! Come on you tell ")
    time.sleep(2)
    print("\n                        Frodo- Okay let me try that ! ")
    time.sleep(1)
    eye_1()
def eye_1():
    eyes=input("\n  Write 'CLOSE' to close Frodo Eyes !   ")
    if eyes.lower()=='close' :
        print("\n \n            Aragorn- Did you see anything Frodo ? ")
        time.sleep(2)
        print("\n \n                           Frodo - Ahh!!! Not yet ! ")
        time.sleep(1)
        print("\n .\n .\n . \n \. \n .\n .\n .\n .\n . ")
        time.sleep(2)
        print( "\n                    Sam- Come on ! Frodo ! Do something ")
        eye_2()
    else :
        print(" Invalid entry .... Rewrite ")
        eye_1()
def eye_2():
    time.sleep(2)
    print("\n \n                        Frodo- Lemme Focus s'more ")
    time.sleep(1)
    print("\n \n . \n . \n . \n .\n . \n . \n . \n . \n . \n ")
    time.sleep(2)
    print(" \n \n               Frodo- I see..... I see... It is left behind when I was hiding from devils .... ")
    time.sleep(1)
    print("\n                    Aragorn- Shit ! This means we gotta move back again or our purpose to move further is nothing ..... ")
    time.sleep(1)
    print("    \n                          Sam- Mr.Frodo , What have you you done....... now come on let's find the ring again ")
    time.sleep(1)
    back_1()
def back_1():
    print(" \n \n   Write North to move back to where the ring was ")
    time.sleep(2)
    dir=input(" \n  Which direction to move :   ")
    while dir.lower()!='east' and dir.lower()!= 'west' and dir.lower()!= 'north' and dir.lower()!= 'south' :
        print( " \n Invalid Entry.... REWRITE ")
        dir=input(" \n  Which direction to move :   ")
    if dir.lower()=='north':
        time.sleep(1)
        nor_1()
    elif dir.lower()=='south':
        print(" \n       We cannot go further until we find the ring Frodo ! ")
        back_1()
    elif dir.lower()=='east' :
        print(" \n  There is nothing in this direction .... Choose again ")
        time.sleep(1)
        back_1()
    elif dir.lower()=='west' :
        print("\n  There is nothing in this direction .... Choose again ")
        back_1()
        
def nor_1():
    print( " \n           Aragorn- Come on lets find the ring now... ")
    time.sleep(2)
    print(" \n                     And stay quiet this time .... be aware of every possible condition ")
    time.sleep(1)
    find_ring()
def find_ring():
    find=input("\n    Write 'find' to start finding the ring ! ")
    time.sleep(1)
    while find.lower()!= 'find' :
        print(" Wrong Entry ! Rewrite ")
        time.sleep(1)
        find=input("\n    Write 'find' to start finding the ring ! ")
    if find.lower()=='find' :
        print(" \n \n              Sam- Did you see the ring somewhere ? ")
        did()
def did():
    time.sleep(1)
    find=input(" Did you Find the Ring :  ")
    while find.lower()!= 'yes' and find.lower()!='no' :
        print(" Wrong Enrty .... Retry ! ")
        time.sleep(1)
        find=input(" Did you Find the Ring :  ")
    if find.lower()== 'yes' :
        print( "\n                        Aragorn- Ahh ! thankgod , you silly fool ! ")
        time.sleep(1)
        print("\n                         Sam-    We would have been in a deep trouble if we have didn't founded it ")
        time.sleep(1)
        next_3()
    elif find.lower()== 'no' :
        print("\n \n                      Aragorn-Alright ! Keep Finding until It is finally found you silly took ")
        time.sleep(1)
        print("\n . \n . \n . \n .\n . \n . \n . \n . \n . \n ")
        time.sleep(3)
        did()
def next_3():
    print("\n \n                          Aragorn- Now Lets get back to the way ... there is alot more to go ")
    time.sleep(1)
    direct=input("\n \n    Please input the direction to move in ")
    while direct.lower()!= 'north' and direct.lower()!='east' and direct.lower()!= 'south' and direct.lower()!='west' :
        print(" \n Invalid Entry .... Rewrite !! ")
        time.sleep(1)
        direct=input("\n \n    Please input the direction to move in ")
    if direct.lower()=='south' :
        time.sleep(2)
        print(" \n                LETS GO          ")
        move_3()
    elif direct.lower()=='east':
        time.sleep(1)
        print(" There is nothing in this direction in a cave ")
        time.sleep(1)
        next_3()
    elif direct.lower()=='west' :
        time.sleep(1)
        print(" \n There is nothing in this direction in a dunland cave ")
        time.sleep(1)
        next_3()
    elif direct.lower()=='north' :
        print("                    Aragorn-  We have to move further frodo ! Towards South ")
        time.sleep(1)
        next_3()
        
def move_3():
    print(" \n             >>>>>>> Dunland Cave <<<<<<<")
    time.sleep(3)
    print("            >>>>> Three ways to go from here<<<<< ")
    time.sleep(1)
    print("\n \n                 Sam- Now which side to go Aragorn ? ")
    time.sleep(2)
    print(" \n            Aragorn- I don't remember Sam !! no idea ")
    time.sleep(1)
    print("\n \n              Frodo-i don't know ..... Let me think ")
    time.sleep(1)
    print("\n . \n . \n . \n .\n . \n . \n . \n . \n ")
    time.sleep(1)
    think=input("\n  write 'think' to let Frodo think : ")
    while think.lower()!='think' :
        print("\n Wrong Entry ... retry ")
        time.sleep(1)
        think=input(" write 'think' to let Frodo think : ")
    if think.lower()== 'think':
        time.sleep(1)
        print(" \n . \n . \n . \n .\n .")
        time.sleep(3)
        print(" \n                Frodo- I have come up with a plan ")
        time.sleep(1)
        print(" \n                    sam- What is that Frodo ")
        time.sleep(1)
        print("                   Frodo- let's do ENEE MINIIII MYNI MO and the way that comes , we will follow that ")
        time.sleep(2)
        print("\n                          Aragorn- and what if we get to the wrong path. Then ? ")
        time.sleep(1)
        print("\n                   Frodo- There is not any other way too Aragorn ")
        time.sleep(1)
        print("                            Or let me know if there is ? ")
        time.sleep(2)
        print(" \n                           Aragorn- ALright ! as you say..... Mr.Frodo !")
        luck_1()
def luck_1():
    num=random.randint(1,3)
    c=input(" Write 'start' to start the guesser spell ")
    while c.lower()!='start' :
        print(" Wrong entry... rewrite ")
        time.sleep(1)
        c=input(" Write 'start' to start the guesser spell ")
    if c.lower()=='start' :
        time.sleep(1)
        print("\n \n                 Frodo- Einee Mineee Myniiii Mo ......... ")
        time.sleep(3)
        print("way",num)
        time.sleep(1)
        print("                      Frodo- way",num, "   yes... Let's move to this way ")
        time.sleep(1)
        print(" \n \n                     Sam- Oh God ... please save me ")
        time.sleep(1)
        print("\n                 Aragorn- Okay ! Let's start moving to this way then ")
        wai=int(input('''\n 
Press "1" to move through way 1
press "2" to move through way 2
press "3" to move through way 3 '''))
    c==num
    while wai!=num :
        print(" wrong one ")
        wai=int(input('''\n 
Press "1" to move through way 1
press "2" to move through way 2
press "3" to move through way 3 '''))
    
    if wai==num :
        print("\n \n \n               Frodo- Quick, let's be quick this time ")
        time.sleep(2)
        dun_1()
def dun_1():
    print(" \n \n \n                     Sam- Look I can see the light from outside... ")
    time.sleep(1)
    print(" \n \n                        Sam- Quick this way !!!! ")
    fol=input('''\n \n
Write 'follow' to start following Sam
Write 'unfollow' to not follow sam ''')
    if fol=='follow' :
        print("\n \n              ****** Following Sam ****** ")
        time.sleep(3)
        fol_sam()
    elif fol=='unfollow' :
        print("\n \n           Sam- No Frodo, this way... or you will  get lost..... ")
        time.sleep(2)
        dun_1()
    else:
        print(" Invalind entry.... Retype")
        dun_1()
def fol_sam():
    print("\n \n                 Aragorn- Ahh ! Finally .... We got out if this hell cave ")
    time.sleep(1)
    print("\n \n \n            Sam- Look ! Frodo ...  we went out of it finally ")
    time.sleep(1)
    print("\n \n \n                  Frodo- Yeeaaah !! Haha ... Finally ")
    time.sleep(1)
    c=input(" Press any key to continue.... ")
    time.sleep(1)
    isen()
def isen():
    print("\n \n                 Aragorn- We are at the isengard now..... lets move fast now towards Gondor ")
    time.sleep(2)
    isen45()
def isen45()  :
    print(" \n \n \n                >>>>THE GONDOR IS TOWARDS SOUTH-EAST<<<< \n \n \n ")
    time.sleep(1)
    dir=input("   Choose the direction to move :    ")
    if dir.lower()=='south-east' or dir.lower()=='south east':
        time.sleep(2)
        walk()
    else :
        print(" Wrong entry ... RETRY ")
        isen45()
def walk():
    move=input('''
Write 'run' to go  running
write 'walk' to go walking
write 'stay' to stay at the place ''')
    while move.lower()!='run' and move.lower()!='walk' and move.lower()!='stay' :
        print(" \n \n Wrong entry ")
        time.sleep(2)
        move=input('''
Write 'run' to go  running
write 'walk' to go walking
write 'stay' to stay at the place ''')
    if move.lower()=='run' :
        print("\n \n                  Aragorn-Running will make you more weak... you have'nt eaten anything ")
        time.sleep(1)
        sure_1()
    elif move.lower()=='walk':
        print(" \n \n                    Aragorn-Good to go Froodo...lets go ")
        time.sleep(1)
        eaty()
    elif move.lower()=='stay' :
        print("\n \n                          Aragorn- If you wish to stay then .... ! ")
        time.sleep(2)
        eaty()
def sure_1():
    sure=input("\n   Are you sure ? You want to go by running ")
    while sure.lower()!='yes' and sure.lower()!='no' :
        print(" \n Write Correct Entry ... ")
        time.sleep(1)
        sure=input("\n   Are you sure ? You want to go by running ")
    if sure.lower()=='yes' :
        eaty()
    elif sure.lower()=='no' :
        print(" \n   >>>>>>Choose what to do then<<< \n \n ")
        walk()
def eaty():
    time.sleep(1)
    print("\n \n                  Aragorn- Okay , Lets eat something then first ")
    eat=input( " \n \n Would youlike to eat ? ")
    time.sleep(2)
    while eat.lower()!='yes' and eat.lower()!='no':
        print("\n  Incorrect Command ")
        time.sleep(1)
        eat=input( " \n \n Would youlike to eat ? ")
    if eat.lower()=='yes':
        print("\n \n            Aragorn- Here you go Frodo... ")
        time.sleep(1)
        print("\n                        A bite from it and your stomach will be full ")
        hand()
    elif  eat.lower()=='no':
        print(" \n \n              Aragorn- There is still a long way to go... Eat something please ")
        time.sleep(1)
        print("\n                            Here, take this ")
        hand()
def hand():
    take=input(" Press 'take' to take the sandwich from Aragorn ?")
    while take.lower()!='take' :
        print(" \n Wrong Entry... retype ")
        time.sleep(1)
        take=input(" Press 'take' to take the sandwich from Aragorn ?")
    if  take.lower()=='take' :
        print("\n                    Frodo- Yess! thats my boy !! ")
        a=input("\n \n  Press any key to get done with eating ")
        chck_5()
def chck_5():
    time.sleep(2)
    check=input("\n \n Check the ring ... is it in the pocket ?")
    while check.lower()!='yes' and check.lower()!='no':
        print("Wrong Entry....retype ")
        time.sleep(2)
        check=input("\n \n Check the ring ... is it in the pocket ?")
    if check.lower()=='yes' :
        print("\n \n            Great.....Let's start moving then ")
        time.sleep(1)
        moving()
    elif check.lower()=='no':
        print("\n \n           Aragorn- What do you mean Frodo ? Check again ")
        chck_5()
def moving():
    print("\n \n  Write move to start moving....   ")
    move=input(" What to do now ? ")
    if move.lower()=='move':
        print("\n \n  Okay let's go.... ")
        gondor__1()
    else :
        print("\n \n  Wrong Entry.... RETRY   ")
        time.sleep(1)
        moving()
def gondor__1():
    print(" \n.\n.\n.\n.\n.\n.\n.\n.\n. ")
    time.sleep(3)
    print("\n            Sam- Look Frodo , we finally reached GONDOR ")
    time.sleep(1)
    print("                   Aragorn- Gandalf is in the Gondor... we must meet him first ")
    time.sleep(1)
    print("\n \n                   Frodo- But where will he be  in this big place ? ")
    time.sleep(2)
    print(" \n                Aragorn- I know a place Frodo where he could be.....")
    time.sleep(1)
    print(" \n                          Come on, follow me ")
    time.sleep(2)
    fol=input("\n \n  write follow to Follow Aragorn to Gandalf ")
    time.sleep(1)
    while fol.lower()!='follow':
        print(" Wrong Input ... Retry ")
        fol=input("\n \n  write follow to Follow Aragorn to Gandalf ")
    if fol.lower()=='follow':
        time.sleep(1)
        but()
def but():
    print("\n                   Frodo-But where are we going Aragorn ! ")
    time.sleep(1)
    print("\n                 Aragorn- well, it is not in Gongor.... but Helms deep , near MORDOR")
    time.sleep(2)
    print(" \n                  Frodo-And how do you know he will be there .... ")
    time.sleep(1)
    print("                   Aragorn-Because he must be there to seek help to Boromir to fight Sauron ")
    time.sleep(2)
    print("                           He has created warriors that cannot be defeated easily thus he must be with Boromir ")
    time.sleep(1)
    print("\n                          A good friend of him......indeed ")
    time.sleep(1)
    print("\n                      Frodo- Okay if you say  so ... ")
    time.sleep(2)
    print("  \n                       Sam-lets go then... ")
    time.sleep(1)
    print("\n                      Frodo- Yeah,  lets  go !!! ")
    time.sleep(3)
    c=input("\n \n          Press any key to continue ")
    time.sleep(1)
    helms_d()
def helms_d():
    print("\n \n \n                >>>>>>>HELMS DEEP<<<<<<< ")
    time.sleep(3)
    met=input("\n Write 'meet' to go to Gandalf :   ")    
    while met.lower()!='meet' :
        print("\n \n  Wrong Entry !! ")
        met=input("\n Write 'meet' to go to Gandalf :   ")
    if met.lower()=='meet':
        time.sleep(2)
        print(" \n \n             Gandalf- Frodo !! Where were you left ")
        time.sleep(1)
        print(" \n \n                     Frodo- Gandalf ,  there were lot of hardships in our way... where do I start from ")
        time.sleep(1)
        print("\n                         Frodo- And where were you ? when I came to riverdale ")
        time.sleep(1)
        print("\n \n              Gandalf- Sauron had kidnapped me...")
        time.sleep(1)
        print(" \n                Gandalf- I escaped him then came here to Boromir ")
        time.sleep(2)
        print("\n                         Frodo-  Now what we have to do ........ and where to go ")
        time.sleep(2)
        print("\n               Gandalf- The Orcs of Sauron are reaching to get the ring and conquer it ")
        time.sleep(1)
        print("\n               Gandalf- I am asking every person to make war and stop him")
        time.sleep(1)
        print("\n                          Frodo- What if he reach us and get the ring ?" )
        time.sleep(1)
        print(" \n              Gandalf- Exactly Frodo ! You gotta move towards Mordor !!")
        time.sleep(1)
        print("\n \n                             Frodo- But where in mordor ? What if he reaches us  ?")
        time.sleep(1)
        print(" \n                Gandalf- Exactly ! Before him , you have to destroy the ring ")
        time.sleep(1)
        print(" \n                         You and Sam will go there ! ")
        time.sleep(1)
        print(" \n                               Frodo- Me and Sam ? What about Aragorn ")
        time.sleep(1)
        print("\n \n                  Gandalf- He will stay with me for the war ")
        time.sleep(1)
        print("\n                      Gandalf-Don't worry Frodo .... Everything will  be fine ")
        time.sleep(1)
        print("\n                                Frodo- Ummm.... Okay Gandalf is you say so ")
        time.sleep(1)
        mor()
def mor():
    c=input("\n       Press any key to continue :  ")
    time.sleep(1)
    print("         Sam- Let's Go  Frodo then...until it's too late")
    time.sleep(1)
    move=input("\n  Write 'go' to make them go ")
    while move.lower()!='go' :
        print("\n \n Incorrect entry...Rewrite")
        time.sleep(1)
        move=input("\n  Write 'go' to make them go ")
    if move.lower()=='go' :
        print("\n \n           Frodo- Let's Go sam ")
        direct_5()
def direct_5():
    print("\n \n                >>>>MORDOR IS TOWARDS SOUTH<<<< \n ")
    time.sleep(2)
    choose=input(''' \n Choose the direction to move : ''')
    while choose.lower()!='north' and choose.lower()!='south' and choose.lower()!='east' and choose.lower()!='west' :
        print("\n  Invalid Entry....Rewrite ")
        time.sleep(1)
        choose=input(''' \n Choose the direction to move : ''')
    if choose.lower()=='south' :
        southee()
    elif choose.lower()=='north' :
        print(" \n \n              Sam- We have to move forward not backward.... ")
        time.sleep(1)
        direct_5()
    elif choose.lower()=='east' :
        print(" \n \n               Sam- No , towards North Frodo... the Mordor is towards North ")
        time.sleep(1)
        direct_5()
    elif choose.lower()=='west':
        print(" \n \n            Sam- No, towards North Frodo.... the Mordor is towards North ")
        direct_5()
def southee():
    mov=input(" \n  write 'move' to start moving  ")
    if mov.lower()=='move' :
        toward()
    else :
        print(" Wrong Entry.....rewrite")
        time.sleep(1)
        southee()
def toward():
    time.sleep(1)
    print("\n \n                       >>>>MORDOR<<<< ")
    time.sleep(4)
    with open("import files//doom.txt","r") as o:
        print(o.read())
    climbo()
def climbo():
    c=input(" Press Any key to continue ")
    clim=input(" \n \n  Write 'climb' to let Frodo start climbing ")
    while clim.lower()!='climb' :
        print("\n \n Wrong Entry.... REWRITE ")
        clim=input(" \n \n  Write 'climb' to let Frodo start climbing ")
    if 'climb' in clim :
        check_6()
def check_6():
    time.sleep(2)
    print("\n          Sam- Frodo, is the ring in the pocket ?")
    time.sleep(1)
    chek=input(" write 'check' to check the ring :  ")
    while chek.lower()!='check' :
        print(" Wrong Entry.... Retry ")
        time.sleep(1)
        chek=input(" write 'check' to check the ring :  ")
    if  'check' in chek.lower() :
        pocket()
def pocket():
    ring=input(" \n \n Is the ring in the pocket ?")
    while ring.lower()!='yes' and ring.lower()!='no':
        print("\n Wrong Entry... REWRITE ")
        time.sleep(1)
        ring=input(" \n \n Is the ring in the pocket ?")
    if 'yes' in ring.lower() :
        print(" \n        Cool , We are Good to go then ")
        cont_6()
    elif 'no' in ring.lower() :
        print("\n \n            Sam- Where is the ring then Frodo ")
        doubt()
def doubt():
    print("\n               Frodo- I don't know... I haven't checked it since I slept ")
    time.sleep(1)
    print(" \n                  Sam-  Here it is Frodo......haha ")
    time.sleep(1)
    print("\n                Frodo- Why did you took it Sam ?")
    time.sleep(1)
    print("\n                   Sam- Haha...nothing....I was just pranking you...Mr.Frodo ")
    time.sleep(1)
    print("\n                Frodo- That  wasn't Funny... Sam ")
    a=input("\n \n  Press any  key  to continue !! ")
    cont_6()
def cont_6():
    time.sleep(1)
    upar=input(" Write 'up'  to start Frodo moving up the mountain ")
    if 'up' in upar.lower():
        print("\n . \n .  \n . \n . \n . \n . \n . \n . \n . \n .\n ")
        time.sleep(3)
        top()
    else:
        print("\n Wrong entry...retry ")
        cont_6()
def top():
    print(" \n \n       >>>>>>>>>>>YOU ARE ON THE TOP OF THE MOUNTAIN<<<<<<<<<<<< ")
    time.sleep(2)
    print("\n \n               Frodo- Finally we are to the end of the mission " )
    time.sleep(1)
    print(" \n \n        Sam- Yes Frodo.... Finally we are ")
    time.sleep(1)
    print("\n                  Frodo- Let's throw the ring in the Fire.......  ")
    time.sleep(1)
    print("  \n \n                    So to end Sauron completely ")
    wait_3()
def wait_3():
    out=input("\n Take out the ring  ? ")
    while out.lower()!='take out' :
        print("\n Wrong Entry.... ")
        time.sleep(1)
        print("\n Write 'Take out' to take the ring out ")
        out=input("\ Take out the ring  ? ")
    if 'take out' in out.lower():
        print("\n        Frodo- Oh ! look , the last glimpse of the ring ")
        time.sleep(1)
        print("                 My precious ")
        greed()
def greed():
    time.sleep(2)
    print("                 Sam- Frodo, can I see the ring for the last time ")
    time.sleep(1)
    print("\n            Frodo- No Sam, the ring makes the person greedy ... ")
    time.sleep(1)
    print("                     I don't want you to be greedy at the  very last time of the ring ")
    time.sleep(1)
    print("\n               Sam- Don't you trust me Frodo ? ")
    time.sleep(1)
    print("\n            Frodo- No Sam ! ")
    time.sleep(1)
    print("\n                 Sam- Don't say like that.... come on , give me the ring ")
    time.sleep(1)
    print("\n \n               *****SAM TRIES TO REACH TOWARDS THE RING*****")
    time.sleep(2)
    push=input("\n Write 'push' to push Sam away ")
    while push.lower()!='push' :
        print(" Incorrect Entry... Rewrite ")
        time.sleep(1)
        push=input("\n Write 'push' to push Sam away ")
    if 'push' in push.lower() :
        print("         Frodo- Sam ! don't !! stay away from it ")
        fall()
def fall():
    print("\n \n           Sam - Frodo why are you pushing me ")
    time.sleep(1)
    print(" \n          Frodo- This ring is my precious ")
    time.sleep(1)
    print("\n              Sam- throw it in... ")
    time.sleep(1)
    print("\n           Frodo- No I won't ")
    time.sleep(1)
    print("\n \n         ******Sam snatches the ring****** ")
    time.sleep(2)
    print("\n \n           Sam- Haaah !! Finally ....  ")
    time.sleep(1)
    print("                     Let  me wear it ... ")
    time.sleep(1)
    print("\n \n         Frodo- Sam ,No ! Throw it !! ")
    time.sleep(2)
    print("\n \n            ******** Push Sam into the FIRE ********* ") 
    time.sleep(1)
    pus=input("write 'push' to push Sam in the Fire : ")
    while pus.lower()!='push' :
        print(" Wrong Entry ....Retype..... ")
        time.sleep(1)
        pus=input("write 'push' to push Sam in the Fire : ")
    if 'push' in pus.lower():
        print("\n \n         Sam- Frodo, what are you doing !! ")
        time.sleep(2)
        print(" \n \n               Frodo- I am doing what you deserve along with this ring ")
        time.sleep(1)
        print("\n            Sam- You cannot do that to me ! ")
        print("\n \n                 Frodo-  well this time...I will ")
        samdie()
def samdie():
    print("\n \n                      Frodo- Bye Bye .....Sam....and .... the Ring ")
    time.sleep(2)
    print(" \n  \n \n \n \n          Sam- Nooooooooooooooooooo ......... ")
    time.sleep(3)
    print(" \n \n \n              ******Sam Dies and the ring of Sauron got destroyed****** ")
    time.sleep(1)
    with open("import files//end.txt","r") as o:
        print(o.read())
        time.sleep(4)
        ended()
def ended():
    end=input("\n \n  Press any key to return to main menu ")
    time.sleep(2)
    print("\n  \n      Loading.......... \n \n")
    time.sleep(3)
    menu()
        
menu()
