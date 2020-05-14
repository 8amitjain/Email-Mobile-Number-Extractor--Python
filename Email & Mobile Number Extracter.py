import re,pyperclip

# create regex for phone number
def phone(num):
    number=re.compile(r'''

(
((\d\d\+)|(\d\d)|(\d\d\s))? #area code types 91+ or 9182... or 91 82....

(\d\d\d\d\d\d\d\d\d\d)  
)

''',re.VERBOSE)
    numberfound=number.findall(num)
    return numberfound

# create regex for mail

def findmail(mail):
    email=re.compile(r'''
            
(               
[a-zA-Z0-9_+.-]+   #name          #[a-zA-z0-9_+.]+ ==word eg "abcd.2381"@gmail.com
@                  #@symbol       # @  == @ in abcd"@"gmail.com
[a-zA-Z0-9_+.-]+   # domain name  #[a-zA-z0-9_+.]+ == gmail in abcd@"gmail.com"

)

''',re.VERBOSE)
    emailfound=email.findall(mail)
    return emailfound
#Paste text
text=pyperclip.paste()


#Extract email/phone
numberfound=phone(text)
emailfound=findmail(text)

#Sort the data
allsortedPhone=[ y[0] for y in numberfound]
allsortedemail=[x for x in emailfound]# no need of this 

#Copy text
Result='\n'.join(allsortedPhone)+'\n\n'+'\n'.join(allsortedemail)
pyperclip.copy(Result)








