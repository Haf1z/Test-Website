#!C:\Users\hafiz666\AppData\Local\Programs\Python\Python37-32\python.exe
#this is the home page in which i imported headers.py which have the template html and css (which is same on every page containing css and navigations) and it opens a div called content and in every page
#i print all of the dynamic data in it and then i closes the div and body and html in a print_footer method in every page. And i use anchor tag to navigate to different pages
import cgitb; cgitb.enable()
import cgi
import sys, os
from Header import *

if __name__ == "__main__":
    print_headers()
    print_top_of_page("home")
    # print('hello')
    print('<img class="home-img" src="soccer-ball.png"/> ')
    print_footer()
    
