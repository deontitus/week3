from django.shortcuts import render

def home_view(request):
    context = {
        "title": "Klaw Courses",
        "user_name": "Deon",
        "courses": ["Python", "Django", "AI", "Web Development"]
    }
    return render(request, "courses/course_list.html", context)
def detail_view(request, name):
    return HttpResponse(f"Course Name: {name}")