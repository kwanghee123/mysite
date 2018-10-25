from django.shortcuts import render
from django.http import HttpResponse
from polls.models import Question, Choice
from django.utils import timezone

def result(request, id):
    question = Question.objects.get(pk=id)
    return render(request, 'polls/result.html', {'question' : question})

def input(request):
    return render(request, 'polls/input.html', {})  # 규칙 : 나의앱명/

def add_question(request):          # 1   질문을 입력할수 있는 주소
    text = request.POST['zzz']      # 1-1 위 주소에 매핑되는 views 함수
    # q = Question(                   # 1-2 html 템플릿
    #     question_text=text,         # 2   html 템플릿 안에서
    #     pub_date=timezone.now())    # 2-1 form 테그 만들기
    # q.save()                        # 2-3 {% csrf_token %} 입력
    # return render(request, 'polls/add.html', {})
    return HttpResponse('입력완료')

def data(request, email, number):   # 변수를 지정해줘서 email, number 순서 상관없음
    # http:localhost:8000/polls/data?user_name=kim
    value = request.GET['user_name']
    return HttpResponse(value + email + str(number))

def vote(request):
    choice = request.POST['choice']
    c = Choice.objects.get(pk=choice)
    c.votes = c.votes + 1
    c.save()      # 투표결과 저장
    #print('@@@@@@', choice)
    return render(request,'polls/vote.html', {})

def detail(request, id):            # url 에서 <int:id> 때문에
    question = Question.objects.get(id=id)
    return render(request, 'polls/detail.html', {'item' : question})

def index(request):
    list = Question.objects.all()
    return render(request, 'polls/index.html', {'question' : list})


