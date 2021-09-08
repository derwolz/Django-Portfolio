from django.shortcuts import render
from myportfolio.forms import *
from .models import *
from django.http import HttpResponse
# Create your views here.

def index(request):
    workexp =  WorkExperience.objects.all()
    workskill = WorkSkill.objects.all()
    for work in workexp:
        if work.is_current:
            work.end_year = 'Current'
    front_skill = CSTag.objects.all().filter(is_front_end=True)
    back_skill = CSTag.objects.all().filter(is_front_end=False)
    
    context = {"currpage":"myportfolio/index.html",'front_skills':front_skill,'back_skills':back_skill,
        'workexp':workexp, 'workskills': workskill}
    return render(request, 'myportfolio/_layout.html', context)
     
def projects(request):
    if (request.method == "GET"):  
        currproject = None   
        reqproj = request.GET.getlist('with')
        if len(reqproj) == 1: # should only have a single response
            #print(reqproj[0])   
            currproject = Project.objects.all().get(name=reqproj[0])
        #    print('---', _currproject)  
            #print('---', currproject)
         
           
    allfilters = CSTag.objects.all()
    #Projects = Project.objects.all()
    form = ProjectFilterForm()
    f = request.GET.getlist('filters')
    Projects = Project.objects.none()
    for it in f:
        Projects |= Project.objects.all().filter(cstag__name__contains=it)
    if len(Projects) == 0:
        Projects = Project.objects.all()
    
    projectsbytags = {}
    Projects = set(Projects)
    for item in Projects:
        projectsbytags[item] = item.cstag_set.all()
    
         

    context = {"currpage":"myportfolio/projects.html","allfilters":allfilters,'projectlist': Projects, 'form': form, }
    return render(request, 'myportfolio/_layout.html', context)
    
def singleproject(request): 
    
    context = {"currpage":"myportfolio/_projectPopup.html",}
    return render(request, 'myportfolio/_layout.html', context)
    
def contact(request):  
    form = ProspectForm()
    if (request.method == 'POST'):
        print('---', request.POST)
        if (addcontact(request.POST)):
            print ('success')
    context = {"currpage":"myportfolio/contact.html","form": form}
    return render(request, 'myportfolio/_layout.html', context)


def addcontact(data):
    Name = data.get("Name")
    Sender = data.get("Sender")
    Message = data.get("Message")
    Prospect.objects.create(name=Name, email=Sender, message=Message)
    return True
    
#def program(request, projectname):
    #data = None
    #data = Project.objects.all().get(name=projectname)
    #print(data)
    #context = {"currpage":"myportfolio/_projectpopup.html", "currproject":data}
    #return render(request, 'myportfolio/_layout.html', context)