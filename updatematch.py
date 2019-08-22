#!C:\Users\hafiz666\AppData\Local\Programs\Python\Python37-32\python.exe
#in this file i update matches between teams
from Header import *
from dbcon import *
import cgitb; cgitb.enable()
import cgi

def print_form(matchid):
    con, cur = connect_to_database()

    cur.execute("SELECT m.id, m.team_1_id, m.team_2_id, m.team_1_score, m.team_2_score, m.location, m.date, t1.name, t2.name from matches m JOIN teams t1 on m.team_1_id = t1.id JOIN teams t2 ON m.team_2_id = t2.id  where m.id=%s" % (matchid))
    match = cur.fetchone()    
    con.close()

    
    print('<center><span class="content-heading">Update Match</span></center> <br>')
    print("""<form method="get" action="updatematch.py">
        <fieldset>
        <legend>%s score</legend>
        <input type="text" name="score1" value="%s">
        </fieldset>
        <fieldset>
        <legend>%s score</legend>
        <input type="text" name="score2" value="%s">
        </fieldset>
        
        <input type="hidden" name="matchid" value ="%s">
        <input style="margin:10px 0px;" class="btn" type="submit" value="Save" name="b1">
        </form>  """ % (match[7], match[3], match[8], match[4], match[0]))


def save_data(score1, score2, matchid):
    con, cur = connect_to_database()
    cur.execute('select * from matches where id = %s' % (matchid))
    match = cur.fetchone()
    if score1 > score2:
        winner = match[1]
    elif score2 > score1:
        winner = match[2]
    else:
        winner = "NULL"
    sql = "update matches set team_1_score = %s , team_2_score = %s, winner = %s where id = %s"
    values = (score1, score2, winner, matchid)
    cur.execute(sql, values)
    con.commit()
    if cur.rowcount > 0:
        print("saved successfuly<br>")
    else:
        print("Error!<br>")
    con.close()


if __name__ == "__main__":
    print_headers()
    print_top_of_page("matches")
    form = cgi.FieldStorage()
    match_id_pre = form.getvalue("matchid")
    team_1_score = form.getvalue("score1")
    team_2_score = form.getvalue("score2")
    
    if form.getvalue("b1") == 'Save' :
        save_data(team_1_score, team_2_score, match_id_pre)

    print_form(match_id_pre)
    print_footer()
    
