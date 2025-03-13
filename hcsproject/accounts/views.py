from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

# Predefined correct answers for 3 steps
QUESTION_ANSWERS = {
    1: "python",  # First question correct answer (case insensitive)
    2: "java",  # Second question correct answer
    3: "python",  # Third question correct answer
}


@login_required
def dashboard(request):
    return render(request, 'accounts/dashboard.html')

def reset_2fa_session(request):
    request.session['auth_step'] = 1

def image_text_view(request):
    """Handles text-based authentication for 3 steps."""
    step = request.session.get('auth_step', 1)
    message = ""

    if request.method == "POST":
        user_text = request.POST.get("user_text", "").strip().lower()

        if QUESTION_ANSWERS.get(step, "") in user_text:
            if step < 3:
                request.session['auth_step'] = step + 1
                return redirect('image_text')  # Go to the next question
            else:
                request.session['auth_step'] = 1  # Reset for next login
                return redirect('dashboard')  # Final step redirects to the dashboard
        else:
            message = "❌ Incorrect. Try again."

    return render(request, f'accounts/image_text_{step}.html', {'message': message})

def image_text_view_options(request):
    """Handles multiple-choice authentication for 3 steps."""
    step = request.session.get('auth_step', 1)

    if request.method == "POST":
        user_choice = request.POST.get("user_choice", "")

        if user_choice == OPTION_ANSWERS.get(step, ""):
            # Move to the next step
            if step < 3:
                request.session['auth_step'] = step + 1
                return redirect('image_text_options')  # Go to the next question
            else:
                request.session['auth_step'] = 1  # Reset for next login
                return redirect('dashboard')  # Final step redirects to the dashboard
        else:
            return redirect('failure_page')  # Redirect to failure page

    return render(request, f'accounts/image_text_options_{step}.html')


def timeout_reset(request):
    reset_2fa_session(request)
    return redirect('login')
