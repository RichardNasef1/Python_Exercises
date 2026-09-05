user = input("What is your name? ")
age = int(input("How old are you? "))
if age < 12 :
    print(f"Hello {user}! You are a minor.")   
else:
    print(f"Welcome {user} You are {age} years old!")
while True:
    print("You are in your apartment, looking for your black cat "
    "(who likes to hide and run away)")
    print("1. Go to the Kitchen")
    print("2. Go to the Bathroom")
    print("3. Go to the Bedroom")
    print("4. Go to the Living Room")
    input("Choose where to look ")