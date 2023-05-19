from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, 'index.html')


def math(req):
    ans = 0
    num = req.POST.get('text', 'default')   
    square = req.POST.get('square','off')
    if square== "on":
        ans = pow(float(num),2)
    params = {'ans': ans}
    return render(req,'math.html',params)
    

def analyze(request):

    djtext = request.POST.get('text', 'default')
    removepunc=request.POST.get('removepunc','off')
    uppercaps=request.POST.get('uppercaps','off')
    removextraspace=request.POST.get('removextraspace','off')
    charcount=request.POST.get('charcount','off')

    # Removing pucntuation
    if removepunc == "on":
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
        params = {'purpose': 'Removed Punctuations', 'analyzed_text': analyzed}
        djtext = analyzed

    # Upper case
    if uppercaps=="on":
        analyzed = ""
        for char in djtext:
            analyzed += char.upper()
        params = {'purpose': 'UPPER CASE', 'analyzed_text': analyzed}
        djtext = analyzed
    
    # Removing xtra spaces
    if removextraspace=="on":
        analyzed = ""
        for index, char in enumerate(djtext):
            if not(djtext[index] == " " and djtext[index+1] == " "):
                analyzed += char
        params = {'purpose': 'Removing xtra spaces', 'analyzed_text': analyzed}
        djtext = analyzed

    # NO of cahracters
    if charcount=="on":
        analyzed = 0
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        for char in djtext:
            if char != " " and char not in punctuations:
                analyzed += 1

        params = {'purpose': 'total no of characters', 'analyzed_text': analyzed}
        djtext = analyzed
    
    if (charcount != "on"and removextraspace != "on" and uppercaps != "on" and removepunc != "on"):
        return HttpResponse('please choose one of the options')
    
    return render(request, 'analyze.html', params)
