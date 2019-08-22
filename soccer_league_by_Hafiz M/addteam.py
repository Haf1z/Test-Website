#!C:\Users\hafiz666\AppData\Local\Programs\Python\Python37-32\python.exe
#in this file I am creating function which adds new team
from Header import *
from dbcon import *
import cgitb; cgitb.enable()
import cgi

def print_form():
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
    statesOpt='<select name="state">'
    for state in states:
        statesOpt += '<option value ="'+ state +'">'+ state+'</option>'
    statesOpt += '</select>'

    con, cur = connect_to_database()
    sql = "select * from coaches"
    cur.execute(sql)
    
    coaches = cur.fetchall()
    
    con.close()

    coachesOpt='<select name="coach">'
    for coach in coaches:
        coachesOpt += '<option value ="'+ str(coach[0]) +'">'+ coach[1] +' '+ coach[2] +'</option>'
    coachesOpt += '</select>'



    print('<center><span class="content-heading">Add a new Team </span></center> <br>')
    print("""<form method="get" action="addteam.py">
        <fieldset>
        <legend>Team name</legend>
        <input type="text" name="name" >
        </fieldset>
        <fieldset>
        <legend>E-mail address</legend>
        <input type="text" name="email">
        </fieldset>
        <fieldset>
        <legend>City</legend>
        <input type="text" name="city">
        </fieldset>
        <fieldset>
        <legend>State</legend>
        %s
        </fieldset>
        <fieldset>
        <legend>Logo URL</legend>
        <input type="text" name="url">
        </fieldset>
        
        <fieldset>
        <legend>Coach</legend>
        %s
        </fieldset>
        
        
        <input style="margin:10px 0px;" class="btn" type="submit" value="Save" name="b1">
        </form>  """ % (statesOpt, coachesOpt))


def save_data(name, email, city, state, url, coach):
    con, cur = connect_to_database()
    sql = "insert into teams (name, email, city, state, logo_url, coach_id) VALUES (%s, %s, %s, %s, %s, %s)"
    values = (name, email, city, state, url, coach)
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
    team_name = form.getvalue("name")
    team_email = form.getvalue("email")
    team_city = form.getvalue("city")
    team_state = form.getvalue("state")
    team_url = form.getvalue("url")
    team_coach = form.getvalue("coach")

    if form.getvalue("b1") == 'Save' and team_name and team_email and team_city and team_state and team_url and team_coach:
        save_data(team_name, team_email, team_city, team_state, team_url, team_coach)

    print_form()
    print_footer()
    
