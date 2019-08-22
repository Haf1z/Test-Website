#this file is for header, top of page and footer of my mini website
def print_headers():
    '''this fucntion prints the headers'''
    print("Content-type: text/html\n")    #printing the content type header
def print_top_of_page(active):
    '''this function prints top of the page'''
    print("""
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <meta http-equiv="X-UA-Compatible" content="ie=edge">
            <link type="text/css" rel="stylesheet" href="stylesheet1.css"/>
            <title>Soccer league</title>
            
        </head>
        <body>
            <div class="container">
                <header>
                    <div id="heading"> 
                        <h1>
                            S<img id="imglogo" alt="" src="soccer-ball.png" />ccer league
                        </h1>
                    </div>
                    </table>
                </header>
                <hr>
                <ul id="navs">
                    <li><a class="%s" href="index.py">Home</a></li>
                    <li><a class="%s" href="teams.py">Teams</a></li>
                    <li><a class="%s" href="players.py">Players</a></li>
                    <li><a class="%s" href="matches.py">Matches</a></li>
                    <li><a class="%s" href="coaches.py">Coaches</a></li>
                </ul>
                <div id="content">


                
                

        """% ("active" if active=="home" else "", "active" if active=="teams" else "", "active" if active=="players" else "", "active" if active=="matches" else "",  "active" if active=="coaches" else ""))

def print_footer():
    """this function prints footer of the page"""
    print("""       
                </div>

                    
            </div>
            
        </body>
        </html>
        """)
