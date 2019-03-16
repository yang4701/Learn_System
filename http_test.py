from socket import *
#创建套接字
s = socket()
s.bind(('127.0.0.1',8000))
s.listen(3)
c,addr = s.accept()#接收浏览器连接
print('Connect from',addr)
data = c.recv(4096)#浏览器发送请求
print(data)
#组织http相应
data = '''HTTP/1.1 200 OK
      Content-Type:text/html
      hello world
      '''

c.send(data.encode())
c.close()
s.close()