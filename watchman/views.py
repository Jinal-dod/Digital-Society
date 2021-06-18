from django.shortcuts import render
from chairman.models import *
from random import *
from .utils import *

# Create your views here.
def w_index(request):
    if'w_email' in request.session:
        uid=Watchman.objects.get(email=request.session['w_email'])
        notice_count=Notice.objects.all().count()
        member_count=Member.objects.all().count()
        event_count=Events.objects.all().count()
        l_event=Events.objects.filter().order_by('-id')[:1]
        l_Notice=Notice.objects.filter().order_by('-id')[:1]
        l_Member=Member.objects.filter().order_by('-id')[:3]
        context={
                'uid':uid,
                'notice_count':notice_count,
                'member_count':member_count,
                'event_count':event_count,
                'l_event':l_event,
                'l_Notice':l_Notice,
                'l_Member':l_Member,
        }
        return render(request,'watchman/w_index.html',{'context':context})
    else:
         return render(request,'watchman/w_login.html')
        
def registration_page(request):
    
    return render(request,'watchman/registration.html')

def register(request):
    if request.POST:
        fname=request.POST['fname']
        lname=request.POST['lname']
        contactNo=request.POST['contactNo']
        email=request.POST['email']
        password=request.POST['password']
        c_email='jinaldod12@gmail.com'
        role='watchman'
        uid=Chairman.objects.all()
        wid=Watchman.objects.create(fname=fname,lname=lname,contactno=contactNo,email=email,password=password,role=role)
        sendmail("For approve Watchman Registration ","w_mail_template",c_email,{'uid':uid})
        s_msg='Your Registration Request is sent to Chairman for approval'
        return render(request,'watchman/w_login.html',{'s_msg':s_msg})

    else:
        s_msg='Rgisteration not Successfully'
        return render(request,'watchman/registration.html',{'s_msg':s_msg})

def w_login(request):
    return render(request,'watchman/w_login.html')

def w_login_evalute(request):
    try:
        u_email=request.POST['email']
        u_password=request.POST['password']
        uid=Watchman.objects.get(email=u_email)
        if uid.password==u_password:
            if uid.role=='watchman':
                if uid.is_verified == True:
                    notice_count=Notice.objects.all().count()
                    member_count=Member.objects.all().count()
                    event_count=Events.objects.all().count()
                    l_event=Events.objects.filter().order_by('-id')[:1]
                    l_Notice=Notice.objects.filter().order_by('-id')[:1]
                    l_Member=Member.objects.filter().order_by('-id')[:3]
                    request.session['w_email']=uid.email
                    context={
                        'uid':uid,
                        'notice_count':notice_count,
                        'member_count':member_count,
                        'event_count':event_count,
                        'l_event':l_event,
                        'l_Notice':l_Notice,
                        'l_Member':l_Member,
                    }
        #send_mail("welcome","welcome to digital society","jinaldod12@gmail.com",["jinaldod8151@gmail.com","jinaldod12@gmail.com"])
                    return render(request,'watchman/w_index.html',{'context':context})
            else:
                e_msg="You Are not Verified please connected chairman"
                return render(request,'watchman/w_login.html',{'e_msg':e_msg})    
        else:
            print("invalid password")
            e_msg="invalid password"
            return render(request,'watchman/w_login.html',{'e_msg':e_msg})    
    except Exception as e:
        print("Email does not exist")
        e_msg="Email does not exist"
        return render(request,'watchman/w_login.html',{'e_msg':e_msg})

def w_forgot_password_page(request):
    return render(request,'watchman/w_forgot_password.html')

def w_send_otp(request):
    if request.POST:
        email=request.POST['email']
        generate_otp=randint(1111,9999)
        uid=Watchman.objects.get(email=email)
        if uid:
            w_sendPasswordMail(" Forgot Password ","w_otp_email",email,{'otp':generate_otp,'uid':uid})
            return render(request,'watchman/w_reset_password.html',{'email':email,'otp':generate_otp})
        else:
            e_msg="Email does not exist"
            return render(request,'watchman/w_forgot_password.html',{'e_msg':e_msg})
    else:
        e_msg="Email does not exist"
        return render(request,'watchman/w_login.html',{'e_msg':e_msg})
    
def w_reset_password(request):
    if request.POST:
        email=request.POST['w_email']
        otp1=request.POST['otp'] 
        otp=request.POST['w_otp']
        newpassword=request.POST['w_newpassword']
        repassword=request.POST['w_repassword']
        uid=Watchman.objects.get(email=email)
        if uid:
            if otp1==otp and newpassword==repassword:
                uid.password=newpassword
                uid.save()
                s_msg="password reset succesfully"
                return render(request,'watchman/w_login.html',{'s_msg':s_msg})
            else:
                e_msg="Email does not exist"
                return render(request,'watchman/w_forgot_password.html',{'e_msg':e_msg})
    else:
        e_msg="Email does not exist"
        return render(request,'watchman/w_login.html',{'e_msg':e_msg})

def w_logout(request):
    if 'w_email' in request.session:
        del request.session['w_email']
        return render(request,"chairman/login.html")
    else:
        return render(request,"chairman/login.html")

def w_add_contect(request):
    if'c_email' in request.session:
        uid=Watchman.objects.get(email=request.session['w_email'])
        context={
            'uid':uid,
        }
        return render(request,'watchman/w_all_contect.html',{'context':context})
    else:
        return render(request,'watchman/w_login.html')

def w_view_notice(request):
    if 'w_email' in request.session:
        uid=Watchman.objects.get(email=request.session['w_email'])
        noticedata=Notice.objects.all().order_by('-id')
        context={
                'uid':uid,
                'noticedata':noticedata,
            }
        return render(request,'watchman/w_view_notice.html',{'context':context})
    else:
        return render(request,'watchman/w_login.html')

def w_view_events(request):
    if'w_email' in request.session:
        uid=Watchman.objects.get(email=request.session['w_email'])
        eventdata=Events.objects.all().order_by('-id')
        context={
                'uid':uid,
                'eventdata':eventdata,
            }
        return render(request,'watchman/w_view_events.html',{'context':context})
    else:
        return render(request,'watchman/w_login.html')

def w_view_member(request):
    if 'w_email' in request.session:
        uid=Watchman.objects.get(email=request.session['w_email'])
        mid=Member.objects.all().order_by('-id')
        context={
            'uid':uid,
            'mid':mid,
            
        }
        return render(request,'watchman/w_view_member.html',{'context':context})
    else:
        return render(request,'watchman/w_login.html')

def w_view_member_profile(request,pk):    #primary key accepted
    if 'w_email' in request.session:
        uid=Watchman.objects.get(email=request.session['w_email'])
        mid=Member.objects.get(id=pk)      #get pk to id
        context={
            'uid':uid, 
            'mid':mid,
        }
        return render(request,'watchman/w_view_member_profile.html',{'context':context})
    else:
        return render(request,'watchman/w_login.html')

def w_view_photos(request):
    if'w_email' in request.session:
        uid=Watchman.objects.get(email=request.session['w_email'])
        photodata=Photos.objects.all().order_by('-id')
        context={
                'uid':uid,
                'photodata':photodata,
            }
        return render(request,'watchman/w_view_photos.html',{'context':context})
    else:
        return render(request,'watchman/w_login.html')

def w_view_videos(request):
    if'w_email' in request.session:
        uid=Watchman.objects.get(email=request.session['w_email'])
        videodata=Videos.objects.all().order_by('-id')
        context={
                'uid':uid,
                'videodata':videodata,
            }
        return render(request,'watchman/w_view_videos.html',{'context':context})
    else:
        return render(request,'watchman/w_login.html')

def w_profile(request):
    if'w_email' in request.session:
        uid=Watchman.objects.get(email=request.session['w_email'])
        context={
                'uid':uid,
            }
        return render(request,'watchman/w_profile.html',{'context':context})
    else:
        return render(request,'watchman/w_login.html')

def w_profile_update(request):
    if'w_email' in request.session:
        uid=Watchman.objects.get(email=request.session['w_email'])
        fname=request.POST['fname']
        lname=request.POST['lname']
        contact_no=request.POST['contact_no']
        address=request.POST['address']
        blood_group=request.POST['blood_group']
        family_member=request.POST['family_member']
        age=request.POST['age']
        newpassword=request.POST['newpassword']
        currentPassword=request.POST['currentPassword']
        
        uid.fname=fname
        uid.lname=lname
        uid.family_contact=family_member
        uid.contactno=contact_no
        uid.address=address
        uid.blood_group=blood_group
        uid.age=age
        if newpassword:
            uid.password=newpassword
            uid.save()

        if "profilePic" in request.FILES:
            profilePic=request.FILES['profilePic']
            uid.profile_pic=profilePic
            uid.save()

        uid.save()
        context={
                'uid':uid,        
            }
        return render(request,'watchman/w_profile.html',{'context':context})
    else:
        return render(request,'watchman/w_login.html')

def w_view_visitors(request):
    if "w_email" in request.session:
        uid=Watchman.objects.get(email=request.session['w_email'])            
        vid=Visitors.objects.all()
        context={
            "uid":uid,
            "vid":vid,
        }
        return render(request,"watchman/w_view_visitors.html",{"context":context})
    else:
        return render(request,"watchman/w_index.html")
        
def add_visitor_page(request):
    print("add_visitor_page Called")
    if "w_email" in request.session:
        uid=Watchman.objects.get(email=request.session['w_email'])
        m = MemberDetails.objects.all()         
        context={
            "uid":uid,
            'm':m,
        }
        return render(request,"watchman/add_visitors.html",{"context":context})
    else:
        return render(request,"watchman/w_index.html")

def add_visitor(request):
    if "w_email" in request.session:
        uid=Watchman.objects.get(email=request.session['w_email'])  
        try:    
            f_name=request.POST['f_name']
            l_name=request.POST['l_name']
            contact_no=request.POST['contact_no']
            email=request.POST['email']
            house_no=request.POST['house_no']
            mem_details = MemberDetails.objects.get(homeno=house_no)
            vid=Visitors.objects.create(vm_id=mem_details,f_name=f_name,l_name=l_name,email=email,contact_no=contact_no,house_no=house_no)
            vid=Visitors.objects.all()
            context={
                "uid":uid,
                "vid":vid,
            }
            return render(request,"watchman/w_view_visitors.html",{"context":context})
        except:
            vid=Visitors.objects.all()
            context={
                "uid":uid,
                "vid":vid,
            }
            return render(request,"watchman/w_view_visitors.html",{"context":context})
    else:
        return render(request,"watchman/w_index.html")
