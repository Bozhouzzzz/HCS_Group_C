from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

PREDEFINED_TEXT = "lebron"

@login_required
def dashboard(request):
    return render(request, 'accounts/dashboard.html')


def image_text_view(request):
    message = ""  # Default message

    if request.method == "POST":
        user_text = request.POST.get("user_text", "").strip().lower()  # Convert input to lowercase

        if PREDEFINED_TEXT in user_text:  # Check if it contains the predefined text
            return redirect('success_page')
        else:
            message = "❌ Incorrect. Try again."

    return render(request, 'accounts/image_text.html', {'message': message})