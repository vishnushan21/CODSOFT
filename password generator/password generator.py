import random
import string

def generate_password(length):

    characters = string.ascii_letters + string.digits + string.punctuation
    
    password = ''.join(random.choice(characters) for i in range(length))
    
    return password

def main():
    print("PASSWORD GENERATOR...!")
    
    while True:
        try:
            length = int(input("\nEnter the desired length of the password: "))
        
            if length <= 0:
                print("Length must be a positive integer. Please try again.")
                continue
            
            password = generate_password(length)
            
            print("\nGenerated Password:", password)
            
            choice = input("\nDo you want to generate another password? (yes/no): ").lower()
            if choice != 'yes':
                print("\nThank you for using the Password Generator. Have a great day!")
                break
            
        except ValueError:
            print("Invalid input! Please enter a valid integer.")

if __name__ == "__main__":
    main()