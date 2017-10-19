#Encryption Using Ceasar Encryption Technique
import random;
#48-57 ==> ascii for 0-9
#65-93 ==> ascii for A-Z
#97-129 ==> ascii for a-z

def encrypt(level,message,pkey):
    if(level == 1):
        key = random.randrange(0, 9)
    elif(level == 2):
        key = random.randrange(0,15)
    elif(level == 3):
        key = random.randrange(0,26)
#Saving the Private Key to File with Value
    file = open('privacy.txt', 'a')
    keydict = {
        pkey : key
    }
    file.write(str(keydict)+"\n")

    file.close()
#Encrypting with Ceasar Method
    for i in range(len(message)):
        asciiv = ord(message[i])
        message[i] = chr((asciiv+key))
        enmsg = "".join(message)
    print("Encrypted Message: " + str(enmsg) +'\n')
    menu()

def decrypt(pkey,enmessage):
#Retrieve the Private Key from File
    file = open('privacy.txt','r')
    flag = 0
    for line in file:
        dict = eval(line)
        if pkey in dict:
            flag = 1
            key = dict[pkey]
            for i in range(len(enmessage)):
                asciiv = ord(enmessage[i])
                enmessage[i] = chr((asciiv - key))
                dmsg = "".join(enmessage)
            print("\n NOTE: If You Don't Understand the Message, You have Entered Wrong Encrypted Message! \n " + dmsg +"\n")
            menu()
            break

    if(not flag):
        print("PRIVATE KEY NOT FOUND!" +'\n')
        menu()

def messageinput():
    message = input("Enter The Message: \n").upper()
    privatekey = input("Enter a Private Key for Decryption: \n").upper()
    level = int(input("Enter the Level of Complexity: \n 1.Low \n 2.Middle \n 3.Strong \n Enter Your Choice: "))

    if (level == 1):
        encrypt(level,list(message),privatekey)
    elif (level == 2):
        encrypt(level, list(message),privatekey)
    elif (level == 3):
        encrypt(level, list(message),privatekey)
    else:
        print ("You have Chosen Wrong!\n")
        messageinput()

def menu():
    selection = int(input("DO YOU WANT TO ENCRYPT OR DECRYPT: \n 1. Encrypt \n 2. Decrypt \n 3. Exit \n Enter Your Choice: "))
    if(selection == 1):
        messageinput()
    elif(selection == 2):
        dmessage = input("Enter The Message: \n")
        privatekey = input("Enter the Private Key: ").upper()
        decrypt(privatekey,list(dmessage))
    else:
        exit()

menu()