# -*- coding:utf-8 -*-

from django.shortcuts import render
from blog.models import Employee
from common.util.choices_field_value import ChoicesFieldValue
from common.util.pagination import Pagination

# Create your views here.

one_page_data_size = 10
show_page_item_len = 9

def index(request):

    try:  
        cur_page = int(request.GET.get('cur_page', '1'))  
    except ValueError:  
        cur_page = 1  
  
    """
    start_pos = (cur_page - 1) * one_page_data_size  
    end_pos = start_pos + one_page_data_size  
    objs = Employee.objects.all()[start_pos:end_pos]  
  
    # 计算总共的页数
    all_obj_counts = Employee.objects.count()
    all_page = all_obj_counts / one_page_data_size
    remain_obj = all_obj_counts % one_page_data_size
    if remain_obj > 0:
        all_page += 1

    # 限制当前页不能小于1和并且大于总页数
    cur_page = 1 if cur_page < 1 else cur_page
    cur_page = all_page if cur_page > all_page else cur_page

    # 获得显示页数的最小页
    start_page = cur_page - show_page_item_len / 2
    if start_page > all_page - show_page_item_len:
        start_page = all_page - show_page_item_len + 1
    start_page = 1 if start_page < 1 else start_page

    # 获得显示页数的最大页
    end_page = cur_page + show_page_item_len / 2
    end_page = all_page if end_page > all_page else end_page
    if end_page < show_page_item_len and all_page > show_page_item_len:
        end_page = show_page_item_len

    # 获得上一页
    pre_page = cur_page - 1
    pre_page = 1 if pre_page < 1 else pre_page

    # 获得下一页
    next_page = cur_page + 1
    next_page = all_page if next_page > all_page else next_page

    # 定义省略符
    start_page_omit_symbol = '...'
    end_page_omit_symbol = '...'

    if start_page <= 1:
        start_page_omit_symbol = ''
    
    if end_page >= all_page:
        end_page_omit_symbol = ''

    page_items = range(start_page, end_page + 1)

    pagination = {
        'objs': objs,
        'all_obj_counts': all_obj_counts,
        'start_pos': start_pos,
        'end_pos': end_pos,
        'all_page': all_page,
        'cur_page': cur_page,
        'pre_page': pre_page,
        'next_page': next_page,
        'page_items': page_items,
        'start_page_omit_symbol': start_page_omit_symbol,
        'end_page_omit_symbol': end_page_omit_symbol,
    }

    print pre_page, start_page_omit_symbol, start_page, cur_page, end_page, end_page_omit_symbol, next_page
    """

    pagination = Pagination.create_pagination(
                                      from_name='blog.models', 
                                      model_name='Employee',
                                      cur_page=cur_page,
                                      start_page_omit_symbol = '...',
                                      end_page_omit_symbol = '...',
                                      one_page_data_size=10,
                                      show_page_item_len=9)
  
    # return render(request, 'employee/index.html',{'pagination':pagination, 'objs': objs, 'all_page': all_page, 'cur_page': cur_page, 'page_items': page_items})
    return render(request, 'employee/index.html',{'pagination':pagination})

def test(request):
    return render(request, 'test.html')
