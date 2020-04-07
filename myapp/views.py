#!/usr/bin/python
# -*- coding: utf-8 -*-
def warn(*args, **kwargs):
    pass

from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.db.models import Q
from .models import *


# Create your views here.

def error_404_view(request, exception):
    return render(request,'404.html')

def index(request):
    try:
        return render(request, 'index.html')
    except:
        return render(request, '404.html')


def getuserfeedbackform(request):
    try:
        return render(request, 'userfeedbackform.html')
    except:
        return render(request, '404.html')


def saveuserfeedbackform(request):
    try:
        obj = UserFeedBack()
        obj.title = request.GET['usertitle']
        obj.description = request.GET['userdescription']
        obj.save()
        mydict = {'feedback': True}
        return render(request, 'userfeedbackform.html', context=mydict)
    except:
        return render(request, '404.html')

import warnings
warnings.warn = warn
import warnings
from sklearn.externals import joblib
from lxml import html
from json import dump, loads
from requests import get
import json
from re import sub
from dateutil import parser as dateparser
from time import sleep
from django.http import HttpResponse
from django.shortcuts import render
import os
import pickle
from sklearn.externals import joblib

import whois
import datetime


def result(request):

        text=request.GET['url']
        try:
            import praw
            nm=text  #"https://www.reddit.com/r/india/comments/fwcz7h/firozabad_police_factchecking_zee_news/"
            reddit = praw.Reddit(client_id='WBTxS7rybznf7Q', client_secret='vJUTUflXITBsQMxeviOfG8mCZoA', user_agent='projectreddit', username='Mysterious_abhE', password='Saxena0705')
            submission = reddit.submission(url=nm)
            #print (submission.comments[0])
            #print (submission.title)
            submission.comments.replace_more(limit=0)
            #co=[]
            tr=[]
            c=''
            for top_level_comment in submission.comments:        
                c+=top_level_comment.body  


            tr=submission.title+nm+c
            import datetime
            import joblib

            filename = 'SGD_model0.02v2cleaned.sav'

            loaded_model = joblib.load(filename)

            arg=loaded_model.predict(([tr]))
            print (arg[0])
            

            link=text
            flair=arg[0]
            obj = Url()
            obj.result = arg[0]
            obj.link = text
            obj.flair = arg[0]
            tags = [result,link,flair]
            tags = list(filter(lambda x: x!="Not Found",tags))
            tags.append(text)
            obj.save()

                
            return render(request,'result.html',{'result':'Real-time analysis successfull','f2':text,'mal': arg[0]})



      
        except:
            return render(request,'404.html')


def api(request):    
        text=request.GET['query']
        try:
            import praw
            nm=text  #"https://www.reddit.com/r/india/comments/fwcz7h/firozabad_police_factchecking_zee_news/"
            reddit = praw.Reddit(client_id='WBTxS7rybznf7Q', client_secret='vJUTUflXITBsQMxeviOfG8mCZoA', user_agent='projectreddit', username='Mysterious_abhE', password='Saxena0705')
            submission = reddit.submission(url=nm)
            #print (submission.comments[0])
            #print (submission.title)
            submission.comments.replace_more(limit=0)
            #co=[]
            tr=[]
            c=''
            for top_level_comment in submission.comments:        
                c+=top_level_comment.body  


            tr=submission.title+nm+c
            import datetime
            import joblib

            filename = 'SGD_model0.02v2cleaned.sav'

            loaded_model = joblib.load(filename)

            arg=loaded_model.predict(([tr]))
            print (arg[0])


            mydict = {
                "query" : text,
                "flair" : arg[0],
                "datetime" : str(datetime.datetime.now())
            }
            response = JsonResponse(mydict)
            return response

                

        except:
            mydict = {
                "query" : text,
                "flair" : "Invalid Url",
                "datetime" : str(datetime.datetime.now())
            }
            response = JsonResponse(mydict)
            return response
            
        

def about(request):
    #return HttpResponse("about")
    try:
        return render(request, 'about.html')
    except:
        return render(request, 'about.html')
    
def geturlhistory(request):
    mydict = {
        "urls" : Url.objects.all().order_by('-created_at')
    }
    return render(request,'list.html',context=mydict)
    '''except:
        return render(request,'404.html')
'''
def discuss(request):
    try:
        mydict = {
            "users" : UserFeedBack.objects.all()
        }
        return render(request,'discuss.html',context=mydict)
    except:
        return render(request,'404.html')

def search(request):
    try:
        query = request.GET['search']
        query = str(query).lower()
        mydict = {
            "urls" : Url.objects.all().filter(Q(link__contains=query) | Q(result__contains=query) | Q(created_at__contains=query) |
            Q(rank__contains=query) | Q(dom__contains=query)  | Q(country__contains=query) | Q(state__contains=query) | Q(emails__contains=query) |
            Q(add__contains=query) | Q(org__contains=query) | Q(city__contains=query)
            ).order_by('-created_at')
        }
        return render(request,'list.html',context=mydict)
    except:
        return render(request,'404.html')

def replyform(request,replyid):
    try:
        obj = UserFeedBack.objects.get(userid=replyid)
        mydict = {
        "replyid" : obj.userid,
        "title" : obj.title,
        "description" : obj.description
        }
        return render(request,'reply.html',context=mydict)
    except:
        return render(request,'404.html')

def savereply(request):
    try:
        print("debug start")
        replyid = request.GET['replyid']
        print(replyid)
        obj = UserFeedBack.objects.get(userid=replyid)
        obj.replied = True
        obj.reply = request.GET['userreply']
        obj.save()
        mydict = {
            "reply" : True,
            "users" : UserFeedBack.objects.all()
        }
        print("debug end")
        return render(request,'discuss.html',context=mydict)

    except:
        return render(request,'404.html')

def searchdiscuss(request):
    try:
        query = request.GET['search']
        query = str(query).lower()
        mydict = {
            "users" : UserFeedBack.objects.all().filter(Q(title__contains=query) | Q(description__contains=query) | Q(created_at__contains=query)
            |  Q(replied__contains=query) | Q(reply__contains=query)
            )
        }
        return render(request,'discuss.html',context=mydict)
    except:
        return render(request,'404.html')

def getdataset(request):
    try:
        return render(request,'getdataset.html')
    except:
        return render(request,'404.html')
			
