from django.shortcuts import render,redirect
from .models import Blog,Comments,Contacts
from .forms import NewForm
from django.contrib.auth import login
from django.contrib.auth.models import User
import tensorflow as tf
from Blogs.forms import CustomUserCreationForm
# import speech_recognition as sr
import tensorflow_hub as hub
import tensorflow_text as text
# Create your views here.
text_recog = []
rate = []
blog = []

def register(request):
    if request.method == "GET":
        return render(
            request, "register.html",
            {"form": CustomUserCreationForm}
        )
    elif request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            return render(
                request, "register.html",
                {"form": CustomUserCreationForm})

def HomeView(request):
    rate.clear()
    blogs = Blog.objects.all()[0:10]
    for i in blogs:
        print(f"Blog Name is {i.Name}, {i.average_rating}")
        blog.append(i.Name)
        rate.append(i.average_rating)
    print(rate)
    rcp = rate.copy()
    bcp = blog.copy()
    index = -1
    for a in range(1,4):
        big = max(rcp)
        print(big)
        index = rcp.index(big)
        print(bcp[index])
        rcp.remove(big)
        bcp.remove(bcp[index])
        print(rcp)
    print(blog)
    # rate.sort()
    # print(rate[-3:])
        # blog_len = len(i.coments.all())
        # for j in i.coments.all():
        #     print("actual rating", j.rating)
        #     avg_rating += float(j.rating)
        #     print(avg_rating)
        #     print(f"Average is : {avg_rating}")
        # print(f"Toal Average is : {avg_rating}") 
        # if blog_len is not 0:
        #     avg_rating = avg_rating/blog_len
        #     print(f"Average Rating is : {avg_rating}")
        # avg_rating = 0.0
    return render(request,'index.html',{
        'blogs':blogs
    })

# def register(request):
#     if request.method == "GET":
#         return render(request,'register.html',{})  
#     else:
#         username = request.POST['name']
#         password = request.POST['password']
#         email = request.POST['email']
#         user = User.objects.create_superuser(username, password, email)
#         user.save()
#         return redirect("Blogs:HomeView")


def ContactView(request):
    if request.method =="GET":
        return render(request,'contact.html',{})
    else:
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']
        contact = Contacts(
            Name = name,
            email = email,
            subject = subject,
            message = message
        )
        contact.save()
        return redirect("Blogs:HomeView")

def BlogView(request,slug):
    if request.method =='GET':
        blog = Blog.objects.filter(slug=slug)

        if blog.exists():
            blog = blog[0]
        return render(request,'blog.html',{
            'blog':blog
        })
    else:
        blog = Blog.objects.filter(slug=slug)[0]
        comment = request.POST['comment']
        name = request.POST['name']
        result = comment
        print(result)
        model = tf.keras.models.load_model('model_py/new_IMDb_bert', compile=False)
        text_recog.append(result)
        print(text_recog)
        prediction = tf.sigmoid(model(tf.constant(text_recog)))
        prediction = f'{prediction[0][0]*10:.3f}'
        com = Comments(
            Comment = comment,
            Name = name,
            rating = prediction
        )
        com.save()
        rating_count = len(blog.coments.all())
        blog.average_rating = (blog.average_rating*rating_count + float(prediction))/(rating_count+1)
        print(f"Average Rating issss : {blog.average_rating}")
        blog.coments.add(com)
        blog.save()
        text_recog.clear()
        print(text_recog)
        print(prediction)
        return render(request, 'blog.html', {
            'blog': blog
        }) 

def AboutView(request):
    blogs = Blog.objects.all()


    return render(request,'about.html',{
        'blogs':blogs
    })

def AddBlog(request):
    if request.method == "GET":
        form = NewForm()
        return render(request,'AddBlog.html',{
            'form':form
        })
    else:
        form = NewForm(request.POST ,request.FILES)
        if form.is_valid():
            Name = form.cleaned_data.get('Name')
            Background_Image = form.cleaned_data.get('Background_Image')
            Subheading1 = form.cleaned_data.get('Subheading1')
            # Image1 = form.files.get('Image1')
            Paragraph1 = form.cleaned_data.get('Paragraph1')
            Subheading2 = form.cleaned_data.get('Subheading2')
            # Image2 = form.files.get('Image2')
            Paragraph2 = form.cleaned_data.get('Paragraph2')
            Subheading3 = form.cleaned_data.get('Subheading3')
            # Image3 = form.files.get('Image3')
            Paragraph3 = form.cleaned_data.get('Paragraph3')
            # video = form.files.get('Video')
            slug = form.cleaned_data.get('slug')
            NewBlog = Blog(
                Name = Name,
                Background_Image = Background_Image,
                Subheading1 = Subheading1,
                # Image1 = Image1,
                Paragraph1 = Paragraph1,
                Subheading2 = Subheading2,
                # Image2 = Image2,
                Paragraph2 = Paragraph2,
                Subheading3 = Subheading3,
                # Image3 = Image3,
                Paragraph3 = Paragraph3,
                # Video = video,
                slug = slug

            )
            NewBlog.save()
        else:
            pass
        return redirect("Blogs:AboutView")

def EditBlog(request,slug):
    blog = Blog.objects.get(slug=slug)
    if request.method == 'GET':

        form = NewForm(instance=blog)

        return render(request,'EditBlog.html',{
            'form':form
        })
    else:
        form = NewForm(request.POST, request.FILES)
        if form.is_valid():
            Name = form.cleaned_data.get('Name')
            Background_Image = form.cleaned_data.get('Background_Image')
            Subheading1 = form.cleaned_data.get('Subheading1')
            # Image1 = form.files.get('Image1')
            Paragraph1 = form.cleaned_data.get('Paragraph1')
            Subheading2 = form.cleaned_data.get('Subheading2')
            # Image2 = form.files.get('Image2')
            Paragraph2 = form.cleaned_data.get('Paragraph2')
            Subheading3 = form.cleaned_data.get('Subheading3')
            # Image3 = form.files.get('Image3')
            Paragraph3 = form.cleaned_data.get('Paragraph3')
            # video = form.files.get('Video')
            slug = form.cleaned_data.get('slug')

            blog.Name=Name
            blog.Background_Image=Background_Image
            blog.Subheading1=Subheading1
            # blog.Image1=Image1
            blog.Paragraph1=Paragraph1
            blog.Subheading2=Subheading2
            # blog.Image2=Image2
            blog.Paragraph2=Paragraph2
            blog.Subheading3=Subheading3
            # blog.Image3=Image3
            blog.Paragraph3=Paragraph3
            # blog.Video=video
            blog.slug=slug


            blog.save()
            return redirect('Blogs:AboutView')

def Analytics(request):
    blogs = Blog.objects.all()[0:10]
    return render(request,'Analytics.html',{
        'blogs':blogs
    })