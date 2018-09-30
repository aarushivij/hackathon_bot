def attendance(roll):    
    textFile = open("attendance.txt")
    lines = textFile.readlines()
    aratt=[]
    for i in range(0,len(lines)):
        aratt.append(lines[i].split(" "))
        if(aratt[i][-1][-1]=='\n'):
            aratt[i][-1]=aratt[i][-1][:-1]
    for i in range(0,len(lines)):
        if(roll==aratt[i][0]):
            t=len(aratt[i])-2
            d=0
            for j in range(2,len(aratt[i])):
                if aratt[i][j]=="P":
                    d=d+1
            return "Your Attendance:"+str(int(d*100/t))

def marks(x):
    user="18312032"
    if x=="Subject_1":
        tex=open("Subject_1_mark.txt")
        text=tex.readlines()
        m=[]
        for i in range(0,len(text)):
            m.append(text[i].split(" "))
            if(m[i][-1][-1]=='\n'):
                m[i][-1]=m[i][-1][:-1]
        
        f=-1;
        for i in range(0,len(m)):
            if m[i][0]==user:
                f=i
                break
        if f!=-1:
            return("\nTutorial Marks:"+m[f][2]+"\nPractical Marks:"+m[f][3]+"\nCWS Marks(25% weightage):"+m[f][4]+"\nMTE Marks(25% weightage):"+m[f][5]+"\nETE Marks(50% weightage):"+m[f][6]+"\nCGPA:"+m[f][7])
        else:
            return("\nThis subject is not taken by you")
    else:
        return("Wrong Choice.")

def stat(subject):
    user="18312032"
    if subject=="Subject_1":
        tex=open("Subject_1_stat.txt")
        text=tex.readlines()
        s=[]
        for i in range(0,len(text)):
            s.append(text[i].split(" "))
            if(s[i][-1][-1]=='\n'):
                s[i][-1]=s[i][-1][:-1]

        f=-1;
        for i in range(0,len(s)):
            if s[i][0]==user:
                f=i
                break

        if f!=-1:
            return("Number of Tutorials submitted: "+s[f][2]+"\nNumber of Practicals submitted: "+s[f][3])
        else:
            return("\nThis subject is not taken by you")

    else:
        return("Wrong Choice.")


def profile(profile):
    roll="18312032"
    text = open("stud_profile.txt")
    lines = text.readlines()
    m=[]
    for i in range(0,len(lines)):
        m.append(lines[i].split(" "))
        if(m[i][-1][-1]=='\n'):
            m[i][-1]=m[i][-1][:-1]
    f=-1
    for i in range(0,len(m)):
        if roll==m[i][0]:
            f=i
            break
    if f!=-1:          
        return("\nName:"+m[f][1]+"\nBranch:"+m[f][2]+"\nYear:"+m[f][3]+"\nBhawan:"+m[f][4]+"\nGroups:"+m[f][5]+"\niitr email-id:"+m[f][6])

def groupattendance(group):
    roll="18312032"
    if(group=="SDS_LABS"):
        textFile = open("SDS_class.txt")
        lines = textFile.readlines()
        aratt=[]
        for i in range(0,len(lines)):
            aratt.append(lines[i].split(" "))
            if(aratt[i][-1][-1]=='\n'):
                aratt[i][-1]=aratt[i][-1][:-1]
        d=0
        z=0
        for i in range(0,len(lines)):
            if(roll==aratt[i][0]):
                t=len(aratt[i])-2
                z=z+t
                for j in range(2,len(aratt[i])):
                    if aratt[i][j]=="P":
                        d=d+1
        if(d!=0):
            return "Your attendance: "+ str(int(d*100/z))
        else:
            return("You are not in this group.")
    elif(group=="MDG"):
        textFile = open("MDG_class.txt")
        lines = textFile.readlines()
        aratt=[]
        for i in range(0,len(lines)):
            aratt.append(lines[i].split(" "))
            if(aratt[i][-1][-1]=='\n'):
                aratt[i][-1]=aratt[i][-1][:-1]
        d=0
        z=0
        for i in range(0,len(lines)):
            if(roll==aratt[i][0]):
                t=len(aratt[i])-2
                z=z+t
                for j in range(2,len(aratt[i])):
                    if aratt[i][j]=="P":
                        d=d+1
        if(d!=0):
            return "Your attendance: "+ str(int(d*100/z))
            #print("\n")
        else:
            return("You are not in this group.")
    elif(group=="INFOSEC"):
        textFile = open("INFOSEC_class.txt")
        lines = textFile.readlines()
        aratt=[]
        for i in range(0,len(lines)):
            aratt.append(lines[i].split(" "))
            if(aratt[i][-1][-1]=='\n'):
                aratt[i][-1]=aratt[i][-1][:-1]
        d=0
        z=0
        for i in range(0,len(lines)):
            if(roll==aratt[i][0]):
                t=len(aratt[i])-2
                z=z+t
                for j in range(2,len(aratt[i])):
                    if aratt[i][j]=="P":
                        d=d+1
        if(d!=0):
            return "Your attendance: " + str(int(d*100/z))
        else:
            return("You are not in this group.")
    elif(group=="DSG"):
        textFile = open("DSG_class.txt")
        lines = textFile.readlines()
        aratt=[]
        for i in range(0,len(lines)):
            aratt.append(lines[i].split(" "))
            if(aratt[i][-1][-1]=='\n'):
                aratt[i][-1]=aratt[i][-1][:-1]
        d=0
        z=0
        for i in range(0,len(lines)):
            if(roll==aratt[i][0]):
                t=len(aratt[i])-2
                z=z+t
                for j in range(2,len(aratt[i])):
                    if aratt[i][j]=="P":
                        d=d+1
        if(d!=0):
            return "Your attendance: " + str(int(d*100/z))
        else:
            return("You are not in this group.")
    else:
        return("INVALID SELECTION OF GROUP")

def group_info(grp):
    if grp=="IMG":
        f=open('img.txt','r')
        file_contents = f.read()
        return(file_contents)
    elif grp=="GG":
        f=open('gg.txt','r')
        file_contents = f.read()
        return(file_contents)
    else:
        return("INVALID INPUT !!!")


def sreview(n):
    if (n=="GG"):    
        file1 = open("GG.txt","r+")
        m=file1.read()
        return(m)
        file1.close()
    elif (n=="IMG"):
        file1=open("IMG.txt","r")
        m=file1.read()
        return(m)
        file1.close()

def greview(subject):
    n=subject.split(" ",1)
    if (n[0]=="GG"):    
        file1 = open("GG.txt","a")
        m=file1.write("> ")
        m=file1.write(n[1])
        m=file1.write("\n")
        file1.close()
        return("your review has been successfully added.")
    elif (n[0]=="IMG"):
        file1 = open("IMG.txt","a")
        m=file1.write("> ")
        m=file1.write(n[1])
        m=file1.write("\n")
        file1.close()
        return("your review has been successfully added.")



class hackathon_bot(object):
    '''
    A docstring documenting this bot.
    '''

    def usage(self):
        return '''This bot will have all the students data'''

    def handle_message(self, message, bot_handler):
        query = message['content']
        reply = "Hello"
        if query.startswith("bot attendance"):
            subject = query.split(" ")[2]
            reply = attendance(subject)
        elif query.startswith("bot marks"):
            subject = query.split(" ")[2]
            reply = marks(subject)
        elif query.startswith("bot create review"):
            subject=query.split(" ",3)[3]
            reply=greview(subject)
        elif query.startswith("bot see review"):
            subject=query.split(" ")[3]
            reply=sreview(subject)
        elif query.startswith("bot show"):
            subject=query.split(" ")[2]
            reply=profile(subject)
        elif query.startswith("bot group info"):
            subject=query.split(" ")[3]
            reply=group_info(subject)
        elif query.startswith("bot acad stats"):
            subject=query.split(" ")[3]
            reply=stat(subject)
        elif query.startswith("bot group attendance"):
            subject=query.split(" ")[3]
            reply=groupattendance(subject)


        bot_handler.send_message({
            'type': '',
            'to': '',
            'subject': "",
            'content': reply
        })
        return
handler_class = hackathon_bot