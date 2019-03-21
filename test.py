exit = False
points=0
name= (raw_input("What is your name? "))
welcome =  (raw_input("Welcome to the Spanish Quiz: Level 1, " +name+ "!"))

hello = (raw_input("How do you say 'Hello' in Spanish?: "))
if hello == "hola":
    points=(points)+1
    print "Correct!"
    print "you have " +str(points)+ " points so far"
elif hello == "Hola":
      points=(points)+1
      print "Correct!"
      print "you have " +str(points)+ " points so far"
else:
    print "Incorrect - the answer is Hola"
    print "you have " +str(points)+ " points so far"



howareyou = (raw_input("How do you say 'How are you' in Spanish?: "))
if howareyou == "como estas":
    points=(points)+1
    print "Correct"
    print "you have " +str(points)+ " points so far"
elif howareyou == "Como estas":
      points=(points)+1
      print "Correct!"
      print "you have " +str(points)+ " points so far"
elif howareyou == "Como Estas":
      points=(points)+1
      print "Correct!"
      print "you have " +str(points)+ " points so far"
elif howareyou == "Como estas?":
      points=(points)+1
      print "Correct!"
      print "you have " +str(points)+ " points so far"
else:
    print "Incorrect - the answer is como estas"
    print "you have " +str(points)+ " points so far"


yourname = (raw_input("How do you say 'What is your name' in Spanish?: "))
if yourname == "como te llamas":
    points=(points)+1
    print "Correct"
    print "you have " +str(points)+ " points so far"
elif yourname == "Como te llamas":
      points=(points)+1
      print "Correct!"
      print "you have " +str(points)+ " points so far"
else:
    print "Incorrect - the correct answer is Como te llamas"
    print "you have " +str(points)+ " points so far"




mynameis = (raw_input("How do you say 'My name is' in Spanish?: "))
if mynameis == "me llamo":
    points=(points)+1
    print "Correct"
    print "you have " +str(points)+ " points so far"
elif mynameis == "Me llamo":
      points=(points)+1
      print "Correct!"
      print "you have " +str(points)+ " points so far"
elif mynameis == "Me Llamo":
      points=(points)+1
      print "Correct!"
      print "you have " +str(points)+ " points so far"
else:
    print "Incorrect - the correct answer is me llamo"
    print "you have " +str(points)+ " points so far"


nicetomeetyou = (raw_input("How do you say 'Nice to meet you' in Spanish?: "))
if nicetomeetyou == "mucho gusto":
    points=(points)+1
    print "Correct"
    print "you have " +str(points)+ " points so far"
elif nicetomeetyou == "Mucho gusto":
      points=(points)+1
      print "Correct!"
      print "you have " +str(points)+ " points so far"
elif nicetomeetyou == "Mucho Gusto":
      points=(points)+1
      print "Correct!"
      print "you have " +str(points)+ " points so far"
else:
    print "Incorrect - the answer is mucho gusto"
    print "you have " +str(points)+ " points so far"


doingwell = (raw_input("How do you say 'I'm doing well' in Spanish?: "))
if doingwell == "yo estoy bien":
    points=(points)+1
    print "Correct"
    print "you have " +str(points)+ " points so far"
elif doingwell == "estoy bien":
      points=(points)+1
      print "Correct!"
      print "you have " +str(points)+ " points so far"
elif doingwell == "Estoy bien":
      points=(points)+1
      print "Correct!"
      print "you have " +str(points)+ " points so far"
elif doingwell == "Yo estoy bien":
      points=(points)+1
      print "Correct!"
      print "you have " +str(points)+ " points so far"
else:
    print "Incorrect - the answer is Estoy bien"
    print "you have " +str(points)+ " points so far"


notdoingwell = (raw_input("How do you say 'I'm not doing well' in Spanish?: "))
if doingwell == "yo estoy mal":
    points=(points)+1
    print "Correct"
    print "you have " +str(points)+ " points so far"
elif notdoingwell == "estoy mal":
      points=(points)+1
      print "Correct!"
      print "you have " +str(points)+ " points so far"
elif notdoingwell == "Estoy mal":
      points=(points)+1
      print "Correct!"
      print "you have " +str(points)+ " points so far"
elif notdoingwell == "Yo estoy mal":
      points=(points)+1
      print "Correct!"
      print "you have " +str(points)+ " points so far"
elif notdoingwell == "No estoy bien":
      points=(points)+1
      print "Correct! But in the curriculum it is Estoy mal"
      print "you have " +str(points)+ " points so far"
elif notdoingwell == "no estoy bien":
      points=(points)+1
      print "Correct! But in the curriculum it is Estoy mal"
      print "you have " +str(points)+ " points so far"
else:
    print "Incorrect - the answer is Estoy mal"
    print "you have " +str(points)+ " points so far"



thankyou = (raw_input("How do you say 'Thank you' in Spanish?: "))
if thankyou == "gracias":
    points=(points)+1
    print "Correct"
    print "you have " +str(points)+ " points so far"
elif thankyou == "Gracias":
      points=(points)+1
      print "Correct!"
      print "you have " +str(points)+ " points so far"
else:
    print "Incorrect - the answer is gracias"
    print "you have " +str(points)+ " points so far"


seeyoulater = (raw_input("How do you say 'See you later' in Spanish?: "))
if seeyoulater == "hasta luego":
    points=(points)+1
    print "Correct"
    print "you have " +str(points)+ " points so far"
elif seeyoulater == "Hasta luego":
      points=(points)+1
      print "Correct!"
      print "you have " +str(points)+ " points so far"
else:
    print "Incorrect - the answer is Hasta luego"
    print "you have " +str(points)+ " points so far"


goodbye = (raw_input("How do you say 'Goodbye' in Spanish?: "))
if goodbye == "Adios":
    points=(points)+1
    print "Correct"
    print "you have " +str(points)+ " points so far"
elif goodbye == "adios":
      points=(points)+1
      print "Correct!"
      print "you have " +str(points)+ " points so far"
else:
    print "Incorrect - the answer is Adios"
    print "you have " +str(points)+ " points so far"


congrats =  (raw_input("Congratulations, " +name+ " , you have completed level one with a score of " + str(points) + " points!"))
level2 = (raw_input("Are you ready for Level 2? (Y for yes, N for no)"))
if level2 == "N":
        exit = True
elif level2 == "n":
        exit = True


seeyoulater = (raw_input("How do you say 'See you later' in Spanish?: "))
if seeyoulater == "hasta luego":
    points=(points)+1
    print "Correct"
    print "you have " +str(points)+ " points so far"
elif seeyoulater == "Hasta luego":
      points=(points)+1
      print "Correct!"
      print "you have " +str(points)+ " points so far"
else:
    print "Incorrect - the answer is Hasta luego"
    print "you have " +str(points)+ " points so far"


goodbye = (raw_input("How do you say 'Goodbye' in Spanish?: "))
if goodbye == "Adios":
    points=(points)+1
    print "Correct"
    print "you have " +str(points)+ " points so far"
elif goodbye == "adios":
      points=(points)+1
      print "Correct!"
      print "you have " +str(points)+ " points so far"
else:
    print "Incorrect - the answer is Adios"
    print "you have " +str(points)+ " points so far"
