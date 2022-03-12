from linecache import _ModuleGlobals
from django.db import models

# Create your models here.

class User(models.Model):
    fname=models.CharField(max_length=100)
    lname=models.CharField(max_length=100)
    email=models.EmailField(verbose_name="Email" , null=False)

# coach herite de user
class Coach(User):
    def __str__(self) -> str:
        return f"{self.fname}"

    #yaani ma 3ndouch 7ata attribut specifique yaani juste les att ta3 user 
    pass

class Student(User):
    def __str__(self) -> str:
        return f"{self.fname}"
    pass   

class Project(models.Model):
    project_name=models.CharField(verbose_name="Titre du projet", max_length=50)
    project_duration=models.IntegerField(verbose_name="duree estime" , default=0)
    time_allocated=models.IntegerField(verbose_name="temps alloué")
    needs=models.TextField(verbose_name="besion" ,max_length=200)
    description=models.TextField(max_length=250)
    isValid=models.BooleanField(default=False)
    creator=models.OneToOneField(
        Student,
        on_delete=models.CASCADE,
        null=True,
        related_name="Project_Owner"
    )
    supervisor=models.ForeignKey(
        Coach,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="project_Coach"
    )
    members=models.ManyToManyField(
        to=Student,
        blank=True,
        related_name="les_memebres",
        through="MembershipInProjects"
    )

class MemebershipInProjects(models.Model):
    project=models.ForeignKey(
        Project,
        on_delete=models.CASCADE
    )
    student=models.ForeignKey(
        Student,
        on_delete=models.CASCADE
    )