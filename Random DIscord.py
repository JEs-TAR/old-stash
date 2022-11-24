print('What is your name, just type your name')
TheName = input()
print(TheName +', can you do maths, type `yes` or `no`')
TheYesorNo = input()
str(TheYesorNo)
if TheYesorNo == 'yes':
    print('So I am gonna ask you a question, you okay with that, type `yes` or `no`')
    The = input()
    str(The)
    if The == 'yes':
        print('If a rocket travels at the speed of 5,000 km per hour,')
        print('and if the moon is 380,000 kms away, then how much')
        print('time is it gonna take the rocket to get there, only write the answer')
        themaths = input()
        str(themaths)
        if themaths == '76':
            print('You have proved that you know maths, Congrats!!!!!')
        else:
            print('Congrats!!!, you are wrong')
           
    else:
        print('You are making me doubt your skills')
else:
    print('Ok, learn some maths')
   