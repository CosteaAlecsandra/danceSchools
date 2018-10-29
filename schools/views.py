from django.shortcuts import render
from django.http import HttpResponse
from django.http import Http404

from .models import School
from .models import SchoolAdministrator
from .models import Comment


# Create your views here.


def home(request):
    schools = School.objects.all()
    return render(request, 'home.html', {'schools': schools})


def school_details(request, id):
    try:
        school = School.objects.get(id=id)
    except School.DoesNotExist:
        raise Http404('School not found!')

    # TODO AC - how should be treated cases of errors, because an empty list of admins is a valid one
    admins = SchoolAdministrator.objects.filter(school=id)

    comments = Comment.objects.filter(school=id)

    return render(request, 'school_details.html', {'school': school, 'admins': admins, 'comments': comments})
