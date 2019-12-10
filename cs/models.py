from django.db import models
from datetime import datetime


class User(models.Model):
    UID = models.BigAutoField(primary_key=True)
    First_Name = models.CharField(max_length=20, null=False)
    Middle_Name = models.CharField(max_length=20)
    Last_Name = models.CharField(max_length=20, null=False)
    Email = models.EmailField(null=False)
    Phone_Number = models.CharField(max_length=10, null=False)
    Type = models.CharField(max_length=10, null=False, default='Developer')
    Password = models.CharField(max_length=100, null=False)


class Team(models.Model):
    TID = models.CharField(max_length=10, null=False)
    DID = models.ForeignKey(User, on_delete=models.CASCADE, null=False)
    Postion = models.CharField(max_length=50)

    class Meta:
        unique_together = (("TID", "DID"),)


class Project(models.Model):
    PID = models.BigAutoField(primary_key=True)
    Title = models.CharField(max_length=1000, null=False)
    TID = models.ForeignKey(Team, on_delete=models.NullBooleanField)
    Client = models.ForeignKey(User, on_delete=models.CASCADE)


class Project_Status(models.Model):
    PS_ID = models.BigAutoField(primary_key=True)
    PID = models.ForeignKey(Project, on_delete=models.CASCADE)
    Status = models.TextField(null=False)
    Date_Time = models.DateTimeField(default=datetime.utcnow())
    Completed_Precentage = models.FloatField(default=0.0)
    Remaining_Precentage = models.FloatField(default=100.0)


class Complaints(models.Model):
    CID = models.BigAutoField(primary_key=True)
    UID = models.ForeignKey(User, on_delete=models.CASCADE)
    Complaint = models.TextField(null=False)
    Date_Time = models.DateTimeField(default=datetime.utcnow())
    Action_Taken = models.TextField(default=None)


'''class Message(models.Model):
    MID=models.BigAutoField(primary_key=True)
    Sender=models.ForeignKey(User, on_delete=models.CASCADE)
    Receiver=models.ForeignKey(User)
    Date_Time=models.DateTimeField(default=datetime.utcnow())'''
