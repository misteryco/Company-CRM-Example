from django.contrib.auth import views as auth_views, mixins as auth_mixins, get_user_model, login
from django.core.exceptions import PermissionDenied
from django.http import HttpResponse, HttpResponseBadRequest
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views import generic as views

from django.views.decorators.csrf import csrf_protect

from crm_for_companies.web.forms import EditUserForm

UserModel = get_user_model()


class HomePage(views.ListView):
    model = UserModel
    template_name = 'index.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        return context


class UserDetailsView(views.DetailView):
    template_name = 'profile-details.html'
    model = UserModel

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        object_pk = context.get('object').pk
        context['user_ID'] = object_pk
        return context


class EditUserView(views.UpdateView):
    template_name = 'edit-user-no-csrft.html'
    model = UserModel
    fields = ('username', 'email',)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form_title'] = 'Edit Profile'
        context['form__button_title'] = 'Save Changes'
        return context

    def get_success_url(self):
        return reverse_lazy(
            'Details',
            kwargs={'pk': self.object.pk})

# disabled after re-enabling CSRF middleware in settings file
# @csrf_protect
# def edit_user_view(request, pk):
#     this_user = UserModel.objects.filter(pk=pk).get()
#     if request.method == 'POST':
#         form = EditUserForm(request.POST, instance=this_user)
#         if form.is_valid():
#             form.save()
#             return redirect('Details', pk=this_user.pk)
#     else:
#         form = EditUserForm(instance=this_user)
#     context = {
#         'form': form,
#         'object': this_user,
#     }
#     return render(request, template_name='edit-user.html', context=context)

# disabled after re-enabling CSRF middleware in settings file
# def edit_user_cookie_protection_view(request, pk):
#     this_user = UserModel.objects.filter(pk=pk).get()
#     csrf_token_value = "55555"
#     if request.method == 'POST':
#         # Verify CSRF token
#         csrf_token = request.COOKIES.get('csrftoken')
#         if not csrf_token or csrf_token != csrf_token_value:
#             return HttpResponseBadRequest('Invalid CSRF token')
#         # Process the POST request
#         form = EditUserForm(request.POST, instance=this_user)
#         if form.is_valid():
#             form.save()
#             return redirect('Details', pk=this_user.pk)
#     else:
#         form = EditUserForm(instance=this_user)
#     context = {
#         'form': form,
#         'object': this_user,
#     }
#
#     response = render(request, template_name='edit-user.html', context=context)
#     response.set_cookie(key='csrftoken', value=csrf_token_value, samesite='Strict')
#     return response
