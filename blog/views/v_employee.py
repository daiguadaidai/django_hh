# -*- coding:utf-8 -*-

from django.shortcuts import render
from blog.models import Employee
from common.util.choices_field_value import ChoicesFieldValue

# Create your views here.

ONE_PAGE_OF_DATA = 10
PAGE_HSOW_LENG = 9

def index(request):

    emps = Employee.objects.all()

    try:  
        cur_page = int(request.GET.get('cur_page', '1'))  
        pageType = str(request.GET.get('pageType', ''))  
    except ValueError:  
        cur_page = 1  
        pageType = ''  
  
    # 判断点击了【下一页】还是【上一页】
    if pageType == 'pageDown':  
        cur_page += 1  
    elif pageType == 'pageUp':  
        cur_page -= 1  
  
    start_pos = (cur_page - 1) * ONE_PAGE_OF_DATA  
    end_pos = start_pos + ONE_PAGE_OF_DATA  
    emps = Employee.objects.all()[start_pos:end_pos]  
  
    all_post_counts = Employee.objects.count()
    all_page = all_post_counts / ONE_PAGE_OF_DATA
    remain_obj = all_post_counts % ONE_PAGE_OF_DATA
    if remain_obj > 0:
        all_page += 1

    # 获得显示页数的最小页
    start_page = cur_page - PAGE_HSOW_LENG / 2
    if start_page > all_page - PAGE_HSOW_LENG:
        start_page = all_page - PAGE_HSOW_LENG + 1
    start_page = 1 if start_page < 1 else start_page


    # 获得显示页数的最大页
    end_page = cur_page + PAGE_HSOW_LENG / 2
    end_page = all_page if end_page > all_page else end_page
    if end_page < PAGE_HSOW_LENG and all_page > PAGE_HSOW_LENG:
        end_page = PAGE_HSOW_LENG

    # 获得上一页
    pre_page = cur_page - 1
    pre_page = 1 if pre_page < 1 else pre_page

    # 获得下一页
    next_page = cur_page + 1
    next_page = all_page if next_page > all_page else next_page

    start_page_omit_symbol = '...'
    end_page_omit_symbol = '...'

    if start_page <= 1:
        start_page_omit_symbol = ''
    
    if end_page >= all_page:
        end_page_omit_symbol = ''


    print pre_page, start_page_omit_symbol, start_page, cur_page, end_page, end_page_omit_symbol, next_page

    page_items = range(start_page, end_page + 1)
  
    return render(request, 'employee/index.html',{'emps': emps, 'all_page': all_page, 'cur_page': cur_page, 'page_items': page_items})

def test(request):
    return render(request, 'test.html')
