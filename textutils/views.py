# I have created this file -Prateek
from ast import AnnAssign
from django.http import HttpResponse
from django.shortcuts import render

def index(request):    
    return render(request, 'index.html')
    


def analyze (request):
    djtext = request.POST.get('text', 'default')

    removepunc = request.POST.get('removepunc', 'off')
    fullcaps = request.POST.get('fullcaps', 'off')
    newlineremover = request.POST.get('newlineremover', 'off')
    extraspaceremover = request.POST.get('extraspaceremover', 'off')
    charcount = request.POST.get('charcount', 'off')
    if removepunc == "on":            
        
        punctuations = ''':/()-[]{};'"\,<>.?@^*+?.,\\^$|#\s]/,"\\$&;_"'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
        params = {'purpose':'Removed Punctions', 'analyzed_text': analyzed }
        djtext = analyzed
        
    if(fullcaps == "on"):
        analyzed=""
        for char in djtext:
            analyzed = analyzed + char.upper()
        params = {'purpose':'Changed to Uppercase', 'analyzed_text': analyzed }
        djtext = analyzed
        
    if(newlineremover == "on"):
        analyzed=""
        for char in djtext:
            if char !="\n" and char != "\r":
                analyzed = analyzed + char
        params = {'purpose':'Removed New Lines ', 'analyzed_text': analyzed }
        djtext = analyzed
        
    if(extraspaceremover == "on"):
        analyzed=""
        for index, char in enumerate(djtext):
            if not(djtext[index] == " " and djtext[index+1] == " "):
                analyzed = analyzed + char
        params = {'purpose':'Removed Extra Spaces ', 'analyzed_text': analyzed }
        djtext =analyzed
        

    if(charcount == "on"):  
        newtext = djtext.replace(" ", "")          
        analyzed = len(newtext)
        params = {'purpose':'Total number of chars in text is ', 'analyzed_text': str(analyzed) }
        
    
    if(removepunc != "on" and fullcaps !="on" and newlineremover != "on" and extraspaceremover != "on" and charcount != "on"):
        return HttpResponse("Please select the operation")


    return render(request, 'analyze.html', params)

