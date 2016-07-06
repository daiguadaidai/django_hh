# -*- coding:utf-8 -*-

from django.db import models
from common.util.choices_field_value import ChoicesFieldValue

# Create your models here.

class Dept(models.Model):
    dept_id = models.BigIntegerField(primary_key=True)
    name = models.CharField(unique=True, max_length=10)
    dept_code = models.CharField(unique=True, max_length=5)
    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        """Java toString 方法"""
        return self.name

    class Meta:
        managed = False
        db_table = 'dept'


class Employee(models.Model):
    employee_id = models.BigIntegerField(primary_key=True)
    name = models.CharField(unique=True, max_length=10)
    age = models.IntegerField()
    gender = models.IntegerField(choices=ChoicesFieldValue.gender())
    create_time= models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)

    # ManyToOne
    dept = models.ForeignKey(Dept)

    def __unicode__(self):
        """Java toString 方法"""
        return self.name

    class Meta:
        managed = False
        db_table = 'employee'


class Engine(models.Model):
    engine_id = models.AutoField(primary_key=True)
    code = models.CharField(unique=True, max_length=5)
    create_time= models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        """Java toString 方法"""
        return self.code

    class Meta:
        managed = False
        db_table = 'engine'


class Car(models.Model):
    car_id = models.AutoField(primary_key=True)
    # engine_id = models.IntegerField()
    name = models.CharField(unique=True, max_length=5)
    create_time= models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)

    # engine = models.OneToOneField(Engine)
    engine = models.ForeignKey(Engine, unique=True)

    def __unicode__(self):
        """Java toString 方法"""
        return self.name

    class Meta:
        managed = False
        db_table = 'car'
