from django.shortcuts import render,redirect
from .models import *
from django.contrib.auth.models import User
from django.contrib import messages 
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator

# Create your views here.
@login_required(login_url="/login/")
def receipes(request):

    if request.method == "POST":
        data=request.POST
        r_name=data.get('receipe_name')
        r_image= request.FILES.get('receipe_image')
        r_desc = data.get('receipe_description')
        r_country=data.get('receipe_country')

        Receipe.objects.create(
            receipe_name=r_name,
            receipe_image=r_image,
            receipe_description=r_desc,
            receipe_country=r_country
        )
        return redirect('/receipes/')
    queryset = Receipe.objects.all()

    if request.GET.get('search'):
        queryset =queryset.filter(receipe_name__icontains=request.GET.get('search'))

    context = {'receipes':queryset}



    
    return render(request,'receipes.html',context)

def delete_recepie(request,id):
    queryset = Receipe.objects.get(id=id)
    queryset.delete()

    return redirect('/receipes/')

def update_recepie(request,id):
    queryset = Receipe.objects.get(id=id)

    if request.method == "POST":
        data=request.POST
        r_name=data.get('receipe_name')
        r_image= request.FILES.get('receipe_image')
        r_desc = data.get('receipe_description')
        r_country=data.get('receipe_country')

        queryset.receipe_name=r_name
        queryset.receipe_description=r_desc
        queryset.receipe_country=r_country

        if r_image:
            queryset.receipe_image = r_image

        queryset.save()  
        return redirect('/receipes/')   




    context = {'receipe':queryset}


    return render(request,'update_receipes.html',context)

def login_page(request):
    if request.method =='POST':
        username=request.POST.get('username')
        password = request.POST.get('password')

        if not User.objects.filter(username = username).exists():
            messages.error(request,'Invalid username')
            return redirect('/login/')
        user = authenticate(username = username,password = password)

        if user is None:
            messages.error(request,'Invalid password')
            return redirect('/login/')
        else:
            login(request,user)
            return redirect('/receipes/')


    return render(request,'login.html')



def register_page(request):

    if request.method == "POST":
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        password = request.POST.get('password')

        user =User.objects.filter(username=username)
        if user.exists():
            messages.info(request,'already taken')
            return redirect('/register/')

        user = User.objects.create(
              first_name= first_name,
              last_name= last_name,
              username=username,
        )
        print(user)
        user.set_password(password)
        user.save()
        messages.info(request,'Account created sucssesfully')
        # data = User.objects.all()
        # print("hii")
        # print(data)

        return redirect('/register/')

    return render(request,'register.html')

def logout_page(request):
    logout(request)
    return redirect('/login/')
from django.db.models import Q

def student_get(request):
    queryset = Student.objects.all()
    if request.GET.get('search'):
        search = request.GET.get('search')
        # queryset=queryset.filter(Q(student_name__icontains=search)|
        #                          Q(department__department__icontains=search)|
        #                          Q(student_id__student_id__icontains=search)|
        #                          Q(student_email___icontains=search)
        #                          )  
        queryset = queryset.filter(
            student_name__icontains=search
           
        )
    paginator = Paginator(queryset, 25)  # Show 25 contacts per page.

    page_number = request.GET.get("page",1)
    page_obj = paginator.get_page(page_number)
    
    return render(request,'report/student.html',{'queryset':page_obj})

    

