from sklearn import tree
from sklearn.preprocessing import LabelEncoder
from deep_translator import GoogleTranslator
import jdatetime
import mysql.connector as mysql 
import kharid
import numpy as np
def f_cars (car_name) :
    db = mysql.connect(
            host = "localhost",
            user = "root",
            password = "",
            database = "car_list"
        )
    cursor = db.cursor()
    cursor.execute("DELETE FROM cars;")
    db.close()
    x = []
    y = []
    kharid.kh_cars(car_name)
    
    db = mysql.connect(
        host = "localhost",
        user = "root",
        password = "",
        database = "car_list"
    )
    N_cars = list()
    M_cars = list ()
    K_cars = list ()
    cursor = db.cursor()
    cursor.execute("SELECT * FROM cars;")
    z = cursor.fetchall()
    if z != [] :
        for i in z :
            N_cars.append(i[0])
            M_cars.append(i[1])
            K_cars.append(i[2])
            y.append(i[3])
        
        for i in range(0 , len(K_cars)):
            if ',' in K_cars[i] :
                ahrom = K_cars[i].split(',')
                K_cars[i]=''.join(ahrom)
        
        for i in range (0,len(y)) :
            if ',' in y[i] :
                ahrom = y[i].split(',')
                y[i] = ''.join(ahrom)
        
        label_encoder = LabelEncoder()
        cars_encoded = label_encoder.fit_transform(N_cars)
        name_dict = dict()
        for i in range(0 , len(cars_encoded)) :
            ahrom = cars_encoded[i] in name_dict
            if ahrom == False : 
                name_dict[cars_encoded[i]] = N_cars[i]
                name_dict[N_cars[i]] = cars_encoded[i]

        for i in range(0 , len(K_cars)):
            x.append([cars_encoded[i] , int(M_cars[i]) , int(K_cars[i])])
        
        clf = tree.DecisionTreeClassifier()
        clf = clf.fit(x , y)
        
        name_cars = list ()
        for i in N_cars :
            ahrom = i in name_cars 
            if ahrom == False :
                name_cars.append(i)
        today= jdatetime.date.today()
        number = ['1','2','3','4','5','6','7','8','9','0']
        name_cars_p = list()
        while True:
            name_car = input ("Enter the car name : ")
            name_car = GoogleTranslator(source="fa" , target="en").translate(name_car)
            for i in  range(0 , len(name_cars)) :
                name_cars_p.append(GoogleTranslator(source="en" , target="fa").translate(name_cars[i]))
            ahrom = name_car in name_cars
            if ahrom == False :
                print ('''Please enter the correct car name, for example:\n%s''' %' , '.join(name_cars_p))
            else :
                break
        while True :
            ahrom_1 = 0
            model_car = input ("Enter the car model : ")
            if len (model_car) == 4 :
                for i in model_car :
                    ahrom = i in number 
                    if ahrom == True :
                        ahrom_1+=1
                if ahrom_1 == 4 :
                    if today.year >= int(model_car)and 1320 < int(model_car):
                        break
                    else :
                        print ('The entered model is incorrect: \nthe correct way to enter the model {for example 1400}')
                else :
                    print ('The entered model is incorrect: \nthe correct way to enter the model {for example 1400}')
            else:
                print ('The entered model is incorrect: \nthe correct way to enter the model {for example 1400}')


        while True :
            ahrom_1 = 0
            operation_car = input ("Enter the operation of the car : ")
            for i in operation_car :
                ahrom = i in number
                if ahrom == True :
                    ahrom_1+= 1
            if ahrom_1 == len(operation_car):
                    break
            else :
                    print ('The machine operation was entered incorrectly. Please enter only the number')

        new_data = [[int(name_dict[name_car]),int(model_car) ,int(operation_car)] ]

        answer = clf.predict(new_data)
        return (answer[0])
    else :
        print ("!!!!  404  !!!!")
        
f_cars('samand')