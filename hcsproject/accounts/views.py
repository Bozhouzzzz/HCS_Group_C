from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

PREDEFINED_TEXT = "lebron"
CORRECT_ANSWER = "Lebron James"
@login_required
def dashboard(request):
    return render(request, 'accounts/dashboard.html')


def image_text_view(request):
    message = ""  # Default message

    if request.method == "POST":
        user_text = request.POST.get("user_text", "").strip().lower()  # Convert input to lowercase

        if PREDEFINED_TEXT in user_text:  # Check if it contains the predefined text
            return redirect('dashboard')
        else:
            message = "❌ Incorrect. Try again."

    return render(request, 'accounts/image_text.html', {'message': message})



def image_text_view_options(request):
    if request.method == "POST":
        user_choice = request.POST.get("user_choice", "")  # Get selected option

        if user_choice == CORRECT_ANSWER:
            return redirect('dashboard')  # Redirect to success page
        else:
            return redirect('failure_page')  # Redirect to failure page

    return render(request, 'accounts/image_text_options.html')