# the slicer collects an email from the user
# the email is sliced using the @ with the first aprt being the username and the second part as the domain
#the domain is splitted further using the . into two parts

def Main_App():
    print("welcome to the email slicer")
    print("")
    print("")
    email_input=input("enter your email address:")
    (username,domain)=email_input.split("@")
    (domain,extension)=domain.split(".")

    print("username: " , username)
    print("domain : " ,domain)
    print("extension: " ,extension)
while True:
    Main_App()
    
