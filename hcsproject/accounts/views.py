from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from django.contrib import messages

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

# class CustomLoginView(LoginView):
#     template_name = 'accounts/login.html'

#     def get(self, request, *args, **kwargs):
#         """检查 timeout 参数并显示超时消息"""
#         if "timeout" in request.GET:  
#             messages.error(request, "Session timed out. Please log in again.")
#         return super().get(request, *args, **kwargs)


class CustomLoginView(LoginView):
    template_name = 'accounts/login.html'

    def get(self, request, *args, **kwargs):
        """检查 timeout 参数并显示超时消息"""
        if request.GET.get("timeout"):
            messages.error(request, "Session timed out. Please log in again.")
            print("Added timeout message!")  # Debug 信息

        return super().get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        """确保 `messages` 在 POST 之后仍然可用"""
        context = super().get_context_data(**kwargs)
        context['messages'] = messages.get_messages(self.request)
        return context
