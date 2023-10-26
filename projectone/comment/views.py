from django.shortcuts import redirect
from django.views.generic import TemplateView
from comment.forms import CommentForm


class CommentView(TemplateView):
    http_method_name = ['post']
    template_name = 'comment/result.html'

    def post(self, request):
        form = CommentForm(request.POST)
        target = request.POST.get('target')

        if form.is_valid():
            comment = form.save(commit=False)
            comment.target = target
            comment.save()
            return redirect(target)

        context = {
            'succeed': False,
            'form': form,
            'target': target,
        }
        return self.render_to_response(context)
