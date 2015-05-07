import re

def parseMessage(message):
    tmpHeaders={}
    #print 'parse message \n'+message
    pattern=re.compile(r'^([\w|\-]*):(.*)',re.M)
    r=pattern.findall(message)
    for h,v in r:
        tmpHeaders[h]=v
    #print tmpHeaders
    return tmpHeaders

def parseLogin(contact):
    p=re.compile(r'<sip:([\w|\.]*)@*')
    r=p.findall(contact)
    #print r[0]
    return r[0]
    
                    
                       
    
    
