from tornado import ioloop, web
import soco
import json

print("restarted")

class YoHandler(web.RequestHandler):
    def get(self, *args, **kwargs):
        username = self.get_argument("username", None, False)
        if username == None:
            self.write("error: no username")
        else:
            self.write("received yo from " + username)
            print("yo from " + username)

        self.finish() #End the HTTP Request, real stuff begins.


class IndexHandler(web.RequestHandler):
    def get(self, *args, **kwargs):
        self.write("Hello World!") #Why not

conf = json.loads(open("conf.json", "r").read())
playlists = json.loads(open("playlists.json", "r").read())




app = web.Application([
    (r'/', IndexHandler),
    (r'/yocall', YoHandler),
    (r'/yocall/([^/]+)', YoHandler),
], debug=True)

if __name__ == '__main__':
    app.listen(conf['portnum'])
    ioloop.IOLoop.instance().start()