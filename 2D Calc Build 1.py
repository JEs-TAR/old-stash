import time
import math
fig_rect="Rectangle"
fig_sqr="Square"
fig_tri="Triangle"
fig_circle = "Circle"
pi= 3.14

name=input("What is your name? ")
print("Hi " + name)

input_fig =input("What Figure you want to calculate the Dimensions of ") 
input_fig = input_fig.capitalize()


if input_fig == fig_rect:
    print("You have Chosen Rectangle ")
    find_1 ="Length"
    find_2="Breadth" 
    find_area="Area"
    find_peri = "Perimeter"
    Question_rect=input("What do you want to calculate : ")
    Question_rect = Question_rect.capitalize()

    if Question_rect == find_1:
        Breadth_1 = float(input("Enter Breadth of the Rectangle : " ))
        time.sleep(1)
        Area_1 = float(input("Enter Area of the Rectangle : " ))
        Lenght_final = (Area_1 / Breadth_1)
        print("The Length is " + str(Lenght_final) )
    elif  Question_rect == find_2:
        Lenght_1 = float(input("Enter the Length of the Rectangle :  "))
        time.sleep(1)
        Area_2 = float(input("Enter Area of the Rectangle : " ))
        Breadth_final = (Area_2 / Lenght_1)
        print("The Breadth is " + str(Breadth_final))
    elif Question_rect == find_area:
        Length_3 = float(input("Enter the Length of the Rectangle :  "))
        time.sleep(1)
        Breadth_3 = float(input("Enter Breadth of the Rectangle : " ))
        Area_final = ( Length_3 * Breadth_3)
        print("The Area is " + str(Area_final) + " sq units")
    elif Question_rect == find_peri:
        Length_4 = float(input("Enter the Length of the Rectangle :  "))
        time.sleep(1)
        Breadth_4 = float(input("Enter Breadth of the Rectangle : " ))
        Peri_final = ((Length_4 + Breadth_4)*2)
        print("The Perimeter is " + str(Peri_final) + " units")
    else:
        print("You can only find Length , Breadth , Area , Perimeter :) ")


elif input_fig == fig_sqr:
    print("You Have Chosen Square ")
    find_s = "Side"
    find_sarea = "Area"
    find_periS = "Perimeter"
    Question_sqr = input("What do you want to calculate : ")
    Question_sqr = Question_sqr.capitalize()

    if Question_sqr == find_s:
        area_1_s = float(input("Enter the Area of the Square: "))
        side_1_final = ( area_1_s / 4 )
        print("The Length of the side is :  " + str(side_1_final) + " units")
    elif Question_sqr == find_sarea:
        side_2 = float(input("Enter the length of the side"))
        area_1_final = (side_2 * side_2)
        print("The Area is : " + str(area_1_final) + " sq units")
    elif Question_sqr == find_periS:
        side_3 = float(input("Enter the length of the Side"))
        peri_s = ( 4 * side_3)
        print("The Perimeter of the square is : " + str(peri_s) + " units" )
    else:
        print("You can only calculate Side , Area , Perimeter ")
         
elif input_fig == fig_circle:
    print("You have chosen Circle ")
    find_areaC = "Area"
    find_radius = "Radius"
    find_circle_C = "Circumference"
    question_circle = input("What do you want to calculate ")
    question_circle = question_circle.capitalize()

    if question_circle == find_areaC:
        radius_1 = float(input("Enter Radius  of the Circle : " ))
        time.sleep(1)
        Area_1_C = ( float(pi) * (radius_1 *radius_1))
        print("The Area is " + str(Area_1_C) )
    elif  question_circle == find_radius:
        Area_2 = float(input("Enter the Area of the Circle :  "))
        time.sleep(1)
        Radius_final = (Area_2 / float(pi))
        print("The Radius is " + str(Radius_final) + " Units" " ; Diameter = " + str(2 * Radius_final)) 
    
    elif question_circle == find_circle_C:
        radius_3 = float(input("Enter Radius  of the Circle : " ))
        Circum_final = ( 2 * float(pi) (radius_3 * radius_3))
        print("The Circumference of the Circle is : " + str(Circum_final) + " units")
    else:
        print("You can calculate Radius , Area , Circumference :)")

elif input_fig == fig_tri:
    print("You have chosen Triangle ")
    perimeter_tri = "Perimeter"
    Area_tri = 'Area'
    question_tri = input("What do you want to calculate ")
    question_tri = question_tri.capitalize()

    if question_tri == Area_tri:
        hb_know = input (" Do you know height and base of the triangle ? ")
        hb_know = hb_know.capitalize()
        
        while hb_know != 'Yes' or 'No':
            print('Type Yes or No by Re-running the script ')
        


        if hb_know == 'Yes':
            h =input("Enter the Height of the Triangle : " )
            b =input("Enter the Base of the Triangle : " )
            area_final_tri = (0.5 * int(h) * int(b) )
            print("The Area of Triangle is " +  str(area_final_tri) + " sq.units" )
        
        elif hb_know == 'No':
            semi_p = (input('Enter the Perimeter of the triangle :  '))
            semi_p_1 = int(semi_p) / 2 
            Enter_side_1 = input("Enter the lenght of Side 1 : ")
            Enter_side_2 = input("Enter the lenght of Side 2 : ")
            Enter_side_3 = input("Enter the lenght of Side 3 : ")
            Area_tri_final = math.sqrt(int(semi_p_1)* (int(semi_p_1) - Enter_side_1) * (int(semi_p_1) - Enter_side_2) * (int(semi_p_1) - Enter_side_3))
            print('The area of the Triangle is ' + str(Area_tri_final) + ' sq units')

        else:
            print("Type 'Yes' or 'No' ")

    elif question_tri == perimeter_tri:
        side_1 = (input('Enter the length of first side :  '))
        side_2 = (input('Enter the length of second side :  '))
        side_3 = (input('Enter the length of third side :  '))
        peri_tri_final = (int(side_1) + int(side_2) + int(side_3))
        peri_ans = print("The Perimeter of the Triangle is " + str(peri_tri_final)+ " sq units")

    else:
        print('You can only canculate Area and Perimeter right now ! ')

else:
    print("You can only calculate dimensions of Rectangle , Square , Circle and Triangle ! ")

        
    

        



    

        

    
     