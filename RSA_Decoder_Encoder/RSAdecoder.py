#this code performs an RSA decryption of a message

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

def alphabet(x):
    string=str(x)
    message=''
    for j in range(0,len(string)-1,2):
        letter=string[j]+string[j+1]
        letter=letter.replace('11','A')
        letter=letter.replace('12','B')
        letter=letter.replace('13','C')
        letter=letter.replace('14','D')
        letter=letter.replace('15','E')
        letter=letter.replace('16','F')
        letter=letter.replace('17','G')
        letter=letter.replace('18','H')
        letter=letter.replace('19','I')
        letter=letter.replace('20','J')
        letter=letter.replace('21','K')
        letter=letter.replace('22','L')
        letter=letter.replace('23','M')
        letter=letter.replace('24','N')
        letter=letter.replace('25','O')
        letter=letter.replace('26','P')
        letter=letter.replace('27','Q')
        letter=letter.replace('28','R')
        letter=letter.replace('29','S')
        letter=letter.replace('30','T')
        letter=letter.replace('31','U')
        letter=letter.replace('32','V')
        letter=letter.replace('33','W')
        letter=letter.replace('34','X')
        letter=letter.replace('35','Y')
        letter=letter.replace('36','Z')
        message=message+letter
    return message


def user_info_to_decode(int):
    if int==0: #use the test example
        k = 12398737
        p = 123456789012345681631
        q = 7746289204980135457
        m = p * q
        b = [568785302227887190999970106280895846059, 638700366373507681029575235540648728578,
             873707816600924929368968544201356254695, 923350093551033535545426525613714735382,
             302705207374849933778332257939414701614, 104686864942526994812158057926484652568,
             168755691091513821145051905674195262792, 910216509306128117592425198718906605700,
             98880592333209693576586984993838747356, 382090227902153277661969404439638024167,
             191484149350820515057025102392062759182, 871891386825374980001064420825474105444,
             162898391215627354089714516892151338260, 48682229962145410141769965198980001074,
             4307309085074433740150189007018484448]
    else: #ask the suer for their message to decode
        p=input('What is the private key p?')
        q=input('What is the private key q?')
        k=input('What is the pubic key k relatively prime to phi(m)=phi(pq)?')
        m=p*q

        #obtain the message to decode
        b=[]
        message=1
        while message!=0:
           message=input('What is the message to decode? Enter return between each string of digits. When finished, type 0:   ')
           if message!=0:
               b.append(message)
    return k, p, q, m, b

userinput=input('If you would like to use the test example, type 0. If you would like to enter in your own data, type 1.')

k,p,q,m,b=user_info_to_decode(userinput)


#compute phi(m)
phim=phi(p,q)

#verify gcd(phi(m),k)=1
if gcd(phim,k)!=1:
    print('cant use algorithm - gcd(phi(m),k) does not equal 1')
        
#find a positive solution u to k*u-phi*v=1
u=lin_soln(k,phim)[0]

for i in range(len(b)):
#    verify gcd(b,m)=1
    if gcd(b[i],m)!=1:
        print('cant use algorithm - gcd(b,m) does not equal 1')

    #use successive squares to calculate b^u
    y=succ_square(b[i],u,m)
 
    #decode message
    print(alphabet(y), end='')


print(' ')
