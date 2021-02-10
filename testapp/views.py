from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages
from testapp.models import Company_Register,Project_Skills,Incentiv,Plans,Project_Detailss,Create_Project
# Create your views here.
def company_landing_page(request):
	return render(request,'company.html')
def signin(request):
    if request.method=="POST":
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user:
            auth.login(request,user)
            return redirect('/dashboard_menu')
        else:
            messages.info(request,'Invalid credential')  
            return redirect('/signin')  
    else:
        return render(request,'login.html')
def company_register(request):
	return render(request,'company_register.html')
def multistepform_save(request):
    if request.method=="POST":
    	companyname=request.POST["companyname"]
    	cityname=request.POST["cityname"]
    	username=request.POST['username']
    	first_name=request.POST["first_name"]
    	last_name=request.POST["last_name"]
    	
    	email=request.POST["email"]
    	password=request.POST["password"]
    	cnf_password=request.POST["cnf_password"]
    	jobtitle=request.POST["jobtitle"]
    	mobno=request.POST["mobno"]
    	if User.objects.filter(username=username).exists():
    		messages.info(request,'Username Taken')
    		return redirect('/company_register')
    	elif User.objects.filter(email=email).exists():
    		messages.info(request,'Email Id Taken') 
    		return redirect('/company_register')
    	elif password != cnf_password:
    		messages.info(request,'Confirm Password not Match') 
    		return redirect('/company_register')
    	else:
    		user=User.objects.create_user(username=username,email=email,first_name=first_name,last_name=last_name,password=password)
    		user.save()
    		user_id=user.id
    		cr=Company_Register(user_id=user_id,companyname=companyname,cityname=cityname,jobtitle=jobtitle,mobno=mobno,cnf_password=cnf_password)
    		cr.save()
    		messages.success(request,"Data Save Successfully")
    		return redirect('/company_register')
def dashboard_menu(request):
	return render(request,'home.html')
def logout(request):
    auth.logout(request)
    return redirect('/signin')
def new_project_screen(request):
	return render(request,'new_project_screen1.html')
def project_skill(request):
    if request.method=='POST':
        skill=request.POST.getlist('skill')
        nda=request.POST['nda']
        user=User.objects.all()
        user_id=user[0].id
        data=Project_Skills(user_id=user_id,skill=skill,nda=nda)
        data.save()
        return redirect('/incentives')
    else:
        return render(request,'talent_pool_project_-_skills_required.html')
def incentives(request):
    if request.method=='POST':
        cash_prize=request.POST['cash_prize']
        cash_prize_description=request.POST['cash_prize_description']
        letter_of_recommendation=request.POST['letter_of_recommendation']
        letter_of_recommendation_description=request.POST['letter_of_recommendation_description']
        internship_opportunity=request.POST['internship_opportunity']
        internship_opportunity_description=request.POST['internship_opportunity_description']
        team_lunch_with_ceo=request.POST['team_lunch_with_ceo']
        team_lunch_with_ceo_description=request.POST['team_lunch_with_ceo_description']
        job_opportunity=request.POST['job_opportunity']
        job_opportunity_description=request.POST['job_opportunity_description']
        user=User.objects.all()
        user_id=user[0].id
        data=Incentiv(user_id=user_id,cash_prize=cash_prize,cash_prize_description=cash_prize_description,letter_of_recommendation=letter_of_recommendation,letter_of_recommendation_description=letter_of_recommendation_description,internship_opportunity=internship_opportunity,internship_opportunity_description=internship_opportunity_description,team_lunch_with_ceo=team_lunch_with_ceo,team_lunch_with_ceo_description=team_lunch_with_ceo_description,job_opportunity=job_opportunity,job_opportunity_description=job_opportunity_description)
        data.save()
        return redirect('/project_optimization')
    else:
        return render(request,'talent_pool_project_-_incentives.html')
def project_optimization(request):
    if request.method=='POST':
        plan=request.POST['plan']
        user=User.objects.all()
        user_id=user[0].id
        data=Plans(user_id=user_id,plan=plan)
        data.save()
        return redirect('/')
    else:
        return render(request,'talent_pool_project_-_optimize_your_project.html')
def project_detail(request):
    if request.method=='POST':
        project_title=request.POST['project_title']
        project_type=request.POST['project_type']
        deadline_date=request.POST['deadline_date']
        choose_template=request.POST['choose_template']
        description=request.POST['description']
        user=User.objects.all()
        user_id=user[0].id
        data=Project_Detailss(user_id=user_id,project_title=project_title,project_type=project_type,deadline_date=deadline_date,choose_template=choose_template,description=description)
        data.save()
        return redirect('/project_skill')
    else:
        # data=Project_Details.objects.all()
        # data_pro=data[0].id
        # print('sdfhgdgfdfgdfksgdfdfysy',data_pro)
        return render(request,'talent_pool_project_-_project_details.html')
def create_project(request):
    if request.method=='POST':
        project_title=request.POST['project_title']
        project_type=request.POST['project_type']
        deadline_date=request.POST['deadline_date']
        choose_template=request.POST['choose_template']
        description=request.POST['description']
        skill=request.POST.getlist('skill')
        nda=request.POST['nda']
        cash_prize=request.POST['cash_prize']
        cash_prize_description=request.POST['cash_prize_description']
        letter_of_recommendation=request.POST['letter_of_recommendation']
        letter_of_recommendation_description=request.POST['letter_of_recommendation_description']
        internsip_opportunity=request.POST['internsip_opportunity']
        internsip_opportunity_description=request.POST['internsip_opportunity_description']
        job_opportunity=request.POST['job_opportunity']
        job_opportunity_description=request.POST['job_opportunity_description']
        team_lunch_with_ceo=request.POST['team_lunch_with_ceo']
        team_lunch_with_ceo_description=request.POST['team_lunch_with_ceo_description']
        plan=request.POST['plan']
        user=User.objects.all()
        user_id=user[0].id
        for sk in skill:
            print(sk)
        data=Create_Project(user_id=user_id,project_title=project_title,project_type=project_type,deadline_date=deadline_date,choose_template=choose_template,description=description,skill=sk,nda=nda,cash_prize=cash_prize,cash_prize_description=cash_prize_description,letter_of_recommendation=letter_of_recommendation,letter_of_recommendation_description=letter_of_recommendation_description,internsip_opportunity=internsip_opportunity,internsip_opportunity_description=internsip_opportunity_description,job_opportunity=job_opportunity,job_opportunity_description=job_opportunity_description,team_lunch_with_ceo=team_lunch_with_ceo,team_lunch_with_ceo_description=team_lunch_with_ceo_description,plan=plan)
        data.save()
        messages.success(request,"Data Save Successfully")
        return redirect('/create_project')
    else:
        data=Create_Project.objects.last()
        param={'data':data}
        return render(request,'create_project.html',param)
def explore_virtual_teams_screen(request):
    return render(request,'explore_virtual_teams_screen.html')
def project_detail_preview(request,id):
    data=Create_Project.objects.get(id=id)
    param={'data':data}
    return render(request,'project_detail_preview.html',param)