from django.db import models

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
    profile_pic=models.FileField(upload_to="img/",blank=True,default="default.jpg")  

    def __str__(self):
        return self.fname

class Member(models.Model):
    user_id =  models.ForeignKey(User,on_delete=models.CASCADE)
    m_id = models.ForeignKey(MemberDetails,on_delete=models.CASCADE)
    fname = models.CharField(max_length = 20)
    lname = models.CharField(max_length = 20)
    profile_pic=models.FileField(upload_to="img/",blank=True) 

    def __str__(self):
        return self.fname 

class Notice(models.Model):
    title = models.CharField(max_length = 20)
    description = models.CharField(max_length = 200)
    created_at = models.DateTimeField(auto_now_add = True, blank = False)
    updated_at = models.DateTimeField(auto_now_add = True, blank = False)

    def __str__(self):
        return self.title
class Events(models.Model):
    title = models.CharField(max_length = 20)
    description = models.CharField(max_length = 200)
    event_pic=models.FileField(upload_to="img/",blank=True) 
    created_at = models.DateTimeField(auto_now_add = True, blank = False)
    updated_at = models.DateTimeField(auto_now_add = True, blank = False)

    def __str__(self):
        return self.title

class Watchman(models.Model):
    
    fname = models.CharField(max_length = 20)
    lname = models.CharField(max_length = 20)
    contactno = models.CharField(max_length = 20)
    email = models.EmailField(max_length = 20)
    password = models.CharField(max_length = 20)
    address = models.CharField(max_length = 200)
    family_contact = models.CharField(max_length = 20)
    age = models.CharField(max_length = 20)
    blood_group = models.CharField(max_length = 20)
    role = models.CharField(max_length = 20)
    is_verified = models.BooleanField(default = False)    

    def __str__(self):
        return self.email 
