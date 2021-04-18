def dnsTranslate(serverName):
  if(serverName == 1):
    dest = ('127.0.0.1', 3000)
    return dest
  else:
    dest = ('127.0.0.1', 3001)
    return dest