from tornado import ioloop, web
import soco
import json

print("restarted")

class YoHandler(web.RequestHandler):
    def get(self, *args, **kwargs):
        username = self.request.path[1:] #Where the Yo was sent

        yofrom = self.get_argument("username", None, False)
        if yofrom == None:
            self.write("error: no username")
            return
        else:

            print("yo from " + yofrom)

        #self.write("hi, yo")
        #self.finish() #End the HTTP Request, real stuff begins.

        playlists = json.loads(open("playlists.json", "r").read())

        id = None
        for playlist in playlists:
            if playlist['name'] == username:
                id = playlist['id']
                break

        if id == None:
            print("Playlist not found")
            self.write("received yo from " + yofrom + " to " + username + ". Playlist does not exist.")
            return
        else:
            print("playlist id: " + id)
            self.write("received yo from " + yofrom + " to " + username + ". Playlist does exist, id is " + id)
        self.finish()




class IndexHandler(web.RequestHandler):
    def get(self, *args, **kwargs):
        self.write("Hello World!") #Why not

conf = json.loads(open("conf.json", "r").read())
#playlists = json.loads(open("playlists.json", "r").read())




app = web.Application([
    (r'/', IndexHandler),
    #(r'/yocall', YoHandler),
    #(r'/yocall/([^/]+)', YoHandler),
    (r'/([^/]+)', YoHandler),
], debug=True)

if __name__ == '__main__':
    app.listen(conf['portnum'])
    ioloop.IOLoop.instance().start()