#!C:\Users\hafiz666\AppData\Local\Programs\Python\Python37-32\python.exe
from Header import *
from dbcon import *
import cgitb; cgitb.enable()
import cgi


def print_content():

    print('<center><span class="content-heading">All Matches</span> <a class="pull-right btn btn-add" href="addmatch.py"> Add + </a></center> <br>')
    # print('<ul class="team-list">')
    con, cur = connect_to_database()
    cur.execute("SELECT m.id, m.team_1_id, m.team_2_id, m.team_1_score, m.team_2_score, m.location, m.date, t1.name, t2.name from matches m JOIN teams t1 on m.team_1_id = t1.id JOIN teams t2 ON m.team_2_id = t2.id")
    matches = cur.fetchall()
    print('<table class="striptable"> <tr> <th> Match </th> <th> Goals </th> <th> Location </th> <th> Date </th> <th> Action </th>   </tr>')
    for match in matches :
        print('<tr> <td> %s vs %s </td> <td> %s:%s </td> <td>%s </td> <td> %s </td> <td> <a class="btn btn-add" href="match.py?id=%d">Show </a> </td> </tr>' %(match[7], match[8], match[3], match[4], match[5], match[6], match[0]))
        # print('<a href="match.py?id=%d"><li> %s </li> </a>' %(team[0],team[1]))
    # print(teams)
    con.close()
    print('</table>')
    # print('</ul>')


if __name__ == "__main__":
    print_headers()
    print_top_of_page("matches")
    print_content()
    print_footer()
    
