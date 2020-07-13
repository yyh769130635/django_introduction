from django.shortcuts import render
from django.http import HttpResponse
from blog.models import Article
from django.core.paginator import Paginator


# Create your views here.


def index(request):
    return HttpResponse("hello world")


def article_content(request):
    article = Article.objects.all()[0]
    title = article.title
    brief_content = article.brief_content
    content = article.content
    publish_date = article.publish_date
    article_id = article.article_id
    return_str = "title: %s, brief_content: %s, content:%s, article_id:%s, " \
                 "publish_date:%s " % (title, brief_content, content, article_id, publish_date)
    return HttpResponse(return_str)


# 主页面
def get_index_page(request):
    page = request.GET.get('page', '1')
    if page:
        page = int(page)
    else:
        page = 1
    # print('page param: ', page)
    all_article = Article.objects.all()
    top5_article_list = Article.objects.order_by('-publish_date')[:4]
    paginator = Paginator(all_article, 3)  # 实现分页
    page_num = paginator.num_pages
    # page_count=paginator.count
    # print(type(page_count))
    page_article_list = paginator.page(page)

    if page_article_list.has_next():
        next_page = page + 1
    else:
        next_page = page
    if page_article_list.has_previous():
        previous_page = page - 1
    else:
        previous_page = page

    return render(request, 'blog/index.html', {'article_list': page_article_list,
                                               'page_num': range(1, page_num + 1),
                                               'curr_page': page,
                                               'previous_page': previous_page,
                                               'next_page': next_page,
                                               'top5_article_list': top5_article_list})


def get_detail_page(request, article_id):
    all_article = Article.objects.all()
    curr_article = None
    previous_article = None
    next_article = None
    previous_index = 0
    next_index = 0
    for index, article in enumerate(all_article):
        if index == 0:
            previous_index = 0
            next_index = index + 1
        elif index == len(all_article) - 1:
            previous_index = index - 1
            next_index = index
        else:
            previous_index = index - 1
            next_index = index + 1
        if article.article_id == article_id:
            curr_article = article
            previous_article = all_article[previous_index]
            next_article = all_article[next_index]
            break

    section_list = curr_article.content.split("\n")
    return render(request, 'blog/details.html', {'curr_article': curr_article,
                                                 'section_list': section_list,
                                                 'previous_article': previous_article,
                                                 'next_article': next_article
                                                 }, )
