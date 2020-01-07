from django.shortcuts import render, redirect, get_object_or_404
from menu2.models import Experiment
from menu3.models import Event
from menu4.models import Comment

################################## ผลรวม ###########################################

def sumary(request):
    #รายวิชา
    physicsum = Experiment.objects.filter(course = 'ฟิสิกส์').count()
    chemsum = Experiment.objects.filter(course = 'เคมี').count()
    biosum = Experiment.objects.filter(course = 'ชีววิทยา').count()
    scisum = Experiment.objects.filter(course = 'โครงงานวิทยาศาสตร์').count()

    #โครงการ
    meetsum = Event.objects.filter(types = 'การประชุม').count()
    trainsum = Event.objects.filter(types = 'การฝึกอบรม').count()
    seminsum = Event.objects.filter(types = 'การสัมมนา').count()
    consum = Event.objects.filter(types = 'การเสวนา').count()

    context = {
        'physicsum' : physicsum,
        'chemsum'   : chemsum,
        'biosum'    : biosum,
        'scisum'    : scisum,
        'meetsum'   : meetsum,
        'trainsum'  : trainsum,
        'seminsum'  : seminsum,
        'consum'    : consum,
    }
    return render(request ,'menu4/sumary.html', context)

################################## คอมเมนต์ ###########################################

def comment(request):
    return render(request ,'menu4/comment.html')

def add_comment(request):
    if request.method == 'POST':
        username = request.POST['username'] #.get('username', False)
        email = request.POST['email'] #.get('email', False)
        comment = request.POST['comment'] #.get('comment', False)

        comments = Comment.objects.all()
        comments = Comment(username = username, email = email, comment = comment)
        if comments:
           comments.save()
           return redirect('comment')