from .models import Article
from django.shortcuts import render, redirect
from django.http import Http404
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

def archive(request):
	return render(request, 'archive.html', {"posts": Article.objects.all()})

def get_article(request, article_id):
	try:
		post = Article.objects.get(id=article_id)
		return render(request, 'article.html', {"post": post})
	except Article.DoesNotExist:
		raise Http404

def create_post(request):
	if not request.user.is_anonymous:
		if request.method == "POST":
			form = {
				'text': request.POST["text"], 'title': request.POST["title"]
			}
		# в словаре form будет храниться информация, введенная пользователем
			if form["text"] and form["title"]:
				#title is not unique
				if title_exist(form["title"]):
					form['errors'] = u"Статья с таким названием уже существует"
					return render(request, 'create_post.html', {'form': form})
		# если поля заполнены без ошибок
				new_article = Article.objects.create(text=form["text"], title=form["title"], author=request.user)
				return redirect('get_article', article_id=new_article.id)
			# перейти на страницу поста
			else:
		# если введенные данные некорректны
				form['errors'] = u"Не все поля заполнены"
				return render(request, 'create_post.html', {'form': form})
		else:
		# просто вернуть страницу с формой, если метод GET
			return render(request, 'create_post.html', {})
	else:
		raise Http404

def loginn(request):
	if request.user.is_anonymous:
		if request.method == "POST":
			data = { 'username': request.POST['username'], 
					 'password': request.POST['password']}
			
			if data["username"] and data["password"]:
				try:
					User.objects.get(username=data["username"])
				except User.DoesNotExist:
					data['error'] = u'Пользователя с таким логином не существует'
					return render(request, 'login.html', {'form': data})
				
				user = authenticate(username=data["username"], password=data["password"])

				if user is not None: ############## login ????
					login(request, user)
					return redirect('archive')
				else:
					data['error'] = u'Неверный пароль'
					return render(request, 'login.html', {'form': data})

			else:
				data['error'] = u"Не все поля заполнены"
				return render(request, 'login.html', {'form': data})
	
		else:
			# просто вернуть страницу с формой, если метод GET
				return render(request, 'login.html', {})
	else:
		return redirect('archive')

def register(request):
	if request.user.is_anonymous:
		if request.method == "POST":
			data = { 'username': request.POST['username'], 
					 'password': request.POST['password'],
					 'email': request.POST['email']}

			if data["username"] and data["password"]:
				try:
					test = User.objects.get(username=data["username"])
					print(f'test = {test}')
					data['error'] = u'Пользователь с таким логином существует'
					return render(request, 'register.html', {'form': data})

				except User.DoesNotExist:
					#### register
					print('kek')
					user = User.objects.create_user(data["username"], data["email"], data["password"])
					print(user)
					login(request, user)
					return redirect('archive')

			else:
				data['error'] = u"Не все поля заполнены"
				return render(request, 'register.html', {'form': data})

		else:
			# просто вернуть страницу с формой, если метод GET
				return render(request, 'register.html', {})
	else:
		print(request.user)
		return redirect('archive')

def logoutt(request):
	if not request.user.is_anonymous:
		logout(request)
	return redirect('archive')

def title_exist(title):
        try:
            Article.objects.get(title=title)
            return True
        except Article.DoesNotExist:
            return False

