import struct
import arcade

def read_header(f):
    buffer = f.read(8)
    return struct.unpack("LL",buffer)

def read_rgb(f):
    buffer = f.read(3)
    return struct.unpack('BBB',buffer)

def draw_point(x,y,r,g,b,win_height):
    arcade.draw_point(x, win_height-y,(r,g,b),1)

def draw_pic(filename):
    with open (filename, 'rb') as f:
        w,h = read_header(f)
        arcade.open_window(w,h,filename)
        arcade.set_background_color(arcade.color.BLACK)
        arcade.start_render()
    