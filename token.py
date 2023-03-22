import requests
import json
import os,sys,datetime,time

M = '\x1b[1;91m' # MERAH
O = '\x1b[1;96m' # BIRU MUDA
N = '\x1b[0m'    # WARNA MATI
H = '\x1b[1;92m' # HIJAU
K = '\x1b[1;93m' # KUNING

# 100090050337774

P = '\x1b[1;97m' # PUTIH
M = '\x1b[1;91m' # MERAH
H = '\x1b[1;92m' # HIJAU
K = '\x1b[1;93m' # KUNING
B = '\x1b[1;94m' # BIRU
U = '\x1b[1;95m' # UNGU
O = '\x1b[1;96m' # BIRU MUDA
N = '\x1b[0m'    # WARNA YANG UDAH GAK PERAWAN :V
J = '\033[38;2;255;127;0;1m' # ORANGE

dic = {'1':'January','2':'February','3':'March','4':'April','5':'May','6':'June','7':'July','8':'August','9':'September','10':'October','11':'November','12':'December'}
dic2 = {'01':'January','02':'February','03':'March','04':'April','05':'May','06':'June','07':'July','08':'August','09':'September','10':'October','11':'November','12':'Devember'}
tgl = datetime.datetime.now().day
bln = dic[(str(datetime.datetime.now().month))]
thn = datetime.datetime.now().year
hour = datetime.datetime.now().hour
ment = datetime.datetime.now().minute
detk = datetime.datetime.now().second
az = '''

Token:
'''
#--> Pengkondisian Jam Untuk Salam Harian

#os.system("rm -rf akses")
#os.system("mkdir akses")
try:os.mkdir('akses')
except:pass
   
os.system("clear")
print '\x1b[1;93m'
banner = '''
           __                _                 _
          / _| __ _  ___ ___| |__   ___   ___ | | __
         | |_ / _` |/ __/ _ \ '_ \ / _ \ / _ \| |/ /
         |  _| (_| | (_|  __/ |_) | (_) | (_) |   <
         |_|  \__,_|\___\___|_.__/ \___/ \___/|_|\_|
'''
banner1 = '''
\x1b[1;92m                           Author : Ardia Trista
\x1b[1;92m                           Github : github.com/KutuMobaa

'''

print banner
print banner1
user=raw_input('\x1b[1;96m Masukan No/Email : \x1b[1;93m')
passw=raw_input('\x1b[1;96m Password: \x1b[1;93m')
print '\x1b[1;92m'
print " Loading "
time.sleep(0.3)
os.system("clear")
print " lOading "
time.sleep(0.3)
os.system("clear")
print " loAding "
time.sleep(0.3)
os.system("clear")
print " loaDing "
time.sleep(0.3)
os.system("clear")
print " loadIng "
time.sleep(0.2)
os.system("clear")
print " loadiNg "
time.sleep(0.3)
os.system("clear")
print " loadinG "
get = requests.get('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email='+user+'&locale=en_US&password='+passw+'&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
up = get.content
pu = json.loads(up)
if "session_key" in up:
    print ' '
    print '\x1b[1;93m Berhasil Login '
    time.sleep(1)
    os.system("clear")
    print '\x1b[1;93m'
    print banner
    print '\x1b[1;97m'
    print " Sekarang Pukul \x1b[1;92m"+str(hour)+': '+str(ment)+"\x1b[1;97m Menit"
    print ''
    print '\x1b[1;92m email: \x1b[1;95m' + pu['identifier']
    print ' '
    time.sleep(1)
    print '\x1b[1;92m token: \x1b[1;95m'+ pu["access_token"]
#    open('akses/token.txt', 'a').write(pu["access_token"]+(az))
    open('akses/'+str(tgl)+'-'+str(bln)+'-'+str(thn)+'-token.txt', 'a').write(pu["access_token"]+(az))
    print " "
#    print '  token tersimpan di '+str(tgl)+'-'+str(bln)+'-'+str(thn)+'-token.txt'
    print "\x1b[1;92m Token Berhasil Tersimpan Di\x1b[1;93m akses/token.txt"
    print ""
else:
    print ''
    print '\x1b[1;91m maaf username/password salah'
    print ''
