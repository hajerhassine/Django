from tabnanny import verbose
from django.db import models
from django.core.validators import MinValueValidator ,  MaxValueValidator


# Create your models here.
class User(models.Model):
    FirstName  = models.CharField(max_length=100)
    LastName = models.CharField(max_length=100)
    Email = models.EmailField(max_length=254)

class Student(User):
    pass

class Coach(User):
    pass

class Project(models.Model):
    project_name = models.CharField( 
        verbose_name="Titre du projet",max_length=50)
    project_duration = models.IntegerField(
            verbose_name="duree Estimee",default=0)
    time_allocated = models.IntegerField(
        verbose_name="temps alloue",
        validators=[
            MinValueValidator(1,'the minimum Value required is 1'),
            MaxValueValidator(10,'the maximum Value required is 10'),
        ])
    needs = models.TextField(verbose_name="Besoins", max_length=250)
    description = models.TextField(max_length=250)
    isValid =models.BooleanField(default=False)

    creator = models.OneToOneField(
        Student,
        on_delete=models.CASCADE,
        related_name="Project_Owner"
    )
    supervisor =models.ForeignKey(
        to=Coach,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name="project_Coach"
        )
    members=models.ManyToManyField(
        to=Student,
        blank=True,
        related_name="les_membres",
        through="MembershipInProjects"
    )
class MembershipInProjects(models.Model):
    Project = models.ForeignKey(
        Project,
        on_delete=models.CASCADE
    )
    Student= models.ForeignKey(
        Student,
        on_delete=models.CASCADE
    )
    time_allocated =models.IntegerField()
    def __str__(self):
        return f'{self.Project} _ {self.Student}'

class Meta:
    verbose_name_plural ="Membership"