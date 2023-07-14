import json
from rest_framework.response import Response
from django.shortcuts import render, redirect
from django.conf import settings
from django.http import JsonResponse
from rest_framework.decorators import api_view
from .db import db
from datetime import datetime



@api_view(['POST'])
def add_budget(request):
    try:
        data = json.loads(request.body)
        print(data)
        year = data['year']
        month = data['month']

        # Check if budget already exists for the given year and month
        existing_budget = db.budget.find_one({'year': year, 'month': month})
        if existing_budget:
            return JsonResponse({'status': 400, 'message': 'Budget already exists for the given year and month'})

        new_budget = {
            'budget': data['budget'],
            'month': month,
            'year': year
        }
        print(new_budget)
        db.budget.insert_one(new_budget)
        return JsonResponse({'status': 200, 'message': 'Budget added successfully'})
    except:
        return JsonResponse({'status': 505, 'message': 'Something went wrong'})
    

@api_view(['POST'])
def add_credit(request):
    try:
        data = json.loads(request.body)
        print(data)
        date = str(data['creditDate'])
        year = date[:4]
        month = date[5:7] 
        new_credit= {
            'creditDetail': data['creditDetail'],
            'creditAmount': data['creditAmount'],
            'creditDate': data['creditDate'],
            'month':month,
            'year':year
        }
        db.credit.insert_one(new_credit)
        return JsonResponse({'status': 200, 'message': 'credit added successfully'})
    except:
        return JsonResponse({'status': 505, 'message': 'Something went wrong'})


@api_view(['POST'])
def add_debit(request):
    try:
        data = json.loads(request.body)
        date = str(data['debitDate'])
        year = date[:4]
        month = date[5:7]
        new_debit= {
            'debitDetail': data['debitDetail'],
            'debitAmount': data['debitAmount'],
            'debitDate': data['debitDate'],
            'month':month,
            'year':year
        }
        db.debit.insert_one(new_debit)
        return JsonResponse({'status': 200, 'message': 'debit added successfully'})
    except:
        return JsonResponse({'status': 505, 'message': 'Something went wrong'})

@api_view(['GET'])
def card_detail(request):
    try:
        current_date = datetime.now()
        month = current_date.month
        year = current_date.year
        budget = db.budget.find_one({'year': year, 'month': month})

        if budget:
            budget['_id'] = str(budget['_id'])
            return JsonResponse({'status': 200, 'message': 'Budget found', 'budget': budget})
        else:
            return JsonResponse({'status': 404, 'message': 'Budget not found'})

    except Exception as e:
        return JsonResponse({'status': 500, 'message': str(e)})


def total_income(request):
    try:
        current_date = datetime.now()
        month = current_date.month
        year = current_date.year

        total_income = db.credit.aggregate([
            {'$match': {'creditDate': {'$regex': f'{year}-{month:02}-.+'}}},
            {'$group': {'_id': None, 'totalIncome': {'$sum': '$creditAmount'}}}
        ])
        
        total_income = list(total_income)

        if total_income:
            total_income = total_income[0]['totalIncome']
            return JsonResponse({'status': 200, 'message': 'Total income found', 'totalIncome': total_income})
        else:
            return JsonResponse({'status': 404, 'message': 'Total income not found'})

    except Exception as e:
        print(e)
        return JsonResponse({'status': 500, 'message': str(e)})



@api_view(['GET'])
def total_expense(request):
    try:
        current_date = datetime.now()
        month = current_date.month
        year = current_date.year

        total_expense = db.debit.aggregate([
            {'$match': {'debitDate': {'$regex': f'{year}-{month:02}-.+'}}},
            {'$group': {'_id': None, 'totalExpense': {'$sum': '$debitAmount'}}}
        ])

        total_expense = list(total_expense)

        if total_expense:
            total_expense = total_expense[0]['totalExpense']
            return JsonResponse({'status': 200, 'message': 'Total expense found', 'totalExpense': total_expense})
        else:
            return JsonResponse({'status': 404, 'message': 'Total expense not found'})

    except Exception as e:
        print(e)
        return JsonResponse({'status': 500, 'message': str(e)})


from datetime import datetime

@api_view(['GET'])
def list_expense(request):
    try:
        current_date = datetime.now()
        month = str(current_date.month).zfill(2)
        year = str(current_date.year) 

        documents = db.debit.find({'year': year, 'month': month})

        data = []
        for document in documents:
            data.append({
                'debitAmount': document['debitAmount'],
                'debitDate': document['debitDate'],
                'debitDetail': document['debitDetail']
            })
            print(data)

        return JsonResponse({'status': 200, 'message': 'Expense documents found', 'data': data})
    
    except Exception as e:
        return JsonResponse({'status': 500, 'message': str(e)})


@api_view(['GET'])
def list_income(request):
    try:
        current_date = datetime.now()
        month = str(current_date.month).zfill(2)
        year = str(current_date.year) 

        documents = db.credit.find({'year': year, 'month': month})

        data = []
        for document in documents:
            data.append({
                'creditAmount': document['creditAmount'],
                'creditDate': document['creditDate'],
                'creditDetail': document['creditDetail']
            })
            print(data)

        return JsonResponse({'status': 200, 'message': 'income documents found', 'data': data})
    
    except Exception as e:
        return JsonResponse({'status': 500, 'message': str(e)})



