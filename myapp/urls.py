from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('APIresult',views.APIresult,name="APIresult"),
    path('getuserfeedbackform',views.getuserfeedbackform,name="getuserfeedbackform"),
    path('upload',views.upload,name="upload"),
    path('automated_testing',views.automated_testing,name="automated_testing"),
    path('saveuserfeedbackform',views.saveuserfeedbackform,name="saveuserfeedbackform"),
    path('dataanalysis',views.dataanalysis,name="dataanalysis"),
    path('themes',views.themes,name="themes"),
    path('api',views.api,name='api'),
    path('search',views.search,name="search"),
    path('result',views.result,name='result'),
    path('about',views.about,name='about'),
    path('geturlhistory',views.geturlhistory,name="geturlhistory"),
    path('discuss',views.discuss,name="discuss"),
    path('reply/<int:replyid>',views.replyform,name="reply"),
    path('savereply',views.savereply,name="reply"),
    path('searchdiscuss',views.searchdiscuss,name="searchdiscuss"),
    path('getdataset',views.getdataset,name='getdataset')

]

