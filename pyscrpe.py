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
    with open("C://Users/vshan/Desktop/Details.csv","a+") as f:
        l=csv.writer(f)
        l.writerow([['SCHOOL CODE'],['SCHOOL NAME'],['SCHOOL ADDRESS'],['CONTACT 1'],['CONTACT 2'],['CONTACT 3'],['EMAIL'],['DOMIAN'],['CATEGORIES 1'],['CATEGORIES 2'],['CATEGORIES 3'],['TYPES 1'],['TYPES 2'],['NAME OF THE HEAD']]) 
    for i in range(1,len(soup.find_all('tr'))):
        #--------------------Extracting First column of the table and printing----------------------------
        code=(soup.find_all('tr')[i].text.strip()[:6].strip());print(code)#extracting school code and printing
        name=(soup.find_all('tr')[i].text.strip()[7:80].strip());print(name)#extracting school name and printing
        z=soup.find_all('tr')[i].td.text.replace('\t','').replace('\n','').replace('\r','').replace('   ','')[6:]
        address=z[:len(z)-8];print(address)#extracts address
        #---------------------Extracting the rest of the column with Exceptional handeling and printing-------------------------------------
        try:
            if i<10:
    #-----------------------------------------------Extracting the contact informations---------------------------------------------------
                contact1=(soup.find_all('tr')[1].find_all('td')[1].text[:17].strip());print(contact1)
                contact2=(soup.find_all('tr')[i].find("div",{"id":("ctl00_ctl00_Cphcontent_Cphleftcontent_rptsearch_ctl0"+str(i-1)+"_Div1")}).text);print(contact2)
                contact3=(soup.find_all('tr')[i].find("div",{"id":("ctl00_ctl00_Cphcontent_Cphleftcontent_rptsearch_ctl0"+str(i-1)+"_Div2")}).text);print(contact3)
                email=(soup.find_all('tr')[i].find("div",{"id":("ctl00_ctl00_Cphcontent_Cphleftcontent_rptsearch_ctl0"+str(i-1)+"_Div3")}).text);print(email)
                domain=(soup.find_all('tr')[i].find("div",{"id":("ctl00_ctl00_Cphcontent_Cphleftcontent_rptsearch_ctl0"+str(i-1)+"_Div6")}).text);print(domain)
            #-------------------------------------------Extracting Categories----------------------------------------------------------
                categories1=(soup.find_all('tr')[i].find("div",{"id":("ctl00_ctl00_Cphcontent_Cphleftcontent_rptsearch_ctl0"+str(i-1)+"_Div4")}).text);print(categories1)
                categories2=(soup.find_all('tr')[i].find("div",{"id":("ctl00_ctl00_Cphcontent_Cphleftcontent_rptsearch_ctl0"+str(i-1)+"_Div5")}).text);print(categories2)
                categories3=(soup.find_all('tr')[i].find_all('td')[2].text.strip()[-15:]).strip();print(categories3)
            #----------------------------------------------Extracting Types-----------------------------------------------------------------
                type1=(soup.find_all('tr')[i].find_all('div')[-1:][0].text)[0:4];print(type1)
                type2=(soup.find_all('tr')[i].find_all('div')[-1:][0].text)[4:];print(type2)
            #---------------------------------------------------Extracting NAME OF THE HEAD------------------------------------------------------
                print("Name of head:",(soup.find_all('tr')[i].find_all('td')[-1:][0]).text)
                nameofhead=(soup.find_all('tr')[i].find_all('td')[-1:][0]).text.encode('utf-8');#It might throw an UnicodeEncodeError due to encoding error
                nameofhead.decode('utf-8')
                
                
            else:
    #----------------------------------------------------Extracting Contact Informations and prnting----------------------------------
                contact1=(soup.find_all('tr')[1].find_all('td')[1].text[:17].strip());print(contact1)
                contact2=(soup.find_all('tr')[i].find("div",{"id":("ctl00_ctl00_Cphcontent_Cphleftcontent_rptsearch_ctl"+str(i-1)+"_Div1")}).text);print(contact2)
                contact3=(soup.find_all('tr')[i].find("div",{"id":("ctl00_ctl00_Cphcontent_Cphleftcontent_rptsearch_ctl"+str(i-1)+"_Div2")}).text);print(contact3)
                email=(soup.find_all('tr')[i].find("div",{"id":("ctl00_ctl00_Cphcontent_Cphleftcontent_rptsearch_ctl"+str(i-1)+"_Div3")}).text);print(email)
                domain=(soup.find_all('tr')[i].find("div",{"id":("ctl00_ctl00_Cphcontent_Cphleftcontent_rptsearch_ctl"+str(i-1)+"_Div6")}).text);print(domain)
        #----------------------------------------------Extracting and printing the categories Details--------------------------------------------
                categories1=(soup.find_all('tr')[i].find("div",{"id":("ctl00_ctl00_Cphcontent_Cphleftcontent_rptsearch_ctl"+str(i-1)+"_Div4")}).text);print(categories1)
                categories2=(soup.find_all('tr')[i].find("div",{"id":("ctl00_ctl00_Cphcontent_Cphleftcontent_rptsearch_ctl"+str(i-1)+"_Div5")}).text);print(categories2)
                categories3=(soup.find_all('tr')[i].find_all('td')[2].text.strip()[-15:]).strip();print(categories3)
        #---------------------------------------------Extracting nad printing Types---------------------------------------------
                type1=soup.find_all('tr')[i].find_all('div')[-1:][0].text[0:4];print(type1)
                type2=soup.find_all('tr')[i].find_all('div')[-1:][0].text[4:];print(type2)
        #-------------------------------------------Extracting NAME OF HEAD----------------------------------------------
                print(",Name of head:",(soup.find_all('tr')[i].find_all('td')[-1:][0]).text)
                nameofhead=(soup.find_all('tr')[i].find_all('td')[-1:][0]).text.encode('utf-8')#It is possible that name must not be properly encoded it might throw an UnicodeEncodeError
                nameofhead.decode('utf-8')
        
            
        except AttributeError:#Handelling AttributeError---------------------
            continue
        except UnicodeEncodeError:#Handelling UnicodeEncodeError   and decoding for the better enreichment of the data-----------
            nameofhead=(soup.find_all('tr')[i].find_all('td')[-1:][0]).text.encode('utf-8')
            (nameofhead.decode('utf-8'))
            #printing the properly Decoded data---------------------
    #-------------------------------------Writing the content to the Csv file---------------------------------------
        with open("C://Users/vshan/Desktop/Details.csv","a+") as f:
            l=csv.writer(f)
            l.writerow([[code],[name],[address],[contact1],[contact2],[contact3],[email],[domain],[categories1],[categories2],[categories3],[type1],[type2],[nameofhead.decode('utf-8')]])

except Exception as e:#Handeling Exception and displaying  what type of error do we get if the program is not properly executed.-------------
    print(str(e))
'''-----------------------------------------------------------FINISHED-------------------------------------------------------'''
