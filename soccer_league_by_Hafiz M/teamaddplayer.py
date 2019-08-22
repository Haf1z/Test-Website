#!C:\Users\hafiz666\AppData\Local\Programs\Python\Python37-32\python.exe
#this file is about adding new player in team
from Header import *
from dbcon import *
import cgitb; cgitb.enable()
import cgi

def print_form(teamid):
    con, cur = connect_to_database()
    sql = "select * from teams"
    cur.execute(sql)
    
    teams = cur.fetchall()
    
    con.close()

    
    teamsOpt='<select name="team" disabled>'
    for team in teams:
        if teamid == str(team[0]):
            selectedif = 'selected'
        else: 
            selectedif = ""
        
        teamsOpt += '<option value ="'+ str(team[0]) +'" '+ selectedif +'>'+ team[1] +'</option>'
    teamsOpt += '</select>'


    print('<center><span class="content-heading">Add a new player to Team </span></center> <br>')
    print("""<form method="get" action="teamaddplayer.py">
        <fieldset>
        <legend>First name</legend>
        <input type="text" name="fname" >
        </fieldset>
        <fieldset>
        <legend>Last name</legend>
        <input type="text" name="lname" >
        </fieldset>
        <fieldset>
        <legend>E-mail address</legend>
        <input type="text" name="email">
        </fieldset>
        <fieldset>
        <legend>Town</legend>
        <input type="text" name="town">
        </fieldset>
        <fieldset>
        <legend>Team</legend>
        %s
        </fieldset>

        <fieldset>
        <legend>Position</legend>
        <input type="text" name="position">
        </fieldset>
        
        
        <input type ="hidden" name="team" value=%s>
        <input style="margin:10px 0px;" class="btn" type="submit" value="Save" name="b2">
        </form>  """ % (teamsOpt, teamid))


def save_data(fname, lname, email, town, team, position):
    con, cur = connect_to_database()
    sql = "insert into players (first_name, last_name, email, town, team_id, position) VALUES (%s, %s, %s, %s, %s, %s)"
    values = (fname, lname, email, town, team, position)
    cur.execute(sql, values)
    con.commit()
    if cur.rowcount > 0:
        print("saved successfuly<br>")
    else:
        print("Error!<br>")
    con.close()


if __name__ == "__main__":
    print_headers()
    print_top_of_page("teams")
    form = cgi.FieldStorage()
    player_team_pre = form.getvalue("teamid")
    player_fname = form.getvalue("fname")
    player_lname = form.getvalue("lname")
    player_email = form.getvalue("email")
    player_town = form.getvalue("town")
    player_team = form.getvalue("team")
    player_position = form.getvalue("position")

    if form.getvalue("b2") == 'Save' :
        save_data(player_fname, player_lname, player_email, player_town, player_team, player_position)
    # if form.getvalue("b1") == 'submit' :
    # save_data(player_fname, player_lname, player_email, player_town, player_team, player_position)
    # else:
        # print("here it is")
    print_form(player_team_pre)
    print_footer()
    
