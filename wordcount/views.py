from django.http import HttpResponse
from django.shortcuts import render
import operator

def home(request):
    # return HttpResponse('Hello')
    return render(request, 'home.html')

def count(request):
    # get text information from the request
    text_content = request.GET['fulltext']

    # split the sentence into word list
    words = text_content.split()

    # word dictionary
    wordDic = {}

    for word in words:
        # Increase if contains
        if word in wordDic:
            wordDic[word] += 1
        # Add if not contains
        else:
            wordDic[word] = 1

    sorted_wordDic = sorted(wordDic.items(), key=operator.itemgetter(1), reverse=True)
    # return the result to count.html file
    return render(request, 'count.html', {'textInfo' : text_content, 'wordCount' : len(words), 'wordDictionary' : sorted_wordDic})

def about(request):
    return render(request, 'about.html')