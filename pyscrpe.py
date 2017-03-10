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
    f=open("C://Users/vshan/Desktop/Details.csv","a+")#Opening and writing the Head contents to the file--------------------
    f.write("SCHOOL NAME / CODE / ADDRESS               CONTACT DETAILS                         CATEGORIES                TYPE                              NAME OF THE HEAD")
    f.write('\n\n')
    f.close()#file close ------------
    for i in range(1,len(soup.find_all('tr'))):
        #--------------------Extracting First column of the table and printing----------------------------
        a=(soup.find_all('tr')[i].text.strip()[:6].strip());print(a)#extracting school code and printing
        b=(soup.find_all('tr')[i].text.strip()[39:82].strip());print(b)#extracting school name and printing
        c=(soup.find_all('tr')[i].text.strip()[150:400].strip());print(c)#extracting school address and printng
        #---------------------Extracting the rest of the column with Exceptional handeling and printing-------------------------------------
        try:
            if i<10:
    #-----------------------------------------------Extracting the contact informations---------------------------------------------------
                d=(soup.find_all('tr')[i].find("div",{"id":("ctl00_ctl00_Cphcontent_Cphleftcontent_rptsearch_ctl0"+str(i-1)+"_Div1")}).text);print(d)
                e=(soup.find_all('tr')[i].find("div",{"id":("ctl00_ctl00_Cphcontent_Cphleftcontent_rptsearch_ctl0"+str(i-1)+"_Div2")}).text);print(e)
                f1=(soup.find_all('tr')[i].find("div",{"id":("ctl00_ctl00_Cphcontent_Cphleftcontent_rptsearch_ctl0"+str(i-1)+"_Div3")}).text);print(f1)
                g=(soup.find_all('tr')[i].find("div",{"id":("ctl00_ctl00_Cphcontent_Cphleftcontent_rptsearch_ctl0"+str(i-1)+"_Div6")}).text);print(g)
            #-------------------------------------------Extracting Categories----------------------------------------------------------
                h=(soup.find_all('tr')[i].find("div",{"id":("ctl00_ctl00_Cphcontent_Cphleftcontent_rptsearch_ctl0"+str(i-1)+"_Div4")}).text);print(h)
                i1=(soup.find_all('tr')[i].find("div",{"id":("ctl00_ctl00_Cphcontent_Cphleftcontent_rptsearch_ctl0"+str(i-1)+"_Div5")}).text);print(i1)
            #----------------------------------------------Extracting Types-----------------------------------------------------------------
                j=(soup.find_all('tr')[i].find_all('div')[-1:][0].text)[0:4];print(j)
                k=(soup.find_all('tr')[i].find_all('div')[-1:][0].text)[4:];print(k)
                y=(soup.find_all('tr')[i].find_all('td')[2].text.strip()[-15:]).strip();print(y)
            #---------------------------------------------------Extracting NAME OF THE HEAD------------------------------------------------------
                print((soup.find_all('tr')[i].find_all('td')[-1:][0]).text)
                m=(soup.find_all('tr')[i].find_all('td')[-1:][0]).text.encode('utf-8');#It might throw an UnicodeEncodeError due to encoding error
                m.decode('utf-8')
                
                
            else:
    #----------------------------------------------------Extracting Contact Informations and prnting----------------------------------
                d=(soup.find_all('tr')[i].find("div",{"id":("ctl00_ctl00_Cphcontent_Cphleftcontent_rptsearch_ctl"+str(i-1)+"_Div1")}).text);print(d)
                e=(soup.find_all('tr')[i].find("div",{"id":("ctl00_ctl00_Cphcontent_Cphleftcontent_rptsearch_ctl"+str(i-1)+"_Div2")}).text);print(e)
                f1=(soup.find_all('tr')[i].find("div",{"id":("ctl00_ctl00_Cphcontent_Cphleftcontent_rptsearch_ctl"+str(i-1)+"_Div3")}).text);print(f1)
                g=(soup.find_all('tr')[i].find("div",{"id":("ctl00_ctl00_Cphcontent_Cphleftcontent_rptsearch_ctl"+str(i-1)+"_Div6")}).text);print(g)
        #----------------------------------------------Extracting and printing the categories Details--------------------------------------------
                h=(soup.find_all('tr')[i].find("div",{"id":("ctl00_ctl00_Cphcontent_Cphleftcontent_rptsearch_ctl"+str(i-1)+"_Div4")}).text);print(h)
                i1=(soup.find_all('tr')[i].find("div",{"id":("ctl00_ctl00_Cphcontent_Cphleftcontent_rptsearch_ctl"+str(i-1)+"_Div5")}).text);print(i1)
        #---------------------------------------------Extracting nad printing Types---------------------------------------------
                j=soup.find_all('tr')[i].find_all('div')[-1:][0].text[0:4];print(j)
                k=soup.find_all('tr')[i].find_all('div')[-1:][0].text[4:];print(k)
                y=(soup.find_all('tr')[i].find_all('td')[2].text.strip()[-15:]).strip();print(y)
        #-------------------------------------------Extracting NAME OF HEAD----------------------------------------------
                print((soup.find_all('tr')[i].find_all('td')[-1:][0]).text)
                m=(soup.find_all('tr')[i].find_all('td')[-1:][0]).text.encode('utf-8')#It is possible that name must not be properly encoded it might throw an UnicodeEncodeError
                m.decode('utf-8')
        
            
        except AttributeError:#Handelling AttributeError---------------------
            continue
        except UnicodeEncodeError:#Handelling UnicodeEncodeError   and decoding for the better enreichment of the data-----------
            m=(soup.find_all('tr')[i].find_all('td')[-1:][0]).text.encode('utf-8')
            (m.decode('utf-8'))
            #printing the properly Decoded data---------------------
    #-------------------------------------Writing the content to the Csv file---------------------------------------
        f=open("C://Users/vshan/Desktop/Details.csv","a+")#location of the file can be changed according to the handeler--------------------
        f.write(a);f.write('                                                      ');f.write(d);f.write('                                      ');f.write(h);f.write('                                    ');f.write(j);f.write('                                         ');f.write(m.decode('utf-8'));f.write('\n')
        f.write(b);f.write('                                            ');f.write(e);f.write('                                       ');f.write(i1);f.write('                                        ');f.write(k);f.write('                                        ');f.write('\n');
        f.write('                                                                 ');f.write(f1);f.write('         ');f.write(y);f.write('\n')      
        f.write('                                                                  ');f.write(g);f.write('\n')
        f.write(c);f.write('\n\n\n\n')
        f.close()#file close----------

except Exception as e:#Handeling Exception and displaying  what type of error do we get if the program is not properly executed.-------------
    print(str(e))
'''----------------------------------------------------FINISHED-------------------------------------------------------'''
