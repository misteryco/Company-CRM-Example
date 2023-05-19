from django.contrib.auth import views as auth_views, mixins as auth_mixins, get_user_model, login
from django.core.exceptions import PermissionDenied
from django.urls import reverse_lazy
from django.views import generic as views

UserModel = get_user_model()


# class UserDetailsView(auth_mixins.LoginRequiredMixin, views.DetailView):
# class GuiPage(views.DetailView):
class UserDetailsView(views.DetailView):
    template_name = 'profile-details.html'
    model = UserModel

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        object_pk = context.get('object').pk
        context['user_ID'] = object_pk
        return context


class EditUserView(views.UpdateView):
    template_name = 'edit-user.html'
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
