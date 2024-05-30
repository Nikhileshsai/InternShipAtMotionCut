import random
import string

def generate_passwords(size=4):
    if size < 4:
        raise ValueError("Password needs atleast 4 characters")
    LowerCase = string.ascii_lowercase
    UpperCase = string.ascii_uppercase
    Number    = string.digits
    SpecialCharacters = string.punctuation
    password = [random.choice(LowerCase),random.choice(UpperCase),random.choice(Number),random.choice(SpecialCharacters)]
    if size > 4:
        AllCharacters = LowerCase+UpperCase+Number+SpecialCharacters
        password += random.choices(AllCharacters,k=size-4)
    random.shuffle(password)
    return ''.join(password)

def main():
    NoOFPasswords = int(input("How many Passwords do you want?\n"))
    if NoOFPasswords < 1:
        raise ValueError("Please Enter atleast 1")
    LengthOfPassword = int(input("Enter the Required Length of the password (Minimum of 4 characters):\n"))
    for i in range(0,NoOFPasswords):
        print(f"Password No.{i}:  {generate_passwords(LengthOfPassword)}")
if __name__ =="__main__":
    main()        

    