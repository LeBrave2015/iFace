from django.shortcuts import render, get_object_or_404, get_list_or_404
## connect with the database
from django.utils import timezone
from .models import Post, Photo
from .forms import PostForm
from django.shortcuts import redirect
from .forms import ImageForm
from django.conf import settings
# Create your views here.

def post_list(request):
	posts=Post.objects.all().order_by('create_date')
	return render(request, 'blog/post_list.html',{'post_it': posts})

def post_detail_detail(request, pk):
	post=get_object_or_404(Post, pk=pk)
	return render(request, 'blog/post_detail_detail.html', {'post': post})

def post_detail(request, pk):
	post=get_object_or_404(Post, pk=pk)
	return render(request, 'blog/post_detail.html', {'post': post})

def add(request):
	if request.method=="POST":
		form=PostForm(request.POST)
		if form.is_valid():
			post=form.save(commit=False)
			post.author=request.user
			post.published_date=timezone.now()
			post.save()
			return redirect('post_detail', pk=post.pk)
	form=PostForm()
	return render(request, 'blog/post_edit.html', {'form':form})

##def thank_you(request):
##	return render(request, 'thank_you.html')

def image(request):
	if request.method=="POST":
		form=ImageForm(request.POST, request.FILES)
		if form.is_valid():
			print request.FILES
			print form.cleaned_data
			## both (below) work!
			print request.FILES
			save_file(request.FILES['image'])
			#save_file(form.cleaned_data['image'])
			return render(request, 'blog/thank_you.html')
	else:
		form=ImageForm()
		images=get_list_or_404(Photo)
		return render(request, 'blog/images.html', {'images': images, 'form': form})
		

def save_file(file):
    ''' lovely helper to save a file
    ''' 
    filename = file.name
    fd = open('%s/%s' % (settings.MEDIA_ROOT, str(filename)), 'wb')
    for chunk in file.chunks():
        fd.write(chunk)
    fd.close()	
