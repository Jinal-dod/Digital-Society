from django.shortcuts import render,redirect
from .models import *
from .utils import *    #from django.core.mail import send_mail
from random import *
from .paytm import generate_checksum, verify_checksum
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
from django.http import JsonResponse

# Create your views here.
def index(request):
    try:
        if'c_email' in request.session:
            uid=User.objects.get(email=request.session['c_email'])
            cid=Chairman.objects.get(user_id=uid)
            notice_count=Notice.objects.all().count()
            member_count=Member.objects.all().count()
            event_count=Events.objects.all().count()
            l_event=Events.objects.filter().order_by('-id')[:1]
            l_Notice=Notice.objects.filter().order_by('-id')[:1]
            l_Member=Member.objects.filter().order_by('-id')[:3]   
            context={
                'uid':uid,'cid':cid,'notice_count':notice_count,
                'member_count':member_count, 'event_count':event_count,
                'l_event':l_event, 'l_Notice':l_Notice, 'l_Member':l_Member,
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
        if uid.password==u_password:  
            if uid.role=='chairman':
                request.session['c_email']=uid.email    
                return redirect('index')
            #send_mail("welcome","welcome to digital society","jinaldod12@gmail.com",["jinaldod8151@gmail.com","jinaldod12@gmail.com"])
            # return render(request,'chairman/index.html',{'context':context})
        else:
            print("invalid password")
            e_msg="invalid password"
            return render(request,'chairman/c_login.html',{'e_msg':e_msg})    
    except Exception as e:
        print("Email does not exist")
        e_msg="Email does not exist"
        return render(request,'chairman/c_login.html',{'e_msg':e_msg})

def loginpage(request):
    try:
        email=request.POST['email']
        password=request.POST['password']
        role=request.POST['role'] 
        try: 
            uid=User.objects.get(email=email)
            if role=="chairman":       
                if uid.password == password:  
                    cid=Chairman.objects.get(user_id=uid)
                    request.session['c_email']=uid.email    
                    return redirect('index')
                else:
                    e_msg="Invalid password.Plz try againe"
                    return render(request,"chairman/login.html",{'e_msg':e_msg}) 

            elif role=="member":
                if uid.password == password:
                    cid=Member.objects.get(user_id=uid)
                    request.session['m_email']=uid.email
                    return redirect('m_index')
                else:
                    e_msg="Invalid password"
                    return render(request,"chairman/login.html",{'e_msg':e_msg})  
            else:
                e_msg="Select a valid role"           
                return render(request,"chairman/login.html",{'e_msg':e_msg}) 
        except:
            uid=Watchman.objects.get(email=email)
            if uid.role==role:
                if uid.password == password:   
                    request.session['w_email']=uid.email           
                    return redirect('w_index')
                else:
                    print("Invalid password")
                    e_msg="Invalid password"
                    return render(request,"chairman/login.html",{'e_msg':e_msg})     
            else:
                e_msg="Select a valid role"           
                return render(request,"chairman/login.html",{'e_msg':e_msg})
    except:
        return render(request,"chairman/login.html")

def logout(request):
    if 'c_email' in request.session:
        del request.session['c_email']
        return render(request,'chairman/login.html')
    else:
        return render(request,'chairman/login.html')

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
                return render(request,'chairman/reset_password.html',{'email':email})
                
            elif uid.role=='member':
                cid=Member.objects.get(user_id=uid)
                sendmail(" Forgot Password ","mail_template",email,{'otp':generate_otp,'cid':cid})
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
        
        if uid:
            if str(uid.otp)==otp and newpassword==repassword:
                uid.password=newpassword
                uid.save()  
                s_msg="password reset succesfully"
                return render(request,'chairman/login.html',{'s_msg':s_msg})
            else:
                e_msg="invalid otp or password"
                return render(request,'chairman/reset_password.html',{'e_msg':e_msg})
    except Exception as e:
        e_msg="Email does not exist"
        return render(request,'chairman/forgot_password.html',{'e_msg':e_msg})

def add_contect(request):
    if'c_email' in request.session:
        uid=User.objects.get(email=request.session['c_email'])
        cid=Chairman.objects.get(user_id=uid)
        context={
            'uid':uid,
            'cid':cid,
        }
        return render(request,'chairman/all_contect.html',{'context':context})
    else:
        return render(request,'chairman/c_login.html')

def add_notice(request):
    if'c_email' in request.session:
        uid=User.objects.get(email=request.session['c_email'])
        cid=Chairman.objects.get(user_id=uid)  
        if request.POST:
            title=request.POST['title']
            desc=request.POST['desc']
            nid=Notice.objects.create(title=title,description=desc)
            return redirect('view-notice')
        else:
            context={
                'uid':uid,
                'cid':cid,
            }
            return render(request,'chairman/add_notice.html',{'context':context})
    else:
        return render(request,'chairman/c_login.html')

def view_notice(request):
    if'c_email' in request.session:
        uid=User.objects.get(email=request.session['c_email'])
        cid=Chairman.objects.get(user_id=uid)
        noticedata=Notice.objects.all().order_by('-id')
        context={
                'uid':uid,
                'cid':cid,
                'noticedata':noticedata,
            }
        return render(request,'chairman/notice_list.html',{'context':context})
    else:
        return render(request,'chairman/c_login.html')

def delete_notice(request,pk):
    if'c_email' in request.session:
        uid=User.objects.get(email=request.session['c_email'])
        cid=Chairman.objects.get(user_id=uid)
        nid=Notice.objects.get(id=pk)
        noticedata=Notice.objects.all().order_by('-id')
        nid.delete()
        context={
            'uid':uid,
            'cid':cid,
            'noticedata':noticedata,
            'nid':nid,
        }
        return render(request,'chairman/notice_list.html',{'context':context})
    else:
        return render(request,'chairman/c_login.html')
        
def profile(request):
    if'c_email' in request.session:
        uid=User.objects.get(email=request.session['c_email'])
        cid=Chairman.objects.get(user_id=uid)
        context={
                'uid':uid,
                'cid':cid,
            }
        return render(request,'chairman/profile.html',{'context':context})
    else:
        return render(request,'chairman/c_login.html')

def profile_update(request):
    if'c_email' in request.session:
        uid=User.objects.get(email=request.session['c_email'])
        cid=Chairman.objects.get(user_id=uid)

        c_fname=request.POST['c_fname']
        c_lname=request.POST['c_lname']
        c_address=request.POST['c_address']
        c_contact_no=request.POST['c_contact_no']
        c_homeno=request.POST['c_homeno']
        c_jobProfession=request.POST['c_jobProfession']
        c_job_address=request.POST['c_job_address']
        c_vehicle_type=request.POST['c_vehicle_type']
        c_vehicle_no=request.POST['c_vehicle_no']
        c_blood_group=request.POST['c_blood_group']
        c_family_member=request.POST['c_family_member']
        c_newpassword=request.POST['c_newpassword']

        if "c_profilePic" in request.FILES:
            c_profilePic=request.FILES['c_profilePic']
            cid.profile_pic=c_profilePic
            cid.save()
        
        if c_newpassword:
            uid.password=c_newpassword
            uid.save()

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
        
        cid.save()
        mid.save()

        context={
                'uid':uid,
                'cid':cid,
                'mid':mid,    
            }
        return render(request,'chairman/profile.html',{'context':context})
    else:
        return render(request,'chairman/c_login.html')
        
def add_events(request):
    if'c_email' in request.session:
        uid=User.objects.get(email=request.session['c_email'])
        cid=Chairman.objects.get(user_id=uid)
        if request.POST:
            title=request.POST['title']
            desc=request.POST['desc']
            eid=Events.objects.create(title=title,description=desc)
            if "eventpic" in request.FILES:
                eventpic=request.FILES['eventpic']
                eid.event_pic=eventpic
                eid.save()
            return redirect('view-events')
        else:
            context={
                'uid':uid,
                'cid':cid,
             }
            return render(request,'chairman/add_events.html',{'context':context})
    else:
        return render(request,'chairman/c_login.html')

def view_events(request):
    if'c_email' in request.session:
        uid=User.objects.get(email=request.session['c_email'])
        cid=Chairman.objects.get(user_id=uid)
        eventdata=Events.objects.all().order_by('-id')
        context={
                'uid':uid,
                'cid':cid,
                'eventdata':eventdata,
            }
        return render(request,'chairman/view_events.html',{'context':context})
    else:
        return render(request,'chairman/c_login.html')

def delete_event(request,pk):
    if'c_email' in request.session:
        uid=User.objects.get(email=request.session['c_email'])
        cid=Chairman.objects.get(user_id=uid)
        eid=Events.objects.get(id=pk)
        eventdata=Events.objects.all().order_by('-id')
        eid.delete()
        context={
            'uid':uid,
            'cid':cid,
            'eventdata':eventdata,
            'eid':eid,
        }
        return render(request,'chairman/view_events.html',{'context':context})
    else:
        return render(request,'chairman/c_login.html')

def view_complain(request):
    if "c_email" in request.session:
        uid=User.objects.get(email=request.session['c_email'])
        cid=Chairman.objects.get(user_id=uid)
        complaindata=complain.objects.all().order_by('-id')
        print("------",complaindata)
        context={
                'uid':uid,
                'cid':cid,
                'complaindata':complaindata,
            }
        return render(request,'chairman/view_complain.html',{'context':context}) 
    else:
        return render(request,'chairman/c_login.html') 

def view_suggestion(request):
    if "c_email" in request.session:
        uid=User.objects.get(email=request.session['c_email'])
        cid=Chairman.objects.get(user_id=uid)
        suggestiondata=Suggestion.objects.all().order_by('-id')
        print("------",suggestiondata)
        context={
                'uid':uid,
                'cid':cid,
                'suggestiondata':suggestiondata,
            }
        return render(request,'chairman/view_suggestion.html',{'context':context})
    else:
        return render(request,'chairman/c_login.html')  

def add_photos(request):
    if'c_email' in request.session:
        uid=User.objects.get(email=request.session['c_email'])
        cid=Chairman.objects.get(user_id=uid)
        if request.POST:
            title=request.POST['title']
            Photofile=request.FILES['Photofile']
            eid=Photos.objects.create(title=title,photofile=Photofile)
            return redirect('view-photos')   
        else:
            context={
            'uid':uid,
            'cid':cid,
            }
            return render(request,'chairman/add_photos.html',{'context':context})
    else:
        return render(request,'chairman/c_login.html')

def view_photos(request):
    if'c_email' in request.session:
        uid=User.objects.get(email=request.session['c_email'])
        cid=Chairman.objects.get(user_id=uid)
        photodata=Photos.objects.all().order_by('-id')
        context={
                'uid':uid,
                'cid':cid,
                'photodata':photodata,
            }
        return render(request,'chairman/view_photos.html',{'context':context})
    else:
        return render(request,'chairman/c_login.html')

def delete_photo(request,pk):
    if'c_email' in request.session:
        uid=User.objects.get(email=request.session['c_email'])
        cid=Chairman.objects.get(user_id=uid)
        pid=Photos.objects.get(id=pk)
        pid.delete()
        photodata=Photos.objects.all().order_by('-id')
        context={
            'uid':uid,
            'cid':cid,
            'photodata':photodata,
        }
        return render(request,'chairman/view_photos.html',{'context':context})
    else:
        return render(request,'chairman/c_login.html')

def add_videos(request):
    if'c_email' in request.session:
        uid=User.objects.get(email=request.session['c_email'])
        cid=Chairman.objects.get(user_id=uid)
        if request.POST:
            title=request.POST['title']
            videofile=request.FILES['videofile']
            eid=Videos.objects.create(title=title,videofile=videofile)
            return redirect('view-videos')
        else:
            context={
            'uid':uid,
            'cid':cid,
            }
            return render(request,'chairman/add_videos.html',{'context':context})
    else:
        return render(request,'chairman/c_login.html')

def view_videos(request):
    if'c_email' in request.session:
        uid=User.objects.get(email=request.session['c_email'])
        cid=Chairman.objects.get(user_id=uid)
        videodata=Videos.objects.all().order_by('-id')
        context={
                'uid':uid,
                'cid':cid,
                'videodata':videodata,
            }
        return render(request,'chairman/view_videos.html',{'context':context})
    else:
        return render(request,'chairman/c_login.html')

def delete_videos(request,pk):
    if'c_email' in request.session:
        uid=User.objects.get(email=request.session['c_email'])
        cid=Chairman.objects.get(user_id=uid)
        vid=Videos.objects.get(id=pk)
        vid.delete()
        videodata=Videos.objects.all().order_by('-id')
        context={
            'uid':uid,
            'cid':cid,
            'videodata':videodata,  
        }
        return render(request,'chairman/view_videos.html',{'context':context})
    else:
        return render(request,'chairman/c_login.html')

def add_member(request):
    if'c_email' in request.session:
        uid=User.objects.get(email=request.session['c_email'])
        cid=Chairman.objects.get(user_id=uid)
        if request.POST:
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
        
            g_password=f_name[:3]+str(randint(111,999))            
            user_id=User.objects.create(email=email,password=g_password,role=role)

            member_detail_id=MemberDetails.objects.create(contact_no=contact_no,homeno=homeno,address=address,job_profession=job_profession,
                                                        job_address=job_address,vehicle_type=vehicle_type,vehicle_no=vehicle_no,
                                                        blood_group=blood_group,family_member_details=family_member,member_role=role,)
    
            try:
                m_profilepic=request.FILES['m_profilepic']
                member_detail=Member.objects.create(fname=f_name,lname=l_name,user_id=user_id,m_id=member_detail_id,profile_pic=m_profilepic)
            except:
                member_detail=Member.objects.create(fname=f_name,lname=l_name,user_id=user_id,m_id=member_detail_id)
            
            mid=Member.objects.all().order_by('-id')
            context={
                        'uid':uid,
                        'cid':cid,
                        'f_name':f_name,
                        'mid':mid,
                        'l_name':l_name
                    }
            
            sendPasswordMail('Password for login','email_password',email,{'f_name':f_name,'l_name':l_name,'password':g_password})
            return render(request,'chairman/view_member.html',{'context':context})
        else:
            context={
            'uid':uid,
            'cid':cid,
            }
            return render(request,'chairman/add_member.html',{'context':context})

    else:
        return render(request,'chairman/c_login.html')

def view_member_profile(request,pk):    #primary key accepted
    if 'c_email' in request.session:
        uid=User.objects.get(email=request.session['c_email'])
        cid=Chairman.objects.get(user_id=uid)
        mid=Member.objects.get(id=pk)      #get pk to id
        context={
            'uid':uid,
            'cid':cid,
            'mid':mid,
        }
        return render(request,'chairman/view_member_profile.html',{'context':context})
    else:
        return render(request,'chairman/c_login.html')    

def view_member(request):
    if 'c_email' in request.session:
        uid=User.objects.get(email=request.session['c_email'])
        cid=Chairman.objects.get(user_id=uid)
        mid=Member.objects.all().order_by('-id')
        context={
            'uid':uid,
            'cid':cid,
            'mid':mid,   
        }
        return render(request,'chairman/view_member.html',{'context':context})
    else:
        return render(request,'chairman/c_login.html') 

def member_profile_update_page(request,pk):
    uid=User.objects.get(email=request.session['c_email'])
    cid=Chairman.objects.get(user_id=uid)
    mb_id=Member.objects.get(id=pk) 
    memberdata=Member.objects.all() 
        #get pk to id
    context={
        'uid':uid,
        'cid':cid,
        'mb_id':mb_id,
        'memberdata':memberdata,
    }
    return render(request,'chairman/member_update_profile.html',{'context':context})

def member_profile_update(request,pk):
   
    if "c_email" in request.session:
        uid=User.objects.get(email=request.session['c_email'])
        mb_id=Member.objects.get(id=pk)
        cid=Chairman.objects.get(user_id=uid)

        m_fname=request.POST['m_fname']
        m_lname=request.POST['m_lname']
        m_house_no=request.POST['m_house_no']
        m_contect_no=request.POST['m_contect_no']
        m_address=request.POST['m_address']
        m_job_profession=request.POST['m_job_profession']
        m_job_address=request.POST['m_job_address']
        m_vehicle_type=request.POST['m_vehicle_type']
        m_vehicle_no=request.POST['m_vehicle_no']
        m_blood_group=request.POST['m_blood_group']
        m_family_member=request.POST['m_family_member']
        m_newpassword=request.POST['m_newpassword']
        mid=MemberDetails.objects.get(homeno=m_house_no)
        
        mb_id.fname=m_fname
        mb_id.lname=m_lname

        mid.job_profession=m_job_profession
        mid.family_member_details=m_family_member
        mid.contact_no=m_contect_no
        mid.address=m_address
        mid.job_address=m_job_address
        mid.blood_group=m_blood_group
        mid.vehicle_type=m_vehicle_type
        mid.vehicle_no=m_vehicle_no

        if m_newpassword:
            uid.password=m_newpassword
            uid.save()
        if "profilepic" in request.FILES:
            profilepic=request.FILES['profilepic']
            mb_id.profile_pic=profilepic
            mb_id.save()

        mb_id.save()
        mid.save()
       
        context={
                'uid':uid,
                'cid':cid,
                'mb_id':mb_id,
                'mid':mid,
            }
        return render(request,'chairman/member_update_profile.html',{'context':context})
    else:
        return render(request,'chairman/c_login.html')
       
def delete_member(request):

    if 'c_email' in request.session:
        id=request.POST['id']
        mid=Member.objects.get(id=id)
        mid.delete()
        mid.user_id.delete()
        mid.m_id.delete()
        mid_all=list(Member.objects.values())
        context={  
            'mid_all':mid_all,
        }
        return JsonResponse({"context":context})
    else:
        return render(request,'chairman/c_login.html')  


def watchman_list(request):
    if "c_email" in request.session:
        uid=User.objects.get(email=request.session['c_email'])
        cid=Chairman.objects.get(user_id=uid)
        wid=Watchman.objects.all().order_by('-id')
        context={
                'uid':uid,
                'cid':cid,
                'wid':wid,   
            }
        return render(request,'chairman/watchman_list.html',{'context':context})
    else:
        return render(request,'chairman/c_login.html')

def ver_watch(request,pk):
    if "c_email" in request.session:
        uid=User.objects.get(email=request.session['c_email'])
        cid=Chairman.objects.get(user_id=uid)
        wid=Watchman.objects.get(id=pk)
       
        if wid.is_verified == False:
            wid.is_verified = True
            wid.save()
        elif wid.is_verified == True:    
            wid.is_verified = False
            wid.save()
        wid=Watchman.objects.all().order_by('-id')
        context={
                'uid':uid,
                'cid':cid,
                'wid':wid,   
            }
        return render(request,'chairman/watchman_list.html',{'context':context})
    else:
        return render(request,'chairman/c_login.html')

def view_visitors(request):
    if "c_email" in request.session:
        uid=User.objects.get(email=request.session['c_email']) 
        cid=Chairman.objects.get(user_id=uid)           
        vid=Visitors.objects.all().order_by('-id')
        context={
            "uid":uid,
            "cid":cid,
            "vid":vid,
        }
        return render(request,"chairman/view_visitors.html",{"context":context})
    else:
        return render(request,"chairman/c_login.html")

def add_maintenance(request):
    if request.POST:
        title=request.POST['title']
        amount=request.POST['amount']
        due_date=request.POST['due_date']
        uid=User.objects.get(email=request.session['c_email'])         
        cid=Chairman.objects.get(user_id=uid)
        # add maintenance of chairman
        Maintenance.objects.create(user_id=uid,cid=cid,title=title,amount=amount,due_date=due_date)
        # members 
        allmembers = Member.objects.all()
        for i in allmembers:
            mid  = Member.objects.get(id = i.id)
            Maintenance.objects.create(user_id=uid,member_id=mid,title=title,amount=amount,due_date=due_date)

        maintenance_data=Maintenance.objects.all()
        context={
            "uid":uid,
            "cid":cid,
            "maintenance_data":maintenance_data,
        }
        return render(request,"chairman/view_maintenance.html",{"context":context})
    else:
        uid=User.objects.get(email=request.session['c_email'])         
        cid=Chairman.objects.get(user_id=uid)
        context={
            "uid":uid,
            "cid":cid,
        } 
        return render(request,"chairman/add_maintenance.html",{"context":context})

def view_maintenance(request):
    uid=User.objects.get(email=request.session['c_email'])         
    cid=Chairman.objects.get(user_id=uid)
    maintenance_data=Maintenance.objects.filter(cid=cid.id)
    context={
        "uid":uid,
        "cid":cid,
        "maintenance_data":maintenance_data,
    }
    return render(request,"chairman/view_maintenance.html",{"context":context})

def initiate_payment(request,pk):
    try:        
        mid = Maintenance.objects.get(id = pk)
        amount = mid.amount

        if "c_email" in request.session:
            uid = User.objects.get(email = request.session['c_email'])
            transaction = Transaction.objects.create(made_by=uid, amount=amount, main_id=mid)
            transaction.save()

        elif "m_email" in request.session:
            mem_id=User.objects.get(email=request.session['m_email'])
            member_id=Member.objects.get(user_id=mem_id)
            transaction = Transaction.objects.create(made_by=mem_id, amount=amount, main_id=mid,member_id=member_id)
            transaction.save()
        
    except Exception as e:
        print("======>>>> Exception ",e)
        return render(request, 'chairman/pay.html', context={'error': 'Wrong Accound Details or amount'})
    
    merchant_key = settings.PAYTM_SECRET_KEY

    params = (
        ('MID', settings.PAYTM_MERCHANT_ID),
        ('ORDER_ID', str(transaction.order_id)),
        ('CUST_ID', str(transaction.made_by.email)),
        ('TXN_AMOUNT', str(transaction.amount)),
        ('CHANNEL_ID', settings.PAYTM_CHANNEL_ID),
        ('WEBSITE', settings.PAYTM_WEBSITE),
        # ('EMAIL', request.user.email),
        # ('MOBILE_N0', '9911223388'),
        ('INDUSTRY_TYPE_ID', settings.PAYTM_INDUSTRY_TYPE_ID),
        ('CALLBACK_URL', 'http://127.0.0.1:8000/callback/'),
        # ('PAYMENT_MODE_ONLY', 'NO'),
    )

    paytm_params = dict(params)
    checksum = generate_checksum(paytm_params, merchant_key)

    transaction.checksum = checksum
    transaction.save()

    paytm_params['CHECKSUMHASH'] = checksum
    print('SENT: ', checksum)
    return render(request, 'chairman/redirect.html', context=paytm_params)

@csrf_exempt
def callback(request):
    if request.method == 'POST':
        received_data = dict(request.POST)
        paytm_params = {}
        paytm_checksum = received_data['CHECKSUMHASH'][0]
        for key, value in received_data.items():
            if key == 'CHECKSUMHASH':
                paytm_checksum = value[0]
            else:
                paytm_params[key] = str(value[0])
        # Verify checksum
        is_valid_checksum = verify_checksum(paytm_params, settings.PAYTM_SECRET_KEY, str(paytm_checksum))
  
        if ['TXN_SUCCESS'] in received_data.values():
            orderid = received_data['ORDERID']
            print("--->>> type of orderid ",type(orderid))
            s = str(orderid)
            n= s[2:]
            final = n[:-2]
            tid = Transaction.objects.get(order_id=final)

            try:
                memberid = tid.member_id.id
                if memberid:
                    member_id = Member.objects.get(id = memberid)
                    mid = Maintenance.objects.get(id = tid.main_id.id)
                    mid.status="PAID"
                    mid.save()
                    tid.status = "PAID"
                    tid.save()
            except:
                orderid = received_data['ORDERID']
                s = str(orderid)
                n= s[2:]
                final = n[:-2]
                tid = Transaction.objects.get(order_id=final)
                chairman_id = tid.main_id.cid
                mid = Maintenance.objects.get(id = tid.main_id.id)
                mid.status="PAID"
                mid.save()
                tid.status = "PAID"
                tid.save()
        else:
            orderid = received_data['ORDERID']
            s = str(orderid)
            n= s[2:]
            final = n[:-2]
            tid = Transaction.objects.get(order_id=final)
            mid = Maintenance.objects.get(id = tid.main_id.id)
            mid.status="Pending"
            mid.save()

        if is_valid_checksum:
            received_data['message'] = "Checksum Matched"
        else:
            received_data['message'] = "Checksum Mismatched"
            return render(request, 'chairman/callback.html', context=received_data)
        
        return render(request, 'chairman/callback.html', context=received_data)

def maintenance_list(request):
    uid=User.objects.get(email=request.session['c_email'])         
    cid=Chairman.objects.get(user_id=uid)
    maintenance_data=Maintenance.objects.all()
    member_id=Member.objects.all()
    context={
        "uid":uid,
        "cid":cid,
        "maintenance_data":maintenance_data,
        "member_id":member_id,
    }
    return render(request,"chairman/maintenance_list.html",{"context":context})

def check_email(request):
    role = request.POST['role']
    email= request.POST['email']
    uid=User.objects.filter(email=email)
    if uid:
        if uid[0].role == role :
            msg=""
        else:
            msg=  "email does not exist "    
    else:
        msg=  "email does not exist "

    context={
        "msg":msg, 
    }
    return JsonResponse({"context":context})
