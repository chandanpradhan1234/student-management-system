from django.shortcuts import render , HttpResponse
from home.models import Contact
from home.models import Student
from home.models import Faculty
from datetime import datetime

x=datetime.now
# y=x.strftime('%d-%m-%y')

# Create your views here.
def home(request):
    # return HttpResponse("this is home page (/)")
    # context={'name':'chandan' ,'project':'student mangement system final'}
    return render(request, 'home.html', {'date': x})
    

def about(request):
    return render(request, 'about.html')


def faq(request):
    return render(request, 'faq.html')

# def faculty(request):
#     return render(request, 'faculty.html')

# def student(request):
#     return render(request, 'student.html')

def contact(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        city = request.POST['city']
        desc = request.POST['desc']
        
        ins = Contact(name=name, email=email, city=city, desc=desc)
        ins.save()
        print("The data has been written to DB")
        

    return render(request, 'contact.html')


def student(request):
    if request.method == "POST":
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        # dob = request.POST['dob']
        gender = request. POST.get('gender')
        collage = request.POST['collage']
        city = request.POST['city']
        course = request.POST['course']
        photo = request.POST['photo']
        ano = request.POST['ano']
        pno = request.POST['pno']
        phno = request.POST['phno']
        

        # placement deatils:
        semester = request.POST['semester']
        company = request.POST['company']
        location = request.POST['location']
        package = request.POST['package']
        job = request.POST['job']

        # Performance Deatils :
        semester = request.POST['semester']
        percent = request.POST['percent']
        grade = request.POST['grade']
        activity = request.POST['activity']
        
        print(lname, email, gender, collage, city, course, photo, ano, pno, phno, company, location, package, job, semester, percent, grade, activity)
        info = Student(fname=fname, lname=lname, email=email, gender=gender, collage=collage, city=city, course=course, photo=photo, ano=ano, pno=pno,
                       phno=phno, company=company, location=location, package=package, job=job, semester=semester, percent=percent, grade=grade, activity=activity)
        info.save()
        print("The data has been written to DB")

    return render(request, 'student.html')


def faculty(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        # dob = request.POST['dob']
        gender = request. POST.get('gender')
        collage = request.POST['collage']
        ano = request.POST['ano']
        phno = request.POST['phno']
        exp = request.POST['exp']

        print(name, email, gender, collage, ano,phno,exp)

        data = Faculty(name=name,email=email, gender=gender, collage=collage, ano=ano, phno=phno,exp=exp)
        data.save()
        print("The data has been written to DB")
        # return render(request, 'faculty.html')
    return render(request, 'faculty.html')

    
        
        
        
   

    
