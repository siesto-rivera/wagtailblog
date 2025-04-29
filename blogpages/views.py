from django.shortcuts import render, redirect, get_object_or_404
from blogpages.forms import BlogDetailForm
from blogpages.models import BlogIndex
from wagtail.models import Page

def blog_create(request):
    if request.method == 'POST':
        form = BlogDetailForm(request.POST)
        if form.is_valid():
            blog_detail = form.save(commit=False)

            # 부모 페이지 찾기 (BlogIndex)
            blog_index = BlogIndex.objects.first()  # 또는 특정 BlogIndex를 가져오기
            blog_detail.title = form.cleaned_data['title']

            # 부모 설정
            blog_index.add_child(instance=blog_detail)

            # 게시 (published 상태로 만들기)
            blog_detail.save_revision().publish()

            return redirect(blog_index.url)
    else:
        form = BlogDetailForm()

    return render(request, 'blogpages/blog_create.html', {'form': form})
