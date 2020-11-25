from django.views.generic import TemplateView

from django.shortcuts import get_object_or_404, redirect, render

import os
import smtplib, ssl


class HomePageView(TemplateView):
    template_name = 'pages/home.html'


class AboutPageView(TemplateView):
    template_name = 'pages/about.html'

def register_tutor_view(request):
    if request.method == 'POST':
        course_title = request.form['course_title']
        author = request.form['author']
        category = request.form['category']
        if file:
            # Then attach to email as attachment
            pass
        """
            Using SMTP_SSL()
        """
        smtp_server = "smtp.gmail.com"
        sender_email = os.environ.get("SENDER_EMAIL") 
        receiver_email = os.environ.get("ADMINS_EMAIL")
        password = os.environ.get("PASSWORD")
        message = """\
        {}

        Hi there,
        A message from {}, {}. 
        {}.""".format(sender_email, name, email, content)

        # Create a secure SSL context
        context = ssl.create_default_context()

        with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
            server.login(sender_email, password)
            server.sendmail(sender_email, receiver_email, message)
        return redirect()

    return render(request, "pages/register_tutor.html", {})

def user_profile_view(request):
    return render(request, "pages/user_profile.html", {})