from django.shortcuts import render
from .models import Question
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage
from django.contrib import messages
# Create your views here.

def home(request):
    return render(request,'quiz/base.html')

def exam(request):
    post_list = Question.objects.all()
    paginator = Paginator(post_list, 1)
    page_number = request.GET.get('page')
    try:
        post_list = paginator.page(page_number)
    except PageNotAnInteger:
        post_list = paginator.page(1)
    except EmptyPage:
        post_list = paginator.page(paginator.num_page)
    if request.method == 'POST':
        for post in post_list:
            sub = request.POST.get(str(post.id))
            if sub == post.right_ans:
                info = messages.info(request, 'Three credits remain in your account.')
                return render(request,'quiz/ExamPage.html', {'post_list':post_list,'ans':info})
            elif sub != post:
                print('incorrect')
            else:
                print('please select ')
    return render(request, 'quiz/ExamPage.html', {'post_list': post_list,})
