from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordChangeForm
from django.contrib.auth.models import User
from requester.forms import RequesterForm, ChallengeForm, CommentForm, DatesForm
from requester.models import Requester, Challenge, Category, Comment, Requester, Dates
from django.views.generic import FormView, ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView, View, RedirectView
from django.views.generic.edit import ModelFormMixin
from django.urls import reverse_lazy
from braces.views import LoginRequiredMixin
from django.views.generic.edit import BaseCreateView
from django.views.generic.list import BaseListView
from django.views.generic.base import TemplateResponseMixin
from multi_form_view import MultiFormView

class Challenges(ListView):
    model = Challenge
    template_name = 'requester/challenges.html'
    context_object_name = 'challenges'
    paginate_by = 3

    def get_context_data(self, **kwargs):
        context = super(Challenges, self).get_context_data(**kwargs)
        context['comments'] = Comment.objects.all()
        context['dates'] = Dates.objects.all()
        return context

class ChallengeDisplay(DetailView):
    model = Challenge
    def get_object(self):
        object = super(ChallengeDisplay, self).get_object()
        object.save()
        return object

    def get_context_data(self, **kwargs):
        context = super(ChallengeDisplay, self).get_context_data(**kwargs)
        context['comments'] = Comment.objects.filter(challenge=self.get_object())
        context['dates'] = Dates.objects.filter(challenge=self.get_object())
        context['form_a'] = CommentForm
        return context

class ChallengeComment(LoginRequiredMixin, FormView):
    model = Comment
    form_class = CommentForm
    template_name = 'requester/challenge_detail.html'
    login_url = 'login'

    def form_valid(self, form_a):
        form_a.instance.by = self.request.user
        challenge = Challenge.objects.get(pk=self.kwargs['pk'])
        form_a.instance.challenge = challenge
        form_a.save()
        return super(ChallengeComment, self).form_valid(form_a)

    def get_success_url(self):
        return reverse('challenge_detail', kwargs={'pk': self.kwargs['pk']})

class ChallengeDetail(DetailView):
    def get(self, request, *args, **kwargs):
        view = ChallengeDisplay.as_view()
        return view(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        view = ChallengeComment.as_view()
        return view(request, *args, **kwargs)

class ChallengeCreate(CreateView):
    model = Challenge
    success_url = '/challenger/'
    form_class = ChallengeForm
    template_name = 'requester/challenge_form.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.save()
        return super(ChallengeCreate, self).form_valid(form)

class Challenge_Dates_Display(DetailView):
    model = Challenge
    def get_object(self):
        object = super(Challenge_Dates_Display, self).get_object()
        object.save()
        return object

    def get_context_data(self, **kwargs):
        context = super(Challenge_Dates_Display, self).get_context_data(**kwargs)
        context['comments'] = Comment.objects.filter(challenge=self.get_object())
        context['dates'] = Dates.objects.filter(challenge=self.get_object())
        context['form_a'] = CommentForm
        return context

class ChallengeDates(CreateView):
    model = Dates
    success_url = '/challenger/'
    form_class = DatesForm
    template_name = 'requester/challenge_dates.html'

    def form_valid(self, form):
        challenge = Challenge.objects.get(pk=self.kwargs['pk'])
        form.instance.challenge = challenge
        form.save()
        return super(ChallengeDates, self).form_valid(form)

class Challenge_Dates_Detail(DetailView):
    def get(self, request, *args, **kwargs):
        view = Challenge_Dates_Display.as_view()
        return view(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        view = ChallengeComment.as_view()
        return view(request, *args, **kwargs)

class ChallengeUpdate(UpdateView):
    model = Challenge
    success_url = '/challenger/'
    form_class = ChallengeForm
    template_name = 'requester/challenge_update.html'

class ChallengeDelete(DeleteView):
    model = Challenge
    success_url = reverse_lazy('challenger')

class ChallengeCategory(ListView):
    model = Challenge
    template_name = 'requester/challenge_category.html'
    ordering = 'created_at'
    paginate_by = 3

    def get_queryset(self):
        self.category = get_object_or_404(Category, pk=self.kwargs['pk'])
        return Challenge.objects.filter(category=self.category)

    def get_context_data(self, **kwargs):
        context = super(ChallengeCategory, self).get_context_data(**kwargs)
        context['category'] = self.category
        return context

class CreateRequester(CreateView):
    model = Requester
    template_name = 'requester/requester.html'
    success_url = '/requester_profile/'
    fields = (
        'company',
        'address_line_1',
        'city',
        'postal_code',
        'email_address',
        'telephone',
        'picture',
        'description',
    )

    def form_valid(self, form):
        form.instance.username = self.request.user
        form.save()
        return super(CreateRequester, self).form_valid(form)

class RequesterProfile(TemplateView):
    def get(self, request):
        return render(request, 'requester/requester_profile.html')

class Requesters(TemplateView):
    def get(self, request):
        return render(request, 'requester/requesters.html')

class Challenger(TemplateView):
    def get(self, request, *args, **kwargs):
        view = Challenges.as_view(
            template_name = 'requester/challenger.html',
            paginate_by = 10
        )
        return view(request, *args, **kwargs)