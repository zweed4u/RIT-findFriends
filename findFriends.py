#Zachary Weeden
#@zweed4u  search for name in classes listed RIT MyCourses 
#Tested on Python 2.6.6 

import mechanize
import urllib
import cookielib
from bs4 import BeautifulSoup
import html2text
import re
import sys
import StringIO
import getpass
from easygui import passwordbox


try:
    # Browser
    br = mechanize.Browser()

    # Cookie Jar
    cj = cookielib.LWPCookieJar()
    br.set_cookiejar(cj)

    # Browser options
    br.set_handle_equiv(True)


    br.set_handle_gzip(False)


    br.set_handle_redirect(True)
    br.set_handle_referer(True)
    br.set_handle_robots(False)

    # Follows refresh 0 but not hangs on refresh > 0
    br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)

    # User-Agent (this is cheating, ok?)
    br.addheaders = [('User-agent', 'Chrome')]

    # The site we will navigate into, handling it's session
    br.open('https://mycourses.rit.edu/')

    # Inspect name of the form
    '''
    for f in br.forms():
        print f
    '''
    # Select the second (index one) form - the first form is a search query box
    br.select_form(nr=0)





    # User credentials
    #####HANDLE LOGIN CHECKING#####

















    print "     ___ _           _ _______    _                 _   "   
    print "    / __|_)         | (_______)  (_)               | |   "  
    print "  _| |__ _ ____   __| |_____ ____ _ _____ ____   __| | ___" 
    print " (_   __) |  _ \ / _  |  ___) ___) | ___ |  _ \ / _  |/___)"
    print "   | |  | | | | ( (_| | |  | |   | | ____| | | ( (_| |___ |"
    print "   |_|  |_|_| |_|\____|_|  |_|   |_|_____)_| |_|\____(___/ "

    print "         _         _   ____ _ _ _              _   __   _ _"
    print "        | |_  _ _ <_> |_  /| | | | ___  ___  _| | /. | | | |"
    print "        | . \| | | _   / / | | | |/ ._>/ ._>/ . |/_  .|| ' |"
    print "        |___/`_. |<_> /___||__/_/ \___.\___.\___|  |_| `___'"
    print "             <___'                                          "
    print "\n"
    
    username = raw_input("Username: ")
    print "Password: "
    password = passwordbox("Password: ")

    #password = getpass.getpass() #-> echos pass with IDLE
    #password = raw_input("Password: ") -> echos pass


    br.form['username'] = username
    br.form['password'] = password


    # Login
    br.submit()









    #Prints html of main page after login
    #print(br.open('https://mycourses.rit.edu/d2l/lp/ouHome/defaultHome.d2l').read()) 


    regex = '<a class="vui-link vui-outline d2l-link d2l-left" href="(.+?)" title="(.+?)">(.+?)</a>'
    pattern = re.compile(regex)


    regex2 = '<a class="vui-outline" onclick="EmailUser((.+?));;return false;" href="javascript://" title="(.+?)">(.+?)</a>'
    pattern2 = re.compile(regex2)



    ###USE IN WHILE LOOP TO PRINT OUT STR
    ###PROMPT USER FOR HOW MANY CLASSES&&LABS ARE TAKEN AND USE THAT AS COUNTER VAR RATHER THAN i

    htmltext = br.open('https://mycourses.rit.edu/d2l/lp/ouHome/defaultHome.d2l').read()
    classes = re.findall(pattern,htmltext)

    noClass = int(input("How Many Classes/Labs/Recitations are taken? "))
    print "\n"

    class1 = []
    class2 = []
    class3 = []
    class4 = []
    class5 = []
    class6 = []
    class7 = []
    class8 = []
    class9 = []
    class10 = []
    class11 = []
    class12 = []
    
    '''
    class1Name = "Unavailable"
    class2Name = "Unavailable"
    class3Name = "Unavailable"
    class4Name = "Unavailable"
    class5Name = "Unavailable"
    class6Name = "Unavailable"
    class7Name = "Unavailable"
    class8Name = "Unavailable"
    class9Name = "Unavailable"
    class10Name = "Unavailable"
    class11Name = "Unavailable"
    class12Name =  "Unavailable"
    '''        
    linkToList = []
    #urls = []
    i = 0
    print "Classes that are under consideration: \n"
    while i < noClass:   # 9 = 9 classes/labs
        j = 0
        
        
        course = str(classes[i]).split("', '")[1]
        course = str(course).split("Enter ")[1]
        '''
        PRINTS HEADER FOR COURSE
        '''
        print course
        print "================================================"
        
        if i == 0:
            class1.append(course)
            class1Name = course
        if i == 1:
            class2.append(course)
            class2Name = course
        if i == 2:
            class3.append(course)
            class3Name = course
        if i == 3:
            class4.append(course)
            class4Name = course
        if i == 4:
            class5.append(course)
            class5Name = course
        if i == 5:
            class6.append(course)
            class6Name = course
        if i == 6:
            class7.append(course)
            class7Name = course
        if i == 7:
            class8.append(course)
            class8Name = course
        if i == 8:
            class9.append(course)
            class9Name = course
        if i == 9:
            class10.append(course)
            class10Name = course
        if i == 10:
            class11.append(course)
            class11Name = course
        if i == 11:
            class12.append(course)
            class12Name = course



        classLink = str(classes[i]).split("('")[1]
        classLink =  str(classLink).split("',")[0]
        classId =  str(classLink).split("=")[1]
        listLink = "https://mycourses.rit.edu/d2l/lms/classlist/classlist.d2l?ou="+str(classId)
        linkToList.append(listLink)



        rosterPage = br.open(str(linkToList[i])).read()
        rosterNames = re.findall(pattern2,rosterPage)

        

        ###WHILE LOOP NEEDED TO GET LEN OF CLASSLIST AND PRINT EACH
        while j < len(rosterNames): # no of students
            name = str(rosterNames[j]).split("Compose email to ")[1]
            name = str(name).split("', ")[0]
            if i == 0:
                class1.append(name)
            if i == 1:
                class2.append(name)
            if i == 2:
                class3.append(name)
            if i == 3:
                class4.append(name)
            if i == 4:
                class5.append(name)
            if i == 5:
                class6.append(name)
            if i == 6:
                class7.append(name)
            if i == 7:
                class8.append(name)
            if i == 8:
                class9.append(name)
            if i == 9:
                class10.append(name)
            if i == 10:
                class11.append(name)
            if i == 11:
                class12.append(name)
            #PRINTS INDIVIDUAL NAMES
            #print str(name) #+ "\n"
            
            j+=1
        #HELPS KEEP DISPLAY CLEAN
        #print "\n"
        i+=1



    '''
    #### PRINT ARRAYS OF CLASS ROSTERS ####
    if not class1:
        print "Class1 Array wasn't able to be populated."
    else:
        print class1Name
        print class1
    print "\n"
    
    if not class2:
        print "Class2 Array wasn't able to be populated."
    else:
        print class2Name
        print class2
    print "\n"
    
    if not class3:
        print "Class3 Array wasn't able to be populated."
    else:
        print class3Name
        print class3
    print "\n"
    
    if not class4:
        print "Class4 Array wasn't able to be populated."
    else:
        print class4Name
        print class4
    print "\n"
    
    if not class5:
        print "Class5 Array wasn't able to be populated."
    else:
        print class5Name
        print class5
    print "\n"
    
    if not class6:
        print "Class6 Array wasn't able to be populated."
    else:
        print class6Name
        print class6
    print "\n"
    
    if not class7:
        print "Class7 Array wasn't able to be populated."
    else:
        print class7Name
        print class7
    print "\n"
    
    if not class8:
        print "Class8 Array wasn't able to be populated."
    else:
        print class8Name
        print class8
    print "\n"
    
    if not class9:
        print "Class9 Array wasn't able to be populated."
    else:
        print class9Name
        print class9
    print "\n"
    
    if not class10:
        print "Class10 Array wasn't able to be populated."
    else:
        print class10Name
        print class10
    print "\n"
    
    if not class11:
        print "Class11 Array wasn't able to be populated."
    else:
        print class11Name
        print class11
    print "\n"
    
    if not class12:
        print "Class12 Array wasn't able to be populated."
    else:
        print class12Name
        print class12
    '''

    print "\n"


    counter = 0
    findname = raw_input("Search for name of friend as shown on MyCourses (eg. John Doe): ")
    print "\n"

    if findname in class1:
        print str(findname) +" is in " + str(class1Name) + " with you."
        counter +=1
    if findname in class2:
        print str(findname) +" is in " + str(class2Name) + " with you."
        counter +=1
    if findname in class3:
        print str(findname) +" is in " + str(class3Name) + " with you."
        counter +=1
    if findname in class4:
        print str(findname) +" is in " + str(class4Name) + " with you."
        counter +=1
    if findname in class5:
        print str(findname) +" is in " + str(class5Name) + " with you."
        counter +=1
    if findname in class6:
        print str(findname) +" is in " + str(class6Name) + " with you."
        counter +=1
    if findname in class7:
        print str(findname) +" is in " + str(class7Name) + " with you."
        counter +=1
    if findname in class8:
        print str(findname) +" is in " + str(class8Name) + " with you."
        counter +=1
    if findname in class9:
        print str(findname) +" is in " + str(class9Name) + " with you."
        counter +=1
    if findname in class10:
        print str(findname) +" is in " + str(class10Name) + " with you."
        counter +=1
    if findname in class11:
        print str(findname) +" is in " + str(class11Name) + " with you."
        counter +=1
    if findname in class12:
        print str(findname) +" is in " + str(class12Name) + " with you."
        counter +=1
    allClassAndName = class1+class2+class3+class4+class5+class6+class7+class8+class9+class10+class11+class12

    if findname not in allClassAndName:
        counter = 0
        print "'"+str(findname) + "'" + " is not in any of your searched classes.\nTry inputting exact name as shown in MyCourses. (Case-sensitive)"

    
    print "\n"
    print str(findname) +" is in " + str(counter) + " classes with you."

        
####### Instead of going here, use unique 6 digit number and append to url
    '''
    classtext = br.open(str(urls[i])).read()

    classList = re.findall(pattern2,classtext)

    #print classList[2]
    if i==8:        # Conditonal neede because not all classes have classlist tab in same area
        listLink = str(classList[0]).split("('")[1]
        listLink = str(listLink).split("',")[0]
    else:
        listLink = str(classList[2]).split("('")[1]
        listLink = str(listLink).split("',")[0]
    listLink = "https://mycourses.rit.edu"+str(listLink)
    linkToList.append(listLink)

    print linkToList[i]
    '''

        




except:
    print "~~~Exception Thrown! Most likely incorrect login credentials.~~~"
