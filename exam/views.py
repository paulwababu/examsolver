from django.shortcuts import render, redirect
import requests
from django.http import HttpResponse, HttpResponseRedirect
import time
import os
from datetime import datetime
from .models import Monitor
from urllib.parse import urlparse
import cloudinary.uploader

#exams researcher
def exams(request):
    if request.method == 'POST':
        files = request.FILES['files']
        upload_data = cloudinary.uploader.upload(files)
        imageData = upload_data['secure_url']
        nanoNetsApi = 'https://app.nanonets.com/api/v2/OCR/Model/418edf37-d178-4269-9497-93895ccc2f0a/LabelUrls/'
        headers = {'accept': 'application/x-www-form-urlencoded'}
        data = {'urls' : [imageData]}
        response = requests.request('POST', nanoNetsApi, headers=headers, auth=requests.auth.HTTPBasicAuth('Ct3BzSvuao0XGI63hhFGzqQNDrwfkvMe', ''), data=data)
        test = response.json()
        for quiz in test['result']:
            predicted = quiz['prediction']
            q1 = predicted[0]['ocr_text']
            q2 = predicted[1]['ocr_text']
            q3 = predicted[2]['ocr_text']
            q4 = predicted[3]['ocr_text']
            q5 = predicted[4]['ocr_text']
            q6 = predicted[5]['ocr_text']
            q7 = predicted[6]['ocr_text']
            q8 = predicted[7]['ocr_text']
            q9 = predicted[8]['ocr_text']
            q10 = predicted[9]['ocr_text']
            q11 = predicted[10]['ocr_text']
            q12 = predicted[11]['ocr_text']
            q13 = predicted[12]['ocr_text']
            q14 = predicted[13]['ocr_text']

        q1Format = q1.replace(" ", "+")
        q2Format = q2.replace(" ", "+")
        q3Format = q3.replace(" ", "+")
        q4Format = q4.replace(" ", "+")
        q5Format = q5.replace(" ", "+")
        q6Format = q6.replace(" ", "+")
        q7Format = q7.replace(" ", "+")
        q8Format = q8.replace(" ", "+")
        q9Format = q9.replace(" ", "+")
        q10Format = q10.replace(" ", "+")
        q11Format = q11.replace(" ", "+")
        q12Format = q12.replace(" ", "+")
        q13Format = q13.replace(" ", "+")
        q14Format = q14.replace(" ", "+")

        q1SearchUrl = "https://google-search3.p.rapidapi.com/api/v1/search/q="+q1Format
        q2SearchUrl = "https://google-search3.p.rapidapi.com/api/v1/search/q="+q2Format
        q3SearchUrl = "https://google-search3.p.rapidapi.com/api/v1/search/q="+q3Format
        q4SearchUrl = "https://google-search3.p.rapidapi.com/api/v1/search/q="+q4Format
        q5SearchUrl = "https://google-search3.p.rapidapi.com/api/v1/search/q="+q5Format
        q6SearchUrl = "https://google-search3.p.rapidapi.com/api/v1/search/q="+q6Format
        q7SearchUrl = "https://google-search3.p.rapidapi.com/api/v1/search/q="+q7Format
        q8SearchUrl = "https://google-search3.p.rapidapi.com/api/v1/search/q="+q8Format
        q9SearchUrl = "https://google-search3.p.rapidapi.com/api/v1/search/q="+q9Format
        q10SearchUrl = "https://google-search3.p.rapidapi.com/api/v1/search/q="+q10Format
        q11SearchUrl = "https://google-search3.p.rapidapi.com/api/v1/search/q="+q11Format
        q12SearchUrl = "https://google-search3.p.rapidapi.com/api/v1/search/q="+q12Format
        q13SearchUrl = "https://google-search3.p.rapidapi.com/api/v1/search/q="+q13Format
        q14SearchUrl = "https://google-search3.p.rapidapi.com/api/v1/search/q="+q14Format

        searchHeader = { 'x-user-agent': "desktop", 'x-rapidapi-host': "google-search3.p.rapidapi.com", 'x-rapidapi-key': "43628cd680msh1812b1660500eb7p182976jsn5dda2f77f08f" }

        searchResponseQ1 = requests.request("GET", q1SearchUrl, headers=searchHeader)
        searchResponseQ2 = requests.request("GET", q2SearchUrl, headers=searchHeader)
        searchResponseQ3 = requests.request("GET", q3SearchUrl, headers=searchHeader)
        searchResponseQ4 = requests.request("GET", q4SearchUrl, headers=searchHeader)
        searchResponseQ5 = requests.request("GET", q5SearchUrl, headers=searchHeader)
        searchResponseQ6 = requests.request("GET", q6SearchUrl, headers=searchHeader)
        searchResponseQ7 = requests.request("GET", q7SearchUrl, headers=searchHeader)
        searchResponseQ8 = requests.request("GET", q8SearchUrl, headers=searchHeader)
        searchResponseQ9 = requests.request("GET", q9SearchUrl, headers=searchHeader)
        searchResponseQ10 = requests.request("GET", q10SearchUrl, headers=searchHeader)
        searchResponseQ11 = requests.request("GET", q11SearchUrl, headers=searchHeader)
        searchResponseQ12 = requests.request("GET", q12SearchUrl, headers=searchHeader)
        searchResponseQ13 = requests.request("GET", q13SearchUrl, headers=searchHeader)
        searchResponseQ14 = requests.request("GET", q14SearchUrl, headers=searchHeader)

        q1resp = searchResponseQ1.json()
        q1res = q1resp.get('results')

        q2resp = searchResponseQ1.json()
        q2res = q2resp.get('results')

        q4resp = searchResponseQ4.json()
        q4res = q4resp.get('results')

        q5resp = searchResponseQ5.json()
        q5res = q5resp.get('results')

        q6resp = searchResponseQ6.json()
        q6res = q6resp.get('results')

        q7resp = searchResponseQ7.json()
        q7res = q7resp.get('results')

        q8resp = searchResponseQ8.json()
        q8res = q8resp.get('results')

        q9resp = searchResponseQ9.json()
        q9res = q9resp.get('results')

        q10resp = searchResponseQ10.json()
        q10res = q10resp.get('results')
        
        q11resp = searchResponseQ11.json()
        q11res = q11resp.get('results')

        q12resp = searchResponseQ12.json()
        q12res = q12resp.get('results')

        q13resp = searchResponseQ13.json()
        q13res = q13resp.get('results')

        q14resp = searchResponseQ14.json()
        q14res = q14resp.get('results')

        tester = searchResponseQ3.json()
        testa = tester.get('results')

        context = {
            "tester":testa,
            "q1res":q1res,
            "q2res":q2res,
            "q4res":q4res,
            "q5res":q5res,
            "q6res":q6res,
            "q7res":q7res,
            "q8res":q8res,
            "q9res":q9res,
            "q10res":q10res,
            "q11res":q11res,
            "q12res":q12res,
            "q13res":q13res,
            "q14res":q14res,
        }
        return render(request, 'exam_results.html', context)
    return render(request, 'exams.html')
