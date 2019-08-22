#!C:\Users\hafiz666\AppData\Local\Programs\Python\Python37-32\python.exe
#this file about each team information
from Header import *
from dbcon import *
import cgitb; cgitb.enable()
import cgi

def print_content():
    form = cgi.FieldStorage()
    team_id = form.getvalue("id")
    con, cur = connect_to_database()
    # cur.execute("SELECT Count(case when winner = %s then 1 end) as wins from matches where %s in (team_1_id, team_2_id)" % (team_id ,team_id))
    cur.execute("SELECT teams.*, coaches.first_name, coaches.last_name from teams left join coaches on teams.coach_id = coaches.id  where teams.id = %s" % (team_id))
    team = cur.fetchone()
    
    cur.execute("SELECT count(*) as played,Count(case when winner = %s then 1 end) as wins from matches where %s in (team_1_id, team_2_id)" % (team_id ,team_id))
    
    data = cur.fetchall()
    data = data[0]
    winrate = 0
    try:
        winrate = data[1]/data[0] *100
    except ZeroDivisionError:
        pass

    print('<a class="btn btn-add pull-right" href="teamaddplayer.py?teamid=%s">Add Player</a> <a class="btn btn-add pull-right" href="editteam.py?teamid=%s">Edit</a>' % (team_id, team_id))
    print('<img src="%s" class="team-logo">'% (team[5]))
    print('<span><strong> Team name:  </strong> %s </span> <br>' % (team[1]))
    print('<span><strong> City:  </strong> %s, %s </span> <br>' % (team[3], team[4]))
    print('<span><strong> Email:  </strong> %s </span> <br>' % (team[2]))
    print('<span><strong> Win Percentage:  </strong> %.2f </span> <br>' % (winrate))
    print('<span><strong> Wins:  </strong> %s </span> <br>' % (data[1]))
    print('<span><strong> Losses:  </strong> %s </span> <br>' % (data[0]-data[1]))
    print('<span><strong> Played:  </strong> %s </span> <br>' % (data[0]))
    
    print('<hr>')
    cur.execute("SELECT * from players where team_id = %s" % (team_id))
    players = cur.fetchall()
    print('<table class="striptable"> <tr> <th> Name </th> <th> Position </th> <th> Email </th> </tr>')
    for player in players :
        print('<tr> <td> %s %s </td> <td> %s </td> <td>%s </td> </tr>' %(player[1], player[2], player[6], player[3]))
        # print('<a href="match.py?id=%d"><li> %s </li> </a>' %(team[0],team[1]))
    # print(teams)
    con.close()
    print('</table>')
    
    print('<table class="striped">')
    # con.close()
    
    # print('<center><span class="content-heading">Team: %s</span></center><br>')
    

if __name__ == "__main__":
    print_headers()
    print_top_of_page("teams")
    print_content()
    print_footer()
    
