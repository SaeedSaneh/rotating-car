from deep_translator import GoogleTranslator
import kharid
import frosh
print ('''Welcome to the rotating car\n\n''')
while True :
    while True :
        Entrance_0= input ('''    1-Information about the price of the desired car\n    2-Pricing on the car
        Select the desired option : ''') 
        if Entrance_0 == '1'  or Entrance_0 == '2' :
            break
        else : 
            print ('Please use the available options! (1 , 2)')
    Problematic_names = {'who' : 'kia' , 'Hawk' : 'shahin'}
    if Entrance_0 == '1' :
        car_name1 = input ('Enter the car name : ')
        car_name = GoogleTranslator(source="fa" , target="en").translate(car_name1)
        for i in Problematic_names :
            if i == car_name :
                car_name = Problematic_names[i]
        kharid.kh_cars(car_name)   
        
    elif Entrance_0 == '2' :
        car_name1 = input ('Enter the car name : ')
        car_name = GoogleTranslator(source="fa" , target="en").translate(car_name1)
        for i in Problematic_names :
            if i == car_name :
                car_name = Problematic_names[i]
        end = frosh.f_cars(car_name)
        print (end)
    ahrom = 0
    while True :
        ahrom = input("Do you want to try again?  [ y , n ]")
        if ahrom == 'n' or 'y':
            break
        else:
           print ("Please use \"y\" or \"n\".")
    if ahrom == 'n' :
        ahrom = 1
    else :
        ahrom = 0

    if ahrom == 1 :
        print ("godbay !")
        break

