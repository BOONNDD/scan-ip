import ipcalc
import socket,random,re
import threading,configparser
import requests,sys,time,os
bg=''

G = bg+'\033[32m'
O = bg+'\033[33m'
GR = bg+'\033[37m'
R = bg+'\033[31m'

os.system('clear')

banner =(G +'''
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣄⣴⣴⣾⣾⣾⣿⣿⣾⣿⣾⣿⣷⣷⣷⣷⣦⣦⣠⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣿⣿⢿⢛⢏⢟⢟⣿⣿⣿⣿⣿⣿⣿⣿⡿⡟⡟⢝⢟⢿⣿⣿⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢼⣿⣏⣔⣴⣰⢄⢌⠘⠽⣿⣿⣿⣿⡿⠏⢃⢡⣠⣢⣢⣌⣻⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣮⡢⣮⣿⣿⣿⣮⢪⣾⣾⣿⣿⣿⣿⣿⣿⣯⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⢿⣟⠽⠊⠊⠊⠫⢻⣾⣿⣿⣿⣷⠻⠙⠘⠘⠚⢽⢿⣿⣿⣯⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣵⣷⣽⣪⣞⣮⣮⣾⣿⣾⣿⣯⣿⣷⣵⣲⣲⣳⣵⣷⣷⣻⣯⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢗⣿⣿⣿⣺⣿⣿⣿⣿⣿⣿⣿⣿⣿⣗⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢽⣿⣿⣿⣿⣿⣿⢟⣿⣽⣟⣿⣿⣿⢾⣾⢿⡻⣿⣿⣿⣿⣿⢿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢘⣷⣕⢭⠹⣾⣾⣿⣿⣏⡻⡽⣟⡟⣏⣿⣿⣿⣾⡾⠍⣕⢧⣿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢿⣷⣝⢦⡈⠟⠟⠟⠏⠁⣠⣦⡀⠈⠛⠟⠟⠟⢁⡾⣣⣿⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⣿⣿⣎⢷⣷⣶⣵⣮⣦⣫⣫⣫⣦⣵⣶⣵⣾⢾⣱⣿⣿⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⢿⣿⣯⣷⣿⣿⣿⣿⡛⠛⣻⣿⣿⣿⣿⣟⣵⣿⡿⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠛⢿⣷⣿⣿⣿⣿⡏⠀⢻⣿⣿⣿⣿⣾⡿⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⢿⣿⣿⣿⡅⠀⣸⣿⣿⣿⠟⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠻⢿⣧⢀⣾⡿⠟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀      ☠⠀MrBOOND⠀️☠⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀Telegram : @BO_NND⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀

\t''')
for chr in banner:
                        sys.stdout.write(chr)
                        sys.stdout.flush()
                        time.sleep(0.001)

def update():
		statement = f"\n {O} [ ➜ ] Do you want to update IP ranges ?{G} "
		for chr in statement:
			sys.stdout.write(chr)
			sys.stdout.flush()
			time.sleep(0.1)
		decision = input(f'[y/n]:{GR} ')
		if decision.upper() == 'Y':
			os.system('rm .firstusage.log')
		else:return 0
		return decision.upper()
		
ipdict ={}
def createlog():
	if os.path.exists('.firstusage.log'):
		arg = 'r'
		updating = update()
		if updating =='Y':
			arg = 'a+'
			status = '  [ ☣ ] update'
	else:
		status = ' ola mae !'
		arg = 'a+'
	with open('.firstusage.log',arg) as f:
			if len(f.read()) < 1:
				input(f'{G}{status}{GR}\n{R}  [ ⚇ ] Switch to wifi or data connection to update the ipranges list and press Enter  {GR}')
				url ='https://www.cloudflare.com/ips-v4'
				req = requests.get(url).text
				ranges = req.split()
				
				input(f'{G}  [ ⚉ ]Turn off wifi or switch to no data\nand press Enter to continue ')
				f.write(str(ranges))
			else:
				with open('.firstusage.log',arg) as f:
					ranges = f.read().replace('[','').replace(']','').replace('\'','').split(',')
	return ranges


def save(x):
	with open('success.txt','a') as fl:
		fl.write(str(x)+'\n')
		fl.close()
		
def scanner(host):
	sock=socket.socket()
	sock.settimeout(2)
	try:
		sock.connect((str(host),80))
		payload='GET / HTTP/1.1\r\nHost: {}\r\n\r\n'.format(host)
		sock.send(payload.encode())
		response=sock.recv(1024).decode('utf-8','ignore')
		for data in response.split('\r\n'):
			data=data.split(':')
			if re.match(r'HTTP/\d(\.\d)?' ,data[0]):
				print('response status : {}{}{}'.format(O,data[0],GR))
			if data[0]=='Server':
				try:
					if data[1] ==' cloudflare':
						print('{}server : {}\nI found work {}..'.format(G,host,GR))
						save(f'{host}')
						payloadsnd(host)
				except Exception as e:
					print(e)
	except Exception as e:print(e)

def auto_replace(server,ip):
	packet = server.recv(1024).decode('utf-8','ignore')
	status = packet.split('\n')[0]
	if re.match(r'HTTP/\d(\.\d)? 101',status):
		print(f'{O}[TCP] response : {G}{status}{GR}')
		save(f'{ip} response ==== {status}')
	else:
		if re.match(r'HTTP/\d(\.\d)? \d\d\d ',status):
			server.send(b'HTTP/1.1 200 Connection established\r\n\r\n')
			print(f'{O}[TCP] response : {R}{status}{GR}')
			return auto_replace(server,ip)

def payloadsnd(ip):
	
	config = configparser.ConfigParser()
	config.read_file(open('configfile.ini'))
	domain = config['websocket']['custom_domain']
	port =80
	sc=socket.socket()
	sc.connect((str(ip),port))
	payload=f'GET / HTTP/1.0[crlf]Host: {domain}[crlf][crlf]'
	payload=payload.replace('[crlf]','\r\n')
	sc.send(payload.encode())
	auto_replace(sc,ip) 
	
def Main():
	ipdict={}
	ranges = createlog()
	for k,v in enumerate(ranges):
			#clr = random.choice([G,GR,O])
			ipdict[k]=v
	for choose in range(len(ipdict)):
		iprange=[]
		cidr=ipdict[choose]	
		print(cidr)
		for ip in ipcalc.Network(cidr):
				iprange.append(ip)
		for index in range(len(iprange)):			
					try:
						print("{}[ ➙ ] also... ({}/{}) [{}]".format(
						R,index+1,len(iprange),iprange[index],GR))
						sc=threading.Thread(target=scanner,args=(iprange[index],))
						sc.start()
					except KeyboardInterrupt:
						print('{}Verification aborted by Noob! {}'.format(R,GR))
						break
						
if __name__=="__main__":
	Main()
