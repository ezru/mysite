#from django.shortcuts import render
from django.http import HttpResponse
from django.utils.html import escape
from django.views import View

def index(request):
    response = """<h1> Money Manager </h1> <p><b>Hello peeps</b>, this is monenry manager website!</p>"""
    return HttpResponse(response)

def rest(request, guess):
    response = """<html><body>

    <h1> We are in Rest</h1>
    <p>The number you chose is""" + escape(guess) + """. Are you happy with your choice?</p>

    </body></html>"""

    return HttpResponse(response)

class MainView(View):
    def get(self, request):
        response = """ <html><body>
                            <h1>This is main view!</h1>
                            <p> My first real attempt at using class for views </p>
                        </body></html>"""
        return HttpResponse(response)

class RestMainView(View):
    def get(self, request, txting):
        response = """<html><body>
                        <h1> Welcome to Text Live </h1>
                        <p> This is my second attempt at class views </p>
                        <p> This time round I am experimenting with passing strings in GET </p>
                        <p> The message you have passed to me is """ + escape(txting)+ """</p>
                    </body></html>"""
        return HttpResponse(response)
