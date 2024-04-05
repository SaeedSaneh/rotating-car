import re 
import requests
from bs4 import BeautifulSoup
from deep_translator import GoogleTranslator
import mysql.connector as mysql
def kh_cars (car_name) :
    db = mysql.connect(
            host = "localhost",
            user = "root",
            password = "",
            database = "car_list"
        )
    cursor = db.cursor()
    cursor.execute("DELETE FROM cars;")
    db.commit()

    db.close()
    v = list()
    car_n = list() 
    sayt_name = 'https://karnameh.com'
    a = requests.get('https://karnameh.com/buy-used-cars?search=%s' % car_name)
    b = BeautifulSoup(a.text , 'html.parser')
    d = b.find_all('a' ,target="_blank")
    for i in d :
        if len (str(i)) > 2500 :
            v.append(str(i))
    for i in v :
        ii = i
        q= re.findall(r'''<div class="muirtl-19pqxwo"><p class="MuiTypography-root MuiTypography-body1 muirtl-1nf835y">(.*)<!-- -->.*<!-- -->(.*)</p><div class="muirtl-zeshta"><p class="MuiTypography-root MuiTypography-body1 muirtl-5dxzpw">.*</p></div><div class="MuiBox-root muirtl-3bel80"></div><div class="muirtl-1qcgoi9"><div class="muirtl-1snz76b"><svg aria-hidden="true" class="MuiSvgIcon-root MuiSvgIcon-fontSizeMedium muirtl-1hawzcg" data-testid="LocationOnRoundedIcon" focusable="false" viewbox="0 0 24 24"><path d="M12 2c-4.2 0-8 3.22-8 8.2 0 3.18 2.45 6.92 7.34 11.23.38.33.95.33 1.33 0C17.55 17.12 20 13.38 20 10.2 20 5.22 16.2 2 12 2zm0 10c-1.1 0-2-.9-2-2s.9-2 2-2 2 .9 2 2-.9 2-2 2z"></path></svg><p class="MuiTypography-root MuiTypography-body1 muirtl-1x7b2q1">.*</p></div><div class="muirtl-1snz76b"><p class="MuiTypography-root MuiTypography-body1 muirtl-1x7b2q1">.*</p></div><div class="muirtl-1snz76b"><p class="MuiTypography-root MuiTypography-body1 muirtl-1x7b2q1">(.*)<!-- -->.*</p></div></div><div class="MuiBox-root muirtl-1xzznhp"></div><div class="muirtl-1y609i0"><p class="MuiTypography-root MuiTypography-body1 muirtl-1tgtx2d">.*</p><div class="muirtl-1r5to7m"><p class="MuiTypography-root MuiTypography-body1 muirtl-3rge6o">(.*)</p><p class="MuiTypography-root MuiTypography-body1 muirtl-1b4t65i">.*</p></div></div></div>''' , ii)
        if q != [] : 
            car_n.append(q[0])
        
    urls = list ()   
    for i in v :
        i = str (i)
        w = re.findall(r'''<a class="muirtl-16q7pwi" href="(.*)" target=''' , i)
        urls.append((w))
    urls = urls[:-1]

    for i in range (0 , len (urls)) :
        car_n[i]= list (car_n[i])
        car_n[i].append(sayt_name + urls[i][0])
    

    cars_dict = dict()
    for i in car_n :
        if len (i) != 5 :
            del[car_n[car_n.index (i)]]
        ahrom = i[0] in cars_dict 
        if ahrom == False :
            cars_dict[i[0]] = GoogleTranslator(source="fa" , target="en").translate(i[0])
            cars_dict[cars_dict[i[0]]] = i[0]

    # db = mysql.connect(
    #     host = "localhost",
    #     user = "root",
    #     password = "",
    #     database = "car_list"
    # )
    # cursor = db.cursor()
    # db_cars = list()
    # cursor.execute("SELECT * FROM cars;")
    # z = cursor.fetchall()
    # for i in z :
    #     ahrom = list()
    #     for ii in range (0 , 5 ) :
    #         if ii == 0 :
    #             ahrom.append(cars_dict[i[0]])
            
    #         else :
    #             ahrom.append(i[ii]) 
    #     db_cars.append(ahrom)
     
    # db.close()
    # for i in db_cars :
    #     if i in car_n :
    #         del [car_n[car_n.index (i)]]
        
    db = mysql.connect(
            host = "localhost",
            user = "root",
            password = "",
            database = "car_list"
        )
    cursor = db.cursor()
    query = "INSERT INTO cars VALUES (%s , %s , %s , %s , %s);"
    for i in car_n :
        values = (cars_dict[i[0]] , i[1] , i[2] , i[3] , i[4])
        cursor.execute(query , values)
    db.commit()

    db.close()
    # Another site can be added