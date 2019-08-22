#!C:\Users\hafiz666\AppData\Local\Programs\Python\Python37-32\python.exe
from Header import *
from dbcon import *
import cgitb; cgitb.enable()
import cgi


def print_content():
    form = cgi.FieldStorage()
    coach_id = form.getvalue("id")
    con, cur = connect_to_database()
    cur.execute("SELECT coaches.*, teams.name from coaches left join teams on coaches.id = teams.coach_id where coaches.id=%s" % (coach_id))
    coach = cur.fetchone()
    print('<center><span class="content-heading">Coach information</span>')
    print('<table class="striptable"> <tr> <th> Name </th> <th> Team </th> <th> Email </th> </tr>')
    print('<tr> <td> %s %s </td> <td> %s </td> <td>%s </td>  </tr>' %(coach[1], coach[2], coach[4], coach[3]))
    print('</table>')
    con.close()
    



if __name__ == "__main__":
    print_headers()
    print_top_of_page("coaches")
    print_content()
    print_footer()
    
