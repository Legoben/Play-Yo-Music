from tornado import ioloop, web
import soco
import json
import  random
print("restarted")



class YoHandler(web.RequestHandler):
    def addTrack(self, track):
        #kwargs = {'album': track.album, 'album_art_uri': track.album_art_uri, 'creator': track.creator,
        #      'original_track_number': track.original_track_number}
        #content = {'uri': track.uri + "#" + str(random.randint(0,99999)), 'title': track.title, 'parent_id': track.parent_id}
        #content.update(kwargs)

        #print(track.title)

        #ntrack = soco.data_structures.MLTrack(track.uri + "#" + str(random.randint(0,99999)), track.title, track.parent_id, **kwargs)

        #ntrack.item_id = track.parent_id + ":" + str(random.randint(0,99999))



        try:
            player.add_to_queue(track)
        except Exception as e:
            print("first failed", e)
            player.add_uri_to_queue(track.uri)
        finally:
            pass




    def get(self, *args, **kwargs):
        username = self.request.path[1:] #Where the Yo was sent

        yofrom = self.get_argument("username", None, False)
        if yofrom == None:
            self.write("error: no username")
            return
        else:

            print("yo from " + yofrom)

        self.write("hi, yo")
        self.finish() #End the HTTP Request, real stuff begins.

        playlists = json.loads(open("playlists.json", "r").read())

        id = None
        for playlist in playlists:
            if playlist['name'] == username:
                id = playlist['id']
                break

        if id == None:
            print("Playlist not found")
            return
        else:
            print("playlist id: " + id)


        if currlist == id:
            player.pause()
            return


        spl = player.get_sonos_playlists()

        for l in spl:
            if l.item_id == id:
            	if l.title == currlist:
            		player.pause()
            		return
            	
            	currlist = l.title
            	
                player.clear_queue()
                tracks = player.browse(l)

                print(tracks)

                first = tracks.pop()

                print(first)

                self.addTrack(first)


                player.play()

                for track in tracks:
                    self.addTrack(track)

                break









player = soco.discover().pop() #ToDo: User pick which Sonos
currlist = None
#player.play_uri(list.uri)




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