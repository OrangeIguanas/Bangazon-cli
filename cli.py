from Methods.CreateCustomer import *
# This is the CLI for interacting with our DB
print("""\
.----.   .--.  .-. .-. .---.   .--.  .---.  .----. .-. .-.
| {}  } / {} \ |  `| |/   __} / {} \{_   / /  {}  \|  `| |
| {}  }/  /\  \| |\  |\  {_ }/  /\  \/    }\      /| |\  |
`----' `-'  `-'`-' `-' `---' `-'  `-'`---'  `----' `-' `-'
                                                      """) 
print("""                    
      	    =*===
           $.  . $$$
           $ <    D$$
           $ __  $$$
     ,     $$$$  |
    ///; ,---' _ |----.
     \ )(           /  )
     | \/ \.   '  _.|  \              $
     |  \ /(   /    /\_ \          $$$$$
      \ /  (       / /  )         $$$ $$$
           (  ,   /_/ ,`_,-----.,$$  $$$
           |   <----|  \---##     \   $$
           /         \\\           |    $
          '   '                    |
          |                 \      /
          /  \_|    /______,/     /
         /   / |   /    |   |    /
        (   /--|  /.     \  (\  (_
         `----,( ( _\     \ / / ,/
               | /        /,_/,/
              _|/        / / (
             / (        ^-/, |
            /, |          ^-   
 """)
firstPage = input("Hello client developer! I am Bangazon the Centaur. I will be your virtual guide.")
nextPage = input("Press Enter to begin your journey.")

# Initiate a loop 
while True: 

  print(""" Enter a Number: 

      ******************************
         WELCOME TO BANGAZON API
      ******************************
      1.     Create a customer account
      2.     Choose active customer
      3.     Create Payment Option
      4.     Add a product to shopping cart 
      5.     Complete an Order
      6.     See product Popularity
      7.     Leave Bangazon
      """)
  # Store input values to pass as parameters in a new Customer argument 
  try:
    choice = int(input(">"))
    if choice == 1: 
      print("Enter first name:")
      fName = input() 
      print("Enter last name:")
      lName = input() 
      print("Email?")
      email = input() 
      print("Can I get your number?")
      phone = input() 
      print("Enter Address")
      address = input()
      print("Enter Zip Code:")
      zipCode = input()
      print("Enter City")
      city = input()
      print("Enter State")
      state = input()
      # Instantiate new Customer
      newCustomer = Customer(fName, lName, email, phone, city, state, zipCode, address)
      # Store new Customer in DB via save method
      newCustomer.save(newCustomer)
      print(newCustomer.get_full_name())
    elif choice == 2: 


      
  except ValueError: 
      print("ERROR")



                                                            
                                                            
                                                            