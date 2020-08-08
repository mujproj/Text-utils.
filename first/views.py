from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    
    return render(request, 'home.html')

def aboutus(request):
    return render(request, 'aboutus.html')

def contact(request):
    return render(request, 'contact.html')

def analyze(request):
    t = request.POST.get('text', False)
    removepunc = request.POST.get('removepunc', 'off')
    fullcaps = request.POST.get('fullcaps', 'off')
    newlineremover = request.POST.get('newlineremover', 'off')
    extraspaceremover = request.POST.get('extraspaceremover', 'off')
    charcount = request.POST.get('charcount', 'off')
    
    if removepunc == 'on':
        analyzed = ""
        #print('hello')
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        for char in t:
            if char not in punctuations:
                analyzed += char 
                #print(analyzed)
        
        writeup = {'purpose': 'Removed punctuation', 'analyzed_text': analyzed}
        t = analyzed
        #return render(request, 'analyze.html', {'purpose': 'Removed punctuation', 'analyzed_text': analyzed})
    
    if fullcaps == 'on':
        analyzed = ""
        #print('h')
        analyzed = t.upper()

       
        writeup = {'purpose': 'Capitalised every text', 'analyzed_text': analyzed}
        t = analyzed
        #return render(request, 'analyze.html', {'purpose': 'The string is being capitalised', 'analyzed_text': analyzed})

    if newlineremover == 'on':
        analyzed = ""
        for char in t:
            if char != '\n' and char!="\r":
                analyzed = analyzed + char
        
        writeup = {'purpose': 'removed newlines', 'analyzed_text' : analyzed}
        t = analyzed
        #return render(request, 'analyze.html', {'purpose': 'The new line are being removed', 'analyzed_text': analyzed})

    if extraspaceremover == 'on':
        analyzed = ""
        print("extra")
        for index, char in enumerate(t):
            if not(t[index] == " " and t[index + 1] == " "):
                analyzed += char
            
        
        writeup = {'purpose': 'removed extraspaces', 'analyzed_text': analyzed}
        t = analyzed
        #return render(request, 'analyze.html', {'purpose': 'The extra spaces are removed', 'analyzed_text': analyzed})

    if charcount == 'on':
        analyzed = ""
        analyzed = str(len(t))

        
        writeup = {'purpose': 'number of characters are', 'analyzed_text': analyzed}
        t = analyzed
        #return render(request, 'analyze.html', {'purpose': 'Number of characters', 'analyzed_text': analyzed})

            
    if (removepunc != 'on' and fullcaps != 'on' and newlineremover != 'on' and extraspaceremover != 'on' and charcount != 'on'):
        return render(request, 'home.html', {'p': 'Please Choose Atleast One Of the Check Boxes'})

    return render(request, 'analyze.html', writeup)    

