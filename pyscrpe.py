import os
import csv
import urllib.request
import numpy
from bs4 import BeautifulSoup
# using Exception handeling ----------------------
try:
    url=urllib.request.urlopen("http://www.cisce.org/locate-search.aspx?country=0&state=0&dist=0&city=0&location=&schooltype=&cve=&isc=&icse=&schoolclassi=&school=&search=locate")
    get_code=url.read()#Ectracting the html code received from the server------------
    soup=BeautifulSoup(get_code,'lxml')#using BeautifulSoup for parsing the html data or content that we want to use------------
    f=open("C://Users/vshan/Desktop/Details.csv","a+")
    f.write('SCHOOL CODE');f.write(",");f.write('SCHOOL NAME');f.write(',');f.write('SCHOOL ADDRESS');f.write(',');f.write('CATEGORIES 1');f.write(',');f.write('CATEGORIES 2');f.write(',');f.write('CATEGORIES 3');f.write(',');f.write('TYPES 1');f.write(',');f.write('TYPES 2');f.write(',');f.write('NAME OF THE HEAD');f.write(',');f.write("CONTACT INFO 1");f.write(',');f.write("CONTACT INFO 2");f.write(',');f.write('CONTACT INFO 3');f.write(',');f.write('CONTACT INFO 4');f.write(',');f.write('CONTACT INFO 5');f.write('\n');
    for i in range(1,len(soup.find_all('tr'))):
        #--------------------Extracting First column of the table and printing----------------------------
        code=(soup.find_all('tr')[i].text.strip()[:6].strip());print(code)#extracting school code and printing
        name=(soup.find_all('tr')[i].find_all('td')[0].text.replace('\n','').replace('\r','')[7:90].strip().replace(',',''));print(name)#extracting school name and printing
        z=soup.find_all('tr')[i].td.text.replace('\t','').replace('\n','').replace('\r','').replace('   ','')[6:]
        address=z[:len(z)-8];print(address)#extracts address
        f= open("C://Users/vshan/Desktop/Details.csv","a+")
        f.write(code);f.write(',');f.write(name.replace(',',''));f.write(',');f.write(address.replace(',',' ')[len(name)+1:])
        #---------------------Extracting the rest of the column with Exceptional handeling and printing-------------------------------------
        try:
            if i<10:
    #-----------------------------------------------Extracting the contact informations---------------------------------------------------
                contact_info=soup.find_all('tr')[i].find_all('td')[1].text.replace('[O]',',').replace('[F]',',').replace('[E]',',').replace('[Domain]',',').replace('\n','')
            #-------------------------------------------Extracting Categories----------------------------------------------------------
                categories1=(soup.find_all('tr')[i].find("div",{"id":("ctl00_ctl00_Cphcontent_Cphleftcontent_rptsearch_ctl0"+str(i-1)+"_Div4")}).text);print(categories1)
                categories2=(soup.find_all('tr')[i].find("div",{"id":("ctl00_ctl00_Cphcontent_Cphleftcontent_rptsearch_ctl0"+str(i-1)+"_Div5")}).text);print(categories2)
                categories3=(soup.find_all('tr')[i].find_all('td')[2].text.strip()[-15:]).strip();print(categories3)
            #----------------------------------------------Extracting Types-----------------------------------------------------------------
                type1=(soup.find_all('tr')[i].find_all('div')[-1:][0].text)[0:4];print(type1)
                type2=(soup.find_all('tr')[i].find_all('div')[-1:][0].text)[4:];print(type2)
            #---------------------------------------------------Extracting NAME OF THE HEAD------------------------------------------------------
                print("Name of head:",(soup.find_all('tr')[i].find_all('td')[-1:][0]).text)
                
                
            else:
    #----------------------------------------------------Extracting Contact Informations and prnting----------------------------------
                contact_info=soup.find_all('tr')[i].find_all('td')[1].text.replace('[O]',',').replace('[F]',',').replace('[E]',',').replace('[Domain]',',').replace('\n','')
                #----------------------------------------------Extracting and printing the categories Details--------------------------------------------
                categories1=(soup.find_all('tr')[i].find("div",{"id":("ctl00_ctl00_Cphcontent_Cphleftcontent_rptsearch_ctl"+str(i-1)+"_Div4")}).text);print(categories1)
                categories2=(soup.find_all('tr')[i].find("div",{"id":("ctl00_ctl00_Cphcontent_Cphleftcontent_rptsearch_ctl"+str(i-1)+"_Div5")}).text);print(categories2)
                categories3=(soup.find_all('tr')[i].find_all('td')[2].text.strip()[-15:]).strip();print(categories3)
        #---------------------------------------------Extracting nad printing Types---------------------------------------------
                type1=soup.find_all('tr')[i].find_all('div')[-1:][0].text[0:4];print(type1)
                type2=soup.find_all('tr')[i].find_all('div')[-1:][0].text[4:];print(type2)
        #-------------------------------------------Extracting NAME OF HEAD----------------------------------------------
                print(",Name of head:",(soup.find_all('tr')[i].find_all('td')[-1:][0]).text)
                
            
        except AttributeError:#Handelling AttributeError---------------------
            pass
        except UnicodeEncodeError:#Handelling UnicodeEncodeError   and decoding for the better enreichment of the data-----------
            pass
            #printing the properly Decoded data---------------------
   #-------------------------------------Writing the content to the Csv file---------------------------------------
        f= open("C://Users/vshan/Desktop/Details.csv","a+")
        f.write(',');f.write(categories1);f.write(',');f.write(categories2);f.write(',');f.write(categories3);f.write(',');f.write(type1);f.write(',');f.write(type2);f.write(',');f.write(((soup.find_all('tr')[i].find_all('td')[-1:][0]).text).encode('utf-8').decode('utf-8'));f.write(contact_info);f.write('\n');
        f.close()
        
        
except Exception as e:#Handeling Exception and displaying  what type of error do we get if the program is not properly executed.-------------
    print(str(e))
'''-----------------------------------------------------------FINISHED-------------------------------------------------------'''
