from django.shortcuts import render, redirect
from blogpages.models import BlogDetail, BlogIndex
from .forms import BlogDetailForm

def blog_create(request):
    if request.method == 'POST':
        form = BlogDetailForm(request.POST)
        if form.is_valid():
            blog_detail = form.save(commit=False)

            # 1. BlogIndex 부모 페이지 찾기
            blog_index = BlogIndex.objects.first()  # 필요하면 id로 특정 BlogIndex 찾기

            # 2. 제목은 이미 form.save(commit=False)로 채워짐

            # 3. Wagtail 페이지 트리에 추가
            blog_index.add_child(instance=blog_detail)

            # 4. Revision 저장하고, publish로 바로 공개
            blog_detail.save_revision().publish()

            # 5. 저장 후 BlogIndex 목록 페이지로 리다이렉트
            return redirect(blog_index.url)
    else:
        form = BlogDetailForm()

    return render(request, 'blogpages/blog_create.html', {'form': form})
