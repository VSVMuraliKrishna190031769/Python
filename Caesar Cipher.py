#ENCRYPTION
def Encrypt(p,shift):
    c=""
    for i in p:
        if i>='a' and i<='z':
            if ord(i)+shift<=ord('z'):
                c+=chr(ord(i)+shift)
            else:
                k=ord(i)+shift-ord('z')
                c+=chr(ord('a')+k-1)
        elif i>='A' and i<='Z':
            if ord(i)+shift<=ord('Z'):
                c+=chr(ord(i)+shift)
            else:
                k=ord(i)+shift-ord('Z')
                c+=chr(ord('A')+k-1)
        else:
            c+=i
    return c

#DECRYPTION
def Decrypt(c,shift):
    p=""
    for i in c:
        if i>='a' and i<='z':
            if ord(i)-shift>=ord('a'):
                p+=chr(ord(i)-shift)
            else:
                k=ord('a')-(ord(i)-shift)
                p+=chr(ord('z')-(k-1))
        elif i>='A' and i<='Z':
            if ord(i)-shift>=ord('A'):
                p+=chr(ord(i)-shift)
            else:
                k=ord('A')-(ord(i)-shift)
                p+=chr(ord('Z')-(k-1))
        else:
            p+=i
            
    return p

#EQUALITY CHECK
def EqualityCheck(p,c):
    if p==c:
        return True
    return False


#Main Code
t=True
while(t):
    print("Choose an option from below :\n1. Encrypt a message\n2. Decrypt a message\n3. Compare Encryption and decryption\nEnter any other value to exit")
    n=int(input())
    if n==1:
        p=input("Enter the message you want to encrypt : ")
        shift=int(input("Enter the character shift : "))
        print("The ecrypted message of",p,"is : "+Encrypt(p,shift))
    elif n==2:
        c=input("Enter the message you want to decrypt : ")
        shift=int(input("Enter the character shift : "))
        print("The decrypted message of",c,"is : "+Decrypt(c,shift))
    elif n==3:
        o=int(input("Choose an option fron below :\n1. Enter plain text and compare\n2. Enter cipher text and compare\n3. Enter both cipher text and plain text and compare : \n"))
        if o==1:
            inp=input("Enter plain text : ")
            shift=int(input("Enter shift : "))
            if(EqualityCheck(inp,Decrypt(Encrypt(inp,shift), shift))):
                print("Successful")
            else:
                print("Unsuccessful")
        elif o==2:
            inc=input("Enter cipher text : ")
            shift=int(input("Enter shift : "))
            if(EqualityCheck(inc,Encrypt(Decrypt(inc,shift), shift))):
                print("Successful")
            else:
                print("Unsuccessful")
        else:
            inp=input("Enter plain text : ")
            inc=input("Enter cipher text : ")
            shift=int(input("Enter shift : "))
            if(EqualityCheck(Encrypt(inp,shift),inc) and EqualityCheck(Decrypt(inc,shift),inp)):
                print("Successful")
            else:
                print("Unsuccessful")
    else:
        break
