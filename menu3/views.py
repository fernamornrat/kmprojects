from django.shortcuts import render, redirect ,get_object_or_404
from menu3.models import Event, Register
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

###################################### โครงการประชุม ###############################################

#โครงการประชุม
def event_1(request):
    meeting = Event.objects.filter(types = 'การประชุม').order_by('-date')
    meetcount = Event.objects.filter(types = 'การประชุม').count()

    paginator = Paginator(meeting, 3)
    page = request.GET.get('page')
    meeting = paginator.get_page(page)

    try:
        meeting = paginator.page(page)
    except PageNotAnInteger:
        meeting = paginator.page(1)
    except EmptyPage:
        meeting = paginator.page(paginator.num_pages)

    context = {
        'meeting' : meeting,
        'meetcount' : meetcount,
    }
    return render(request ,'menu3/event1/meeting.html' ,context)

#รายละเอียดโครงการประชุม
def event1_detail(request, meeting_id):
    meet = Event.objects.get(pk = meeting_id)
    context = {
        'meeting' : meet,
    }
    return render(request ,'menu3/event1/meeting_detail.html',context)

#ลงทะเบียนการประชุม
def event1_register(request):
    meeting = Event.objects.filter(types = 'การประชุม')

    if request.method == 'POST':
        eventid = request.POST['event']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        phone = request.POST['phone']

        event = Event.objects.get(id = eventid)
        event = Register(event = event, first_name = first_name, last_name = last_name, email = email, phone = phone)
        if event:
           event.save()
           return redirect('meeting')

    context = {
        'meeting' : meeting,
    }
    return render(request ,'menu3/event1/meeting_register.html',context)

###################################### โครงการฝึกอบรม ###############################################

#โครงการฝึกอบรม
def event_2(request):
    training = Event.objects.filter(types = 'การฝึกอบรม').order_by('-date')
    trainingcount = Event.objects.filter(types = 'การฝึกอบรม').count()

    paginator = Paginator(training, 3)
    page = request.GET.get('page')
    training = paginator.get_page(page)

    try:
        training = paginator.page(page)
    except PageNotAnInteger:
        training = paginator.page(1)
    except EmptyPage:
        training = paginator.page(paginator.num_pages)

    context = {
        'training' : training,
        'trainingcount' : trainingcount,
    }
    return render(request ,'menu3/event2/training.html',context)

#รายละเอียดโครงการฝึกอบรม
def event2_detail(request, training_id):
    train = Event.objects.get(pk = training_id)
    context = {
        'training' : train,
    }
    return render(request ,'menu3/event2/training_detail.html',context)

#ลงทะเบียนการฝึกอบรม
def event2_register(request):
    training = Event.objects.filter(types = 'การฝึกอบรม')

    if request.method == 'POST':
        eventid = request.POST['event']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        phone = request.POST['phone']

        event = Event.objects.get(id = eventid)
        event = Register(event = event, first_name = first_name, last_name = last_name, email = email, phone = phone)
        if event:
           event.save()
           return redirect('training')

    context = {
        'training' : training,
    }
    return render(request ,'menu3/event2/training_register.html',context)

###################################### โครงการสัมมนา ##################################################

#โครงการสัมมนา
def event_3(request):
    seminar = Event.objects.filter(types = 'การสัมมนา').order_by('-date')
    seminarcount = Event.objects.filter(types = 'การสัมมนา').count()

    paginator = Paginator(seminar, 3)
    page = request.GET.get('page')
    seminar = paginator.get_page(page)

    try:
        seminar = paginator.page(page)
    except PageNotAnInteger:
        seminar = paginator.page(1)
    except EmptyPage:
        seminar = paginator.page(paginator.num_pages)

    context = {
        'seminar' : seminar,
        'seminarcount' : seminarcount,
    }
    return render(request ,'menu3/event3/seminar.html',context)

#รายละเอียดโครงการสัมมนา
def event3_detail(request, seminar_id):
    semi = Event.objects.get(pk = seminar_id)
    context = {
        'seminar' : semi,
    }
    return render(request ,'menu3/event3/seminar_detail.html',context)

#ลงทะเบียนสัมมนา
def event3_register(request):
    seminar = Event.objects.filter(types = 'การสัมมนา')

    if request.method == 'POST':
        eventid = request.POST['event']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        phone = request.POST['phone']

        event = Event.objects.get(id = eventid)
        event = Register(event = event, first_name = first_name, last_name = last_name, email = email, phone = phone)
        if event:
           event.save()
           return redirect('seminar')

    context = {
        'seminar' : seminar,
    }

    return render(request ,'menu3/event3/seminar_register.html', context)

####################################### โครงการเสวนา ###############################################

#โครงการเสวนา
def event_4(request):
    converse = Event.objects.filter(types = 'การเสวนา').order_by('-date')
    conversecount = Event.objects.filter(types = 'การเสวนา').count()

    paginator = Paginator(converse, 3)
    page = request.GET.get('page')
    converse = paginator.get_page(page)

    try:
        converse = paginator.page(page)
    except PageNotAnInteger:
        converse = paginator.page(1)
    except EmptyPage:
        converse = paginator.page(paginator.num_pages)

    context = {
        'converse' : converse,
        'conversecount' : conversecount,
    }
    return render(request ,'menu3/event4/converse.html',context)

#รายละเอียดโครงการเสวนา
def event4_detail(request, converse_id):
    conver = Event.objects.get(pk = converse_id)
    context = {
        'converse' : conver,
    }
    return render(request ,'menu3/event4/converse_detail.html', context)

#ลงทะเบียนเสวนา
def event4_register(request):
    converse = Event.objects.filter(types = 'การเสวนา')

    if request.method == 'POST':
        eventid = request.POST['event']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        phone = request.POST['phone']

        event = Event.objects.get(id = eventid)
        event = Register(event = event, first_name = first_name, last_name = last_name, email = email, phone = phone)
        if event:
           event.save()
           return redirect('converse')
    
    context = {
        'converse' : converse,
    }
    return render(request ,'menu3/event4/converse_register.html',context)
