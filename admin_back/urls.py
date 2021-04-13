from django.urls import path
from admin_back import views
from django.contrib.auth import views as auth_views

app_name = 'admin_back'

urlpatterns = [
    path('login/', views.loginauth, name='loginauth'),
    path('logout/', views.logout_User, name='logout'),
    path('', views.home, name='home'),
    path('create_question/<int:survey_id>/', views.create_question, name='create_question'),
    path('create_survey/', views.create_survey, name='create_survey'),
    path('form_test', views.form_test, name='form_test'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('manage_survey/', views.manage_survey, name='manage_survey'),
    path('manage_question/<int:survey_id>/', views.manage_question, name='manage_question'),
    path('registration/', views.registration, name='user_registration'),
    path('update_profile/', views.edit_user, name='edit_user'),
    path('change_password/', views.change_password, name='change_password'),
    path('take_survey/<int:survey_id>/', views.take_survey, name='take_survey'),
    path('take_survey/<int:survey_id>/<int:question_id>', views.display_question, name='display_question'),
    path('take_survey/<int:survey_id>/end', views.end_survey, name='end_survey'),
    path('results/', views.results, name='results'),
    path('reset_password/',
         auth_views.PasswordResetView.as_view(template_name='admin_back/password_reset.html', success_url='/admin/reset_password_sent/'),
         name="password_reset"
         ),
    path('reset_password_sent/',
         auth_views.PasswordResetDoneView.as_view(template_name='admin_back/password_reset_sent.html'),
         name='password_reset_done'
         ),

    path('reset/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(template_name='admin_back/password_reset_confirm.html', success_url='/admin/reset_password_complete/'),
         name='password_reset_confirm'
         ),
    path('reset_password_complete/',
         auth_views.PasswordResetCompleteView.as_view(template_name='admin_back/password_reset_complete.html'),
         name='password_reset_complete'
         ),
]
