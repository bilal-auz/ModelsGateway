from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    html = f'''
    <html>
        <body>
            <h1>API is Working</h1>
        </body>
    </html>
    '''
    return HttpResponse(html)
