from django.shortcuts import render
from pdf import models
def cvview(request):
    if request.method =="POST" :
        name = request.POST.get("name")
        email = request.POST.get("email")
        phone = request.POST.get("number")
        summary = request.POST.get("summary")
        school = request.POST.get("school")
        university = request.POST.get("university")
        degree = request.POST.get("degree")
        works = request.POST.get("works")
        skills = request.POST.get("skills")
        PDF = models.profile(name=name,email=email,phone=phone,summary=summary,school=school,
        university=university,degree=degree,previous_works=works,skills=skills)
        PDF.save()
    return render(request,"cv.html")