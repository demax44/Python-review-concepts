#number=1
#while number<5:
    #print(number)
    #number+=1

#counter=26
#while counter>15:
    #print(counter)
    #counter-=3

#print('loop has ended')





#cars=['Audi','Honda','Toyota','Hummer']
#for x in cars:
    #if x=='Audi':
     #   continue
    #print(x)



numbers=[1,2,3,4,5,6]
for x in numbers:
    print(x**3)
    if x==7:
        break
    print('Inside the loop')
else:
    print('Outside loop')





    
    
    
counter=[1,2,3,4,5,6,7,8,9,10]
for x in counter:
    if x==9:
        print('Skip number')
    continue
print(x)




numbers=[1,2,3]
letters=['a','b','c']

for number in numbers:
    for letter in letters:
        print(number,letter)


#var=1
#while var==1:
    #print(var)

def my_introduction(fname,lname,age):
    print('My name is :'+fname+' '+lname+'and my age is:'+str(age))

my_introduction('Dayron','Maxwell',21)




def multiple(num1,num2):
    return num1*num2
result=multiple(2,3)
print('Result={}'.format(result))


def greeting(name):
    return "Hello"+ name
result=greeting('Dayron')
print(result)



def my_bio():
    name='Dayron'
    age=22
    children=3
    return [name,age,children]

listresult=my_bio()
print(listresult)