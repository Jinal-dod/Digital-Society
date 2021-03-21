from django.shortcuts import render
from chairman.models import *
from random import *
from .utils import *
#from django.core.mail import send_mail
# Create your views here.
#return render(request,'member/m_index.html',{'context':context})
def m_index(request):
    try:
        if'm_email' in request.session:
            uid=User.objects.get(email=request.session['m_email'])
            cid=Member.objects.get(user_id=uid)
            context={
                'uid':uid,
                'cid':cid,
            }
            return render(request,'member/m_index.html',{'context':context})
        else:
            return render(request,'member/m_login.html')
    except:
        return render(request,'member/m_login.html')

def m_login(request):
    return render(request,'member/m_login.html')

def m_login_evalute(request):
    try:
        u_email=request.POST['email']
        u_password=request.POST['password']
        uid=User.objects.get(email=u_email)
        print("--------------> uid=",uid)
        if uid.password==u_password:
            print("-------pass",u_password)
            print("   ---------welcom")
            if uid.role=='member':
                cid=Member.objects.get(user_id=uid)
                request.session['m_email']=uid.email
                print("--------------->m_email",request.session['m_email'])
                context={
                    'uid':uid,
                    'cid':cid,
                }
                    #send_mail("welcome","welcome to digital society","jinaldod12@gmail.com",["jinaldod8151@gmail.com","jinaldod12@gmail.com"])
            return render(request,'member/m_index.html',{'context':context})
        else:
            print("invalid password")
            e_msg="invalid password"
            return render(request,'member/m_login.html',{'e_msg':e_msg})    
    except Exception as e:
        print("---------->e  ",e)
        print("Email does not exist")
        e_msg="Email does not exist"
        return render(request,'member/m_login.html',{'e_msg':e_msg})

def m_logout(request):
    if 'm_email' in request.session:
        del request.session['m_email']
        #print("--------------->session _-___m_email",request.session['m_email'])
        return render(request,'member/m_login.html')
    else:
        return render(request,'member/m_login.html')
def m_forgot_password(request):
    return render(request,'member/forgot_password.html') 

def m_send_otp(request):
    try:
        email=request.POST['email']
        generate_otp=randint(1111,9999)
        uid=User.objects.get(email=email)
        print('generate otp-----------------------------------------------')
        if uid:
            print("get uid-----------------------")
            uid.otp=generate_otp
            uid.save()   #update
            if uid.role=='member':
                cid=Member.objects.get(user_id=uid)
                sendmail(" Forgot Password ","mail_template",email,{'otp':generate_otp,'cid':cid})
                print("-------------send otp--------------")
                return render(request,'member/reset_password.html',{'email':email})
        else:
            e_msg="Email does not exist"
            return render(request,'member/forgot_password.html',{'e_msg':e_msg})
    except:
        e_msg="Email does not exist"
        return render(request,'member/forgot_password.html',{'e_msg':e_msg})

def m_reset_password(request):
    try:
        email=request.POST['email']
        otp=request.POST['otp']
        newpassword=request.POST['newpassword']
        repassword=request.POST['repassword']
        uid=User.objects.get(email=email)
        print("----------------->",email)
        if uid:
            if str(uid.otp)==otp and newpassword==repassword:
                print('-------------------->new ',newpassword)
                uid.password=newpassword
                uid.save()  
                print("---------------------------------->rpass",uid.password)
                s_msg="password reset succesfully"
                print('------------>su',s_msg)
                return render(request,'member/m_login.html',{'s_msg':s_msg})
            else:
                e_msg="invalid otp or password"
                return render(request,'member/reset_password.html',{'e_msg':e_msg})
    except Exception as e:
        print("exeption-----------",e)
        e_msg="Email does not exist"
        return render(request,'member/forgot_password.html',{'e_msg':e_msg})

def m_profile(request):
    uid=User.objects.get(email=request.session['m_email'])
    cid=Member.objects.get(user_id=uid)
    noticedata=Notice.objects.all()
    context={
            'uid':uid,
            'cid':cid,
            'noticedata':noticedata
            
        }
    return render(request,'member/m_profile.html',{'context':context})

def m_profile_update(request):
    uid=User.objects.get(email=request.session['m_email'])
    cid=Member.objects.get(user_id=uid)
    newpassword=request.POST['newPassword']
    fname=request.POST['fname']
    lname=request.POST['lname']
    job_profession=request.POST['jobProfession']
    jobAddress=request.POST['jobAddress']
    address=request.POST['address']
    family_member=request.POST['familyMemberDetail']
    contect_no=request.POST['contact_no']
    house_no=request.POST['homeno']
    vehicleType=request.POST['vehicleType']
    vehicleNumber=request.POST['vehicleNumber']
    bloodgroup=request.POST['bloodgroup']
    mid=MemberDetails.objects.get(homeno=house_no)
    cid.fname=fname
    cid.lname=lname
    mid.job_profession=job_profession
    mid.family_member_details=family_member
    mid.contact_no=contect_no
    mid.address=address
    mid.home=house_no
    mid.job_address=jobAddress
    mid.blood_group=bloodgroup
    mid.vehicle_type=vehicleType
    mid.vehicle_no=vehicleNumber
    if "profilepic" in request.FILES:
        profilepic=request.FILES['profilepic']
        cid.profile_pic=profilepic
        cid.save()

    uid.save()
    cid.save()
    mid.save()
    context={
            'uid':uid,
            'cid':cid,
            
        }
    return render(request,'member/m_profile.html',{'context':context})


    