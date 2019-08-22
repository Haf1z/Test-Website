#!C:\Users\hafiz666\AppData\Local\Programs\Python\Python37-32\python.exe
#In this file i am creating function which adds new matches between 2 teams
from Header import *
from dbcon import *
import cgitb; cgitb.enable()
import cgi

def print_form():
    con, cur = connect_to_database()
    sql = "select * from teams"
    cur.execute(sql)
    
    teams = cur.fetchall()
    
    con.close()

    teamsOpt='<select name="team1">'
    for team in teams:
        teamsOpt += '<option value ="'+ str(team[0]) +'">'+ team[1] +'</option>'
    teamsOpt += '</select>'

    teams2Opt='<select name="team2">'
    for team in teams:
        teams2Opt += '<option value ="'+ str(team[0]) +'">'+ team[1] +'</option>'
    teams2Opt += '</select>'
    

    print('<center><span class="content-heading">Create a Match </span></center> <br>')
    print("""<form method="get" action="addmatch.py">
        <fieldset>
        <legend>Select Team 1</legend>
        %s
        </fieldset>
        <fieldset>
        <legend>Select Team 2</legend>
        %s
        </fieldset>
        <fieldset>
        <legend>Location</legend>
        <input type="text" name="location">
        </fieldset>
        <fieldset>
        <legend>Date</legend>
        <input type="date" name="date">
        </fieldset>
        
        <input style="margin:10px 0px;" class="btn" type="submit" value="Save" name="b1">
        </form>  """ % (teamsOpt, teams2Opt))


def save_data(team1id, team2id, location, date):
    con, cur = connect_to_database()
    sql = "insert into matches (team_1_id, team_2_id, team_1_score, team_2_score, location, date) VALUES (%s, %s, %s, %s, %s, %s)"
    values = (team1id, team2id, 0, 0, location, date)
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
    team1_id = form.getvalue("team1")
    team2_id = form.getvalue("team2")
    location = form.getvalue("location")
    match_date = form.getvalue("date")
    if form.getvalue("b1") == 'Save':
        save_data(team1_id, team2_id, location, match_date)

    print_form()
    print_footer()
    
