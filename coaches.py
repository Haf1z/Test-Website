#!C:\Users\hafiz666\AppData\Local\Programs\Python\Python37-32\python.exe
#list of all coaches
import cgitb; cgitb.enable()
import cgi
from Header import *
from dbcon import *

def print_content():

    print('<center><span class="content-heading">List of coaches</span> <a class="pull-right btn btn-add" href="addcoach.py"> Add + </a></center> <br>')
    print('<ul class="team-list">')
    con, cur = connect_to_database()
    cur.execute("SELECT * from coaches")
    coaches = cur.fetchall()
    for coach in coaches :
        print('<a href="coach.py?id=%d"><li> %s </li> </a>' %(coach[0],coach[1]+" "+coach[2]))
    # print(teams)
    con.close()
    
    print('</ul>')

if __name__ == "__main__":
    print_headers()
    print_top_of_page("coaches")
    print_content()
    print_footer()
    
