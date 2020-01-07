from django.shortcuts import render, get_object_or_404
from menu2.models import PPE, Experiment
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

##################################### ฟิสิกส์ ###############################################

def physic(request):
    #มัธยมศึกษาตอนต้น
    physics = Experiment.objects.filter(course = 'ฟิสิกส์').filter(degree = 'มัธยมศึกษาตอนต้น')
    phy_countmid = Experiment.objects.filter(course = 'ฟิสิกส์').filter(degree = 'มัธยมศึกษาตอนต้น').count()

    paginator = Paginator(physics, 3)
    page = request.GET.get('page')
    physics = paginator.get_page(page)

    try:
        physics = paginator.page(page)
    except PageNotAnInteger:
        physics = paginator.page(1)
    except EmptyPage:
        physics = paginator.page(paginator.num_pages)

    #มัธยมศึกษาตอนปลาย
    physic = Experiment.objects.filter(course = 'ฟิสิกส์').filter(degree = 'มัธยมศึกษาตอนปลาย')
    phy_counthi = Experiment.objects.filter(course = 'ฟิสิกส์').filter(degree = 'มัธยมศึกษาตอนปลาย').count()
    
    paginator = Paginator(physic, 3)
    page = request.GET.get('page')
    physic = paginator.get_page(page)

    try:
        physic = paginator.page(page)
    except PageNotAnInteger:
        physic = paginator.page(1)
    except EmptyPage:
        physic = paginator.page(paginator.num_pages)

    context = {
        'physics'       : physics,
        'physic'        : physic,
        'phy_countmid'  : phy_countmid,
        'phy_counthi'   : phy_counthi
    }
    return render(request ,'menu2/physic/physic.html',context)

#รายละเอียดวิชาฟิสิกส์
def physic_detail(request ,physics_id):
    phy = Experiment.objects.get(pk = physics_id)
    head = PPE.objects.filter(ppe_type = 'อุปกรณ์ป้องกันศีรษะ')
    face_and_eyes = PPE.objects.filter(ppe_type = 'อุปกรณ์ป้องกันใบหน้าและตา')
    ear = PPE.objects.filter(ppe_type = 'อุปกรณ์ป้องกันหู')
    respiratory = PPE.objects.filter(ppe_type = 'อุปกรณ์ป้องกันการหายใจ')
    body = PPE.objects.filter(ppe_type = 'อุปกรณ์ป้องกันลำตัว')
    hand = PPE.objects.filter(ppe_type = 'อุปกรณ์ป้องกันมือ')
    foot = PPE.objects.filter(ppe_type = 'อุปกรณ์ป้องกันเท้า')

    context = {
        'physics'       : phy,
        'head'          : head,
        'face_and_eyes' : face_and_eyes,
        'ear'           : ear,
        'respiratory'   : respiratory,
        'body'          : body,
        'hand'          : hand,
        'foot'          : foot
    }
    return render(request ,'menu2/physic/physic_detail.html', context)

###################################### เคมี ###############################################

def chemistry(request):
    #มัธยมศึกษาตอนต้น
    chemistrys = Experiment.objects.filter(course = 'เคมี').filter(degree = 'มัธยมศึกษาตอนต้น')
    chem_countmid = Experiment.objects.filter(course = 'เคมี').filter(degree = 'มัธยมศึกษาตอนต้น').count()

    paginator = Paginator(chemistrys, 3)
    page = request.GET.get('page')
    chemistrys = paginator.get_page(page)

    try:
        chemistrys = paginator.page(page)
    except PageNotAnInteger:
        chemistrys = paginator.page(1)
    except EmptyPage:
        chemistrys = paginator.page(paginator.num_pages)

    #มัธยมศึกษาตอนปลาย
    chemistry = Experiment.objects.filter(course = 'เคมี').filter(degree = 'มัธยมศึกษาตอนปลาย')
    chem_counthi = Experiment.objects.filter(course = 'เคมี').filter(degree = 'มัธยมศึกษาตอนปลาย').count()

    paginator = Paginator(chemistry, 3)
    page = request.GET.get('page')
    chemistry = paginator.get_page(page)

    try:
        chemistry = paginator.page(page)
    except PageNotAnInteger:
        chemistry = paginator.page(1)
    except EmptyPage:
        chemistry = paginator.page(paginator.num_pages)

    context = {
        'chemistrys'    : chemistrys,
        'chemistry'     : chemistry,
        'chem_countmid' : chem_countmid,
        'chem_counthi'  : chem_counthi
    }
    return render(request ,'menu2/chemistry/chemistry.html',context)

#รายละเอียดวิชาเคมี
def chemistry_detail(request, chemistry_id):
    chem = Experiment.objects.get(pk = chemistry_id)
    head = PPE.objects.filter(ppe_type = 'อุปกรณ์ป้องกันศีรษะ')
    face_and_eyes = PPE.objects.filter(ppe_type = 'อุปกรณ์ป้องกันใบหน้าและตา')
    ear = PPE.objects.filter(ppe_type = 'อุปกรณ์ป้องกันหู')
    respiratory = PPE.objects.filter(ppe_type = 'อุปกรณ์ป้องกันการหายใจ')
    body = PPE.objects.filter(ppe_type = 'อุปกรณ์ป้องกันลำตัว')
    hand = PPE.objects.filter(ppe_type = 'อุปกรณ์ป้องกันมือ')
    foot = PPE.objects.filter(ppe_type = 'อุปกรณ์ป้องกันเท้า')
    
    context = {
        'chemistrys'    : chem,
        'head'          : head,
        'face_and_eyes' : face_and_eyes,
        'ear'           : ear,
        'respiratory'   : respiratory,
        'body'          : body,
        'hand'          : hand,
        'foot'          : foot
    }
    return render(request ,'menu2/chemistry/chemistry_detail.html',context)

##################################### ชีววิทยา #############################################

def biology(request):
    #มัธยมศึกษาตอนต้น
    biologys = Experiment.objects.filter(course = 'ชีววิทยา').filter(degree = 'มัธยมศึกษาตอนต้น')
    bio_countmid = Experiment.objects.filter(course = 'ชีววิทยา').filter(degree = 'มัธยมศึกษาตอนต้น').count()

    paginator = Paginator(biologys, 3)
    page = request.GET.get('page')
    biologys = paginator.get_page(page)

    try:
        biologys = paginator.page(page)
    except PageNotAnInteger:
        biologys = paginator.page(1)
    except EmptyPage:
        biologys = paginator.page(paginator.num_pages)

    #มัธยมศึกษาตอนปลาย
    biology = Experiment.objects.filter(course = 'ชีววิทยา').filter(degree = 'มัธยมศึกษาตอนปลาย')
    bio_counthi = Experiment.objects.filter(course = 'ชีววิทยา').filter(degree = 'มัธยมศึกษาตอนปลาย').count()

    paginator = Paginator(biology, 3)
    page = request.GET.get('page')
    biology = paginator.get_page(page)

    try:
        biology = paginator.page(page)
    except PageNotAnInteger:
        biology = paginator.page(1)
    except EmptyPage:
        biology = paginator.page(paginator.num_pages)

    context = {
        'biologys'      : biologys,
        'biology'       : biology,
        'bio_countmid'  : bio_countmid,
        'bio_counthi'   : bio_counthi
    }
    return render(request ,'menu2/biology/biology.html',context)

#รายละเอียดวิชาชีววิทยา
def biology_detail(request, biology_id):
    bio = Experiment.objects.get(pk = biology_id)
    head = PPE.objects.filter(ppe_type = 'อุปกรณ์ป้องกันศีรษะ')
    face_and_eyes = PPE.objects.filter(ppe_type = 'อุปกรณ์ป้องกันใบหน้าและตา')
    ear = PPE.objects.filter(ppe_type = 'อุปกรณ์ป้องกันหู')
    respiratory = PPE.objects.filter(ppe_type = 'อุปกรณ์ป้องกันการหายใจ')
    body = PPE.objects.filter(ppe_type = 'อุปกรณ์ป้องกันลำตัว')
    hand = PPE.objects.filter(ppe_type = 'อุปกรณ์ป้องกันมือ')
    foot = PPE.objects.filter(ppe_type = 'อุปกรณ์ป้องกันเท้า')

    context = {
        'biologys'      : bio,
        'head'          : head,
        'face_and_eyes' : face_and_eyes,
        'ear'           : ear,
        'respiratory'   : respiratory,
        'body'          : body,
        'hand'          : hand,
        'foot'          : foot
    }
    return render(request ,'menu2/biology/biology_detail.html',context)

################################## โครงงานวิทยาศาสตร์ ################################################

def science(request):
    #มัธยมศึกษาตอนต้น
    sciences = Experiment.objects.filter(course = 'โครงงานวิทยาศาสตร์').filter(degree = 'มัธยมศึกษาตอนต้น')
    sci_countmid = Experiment.objects.filter(course = 'โครงงานวิทยาศาสตร์').filter(degree = 'มัธยมศึกษาตอนต้น').count()

    paginator = Paginator(sciences, 3)
    page = request.GET.get('page')
    sciences = paginator.get_page(page)

    try:
        sciences = paginator.page(page)
    except PageNotAnInteger:
        sciences = paginator.page(1)
    except EmptyPage:
        sciences = paginator.page(paginator.num_pages)

    #มัธยมศึกษาตอนปลาย
    science = Experiment.objects.filter(course = 'โครงงานวิทยาศาสตร์').filter(degree = 'มัธยมศึกษาตอนปลาย')
    sci_counthi = Experiment.objects.filter(course = 'โครงงานวิทยาศาสตร์').filter(degree = 'มัธยมศึกษาตอนปลาย').count()

    paginator = Paginator(science, 3)
    page = request.GET.get('page')
    science = paginator.get_page(page)

    try:
        science = paginator.page(page)
    except PageNotAnInteger:
        science = paginator.page(1)
    except EmptyPage:
        science = paginator.page(paginator.num_pages)

    context = {
        'sciences'      : sciences,
        'science'       : science,
        'sci_countmid'  : sci_countmid,
        'sci_counthi'   : sci_counthi
    }
    return render(request ,'menu2/science/science.html',context)

#รายละเอียดโครงงานวิทยาศาสตร์
def science_detail(request, science_id):
    science = Experiment.objects.get(pk = science_id)
    head = PPE.objects.filter(ppe_type = 'อุปกรณ์ป้องกันศีรษะ')
    face_and_eyes = PPE.objects.filter(ppe_type = 'อุปกรณ์ป้องกันใบหน้าและตา')
    ear = PPE.objects.filter(ppe_type = 'อุปกรณ์ป้องกันหู')
    respiratory = PPE.objects.filter(ppe_type = 'อุปกรณ์ป้องกันการหายใจ')
    body = PPE.objects.filter(ppe_type = 'อุปกรณ์ป้องกันลำตัว')
    hand = PPE.objects.filter(ppe_type = 'อุปกรณ์ป้องกันมือ')
    foot = PPE.objects.filter(ppe_type = 'อุปกรณ์ป้องกันเท้า')

    context = {
        'sciences'      : science,
        'head'          : head,
        'face_and_eyes' : face_and_eyes,
        'ear'           : ear,
        'respiratory'   : respiratory,
        'body'          : body,
        'hand'          : hand,
        'foot'          : foot
    }
    return render(request ,'menu2/science/science_detail.html',context)