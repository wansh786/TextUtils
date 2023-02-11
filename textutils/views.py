# I have created this file- Raghuwansh Singh
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, 'index.html')
    #return HttpResponse("Home")

def analyze(request):
    #Get the text
    djtext = request.POST.get('text', 'default')
    # check checkbox value

    removepunc = request.POST.get('removepunc', 'off')
    fullcaps = request.POST.get('fullcaps', 'off')
    newlineremover= request.POST.get('newlineremover', 'off')
    extraspaceremover= request.POST.get('extraspaceremover', 'off')

    # check which checkbox is on
    if removepunc=="on":
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed=analyzed+char
        parms={'purpose':'Remove punctuations','analyzed_text':analyzed}
        djtext=analyzed

    if(fullcaps=="on"):
        analyzed=""
        for char in djtext:
            analyzed=analyzed+char.upper()
        parms = {'purpose': 'Change To Uppercase', 'analyzed_text': analyzed}
        djtext = analyzed

    if(newlineremover=="on"):
        analyzed = ""
        for char in djtext:
            if char!="\n" and char!="\r":
                analyzed = analyzed + char
        parms = {'purpose': 'New Line Remover', 'analyzed_text': analyzed}
        djtext = analyzed

    if (extraspaceremover == "on"):
        analyzed = ""
        for index,char in enumerate(djtext):
            if not( djtext[index]==" " and djtext[index+1]==" "):
                analyzed = analyzed + char
        parms = {'purpose': 'Extra Space Remover', 'analyzed_text': analyzed}

    if(removepunc!="on" and fullcaps!="on" and newlineremover!="on" and extraspaceremover != "on"):

        return HttpResponse("please select any operation")

    return render(request, 'analyze.html', parms)

