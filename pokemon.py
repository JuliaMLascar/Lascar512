#A WILD ZUBAT APPEARS 
# vim: set fileencoding=utf-8 :
from random import randint

end = 0
HP_zubat= 10
HP_me = 20   
capture =0
escaping = 0
        

def attacks(hp,n):
    HP = hp - n
    return HP

print( "First, let's choose your starter.")
print( "1 — Bulbasaur, the grass type.\n2 — Squirtle, the water type.\n3 — Charmander, the fire type.")

starter = input("> ")
    
if starter == "1": 
    starter_name = "Bulbasaur"
        
elif starter =="2" :
    starter_name = "Squirtle"
        
elif starter == "3":
    starter_name = "Charmander"
        
else:
    end = 1
    print( "This pokemon isn't an option!") 
if end == 0 :
    print( "A wild zubat appears! %s, go!" %starter_name )
    
if end == 0:
    while HP_zubat > 0 and HP_me > 0 and capture==0 and escaping == 0:
        print( "What will you do?")
        print( "1 — Attack.\n2 — Switch Pokemon.\n3 — Look through your bag.\n4 — Run.")
        choice = input("> ")  
        
        if choice == "1":
            
            if starter == "1": 
                print( "Which attack to use?")
                print( "1. Tackle \n2. Growl \n3. Vine Whip ")
                
                attack = input("> ")
            
                if attack == "1":
                    print( "Bulbasaur uses tackle. It's effective.") 
                    HP_zubat=attacks(HP_zubat,5)
                    print( "The Zubat uses tackle.")
                    HP_me=attacks(HP_me,5)
                    
                elif attack == "2":
                    print( "Bulbasaur growls. He looks intimidating as hell.")
                    print( "The Zubat uses tackle.")
                    HP_me=attacks(HP_me,5)
                    
                elif attack == "3":
                    print( "Bulbasaur uses vine whip. It's not very effective...")
                    HP_zubat=attacks(HP_zubat,2) 
                    print( "The Zubat uses tackle.")
                    HP_me=attacks(HP_me,5)
                    
            elif starter =="2" :
                print( "Which attack to use?")
                print( "1. Tackle \n2. Tail Whip \n3. Water Gun ")
                attack = input("> ")
            
                if attack == "1":
                    print( "Squirtle uses tackle. It's effective.")
                    HP_zubat=attacks(HP_zubat,5)
                    print( "The Zubat uses tackle.")
                    HP_me=attacks(HP_me,5)
                
                elif attack == "2":
                    print( "Squirtle whips his tail. He's looking adorable.") 
                    print( "The Zubat uses tackle.")
                    HP_me=attacks(HP_me,5)
                    
                elif attack == "3":
                    print( "Squirtle uses water gun. Nice shot!")
                    HP_zubat=attacks(HP_zubat,10)
                
                
            elif starter == "3":
                print( "Which attack to use?")
                print( "1. Scratch \n2. Growl \n3. Ember ") 
                attack = input("> ")
            
                if attack == "1":
                    print( "Charmender uses scratch. It's effective.") 
                    HP_zubat=attacks(HP_zubat,5)
                    print( "The Zubat uses tackle.")
                    HP_me=attacks(HP_me,5)
                
                elif attack == "2":
                    print( "Charmender growls. He looks intimidating as hell.") 
                    print( "The Zubat uses tackle.")
                    HP_me=attacks(HP_me,5)
                    
                elif attack == "3":
                    print( "Charmender uses ember. Nice shot!")
                    HP_zubat=attacks(HP_zubat,10)
                
        elif choice == "2":
            
            print( "You haven't captured any other pokemons yet!") 
            print( "The Zubat uses tackle.")
            HP_me=attacks(HP_me,5)
            
        elif choice == "3":
            print( "You have an old kinder bueno and a pokeball.\n1. Eat the bueno.\n2. Throw the pokeball.")
            choice_bag = input("> ") 
        
            if choice_bag == "1": 
                print( "It's a bit stale, but worth it.")
                print( "The Zubat uses tackle.")
                attacks(HP_me,5)
                
            elif choice_bag == "2":
                print( "You throw the pokeball.") 
                
                if HP_zubat > 6:
                    print( "You've failed the capture.") 
                    
                else:
                    print( "Congrats! You've captured the zubat! Make sure to train it well...")
                    capture = 1
        elif choice == "4":
            chance = randint(0, 9)
            if chance > 5:
                print( "Escaping failed.") 
                print( "The Zubat uses tackle.")
                HP_me=attacks(HP_me,5)
                print( "Your health is ", HP_me)
            elif chance < 6:
                print( "You've run away. You're definitely not a gryffindor, but then again, courage is overrated, right?")
                escaping = 1
        else:
            print( "Not an option!") 

else: 
    print( "Game over!")         

if HP_me <= 0:
    print( "Your pokemon fainted. Did you seriously just lose against a Zubat?? Game over!")   
elif HP_zubat <= 0: 
    print( "The zubat fainted. You can be very proud of defeating this worthy opponent.") 
      



