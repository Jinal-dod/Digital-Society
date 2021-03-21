from django.shortcuts import render
from .models import *
from .utils import *
from random import *
#from django.core.mail import send_mail
# Create your views here.

def index(request):
    try:
        if'c_email' in request.session:
            uid=User.objects.get(email=request.session['c_email'])
            cid=Chairman.objects.get(user_id=uid)
            context={
                'uid':uid,
                'cid':cid,
            }
            return render(request,'chairman/index.html',{'context':context})
        else:
            return render(request,'chairman/c_login.html')
    except:
        return render(request,'chairman/c_login.html')

def login(request):
    return render(request,'chairman/c_login.html')

def login_evalute(request):
    try:
        u_email=request.POST['email']
        u_password=request.POST['password']
        uid=User.objects.get(email=u_email)
        print("--------------> uid=",uid)
        if uid.password==u_password:
            print("-------pass",u_password)
            print("   ---------welcom")
            if uid.role=='chairman':
                cid=Chairman.objects.get(user_id=uid)
                request.session['c_email']=uid.email
                print("--------------->c_email",request.session['c_email'])
                context={
                    'uid':uid,
                    'cid':cid,
                }
            #send_mail("welcome","welcome to digital society","jinaldod12@gmail.com",["jinaldod8151@gmail.com","jinaldod12@gmail.com"])
            return render(request,'chairman/index.html',{'context':context})
        else:
            print("invalid password")
            e_msg="invalid password"
            return render(request,'chairman/c_login.html',{'e_msg':e_msg})    
    except Exception as e:
        print("---------->e  ",e)
        print("Email does not exist")
        e_msg="Email does not exist"
        return render(request,'chairman/c_login.html',{'e_msg':e_msg})

def logout(request):
    if 'c_email' in request.session:
        del request.session['c_email']
        #print("--------------->session _-___c_email",request.session['c_email'])
        return render(request,'chairman/c_login.html')
    else:
        return render(request,'chairman/c_login.html')
def forgot_password(request):
    return render(request,'chairman/forgot_password.html') 

def send_otp(request):
    try:
        email=request.POST['email']
        generate_otp=randint(1111,9999)
        uid=User.objects.get(email=email)
        if uid:
            uid.otp=generate_otp
            uid.save()   #update
            if uid.role=='chairman':
                cid=Chairman.objects.get(user_id=uid)
                sendmail(" Forgot Password ","mail_template",email,{'otp':generate_otp,'cid':cid})
                print("-------------send otp--------------")
                return render(request,'chairman/reset_password.html',{'email':email})
        else:
            e_msg="Email does not exist"
            return render(request,'chairman/forgot_password.html',{'e_msg':e_msg})
    except:
        e_msg="Email does not exist"
        return render(request,'chairman/forgot_password.html',{'e_msg':e_msg})

def reset_password(request):
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
                return render(request,'chairman/c_login.html',{'s_msg':s_msg})
            else:
                e_msg="invalid otp or password"
                return render(request,'chairman/reset_password.html',{'e_msg':e_msg})
    except Exception as e:
        print("exeption-----------",e)
        e_msg="Email does not exist"
        return render(request,'chairman/forgot_password.html',{'e_msg':e_msg})

def add_notice_page(request):
    if'c_email' in request.session:
        uid=User.objects.get(email=request.session['c_email'])
        cid=Chairman.objects.get(user_id=uid)
        context={
            'uid':uid,
            'cid':cid,
        }
        return render(request,'chairman/add_notice.html',{'context':context})

def add_notice(request):
    title=request.POST['title']
    desc=request.POST['desc']
    print("-------------title>>"),title
    print("------------des",desc)
    nid=Notice.objects.create(title=title,description=desc)
    uid=User.objects.get(email=request.session['c_email'])
    cid=Chairman.objects.get(user_id=uid)
    noticedata=Notice.objects.all()
    context={
            'uid':uid,
            'cid':cid,
            'noticedata':noticedata,
        }
    return render(request,'chairman/notice_list.html',{'context':context})

def view_notice(request):
    uid=User.objects.get(email=request.session['c_email'])
    cid=Chairman.objects.get(user_id=uid)
    noticedata=Notice.objects.all()
    context={
            'uid':uid,
            'cid':cid,
            'noticedata':noticedata,
        }
    return render(request,'chairman/notice_list.html',{'context':context})

def profile(request):
    uid=User.objects.get(email=request.session['c_email'])
    cid=Chairman.objects.get(user_id=uid)
    noticedata=Notice.objects.all()
    context={
            'uid':uid,
            'cid':cid,
            'noticedata':noticedata
            
        }
    return render(request,'chairman/profile.html',{'context':context})

def profile_update(request):

    uid=User.objects.get(email=request.session['c_email'])
    cid=Chairman.objects.get(user_id=uid)
    
    c_fname=request.POST['c_fname']
    c_lname=request.POST['c_lname']
    c_contact_no=request.POST['c_contact_no']
    c_homeno=request.POST['c_homeno']
    c_address=request.POST['c_address']
    c_jobProfession=request.POST['c_jobProfession']
    c_job_address=request.POST['c_job_address']
    c_vehicle_type=request.POST['c_vehicle_type']
    c_vehicle_no=request.POST['c_vehicle_no']
    c_blood_group=request.POST['c_blood_group']
    c_family_member=request.POST['c_family_member']
    c_newpassword=request.POST['c_newpassword']
    c_currentPassword=request.POST['c_currentPassword']
    mid=MemberDetails.objects.get(homeno=c_homeno)

    cid.fname=c_fname
    cid.lname=c_lname
    mid.job_profession=c_jobProfession
    mid.family_member_details=c_family_member
    mid.contact_no=c_contact_no
    mid.address=c_address
    mid.job_address=c_job_address
    mid.blood_group=c_blood_group
    mid.vehicle_type=c_vehicle_type
    mid.vehicle_no=c_vehicle_no
    if "c_newpassword" in request.POST:
        uid.password=c_newpassword
        uid.save()
    else:
        uid.password=c_currentPassword
        uid.save()
    if "c_profilePic" in request.FILES:
        c_profilePic=request.FILES['c_profilePic']
        cid.profile_pic=c_profilePic
        cid.save()

    uid.save()
    cid.save()
    mid.save()
    context={
            'uid':uid,
            'cid':cid,
            'mid':mid,
            
        }
    return render(request,'chairman/profile.html',{'context':context})
    


def add_events_page(request):
    if'c_email' in request.session:
        uid=User.objects.get(email=request.session['c_email'])
        cid=Chairman.objects.get(user_id=uid)

        context={
            'uid':uid,
            'cid':cid,
        }
        return render(request,'chairman/add_events.html',{'context':context})
def add_events(request):
    title=request.POST['title']
    desc=request.POST['desc']
    eventpic=request.FILES['eventpic']
    print("-------------title>>"),title
    print("------------des",desc)
    eid=Events.objects.create(title=title,description=desc,event_pic=eventpic)
    uid=User.objects.get(email=request.session['c_email'])
    cid=Chairman.objects.get(user_id=uid)
    eventdata=Events.objects.all()
    context={
            'uid':uid,
            'cid':cid,
            'eventdata':eventdata,
        }
    return render(request,'chairman/view_events.html',{'context':context})
def view_events(request):
    uid=User.objects.get(email=request.session['c_email'])
    cid=Chairman.objects.get(user_id=uid)
    eventdata=Events.objects.all()
    context={
            'uid':uid,
            'cid':cid,
            'eventdata':eventdata,
        }
    return render(request,'chairman/view_events.html',{'context':context})

def add_member_page(request):
    if'c_email' in request.session:
        uid=User.objects.get(email=request.session['c_email'])
        cid=Chairman.objects.get(user_id=uid)
        context={
            'uid':uid,
            'cid':cid,
        }
        return render(request,'chairman/add_member.html',{'context':context})

def add_member(request):
    if'c_email' in request.session:
        uid=User.objects.get(email=request.session['c_email'])
        cid=Chairman.objects.get(user_id=uid)
        role='member'
        f_name=request.POST['f_name']
        l_name=request.POST['l_name']
        email=request.POST['email']
        contact_no=request.POST['contact_no']
        homeno=request.POST['homeno']
        address=request.POST['address']
        job_profession=request.POST['job_profession']
        job_address=request.POST['job_address']
        vehicle_type=request.POST['vehicle_type']
        vehicle_no=request.POST['vehicle_no']
        blood_group=request.POST['blood_group']
        family_member=request.POST['family_member']
        if "m_profilepic" in request.FILES:
            m_profilepic=request.FILES['m_profilepic']
           
    
        g_password=f_name[:3]+str(randint(111,999))            
        user_id=User.objects.create(email=email,password=g_password)
        member_detail_id=MemberDetails.objects.create(contact_no=contact_no,
                                                    homeno=homeno,
                                                    address=address,
                                                    job_profession=job_profession,
                                                    job_address=job_address,
                                                    vehicle_type=vehicle_type,
                                                    vehicle_no=vehicle_no,
                                                    blood_group=blood_group,
                                                    family_member_details=family_member)
   
        
        member_detail=Member.objects.create(fname=f_name,lname=l_name,profile_pic=m_profilepic,user_id=user_id,m_id=member_detail_id)
        
        mid=Member.objects.all()
        context={
                    'uid':uid,
                    'f_name':f_name,
                    'mid':mid,
                }
        
        sendPasswordMail('Password to login','email_password',email,{'password':g_password,'f_name':f_name, 'mid':mid})
        print('-----------------------------',email)
        return render(request,'chairman/view_member.html',{'context':context})
    else:
        return render(request,'chairman/c_login.html')

def view_member(request):
    if 'c_email' in request.session:
        uid=User.objects.get(email=request.session['c_email'])
        cid=Chairman.objects.get(user_id=uid)
        mid=Member.objects.all()
        context={
            'uid':uid,
            'cid':cid,
            'mid':mid,
            
        }
        return render(request,'chairman/view_member.html',{'context':context})
    else:
        return render(request,'chairman/c_login.html') 

def view_member_profile(request,pk):    #primary key accepted
    if 'c_email' in request.session:
        uid=User.objects.get(email=request.session['c_email'])
        cid=Chairman.objects.get(user_id=uid)
        mid=Member.objects.get(id=pk)      #get pk to id
        noticeData=Notice.objects.all()
        context={
            'uid':uid,
            'cid':cid,
            'mid':mid,
            'noticeData':noticeData,

        }
       
        return render(request,'chairman/view_member_profile.html',{'context':context})
    else:
        return render(request,'chairman/c_login.html')    
def member_profile_update(request):
    
    m_fname=request.POST['m_fname']
    m_lname=request.POST['m_lname']
    m_email=request.POST['m_email']
    m_contect_no=request.POST['m_contect_no']
    m_house_no=request.POST['m_house_no']
    m_address=request.POST['m_address']
    m_job_profession=request.POST['m_job_profession']
    m_job_address=request.POST['m_job_address']
    m_vehicle_type=request.POST['m_vehicle_type']
    m_vehicle_no=request.POST['m_vehicle_no']
    m_blood_group=request.POST['m_blood_group']
    m_family_member=request.POST['m_family_member']
    m_newpassword=request.POST['m_newpassword']
    uid=User.objects.get(email=m_email)
    cid=Member.objects.get(user_id=uid)
    mid=MemberDetails.objects.get(homeno=m_house_no)
    # uid=User.objects.get(email=request.session['c_email'])
    # cid=Chairman.objects.get(user_id=uid)
    cid.fname=m_fname
    cid.lname=m_lname
    mid.job_profession=m_job_profession
    mid.family_member_details=m_family_member
    mid.contact_no=m_contect_no
    mid.address=m_address
    mid.homeno=m_house_no
    mid.job_address=m_job_address
    mid.blood_group=m_blood_group
    mid.vehicle_type=m_vehicle_type
    mid.vehicle_no=m_vehicle_no
    if "m_newpassword" in request.POST:
        uid.password=m_newpassword
        uid.save()
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
    return render(request,'chairman/profile.html',{'context':context})

def watchman_list(request):
    uid=User.objects.get(email=request.session['c_email'])
    cid=Chairman.objects.get(user_id=uid)
    wid=Watchman.objects.all()
    context={
            'uid':uid,
            'cid':cid,
            'wid':wid,   
        }
    return render(request,'chairman/watchman_list.html',{'context':context})

def ver_watch(request,pk):
    wid=Watchman.objects.get(id=pk)
    uid=User.objects.get(email=request.session['c_email'])
    cid=Chairman.objects.get(user_id=uid)
    
    if wid.is_verified == False:
        wid.is_verified = True
        wid.save()
    elif wid.is_verified == True:    
        wid.is_verified = False
        wid.save()
    wid=Watchman.objects.all()
    context={
            'uid':uid,
            'cid':cid,
            'wid':wid,   
        }
    return render(request,'chairman/watchman_list.html',{'context':context})


