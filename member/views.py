from django.shortcuts import render
from chairman.models import *
from random import *
from .utils import *

# Create your views here.
def m_index(request):
    try:
        if'm_email' in request.session:
            uid=User.objects.get(email=request.session['m_email'])
            cid=Member.objects.get(user_id=uid)
            notice_count=Notice.objects.all().count()
            member_count=Member.objects.all().count()
            event_count=Events.objects.all().count()
            l_event=Events.objects.filter().order_by('-id')[:1]
            l_Notice=Notice.objects.filter().order_by('-id')[:1]
            l_Member=Member.objects.filter().order_by('-id')[:3]
            context={
                'uid':uid,
                'cid':cid,
                'notice_count':notice_count,
                'member_count':member_count,
                'event_count':event_count,
                'l_event':l_event,
                'l_Notice':l_Notice,
                'l_Member':l_Member,
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
       
        if uid.password==u_password:
            
            if uid.role=='member':
                cid=Member.objects.get(user_id=uid)
                notice_count=Notice.objects.all().count()
                member_count=Member.objects.all().count()
                event_count=Events.objects.all().count()
                l_event=Events.objects.filter().order_by('-id')[:1]
                l_Notice=Notice.objects.filter().order_by('-id')[:1]
                l_Member=Member.objects.filter().order_by('-id')[:3]
                request.session['m_email']=uid.email
             
                context={
                    'uid':uid,
                    'cid':cid,
                    'notice_count':notice_count,
                    'member_count':member_count,
                    'event_count':event_count,
                    'l_event':l_event,
                    'l_Notice':l_Notice,
                    'l_Member':l_Member,
                }
            return render(request,'member/m_index.html',{'context':context})
        else:
            print("invalid password")
            e_msg="invalid password"
            return render(request,'member/m_login.html',{'e_msg':e_msg})    
    except Exception as e:
   
        print("Email does not exist")
        e_msg="Email does not exist"
        return render(request,'member/m_login.html',{'e_msg':e_msg})

def m_logout(request):
    if 'm_email' in request.session:
        del request.session['m_email']
  
        return render(request,'chairman/login.html')
    else:
        return render(request,'chairman/login.html')

def m_forgot_password(request):
    return render(request,'member/m_forgot_password.html') 

def m_send_otp(request):
    try:
        email=request.POST['email']
        generate_otp=randint(1111,9999)
        uid=User.objects.get(email=email)
        if uid:  
            uid.otp=generate_otp
            uid.save()  
            if uid.role=='member':
                cid=Member.objects.get(user_id=uid)
                sendmail(" Forgot Password ","mail_template",email,{'otp':generate_otp,'cid':cid})
              
                return render(request,'member/m_reset_password.html',{'email':email})
        else:
            e_msg="Email does not exist"
            return render(request,'member/m_forgot_password.html',{'e_msg':e_msg})
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
        if uid:
            if str(uid.otp)==otp and newpassword==repassword:
                uid.password=newpassword
                uid.save()  
                s_msg="password reset succesfully"
                return render(request,'member/m_login.html',{'s_msg':s_msg})
            else:
                e_msg="invalid otp or password"
                return render(request,'member/m_reset_password.html',{'e_msg':e_msg})
    except Exception as e:
        e_msg="Email does not exist"
        return render(request,'member/m_forgot_password.html',{'e_msg':e_msg})

def m_add_contect(request):
    if'm_email' in request.session:
        uid=User.objects.get(email=request.session['m_email'])
        cid=Member.objects.get(user_id=uid)
        context={
            'uid':uid,
            'cid':cid,
        }
        return render(request,'member/m_all_contect.html',{'context':context})
    else:
        return render(request,'member/m_login.html')

def m_view_events(request):
    if'm_email' in request.session:
        uid=User.objects.get(email=request.session['m_email'])
        cid=Member.objects.get(user_id=uid)
        eventdata=Events.objects.all().order_by('-id')
        context={
                'uid':uid,
                'cid':cid,
                'eventdata':eventdata,
            }
        return render(request,'member/m_view_events.html',{'context':context})
    else:
            return render(request,'member/m_login.html')

def m_profile(request):
    if'm_email' in request.session:
        uid=User.objects.get(email=request.session['m_email'])
        cid=Member.objects.get(user_id=uid)
        noticedata=Notice.objects.all()
        context={
                'uid':uid,
                'cid':cid,
                'noticedata':noticedata           
            }
        return render(request,'member/m_profile.html',{'context':context})
    else:
            return render(request,'member/m_login.html')

def m_profile_update(request):
    if'm_email' in request.session:
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
    else:
            return render(request,'member/m_login.html')

def m_view_member(request):
    if 'm_email' in request.session:
        uid=User.objects.get(email=request.session['m_email'])
        cid=Member.objects.get(user_id=uid)
        mid=Member.objects.all().order_by('-id')
        context={
            'uid':uid,
            'cid':cid,
            'mid':mid,
        }
        return render(request,'member/m_view_member.html',{'context':context})
    else:
        return render(request,'member/m_login.html')

def m_view_member_profile(request,pk):    #primary key accepted
    if 'm_email' in request.session:
        uid=User.objects.get(email=request.session['m_email'])
        cid=Member.objects.get(user_id=uid)
        mid=Member.objects.get(id=pk)      #get pk to id
        noticeData=Notice.objects.all()
        context={
            'uid':uid,
            'cid':cid,
            'mid':mid,
            'noticeData':noticeData,
        }
        return render(request,'member/m_view_member_profile.html',{'context':context})
    else:
        return render(request,'member/m_login.html')

def m_view_notice(request):
    if'm_email' in request.session:
        uid=User.objects.get(email=request.session['m_email'])
        cid=Member.objects.get(user_id=uid)
        noticedata=Notice.objects.all().order_by('-id')
        context={
                'uid':uid,
                'cid':cid,
                'noticedata':noticedata,
            }
        return render(request,'member/m_view_notice.html',{'context':context})
    else:
            return render(request,'member/m_login.html')

def m_add_complain_page(request):
    if'm_email' in request.session:
        uid=User.objects.get(email=request.session['m_email'])
        cid=Member.objects.get(user_id=uid)
        context={
            'uid':uid,
            'cid':cid,
        }
        return render(request,'member/m_add_complain.html',{'context':context})
    else:
            return render(request,'member/m_login.html')

def m_add_complain(request):
    if'm_email' in request.session:
        m_c_title=request.POST['m_c_title']
        m_c_desc=request.POST['m_c_desc']
        nid=complain.objects.create(title=m_c_title,description=m_c_desc)
        uid=User.objects.get(email=request.session['m_email'])
        cid=Member.objects.get(user_id=uid)
        complaindata=complain.objects.all().order_by('-id')
        context={
                'uid':uid,
                'cid':cid,
                'complaindata':complaindata,
            }
        return render(request,'member/m_view_complain.html',{'context':context})
    else:
            return render(request,'member/m_login.html')

def m_view_complain(request):
    if'm_email' in request.session:
        uid=User.objects.get(email=request.session['m_email'])
        cid=Member.objects.get(user_id=uid)
        complaindata=complain.objects.all().order_by('-id')
        context={
                'uid':uid,
                'cid':cid,
                'complaindata':complaindata,
            }
        return render(request,'member/m_view_complain.html',{'context':context})  
    else:
            return render(request,'member/m_login.html')

def delete_complain(request,pk):
    if'm_email' in request.session:
        uid=User.objects.get(email=request.session['m_email'])
        cid=Member.objects.get(user_id=uid)
        c_id=complain.objects.get(id=pk)
        complaindata=complain.objects.all().order_by('-id')
        c_id.delete()
        context={
            'uid':uid,
            'cid':cid,
            'complaindata':complaindata,
            'c_id':c_id,
        }
        return render(request,'member/m_view_complain.html',{'context':context})
    else:
        return render(request,'chairman/c_login.html')

def m_add_suggestion_page(request):
    if'm_email' in request.session:
        uid=User.objects.get(email=request.session['m_email'])
        cid=Member.objects.get(user_id=uid)
        context={
            'uid':uid,
            'cid':cid,
        }
        return render(request,'member/m_add_suggestion.html',{'context':context})
    else:
            return render(request,'member/m_login.html')

def m_add_suggestion(request):
    if'm_email' in request.session:
        m_s_title=request.POST['m_s_title']
        m_s_desc=request.POST['m_s_desc']
        sid=Suggestion.objects.create(title=m_s_title,description=m_s_desc)
        uid=User.objects.get(email=request.session['m_email'])
        cid=Member.objects.get(user_id=uid)
        suggestiondata=Suggestion.objects.all().order_by('-id')
        context={
                'uid':uid,
                'cid':cid,
                'suggestiondata':suggestiondata,
            }
        return render(request,'member/m_view_suggestion.html',{'context':context})
    else:
            return render(request,'member/m_login.html')

def m_view_suggestion(request):
    if'm_email' in request.session:
        uid=User.objects.get(email=request.session['m_email'])
        cid=Member.objects.get(user_id=uid)
        suggestiondata=Suggestion.objects.all().order_by('-id')
        context={
                'uid':uid,
                'cid':cid,
                'suggestiondata':suggestiondata,
            }
        return render(request,'member/m_view_suggestion.html',{'context':context})  
    else:
            return render(request,'member/m_login.html')

def delete_suggestion(request,pk):
    if'm_email' in request.session:
        uid=User.objects.get(email=request.session['m_email'])
        cid=Member.objects.get(user_id=uid)
        s_id=Suggestion.objects.get(id=pk)
        suggestiondata=Suggestion.objects.all().order_by('-id')
        s_id.delete()
        context={
            'uid':uid,
            'cid':cid,
            'suggestiondata':suggestiondata,
            's_id':s_id,
        }
        return render(request,'member/m_view_suggestion.html',{'context':context})
    else:
        return render(request,'chairman/c_login.html')

def m_view_photos(request):
    if'm_email' in request.session:
        uid=User.objects.get(email=request.session['m_email'])
        cid=Member.objects.get(user_id=uid)
        photodata=Photos.objects.all().order_by('-id')
        context={
                'uid':uid,
                'cid':cid,
                'photodata':photodata,
            }
        return render(request,'member/m_view_photos.html',{'context':context})
    else:
            return render(request,'member/m_login.html')

def m_view_videos(request):
    if'm_email' in request.session:
        uid=User.objects.get(email=request.session['m_email'])
        cid=Member.objects.get(user_id=uid)
        videodata=Videos.objects.all().order_by('-id')
        context={
                'uid':uid,
                'cid':cid,
                'videodata':videodata,
            }
        return render(request,'member/m_view_videos.html',{'context':context})
    else:
            return render(request,'member/m_login.html')

def m_view_visitors(request):
    if "m_email" in request.session:
        uid=User.objects.get(email=request.session['m_email']) 
        cid=Member.objects.get(user_id=uid)           
        vid=Visitors.objects.filter(vm_id=cid.m_id)
        context={
            "uid":uid,
            "cid":cid,
            "vid":vid,
        }
        return render(request,"member/m_view_visitors.html",{"context":context})
    else:
        return render(request,'member/m_login.html')

def s_view_maintenance(request):
    uid=User.objects.get(email=request.session['m_email'])         
    cid=Member.objects.get(user_id=uid)
    maintenance_data=Maintenance.objects.filter(member_id=cid.id).order_by("-id")
    context={
        "uid":uid,
        "cid":cid,
        "maintenance_data":maintenance_data,
    }
    return render(request,"member/s_view_maintenance.html",{"context":context})

def s_maintenance_list(request):
    uid=User.objects.get(email=request.session['m_email'])         
    cid=Member.objects.get(user_id=uid)
    maintenance_data=Maintenance.objects.filter(member_id=cid.id).order_by("-id")
    context={
        "uid":uid,
        "maintenance_data":maintenance_data,
        "cid":cid,
    }
    return render(request,"member/s_maintenance_list.html",{"context":context})  
