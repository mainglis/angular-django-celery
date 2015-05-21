from django.shortcuts import render
from django.views.generic import TemplateView
# from .models import Question, NewChoice
from django.http import HttpResponse

# or option number 2
def index(request):
    # latest_question_list = Question.objects.order_by('-pub_date')[:5]
    # context = {'latest_question_list': latest_question_list}
    # new_choice = NewChoice.objects[:5]
    new_choice = "something pretty awesome from django";
    context = {'new_choice': new_choice}
    print('do i get to index in views')
    return render(request, 'index1.html', context)

def partial(request):
    # latest_question_list = Question.objects.order_by('-pub_date')[:5]
    # context = {'latest_question_list': latest_question_list}
    # new_choice = NewChoice.objects[:5]
    partial_data = "something pretty awesome from django in a partial";
    context = {'partial_data': partial_data}
    print('do i get to the def partial')
    return render(request, 'partial.html', context)

# THIS WORKS BUT IT IS JUST LIKE INDEX
def detail(request, question_id):
    partial_data = "something pretty awesome from django in a partial";
    context = {'partial_data': partial_data}
    # return HttpResponse("You're looking at question %s." % question_id)
    print('do i get to the def detail')
    return render(request, 'partial.html', context)

def render_partial(request, template_name=None):
    template_name = 'partials/{}'.format(template_name)
    context = {
        'you-are-a-unique-snowflake': True,
    }
    return render(request, template_name, context)

# class SamplePartial(TemplateView):
#     def dispatch(self, request, *args, **kwargs):
#         template_name = kwargs['template_name']
#         try:
#             folder = kwargs['folder'] + '/'
#         except:
#             folder = ''
#         if template_name[-1] == '/':
#             self.template_name = 'report/%s%s.html' % (folder, template_name[:-1])
#         else:
#             self.template_name = 'report/%s%s.html' % (folder, template_name)
#         return super(SamplePartial, self).dispatch(request,*args,**kwargs)

class SamplePartial(TemplateView):
    def dispatch(self, request, *args, **kwargs):
        template_name = kwargs['template_name']
        try:
            folder = kwargs['folder'] + '/'
        except:
            folder = ''
        if template_name[-1] == '/':
            self.template_name = 'report/static/partials/%s%s.html' % (folder, template_name[:-1])
        else:
            self.template_name = 'report/static/partials/%s%s.html' % (folder, template_name)
        return super(SamplePartial, self).dispatch(request,*args,**kwargs)

# from http://django-angular.readthedocs.org/en/latest/integration.html#partials
# class PartialGroupView(TemplateView):
#     def get_context_data(self, **kwargs):
#         context = super(PartialGroupView, self).get_context_data(**kwargs)
#         # update the context
#         return context