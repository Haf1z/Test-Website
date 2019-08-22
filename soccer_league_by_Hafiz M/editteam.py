#!C:\Users\hafiz666\AppData\Local\Programs\Python\Python37-32\python.exe
#in this function i am creating function that editing teams
from Header import *
from dbcon import *
import cgitb; cgitb.enable()
import cgi

def print_form(teamid):
    states = {

         'Alabama','Alaska','Arizona','Arkansas','California','Colorado',
         'Connecticut','Delaware','Florida','Georgia','Hawaii','Idaho', 
         'Illinois','Indiana','Iowa','Kansas','Kentucky','Louisiana',
         'Maine' 'Maryland','Massachusetts','Michigan','Minnesota',
         'Mississippi', 'Missouri','Montana','Nebraska','Nevada',
         'New Hampshire','New Jersey','New Mexico','New York',
         'North Carolina','North Dakota','Ohio',    
         'Oklahoma','Oregon','Pennsylvania','Rhode Island',
         'South  Carolina','South Dakota','Tennessee','Texas','Utah',
         'Vermont','Virginia','Washington','West Virginia',
         'Wisconsin','Wyoming'
    }

    con, cur = connect_to_database()

    sql = "select * from teams where id = "+ str(teamid)
    cur.execute(sql)
    
    team = cur.fetchone()

    statesOpt='<select name="state">'
    for state in states:
        if state == str(team[4]):
            selectedif = 'selected'
        else: 
            selectedif = ""

        statesOpt += '<option value ="'+ state +'" '+ selectedif +'>'+ state+'</option>'
    statesOpt += '</select>'

    
    sql = "select * from coaches"
    cur.execute(sql)
    
    coaches = cur.fetchall()
    
    con.close()

    coachesOpt='<select name="coach">'
    for coach in coaches:
        if coach[0] == team[6]:
            selectedif = 'selected'
        else: 
            selectedif = ""
        coachesOpt += '<option value ="'+ str(coach[0]) +'" '+ selectedif +'>'+ coach[1] +' '+ coach[2] +'</option>'
    coachesOpt += '</select>'



    print('<center><span class="content-heading">Edit Team </span></center> <br>')
    print("""<form method="get" action="editteam.py">
        <fieldset>
        <legend>Team name</legend>
        <input type="text" name="name" value="%s">
        </fieldset>
        <fieldset>
        <legend>E-mail address</legend>
        <input type="text" name="email" value="%s">
        </fieldset>
        <fieldset>
        <legend>City</legend>
        <input type="text" name="city" value="%s">
        </fieldset>
        <fieldset>
        <legend>State</legend>
        %s
        </fieldset>
        <fieldset>
        <legend>Logo URL</legend>
        <input type="text" name="url" value="%s">
        </fieldset>
        
        <fieldset>
        <legend>Coach</legend>
        %s
        </fieldset>
        
        <input type="hidden" name="teamid" value ="%s">
        <input style="margin:10px 0px;" class="btn" type="submit" value="Save" name="b1">
        </form>  """ % (team[1], team[2], team[3], statesOpt, team[5], coachesOpt, team[0]))


def save_data(name, email, city, state, url, coach, teamid):
    con, cur = connect_to_database()
    sql = "update teams set name = %s , email = %s , city = %s , state = %s , logo_url = %s , coach_id = %s  where id = %s"
    values = (name, email, city, state, url, coach, teamid)
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
    team_id_pre = form.getvalue("teamid")
    team_name = form.getvalue("name")
    team_email = form.getvalue("email")
    team_city = form.getvalue("city")
    team_state = form.getvalue("state")
    team_url = form.getvalue("url")
    team_coach = form.getvalue("coach")

    if form.getvalue("b1") == 'Save' and team_name and team_email and team_city and team_state and team_url and team_coach:
        save_data(team_name, team_email, team_city, team_state, team_url, team_coach, team_id_pre)

    print_form(team_id_pre)
    print_footer()
    
