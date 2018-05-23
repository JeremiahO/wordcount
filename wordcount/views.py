# Neccessay Imports to get a reponse to request
from django.http import HttpResponse
from django.shortcuts import render
import operator

# Response to home page request
def homepage(request):
    return render(request, 'home.html')

#About page request
def aboutpage(request):
    return render(request, 'about.html')

# Example
'''def eggs(request):
    return HttpResponse('<h1>You are making eggs!</h1>')'''

# count function
def count(request):
    # Here we are calling the fulltext that we record in the html
    fulltext = request.GET['fulltext']
    # Here we are send url back to the client due to their request
    # We created a fulltext key in a dictionary to send html info we recorded back to the user

    wordlist = fulltext.split()

    worddictionary = {}

    for word in wordlist:
        if word in worddictionary:
            #Increase
            worddictionary[word] += 1
        else:
            #AddtoDictionary
            worddictionary[word] = 1

    # Here we sort the list of elements in worddictionary and store it in sortedlist
    sortedlist = sorted(worddictionary.items(), key = operator.itemgetter(1), reverse=True)




    return render(request, 'count.html', {'fulltext': fulltext,'count': len(wordlist), 'worddictionary':sortedlist})
