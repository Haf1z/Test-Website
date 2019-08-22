#!C:\Users\hafiz666\AppData\Local\Programs\Python\Python37-32\python.exe
#this function is about match details 
from Header import *
from dbcon import *
import cgitb; cgitb.enable()
import cgi

def print_content():
    form = cgi.FieldStorage()
    match_id = form.getvalue("id")
    print('<center><span class="content-heading">Matches Details</span>  </center> <br>')
    
    # print('hello %s' %(player_id))
    con, cur = connect_to_database()
    cur.execute("SELECT m.id, m.team_1_id, m.team_2_id, m.team_1_score, m.team_2_score, m.location, m.date, t1.name, t2.name from matches m JOIN teams t1 on m.team_1_id = t1.id JOIN teams t2 ON m.team_2_id = t2.id  where m.id=%s" % (match_id))
    match = cur.fetchone()
    # print(match)
    print('<center><span style="font-size:22px; margin-top: 10px; color:red;"> %s vs %s </span> </center>' % (match[7], match[8]))
    print('<hr>')
    print('<center><span style="font-size:22px; margin-top: 10px;"> %s : %s </span> </center>' % (match[3], match[4]))
    print('<hr>')
    print('<center><span style="font-size:22px; margin-top: 10px;"> Date : %s </span> </center>' % (match[6]))
    print('<hr>')
    print('<center><span style="font-size:22px; margin-top: 10px;"> Location : %s </span> </center>' % (match[5]))
    print('<hr>')
    print('<a class="btn btn-add pull-right"  href="updatematch.py?matchid=%s"> Update match</a>' % (match_id))
    
    
    con.close()
    
    # print('<center><span class="content-heading">Team: %s</span></center><br>')
    

if __name__ == "__main__":
    print_headers()
    print_top_of_page("matches")
    print_content()
    print_footer()
    
