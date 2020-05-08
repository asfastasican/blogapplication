from django.shortcuts import render,get_object_or_404
from testapp.models import Post
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage

# Create your views here.
def post_list(request):
    posts=Post.objects.all()
    paginator=Paginator(posts,3)
    page_number=request.GET.get('page')
    try:
        posts=paginator.page(page_number)
    except PageNotAnInteger:
        posts=paginator.page(1)
    except EmptyPage:
        posts=paginator.page(paginator.num_pages)

    return render(request,'testapp/post_list.html',{'posts':posts})

def post_detail_view(request,id):
    post=Post.objects.get(id=id)
    return render(request,'testapp/post_detail.html',{'post':post})
