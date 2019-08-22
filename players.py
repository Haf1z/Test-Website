#!C:\Users\hafiz666\AppData\Local\Programs\Python\Python37-32\python.exe
#all players info
from Header import *
from dbcon import *


def print_content():

    print('<center><span class="content-heading">List of Players</span> <a class="pull-right btn btn-add" href="addplayer.py"> Add + </a></center> <br>')
    print('<ul class="team-list">')
    con, cur = connect_to_database()
    cur.execute("SELECT * from players")
    players = cur.fetchall()
    for player in players :
        print('<a href="player.py?id=%d"><li> %s </li> </a>' %(player[0],player[1]))
    con.close()
    
    print('</ul>')


if __name__ == "__main__":
    print_headers()
    print_top_of_page("players")
    print_content()
    print_footer()
    
