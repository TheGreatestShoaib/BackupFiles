from subprocess import Popen, PIPE
import random 


def stdout_control(cmd):
    try :
        output = Popen(cmd,shell=True, stdout=PIPE ,stderr=PIPE).communicate()[0]
        # print(output.decode().strip())
        return output.decode().strip()
    
    except:
        pass



icons = random.choice(["🎧 ","🎶","🎵"])


get_album="""dbus-send --print-reply --dest=org.mpris.MediaPlayer2.spotify /org/mpris/MediaPlayer2 org.freedesktop.DBus.Properties.Get string:org.mpris.MediaPlayer2.Player string:Metadata | sed -n '/album/{n;p}' | cut -d '"' -f 2| head -1"""
get_song = """dbus-send --print-reply --dest=org.mpris.MediaPlayer2.spotify /org/mpris/MediaPlayer2 org.freedesktop.DBus.Properties.Get string:org.mpris.MediaPlayer2.Player string:Metadata | sed -n '/title/{n;p}' | cut -d '"' -f 2"""
get_artist = """dbus-send --print-reply --dest=org.mpris.MediaPlayer2.spotify /org/mpris/MediaPlayer2 org.freedesktop.DBus.Properties.Get string:org.mpris.MediaPlayer2.Player string:Metadata | grep -A 4 "albumArtist" | grep string |tail -1 | cut -d '"' -f 2"""


song = stdout_control(get_song)
art = stdout_control(get_artist)
alb = stdout_control(get_album)


if song == "" or art == "":
    print()
else:
    print(f" Playing : {song} by {art}")


