# -*- coding:utf-8 -*-

from django.shortcuts import render
from blog.models import Employee
from common.util.choices_field_value import ChoicesFieldValue

# Create your views here.

def index(request, id):
    user = {'name': 'HH',
            'age': 25,
            'gender': 'gen',
            'brother': {
               'name': 'HH',
               'age': '34',
            },
            'books': ['Python', 'Java']
    }

    emps = Employee.objects.all()

    return render(request, 'index.html', {'title': 'title', 'user': user, 'id': id, 'emps': emps})
