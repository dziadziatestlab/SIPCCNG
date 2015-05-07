#debug
import logger
Log=logger.Logger()

import SocketServer
from protocol import sip



class messageHandler(SocketServer.BaseRequestHandler):
    def handle(self):
        Log.d('request message received')
        #Log.i('message parsing')
        message=sip.Message(self.request[0])
        Log.d(message.getSigPart())
        if message.getMethod()=='REGISTER':
            register=sip.REGISTER(message.getSigPart())
            #print register.getHeaders().keys()
            Log.d('Login: '+register.getLogin())

            #test
            response=register.createResponse()
            Log.d('REGISTER RESPONSE: \n'+response)

            socket=self.request[1]
            socket.sendto(response,self.client_address)
        
        
        










if __name__=="__main__":
    HOST,PORT='',5060
    server=SocketServer.UDPServer((HOST,PORT),messageHandler)
    server.serve_forever()


    
