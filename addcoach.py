#!C:\Users\hafiz666\AppData\Local\Programs\Python\Python37-32\python.exe
#In this file i am creating a function which adds a new coach
from Header import *
from dbcon import *
import cgitb; cgitb.enable()
import cgi

def print_form():
    '''adding new coach with this function'''

    print('<center><span class="content-heading">Add a new Coach </span></center> <br>')
    print("""<form method="get" action="addcoach.py">
        <fieldset>
        <legend>Coach first name</legend>
        <input type="text" name="fname" >
        </fieldset>
        <fieldset>
        <legend>Coach last name</legend>
        <input type="text" name="lname" >
        </fieldset>
        <fieldset>
        <legend>E-mail address</legend>
        <input type="text" name="email">
        </fieldset>
        
        
        <input style="margin:10px 0px;" class="btn" type="submit" value="Save" name="b1">
        </form>  """)


def save_data(fname, lname, email):
    '''saving data and executing SQL'''
    con, cur = connect_to_database()
    sql = "insert into coaches (first_name, last_name, email) VALUES (%s, %s, %s)"
    values = (fname, lname, email)
    cur.execute(sql, values)
    con.commit()
    if cur.rowcount > 0:
        print("saved successfuly<br>")
    else:
        print("Error!<br>")
    con.close()


if __name__ == "__main__":
    print_headers()
    print_top_of_page("coaches")
    form = cgi.FieldStorage()
    coach_fname = form.getvalue("fname")
    coach_lname = form.getvalue("lname")
    coach_email = form.getvalue("email")
 
    if form.getvalue("b1") == 'Save':
        save_data(coach_fname, coach_lname, coach_email)

    print_form()
    print_footer()
    
