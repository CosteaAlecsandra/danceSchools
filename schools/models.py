from django.db import models

# Create your models here.


class SchoolAdministrator(models.Model):
    objects = models.Manager()
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)

    def __str__(self):
        return self.username


class School(models.Model):
    objects = models.Manager()
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    administrators = models.ManyToManyField('SchoolAdministrator')


class Comment(models.Model):
    objects = models.Manager()
    author = models.CharField(max_length=100)
    description = models.TextField()
    rating = models.IntegerField()
    school = models.ForeignKey('School', on_delete=models.CASCADE)


class Participant(models.Model):
    SEX_CHOICES = [('M', 'Male'), ('F', 'Female')]
    firstName = models.CharField(max_length=100)
    lastName = models.CharField(max_length=100)
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    sex = models.CharField(choices=SEX_CHOICES, max_length=1)
    height = models.FloatField()


class Instructor(models.Model):
    firstName = models.CharField(max_length=100)
    lastName = models.CharField(max_length=100)
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    personalDescription = models.TextField(blank=True)


class InstructorPhotos(models.Model):
    photo = models.ImageField()
    instructor = models.ForeignKey('Instructor', on_delete=models.CASCADE)


class CourseType(models.Model):
    name = models.CharField(max_length=100)
    proportion = models.IntegerField()


class Course(models.Model):
    date = models.DateTimeField()
    location = models.CharField(max_length=100)
    description = models.TextField()
    school = models.ForeignKey('School', on_delete=models.CASCADE)
    types = models.ManyToManyField('CourseType')
    participants = models.ManyToManyField('Participant')
    instructors = models.ManyToManyField('Instructor')


class Pair(models.Model):
    name = models.CharField(max_length=50)
    course = models.ForeignKey('Course', on_delete=models.CASCADE)
    participant1 = models.OneToOneField(Participant, null=True, on_delete=models.SET_NULL)


class Event(models.Model):
    description = models.TextField()
    photo = models.ImageField(blank=True)
    author = models.CharField(max_length=100)
    course = models.ForeignKey('Course', on_delete=models.CASCADE)


