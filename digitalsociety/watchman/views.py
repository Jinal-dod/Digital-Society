from django.shortcuts import render
from chairman.models import *

# Create your views here.
# def registration_pa(request):
#     return render(request,'watchman/register.html')
def registration_page(request):
    return render(request,'watchman/registration.html')

def register(request):
    fname=request.POST['fname']
    lname=request.POST['lname']
    contactNo=request.POST['contactNo']
    email=request.POST['email']

    wid=Watchman.objects.create(fname=fname,lname=lname,contactno=contactNo,email=email)

    s_msg='Your Registration Request is sent to Chairman for approval'
    return render(request,'watchman/w_login.html',{'s_msg':s_msg})

def w_login(request):
    return render(request,'watchman/w_login.html')

def w_login_evalute(request):
    try:
        u_email=request.POST['email']
        u_password=request.POST['password']
        uid=Watchman.objects.get(email=u_email)
        print("--------------> uid=",uid)
        if uid.password==u_password:
            print("-------pass",u_password)
            print("   ---------welcom")
            if uid.role=='watchman':
                if uid.is_verified == True:
                    request.session['w_email']=uid.email
                    print("--------------->m_email",request.session['w_email'])
                    context={
                        'uid':uid,
                    }
#send_mail("welcome","welcome to digital society","jinaldod12@gmail.com",["jinaldod8151@gmail.com","jinaldod12@gmail.com"])
                return render(request,'member/m_index.html',{'context':context})
            else:
                e_msg="You Are not Verified please connected chairman"
                return render(request,'watchman/w_login.html',{'e_msg':e_msg})    
        else:
            print("invalid password")
            e_msg="invalid password"
            return render(request,'watchman/w_login.html',{'e_msg':e_msg})    
    except Exception as e:
        print("---------->e  ",e)
        print("Email does not exist")
        e_msg="Email does not exist"
        return render(request,'watchman/w_login.html',{'e_msg':e_msg})

def w_logout(request):
    if 'w_email' in request.session:
        del request.session['w_email']
        #print("--------------->session _-___m_email",request.session['m_email'])
        return render(request,'watchman/w_login.html')
    else:
        return render(request,'watchman/w_login.html')

