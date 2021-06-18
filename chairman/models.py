from django.db import models
import math
from django.utils import timezone

# Create your models here.
class User(models.Model):
    email = models.EmailField(unique=True)
    password = models.CharField(max_length = 20)
    otp = models.IntegerField(default = 459)
    is_active = models.BooleanField(default = True)
    is_verified = models.BooleanField(default = False)
    role = models.CharField(max_length = 10)
    created_at = models.DateTimeField(auto_now_add = True, blank = False)
    updated_at = models.DateTimeField(auto_now_add = True, blank = False)

    def __str__(self):
        return self.email

class MemberDetails(models.Model):
    member_role = models.CharField(max_length = 20)
    homeno = models.CharField(max_length = 20)
    address = models.CharField(max_length = 100)
    job_profession = models.CharField(max_length = 50, blank=True)
    job_address = models.CharField(max_length = 50, blank=True)
    vehicle_type = models.CharField(max_length = 20, blank=True)
    vehicle_no = models.CharField(max_length = 30, blank=True)
    blood_group = models.CharField(max_length = 30, blank=True)
    family_member_details = models.CharField(max_length = 20)
    contact_no = models.CharField(max_length = 30) 

    def __str__(self):
        return self.homeno

class Chairman(models.Model):
    user_id = models.ForeignKey(User,on_delete=models.CASCADE)
    m_id = models.ForeignKey(MemberDetails,on_delete=models.CASCADE)
    fname = models.CharField(max_length = 20)
    lname = models.CharField(max_length = 20)
    contactno = models.CharField(max_length = 20)
    profile_pic=models.FileField(upload_to="img/",blank=True,default="avtar.png")  

    def __str__(self):
        return self.fname

class Member(models.Model):
    user_id =  models.ForeignKey(User,on_delete=models.CASCADE)
    m_id = models.ForeignKey(MemberDetails,on_delete=models.CASCADE)
    fname = models.CharField(max_length = 20)
    lname = models.CharField(max_length = 20)
    profile_pic=models.FileField(upload_to="img/",blank=True,default="avtar.png") 

    def __str__(self):
        return self.fname 

class Notice(models.Model):
    title = models.CharField(max_length = 20)
    description = models.CharField(max_length = 200)
    created_at = models.DateTimeField(auto_now_add = True, blank = False)
    updated_at = models.DateTimeField(auto_now_add = True, blank = False)

    def __str__(self):
        return self.title

    def whenPublished(self):
        now = timezone.now()
        diff= now - self.created_at
        if diff.days == 0 and diff.seconds >= 0 and diff.seconds < 60:
            seconds= diff.seconds
            if seconds == 1 or seconds == 0:
                return str(seconds) +  "second ago"
            else:
                return str(seconds) + " seconds ago"

        if diff.days == 0 and diff.seconds >= 60 and diff.seconds < 3600:
            minutes= math.floor(diff.seconds/60)
            if minutes == 1:
                return str(minutes) + " minute ago"
            else:
                return str(minutes) + " minutes ago"

        if diff.days == 0 and diff.seconds >= 3600 and diff.seconds < 86400:
            hours= math.floor(diff.seconds/3600)
            if hours == 1:
                return str(hours) + " hour ago"
            else:
                return str(hours) + " hours ago"

        # 1 day to 30 days
        if diff.days >= 1 and diff.days < 30:
            days= diff.days
            if days == 1:
                return str(days) + " day ago"
            else:
                return str(days) + " days ago"

        if diff.days >= 30 and diff.days < 365:
            months= math.floor(diff.days/30)
            if months == 1:
                return str(months) + " month ago"
            else:
                return str(months) + " months ago"

        if diff.days >= 365:
            years= math.floor(diff.days/365)
            if years == 1:
                return str(years) + " year ago"
            else:
                return str(years) + " years ago"
   
class Events(models.Model):
    title = models.CharField(max_length = 20)
    description = models.CharField(max_length = 200)
    event_pic=models.FileField(upload_to="img/",blank=True,default="avtar.png") 
    created_at = models.DateTimeField(auto_now_add = True, blank = False)
    updated_at = models.DateTimeField(auto_now_add = True, blank = False)

    def __str__(self):
        return self.title

    def whenPublished(self):
        now = timezone.now()
        diff= now - self.created_at
        if diff.days == 0 and diff.seconds >= 0 and diff.seconds < 60:
            seconds= diff.seconds
            if seconds == 1 or seconds == 0:
                return str(seconds) +  "second ago"
            else:
                return str(seconds) + " seconds ago"

        if diff.days == 0 and diff.seconds >= 60 and diff.seconds < 3600:
            minutes= math.floor(diff.seconds/60)
            if minutes == 1:
                return str(minutes) + " minute ago"
            else:
                return str(minutes) + " minutes ago"

        if diff.days == 0 and diff.seconds >= 3600 and diff.seconds < 86400:
            hours= math.floor(diff.seconds/3600)
            if hours == 1:
                return str(hours) + " hour ago"
            else:
                return str(hours) + " hours ago"

        # 1 day to 30 days
        if diff.days >= 1 and diff.days < 30:
            days= diff.days
            if days == 1:
                return str(days) + " day ago"
            else:
                return str(days) + " days ago"

        if diff.days >= 30 and diff.days < 365:
            months= math.floor(diff.days/30)
            if months == 1:
                return str(months) + " month ago"
            else:
                return str(months) + " months ago"

        if diff.days >= 365:
            years= math.floor(diff.days/365)
            if years == 1:
                return str(years) + " year ago"
            else:
                return str(years) + " years ago"
    
class Watchman(models.Model):
    
    fname = models.CharField(max_length = 20)
    lname = models.CharField(max_length = 20)
    contactno = models.CharField(max_length = 20)
    email = models.EmailField(max_length = 35)
    password = models.CharField(max_length = 20)
    address = models.CharField(max_length = 200, blank=True)
    family_contact = models.CharField(max_length = 20, blank=True)
    age = models.CharField(max_length = 20, blank=True)
    blood_group = models.CharField(max_length = 20,blank=True)
    role = models.CharField(max_length = 20)
    is_verified = models.BooleanField(default = False)
    profile_pic=models.FileField(upload_to="img/",blank=True,default="avtar.png")   


    def __str__(self):
        return self.email 

class complain(models.Model):
    title = models.CharField(max_length = 20)
    description = models.CharField(max_length = 200)
    created_at = models.DateTimeField(auto_now_add = True, blank = False)
    updated_at = models.DateTimeField(auto_now_add = True, blank = False)

    def __str__(self):
        return self.title

    def whenPublished(self):
        now = timezone.now()
        diff= now - self.created_at
        if diff.days == 0 and diff.seconds >= 0 and diff.seconds < 60:
            seconds= diff.seconds
            if seconds == 1 or seconds == 0:
                return str(seconds) +  "second ago"
            else:
                return str(seconds) + " seconds ago"

        if diff.days == 0 and diff.seconds >= 60 and diff.seconds < 3600:
            minutes= math.floor(diff.seconds/60)
            if minutes == 1:
                return str(minutes) + " minute ago"
            else:
                return str(minutes) + " minutes ago"

        if diff.days == 0 and diff.seconds >= 3600 and diff.seconds < 86400:
            hours= math.floor(diff.seconds/3600)
            if hours == 1:
                return str(hours) + " hour ago"
            else:
                return str(hours) + " hours ago"

        # 1 day to 30 days
        if diff.days >= 1 and diff.days < 30:
            days= diff.days
            if days == 1:
                return str(days) + " day ago"
            else:
                return str(days) + " days ago"

        if diff.days >= 30 and diff.days < 365:
            months= math.floor(diff.days/30)
            if months == 1:
                return str(months) + " month ago"
            else:
                return str(months) + " months ago"

        if diff.days >= 365:
            years= math.floor(diff.days/365)
            if years == 1:
                return str(years) + " year ago"
            else:
                return str(years) + " years ago"
    
class Suggestion(models.Model):
    title = models.CharField(max_length = 20)
    description = models.CharField(max_length = 200)
    created_at = models.DateTimeField(auto_now_add = True, blank = False)
    updated_at = models.DateTimeField(auto_now_add = True, blank = False)

    def __str__(self):
        return self.title

    def whenPublished(self):
        now = timezone.now()
        diff= now - self.created_at
        if diff.days == 0 and diff.seconds >= 0 and diff.seconds < 60:
            seconds= diff.seconds
            if seconds == 1 or seconds == 0:
                return str(seconds) +  "second ago"
            else:
                return str(seconds) + " seconds ago"

        if diff.days == 0 and diff.seconds >= 60 and diff.seconds < 3600:
            minutes= math.floor(diff.seconds/60)
            if minutes == 1:
                return str(minutes) + " minute ago"
            else:
                return str(minutes) + " minutes ago"

        if diff.days == 0 and diff.seconds >= 3600 and diff.seconds < 86400:
            hours= math.floor(diff.seconds/3600)
            if hours == 1:
                return str(hours) + " hour ago"
            else:
                return str(hours) + " hours ago"

        # 1 day to 30 days
        if diff.days >= 1 and diff.days < 30:
            days= diff.days
            if days == 1:
                return str(days) + " day ago"
            else:
                return str(days) + " days ago"

        if diff.days >= 30 and diff.days < 365:
            months= math.floor(diff.days/30)
            if months == 1:
                return str(months) + " month ago"
            else:
                return str(months) + " months ago"

        if diff.days >= 365:
            years= math.floor(diff.days/365)
            if years == 1:
                return str(years) + " year ago"
            else:
                return str(years) + " years ago"
    
class Photos(models.Model):
    title = models.CharField(max_length = 20)
    photofile=models.FileField(upload_to="img/",blank=True)
    created_at = models.DateTimeField(auto_now_add = True, blank = False)
    updated_at = models.DateTimeField(auto_now_add = True, blank = False)

    def __str__(self):
        return self.created_at

    def whenPublished(self):
        now = timezone.now()
        diff= now - self.created_at
        if diff.days == 0 and diff.seconds >= 0 and diff.seconds < 60:
            seconds= diff.seconds
            if seconds == 1 or seconds == 0:
                return str(seconds) +  "second ago"
            else:
                return str(seconds) + " seconds ago"

        if diff.days == 0 and diff.seconds >= 60 and diff.seconds < 3600:
            minutes= math.floor(diff.seconds/60)
            if minutes == 1:
                return str(minutes) + " minute ago"
            else:
                return str(minutes) + " minutes ago"

        if diff.days == 0 and diff.seconds >= 3600 and diff.seconds < 86400:
            hours= math.floor(diff.seconds/3600)
            if hours == 1:
                return str(hours) + " hour ago"
            else:
                return str(hours) + " hours ago"

        # 1 day to 30 days
        if diff.days >= 1 and diff.days < 30:
            days= diff.days
            if days == 1:
                return str(days) + " day ago"
            else:
                return str(days) + " days ago"

        if diff.days >= 30 and diff.days < 365:
            months= math.floor(diff.days/30)
            if months == 1:
                return str(months) + " month ago"
            else:
                return str(months) + " months ago"

        if diff.days >= 365:
            years= math.floor(diff.days/365)
            if years == 1:
                return str(years) + " year ago"
            else:
                return str(years) + " years ago"   

class Videos(models.Model):
    title = models.CharField(max_length = 20)
    videofile=models.FileField(upload_to="video/",blank=True) 
    created_at = models.DateTimeField(auto_now_add = True, blank = False)
    updated_at = models.DateTimeField(auto_now_add = True, blank = False)

    def __str__(self):
        return self.title

    def whenPublished(self):
        now = timezone.now()
        diff= now - self.created_at
        if diff.days == 0 and diff.seconds >= 0 and diff.seconds < 60:
            seconds= diff.seconds
            if seconds == 1 or seconds == 0:
                return str(seconds) +  "second ago"
            else:
                return str(seconds) + " seconds ago"

        if diff.days == 0 and diff.seconds >= 60 and diff.seconds < 3600:
            minutes= math.floor(diff.seconds/60)
            if minutes == 1:
                return str(minutes) + " minute ago"
            else:
                return str(minutes) + " minutes ago"

        if diff.days == 0 and diff.seconds >= 3600 and diff.seconds < 86400:
            hours= math.floor(diff.seconds/3600)
            if hours == 1:
                return str(hours) + " hour ago"
            else:
                return str(hours) + " hours ago"

        # 1 day to 30 days
        if diff.days >= 1 and diff.days < 30:
            days= diff.days
            if days == 1:
                return str(days) + " day ago"
            else:
                return str(days) + " days ago"

        if diff.days >= 30 and diff.days < 365:
            months= math.floor(diff.days/30)
            if months == 1:
                return str(months) + " month ago"
            else:
                return str(months) + " months ago"

        if diff.days >= 365:
            years= math.floor(diff.days/365)
            if years == 1:
                return str(years) + " year ago"
            else:
                return str(years) + " years ago"
    
class Visitors(models.Model):
    vm_id = models.ForeignKey(MemberDetails,on_delete=models.CASCADE)
    f_name = models.CharField(max_length = 20)
    l_name = models.CharField(max_length = 20)
    email = models.EmailField(max_length = 35)
    contact_no = models.CharField(max_length = 20)
    house_no = models.CharField(max_length = 20, blank = True)

    def __str__(self):
        return self.f_name

class Maintenance(models.Model):
    user_id = models.ForeignKey(User,on_delete=models.CASCADE,default="",blank=True,null=True)
    member_id = models.ForeignKey(Member,on_delete=models.CASCADE,default="",blank=True,null=True)
    cid = models.ForeignKey(Chairman,on_delete=models.CASCADE,default="",blank=True,null=True)
    title=models.CharField(max_length=100,blank=True)
    amount=models.CharField(max_length=999,blank=True)
    due_date=models.DateTimeField(auto_now_add=True,blank=False)
    created_at = models.DateTimeField(auto_now_add=True,blank=False)
    updated_at = models.DateTimeField(auto_now=True,blank=False)
    status = models.CharField(max_length=20,default="Pending")

    def whenPublished(self):
        now = timezone.now()
        diff= now - self.created_at
        if diff.days == 0 and diff.seconds >= 0 and diff.seconds < 60:
            seconds= diff.seconds
            if seconds == 1 or seconds == 0:
                return str(seconds) +  "second ago"
            else:
                return str(seconds) + " seconds ago"

        if diff.days == 0 and diff.seconds >= 60 and diff.seconds < 3600:
            minutes= math.floor(diff.seconds/60)
            if minutes == 1:
                return str(minutes) + " minute ago"
            else:
                return str(minutes) + " minutes ago"

        if diff.days == 0 and diff.seconds >= 3600 and diff.seconds < 86400:
            hours= math.floor(diff.seconds/3600)
            if hours == 1:
                return str(hours) + " hour ago"
            else:
                return str(hours) + " hours ago"

        # 1 day to 30 days
        if diff.days >= 1 and diff.days < 30:
            days= diff.days
            if days == 1:
                return str(days) + " day ago"
            else:
                return str(days) + " days ago"

        if diff.days >= 30 and diff.days < 365:
            months= math.floor(diff.days/30)
            if months == 1:
                return str(months) + " month ago"
            else:
                return str(months) + " months ago"

        if diff.days >= 365:
            years= math.floor(diff.days/365)
            if years == 1:
                return str(years) + " year ago"
            else:
                return str(years) + " years ago"
       
class Transaction(models.Model):
    main_id = models.ForeignKey(Maintenance, on_delete=models.CASCADE,default="",blank=True,null=True)
    made_by = models.ForeignKey(User, related_name='transactions', on_delete=models.CASCADE)
    member_id = models.ForeignKey(Member,on_delete=models.CASCADE,default="",blank=True,null=True)
    made_on = models.DateTimeField(auto_now_add=True)
    amount = models.IntegerField()  
    order_id = models.CharField(unique=True, max_length=100, null=True, blank=True)
    checksum = models.CharField(max_length=100, null=True, blank=True)
    status = models.CharField(max_length=20,default="Pending")

    def save(self, *args, **kwargs):
        if self.order_id is None and self.made_on and self.id:
            self.order_id = self.made_on.strftime('PAY2ME%Y%m%dODR') + str(self.id)
        return super().save(*args, **kwargs)



