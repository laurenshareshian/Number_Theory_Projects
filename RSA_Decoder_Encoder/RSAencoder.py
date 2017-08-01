#this program RSA encrypts a message from the user
from __future__ import print_function
import math


def gcd(x,y):
    a=max(x,y)
    b=min(x,y)
    while(b!=0):
        c=a%b
        a=b
        b=c
    return a

def phi(x,y):
    phicount=1
    phicount=x*y-x-y+1
    return phicount


def lin_soln(a,b):
    x=1
    g=a
    v=0
    w=b
    while w!=0:
        y=(g-a*x)/b
        t=g%w
        q=g//w #int(math.floor(g/w))
        s=x-q*v
        x=v
        g=w
        v=s
        w=t
    y=(g-a*x)/b

    y=-y

    #make sure the chosen solution has positive x
    while x<0:
        x=x+b
        y=y+a
    return (x,y)

def succ_square(a,k,m):
    b=1
    while k>=1:
        if k%2!=0:
            b=(a*b)%m
        a=(a*a)%m
        k=k//2 #math.floor(k/2)
    b=b%m
    return b

def alphabet(letter):
        letter=letter.replace('A','11')
        letter=letter.replace('B','12')
        letter=letter.replace('C','13')
        letter=letter.replace('D','14')
        letter=letter.replace('E','15')
        letter=letter.replace('F','16')
        letter=letter.replace('G','17')
        letter=letter.replace('H','18')
        letter=letter.replace('I','19')
        letter=letter.replace('J','20')
        letter=letter.replace('K','21')
        letter=letter.replace('L','22')
        letter=letter.replace('M','23')
        letter=letter.replace('N','24')
        letter=letter.replace('O','25')
        letter=letter.replace('P','26')
        letter=letter.replace('Q','27')
        letter=letter.replace('R','28')
        letter=letter.replace('S','29')
        letter=letter.replace('T','30')
        letter=letter.replace('U','31')
        letter=letter.replace('V','32')
        letter=letter.replace('W','33')
        letter=letter.replace('X','34')
        letter=letter.replace('Y','35')
        letter=letter.replace('Z','36')
        number=int(letter)
        return number


def breakup(b,m):
    new=[]
    b=str(b)
    limit=len(str(m)) #(OR DELETE -1 IF YOU WANT IT EQUAL TO DIGITS OF M)

    i=0
    while i<=len(b)-1:#len(b)-limit:
        if i%limit==0:
            if i+limit-1<=len(b):
                new.append(b[i:i+limit])
            else:
                new.append(b[i:])
        i=i+1

    square=[]
    for i in range(len(new)):
        square.append(int(new[i]))

    return square

def user_info_to_decode(int):
    if int==0: #use the test example
        p = 123456789012345681631
        q = 7746289204980135457
        k = 12398737
        m = p * q
        message='WETHEPEOPLEOFTHEUNITEDSTATESINORDERTOFORMAMOREPERFECTUNIONESTABLISHJUSTICEINSUREDOMESTICTRANQUILITYPROVIDEFORTHECOMMONDEFENSEPROMOTETHEGENERALWELFAREANDSECURETHEBLESSINGSOFLIBERTYTOOURSELVESANDOURPROSTERITYDOORDAINANDESTABLISHTHISCONSTITUTIONFORTHEUNITEDSTATESOFAMERICA'

    else: #ask the suer for their message to decode
        p=input('What is the private key p?')
        q=input('What is the private key q?')
        k=input('What is the pubic key k relatively prime to phi(m)=phi(pq)?')
        m=p*q

        #obtain the message to decode
        message=input('What is the message to encode?')

    return p,q,k,m,message

userinput=input('If you would like to use the test example, type 0. If you would like to enter in your own data, type 1.')
p,q,k,m,message=user_info_to_decode(userinput)

#compute phi(m)
phim=phi(p,q)

#verify gcd(phi(m),k)=1
if gcd(phim,k)!=1:
    print('cant use algorithm - gcd(phi(m),k) does not equal 1')

#convert letters to numbers
b=alphabet(message)


#break up message into strings of digits that are equal to the digits of m
square=breakup(b,m)


print('The encoded message is: ')
for i in range(len(square)):
    #verify gcd(b,m)=1       
    if gcd(square[i],m)!=1:
        print('cant use algorithm - gcd(b,m) does not equal 1')

    #use successive squares to calculate b^k
    y=succ_square(square[i],k,m)

    #encode message
    print(y)


