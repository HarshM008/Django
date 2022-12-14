# importing HTTPresponse and render

from django.http import HttpResponse
from django.shortcuts import render

# views.index for home page
def index(request):
    return render(request, 'index.html')


# views.analyze for result page
def analyze(request):
    djtext = request.GET.get('text', 'default')  # Get the text

    # Check checkbox values and storing them with get method inside variable
    removepunc = request.GET.get('removepunc', 'off')
    capitalize = request.GET.get('capitalize', 'off')
    new_line_remover = request.GET.get('new_line_remover', 'off')
    extraspaceremover = request.GET.get('extraspaceremover', 'off')

    if len(djtext)>0:

        if removepunc == "on":
            # function logic
            punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
            analyzed = ""
            for char in djtext:
                if char not in punctuations:
                 analyzed = analyzed + char
            params = {'purpose': 'After modification is:', 'analyzed_text': analyzed}
            djtext = analyzed


        if capitalize == "on":
            analyzed = ""
            for char in djtext:
             analyzed = analyzed + char.upper()
            params = {'purpose': 'After modification is:', 'analyzed_text': analyzed}
            djtext = analyzed


        if new_line_remover == "on":
            analyzed = ""
            for char in djtext:
                if char != "\n" and char != "\r":
                 analyzed = analyzed + char
            params = {'purpose': 'After modification is:', 'analyzed_text': analyzed}
            djtext = analyzed



        if extraspaceremover == "on":
            analyzed = ""
            for index, char in enumerate(djtext):
                if not (djtext[index] == " " and djtext[index + 1] == " "):
                    analyzed = analyzed + char

            params = {'purpose': 'After modification is:', 'analyzed_text': analyzed}
            djtext = analyzed

        if (removepunc != "on" and capitalize != "on" and new_line_remover != "on" and extraspaceremover != "on"):
            return HttpResponse("<h3> Select any one option!!! </h3>")

        return render(request, 'analyze.html', params)

    else:
        return HttpResponse("<h3>Enter some text!!! </h3>")

