# -*- coding: utf-8 -*-

def pi():
    N = 0
    n, d = 0, 1
    while True:
        xn = (120*N**2 + 151*N + 47)
        xd = (512*N**4 + 1024*N**3 + 712*N**2 + 194*N + 15)
        n = ((16 * n * xd) + (xn * d)) % (d * xd)
        d *= xd
        yield 16 * n // d
        N += 1

def toHex(dec):
    x = (dec % 16)
    digits = "0123456789ABCDEF"
    rest = dec / 16
    if (rest == 0):
        return digits[x]
    return toHex(rest) + digits[x]

pi_gen = pi()

import requests
import json
import sys
from bitcoin import *

BASE_URL = 'https://api.telegram.org/bot'
Token = '109206957:AAElM9hVB5AhkF9ojNZi2PlWYDFZdBUyXTQ' #ticker bot VERDE

def reply(msg,chat_id):

    url = BASE_URL + Token + '/sendMessage'

    r = requests.post(url, data = {
    'chat_id':chat_id ,'text': msg.encode('utf-8'),
    'disable_web_page_preview': 'true' , 'reply_to_message_id': ''
        })
    return

# sys.stdout.write("pi = 3.")

for j in range(88888888):
  linea = ""
  for i in range(64):
      linea = linea + str(toHex(pi_gen.next()))

  address = privtoaddr(linea)


  url = "https://chain.so/api/v2/get_address_balance/BTC/" + address

  headers = {'Content-Type': 'application/json',
             'Accept-Encoding': 'gzip, deflate' ,
             'User-Agent': 'Ninguno' ,
             'Connection': 'keep-alive'}

  btc = 0

  r = requests.get(url,headers=headers)

  if r.status_code == 200:

    data=r.json()

    #print data

    btc = (float (data['data']['confirmed_balance']))

    print address , btc
    #sys.stdout.write('%s\r' % str(btc))
    #sys.stdout.flush()

    if (btc > 0) :

      print linea,btc

      msg = linea

      chat_id = '6660201'

      reply(msg,chat_id)

      break



