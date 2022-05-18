from flask import render_template,request,redirect,url_for
from . import main
from ..requests import get_quotes
from ..models import Quote

#Displaying views function
@main.route('/')
def index():
    #home page
    todays_quote = get_quotes()

    title= 'Welcome to Insyder'
    return render_template('index.html',title=title,todays_quote=todays_quote)

