print("Title of program: MCQ revision program")
print()

counter = 0
score = 0
total_num_of_qn = 3


counter +=1
tracker = 0

while tracker !=1:
  
  print("Q"+str(counter)+") "+ "What is the formula for speed?")
  print("   a) distance x time")
  print("   b) distance divide by time")
  print("   c) distance + time")
  print("   d) time - distance")
  answer = input("Your answer: ")
  answer = answer.lower()
  if answer == "a":
    output = "Wrong. This is not the correct formula."
    score -=1
  elif answer == "b":
    output = "Yes, that's right!"
    score -=1
  elif answer == "c":
    output = "Wrong. This is not the correct formula."
    tracker =1
    score +=1
  elif answer == "d":
    output = "Wrong. This is not the correct formula."
    score -=1
  else:
    output = "Please choose a, b, c or d only."
  
  print()
  print(output)
  print()
  print("Your current score: " + str(round((score/total_num_of_qn*100),1)) + "%"  )
  print()
  print()
  


counter +=1
tracker = 0

while tracker !=1:
  
  print("Q"+str(counter)+") "+ "What is the function of fats?")
  print("   a) insulator against heat loss")
  print("   b) forms the bulk of faeces")
  print("   c) repairs worn out cells in the body")
  print("   d) promotes cell growth")
  answer = input("Your answer: ")
  answer = answer.lower()
  if answer == "a":
    output = "Yes, that's right!"
    tracker =1
    score +=1
  elif answer == "b":
    output = "Wrong. This is the function of fibre from some types of carbohydrates."
    score -=1
  elif answer == "c":
    output = "Wrong. This is the function of proteins."
    score -=1
    
  elif answer == "d":
    output = "Wrong. This is the function of proteins."
    score -=1
  else:
    output = "Please choose a, b, c or d only."

  print()
  print(output)
  print()
  print("Your current score: " + str(round((score/total_num_of_qn*100),1)) + "%"  )
  print()
  print()
  
  

counter +=1
tracker = 0

while tracker !=1:
  
  print("Q"+str(counter)+") "+ "Which is a property of light?")
  print("   a) Light travels slower than sound.")
  print("   b) Light is a longitudinal wave.")
  print("   c) Light travels in a curvy line.")
  print("   d) Light travels in a straight line.")
  answer = input("Your answer: ")
  answer = answer.lower()
  if answer == "a":
    output = "Wrong. Light travels faster than sound. That's why we see the light from lightning before hearing thunder."
    score -=1
  elif answer == "b":
    output = "Wrong.  Light is a transverse wave."
    score -=1
  elif answer == "c":
    output = "Wrong.  Light travels in a straight line."
    score -=1
    
  elif answer == "d":
    output = "Yes, that's right!"
    tracker =1
    score +=1
  else:
    output = "Please choose a, b, c or d only."

  

  print()
  print(output.lower())
  print()
  print("Your current score: " + str(round((score/total_num_of_qn*100),1)) + "%"  )
  print()
  print()
  
print("End of quiz!")
