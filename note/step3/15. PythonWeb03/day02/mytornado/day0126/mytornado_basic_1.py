# 孙　伟　

# CTRL+Y 删除一行
# CTRL+D 复制一行

# ｔｏｒｎａｄｏ最基本的功能演示

# ALT+ENTER 万能提示

import tornado
from tornado.httpserver import HTTPServer
from tornado.ioloop import IOLoop
from tornado.web import Application, RequestHandler

# 用来响应用户请求
class IndexHandler(RequestHandler):
    #响应以ｇｅｔ方式发起的请求
    def get(self, *args, **kwargs):
        #　服务器给浏览器的响应内容
        self.write('hello aid1710')
    #响应以post方式发起的请求
    def post(self, *args, **kwargs):
        pass


#创建Ａｐｐｌｉｃａｔｉｏｎ对象，进行若干个对服务器的设置
#例如：路由列表，模板路径，静态资源路径等
app = Application([('/',IndexHandler)])
#创建服务器程序
server = HTTPServer(app)
#服务器监听某个端口(建议使用１００００以上的端口)
server.listen(8888)#10000
#启动服务器（在当前进程中启动服务器）
IOLoop.current().start()


