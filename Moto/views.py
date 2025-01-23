from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login
from .models import UserProfile
from datetime import date
from django.contrib import messages
from .models import Company,ApplyCompany


def add_company(request):
    if request.method == 'POST':
        # Get data from the request
        company_name = request.POST.get('companyName', '')
        company_address = request.POST.get('companyAddress', '')
        image = request.FILES.get('companyLogo', None)

        # Ensure all required fields are present
        if company_name and company_address and image:
            # Save the company instance
            company = Company(name=company_name, address=company_address, image=image)
            company.save()
            messages.success(request, "Company added successfully!")  # Optional feedback
            return redirect('dashboard')  # Redirect to avoid resubmitting form
        else:
            # Handle missing data
            messages.error(request, "All fields are required!")

    # Retrieve all companies to display in the template
    companies = Company.objects.all()

    # Pass data to the template
    return render(request, 'admin/add_companies.html', context={'companies': companies})

# Create your views here. 
def register_user(request):   
    if request.method=='POST':
        username=request.POST['username']
        email=request.POST['email']
        password=request.POST['password']
        dob = request.POST['DOB']
        Gender = request.POST['gender']
        address = request.POST['address']
    
        user = User.objects.create_user(username=username, email=email, password=password)
        user.set_password(password)
        user.save()
        user_profile = UserProfile(user=user, gender=Gender,dob=dob,address=address)
        user_profile.save()
        return redirect("login")
    return render(request,'accounts/register.html')

def loginuser(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        authenticated_user=authenticate(request,username=username,password=password)
        if authenticated_user is not None:
            login(request,authenticated_user)
            return redirect("dashboard")
    return render(request,'accounts/login.html')

def dashboard(request):
    comapnies = Company.objects.all()
    # print(comapnies)
    return render(request,'accounts/dashboard.html',context={'comapnies':comapnies})

def edit_profile(request):
    # Logic to handle profile editing
    return render(request, 'edit_profile.html')


def delete_company(request, id):
    comapnies = Company.objects.get(id=id)
    comapnies.delete()
    return redirect('dashboard')

def apply_company(request, company_id):
    if request.method=='POST':
        user = request.POST['username']
        email = request.POST['email']
        phone_number = request.POST['phone_number']
        upload_resume = request.FILES['upload_dresume']
        cover_letter = request.POST['cover_letter']

        new_content = ApplyCompany.objects.create(full_name=user,email=email,phone_number=phone_number,upload_resume=upload_resume,cover_letter=cover_letter)
        new_content.save()
        return redirect('dashboard')
    return render(request, 'accounts/apply_company.html', {'company_id': company_id})
