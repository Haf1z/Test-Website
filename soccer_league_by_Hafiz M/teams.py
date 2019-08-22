#!C:\Users\hafiz666\AppData\Local\Programs\Python\Python37-32\python.exe
from Header import *
from dbcon import *

def print_content():

    print('<center><span class="content-heading">List of Teams</span> <a class="pull-right btn btn-add" href="addteam.py"> Add + </a></center> <br>')
    print('<ul class="team-list">')
    con, cur = connect_to_database()
    cur.execute("SELECT * from teams")
    teams = cur.fetchall()
    for team in teams :
        print('<a href="team.py?id=%d"><li> %s </li> </a>' %(team[0],team[1]))
    # print(teams)
    con.close()
    
    print('</ul>')

if __name__ == "__main__":
    print_headers()
    print_top_of_page("teams")
    print_content()
    print_footer()
    
