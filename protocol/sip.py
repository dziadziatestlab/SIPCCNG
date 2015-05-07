import utils



_REGISTERRESPONSE=['Via','From','To','Call-ID','CSeq','Contact','Content-Length']




class Message():
    def __init__(self,data):
        self.data=data  #message received from client
        self.sig=None   #signaling part of message
        self.body=None  #body part of message
        self.sig,self.body=self.data.split('\r\n\r\n',1)    #signaling and body decomposition
        

        
    def getSigPart(self):
        return self.sig
        
    def getMethod(self):
        self.method,self.value=self.sig.split(' ',1)
        return self.method
    




class REGISTER():
    def __init__(self,data):
        self.data=data
        self.headers=dict
        if data!=None:
            self.headers=utils.parseMessage(data)

    def getHeaders(self):
        return self.headers

    def getLogin(self):
        return utils.parseLogin(self.headers['Contact'])

    def createResponse(self):
        response='SIP/2.0 200 OK\n'
        for i in _REGISTERRESPONSE:
            response+=i+":"+self.headers[i]+"\n"
        return response+'\r\n\r\n'
        
                                
        
        

        
