#!C:\Users\hafiz666\AppData\Local\Programs\Python\Python37-32\python.exe
#info about player
from Header import *
from dbcon import *
import cgitb; cgitb.enable()
import cgi

def print_content():
    form = cgi.FieldStorage()
    player_id = form.getvalue("id")
    con, cur = connect_to_database()
    cur.execute("SELECT players.*, teams.name from players left join teams on players.team_id = teams.id where players.id = %s" % (player_id))
    player = cur.fetchone()
    print('<center><span class="content-heading">Player information</span>')
    print('<table class="striptable"> <tr> <th> Name </th> <th> Position </th> <th> Email </th>  <th> Team </th>  <th> town </th> </tr>')
    # for player in players :
    print('<tr> <td> %s %s </td> <td> %s </td> <td>%s </td> <td>%s </td> <td> %s </td>  </tr>' %(player[1], player[2], player[6], player[3], player[7], player[4]))
        # print('<a href="match.py?id=%d"><li> %s </li> </a>' %(team[0],team[1]))
    # print(teams)
    print('</table>')
    con.close()
    
    # print('<center><span class="content-heading">Team: %s</span></center><br>')
    

if __name__ == "__main__":
    print_headers()
    print_top_of_page("players")
    print_content()
    print_footer()
    
