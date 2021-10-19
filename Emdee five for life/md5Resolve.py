import requests 
import hashlib
import re
import sys
#Fatake

url = "http://206.189.18.74:30800"
r = requests.session()

## Se pide un paquete
paqueteGet = r.get(url)

# Buscando expresion regular
lineaHTML = re.search("<h3 align='center'>+.*?</h3>",paqueteGet.text)

# simplificando regex parte del texto
extract = re.search("'>.*<",lineaHTML[0])

#Obteniendo texto a md5
toMD5 = re.search("[^|'|>|<]...................",extract[0])

# hasheando
md5Text = hashlib.md5(toMD5[0].encode('utf-8')).hexdigest()

# Armado paquete
data={'hash': md5Text}
paquetePost = r.post(url = url, data = data)

flag = re.search("<p align='center'>+.*?</p>",paquetePost.text)

print("[+] Haciendo peticion a 206.189.18.74:30800 : \n {}".format(paqueteGet.text))
print("[+] Encontre texto a sacar md5: {}".format(lineaHTML[0]))
print("[+] Texto to MD5 {}".format(toMD5[0]))
print("[+] MD5{}".format(md5Text[0]))
print("[+] Salida final {}".format(paquetePost.text))
print("[+] Flag {}".format(flag))

