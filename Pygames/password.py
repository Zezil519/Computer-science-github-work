pass1 = ""
pass2 = ""

def getPword(attempt):
  if attempt == 1:
    quit = False
    while quit == False:
      pass1 = input("enter password:")
      if len(pass1) > 8 or len(pass1) < 6:
        print("Error. Passwords must be 6 to 8 characters long.")
      else:
        quit = True
        return getPword(2)
  if attempt == 2:
    while True:
      pass2 = input("enter password again:")
      if pass1 != pass2:
        print("Error-passwords do not match")
        return getPword(1)
      else:
        print("password change successful")
        return pass1



password = getPword(1)
print(password)
  

        
        

