from django.http import HttpRequest, JsonResponse
from django.utils.translation import gettext as _
from django.views import View
from django.views.generic import ListView, DetailView, TemplateView

from .forms import ContactForm
from .models import Post
from .tasks import send_message


class ContextMixin:

    context = {
        'site_title': 'VeryCoolNewsPortal',
        'facebook': 'https://facebook.com',
        'twitter': 'https://twitter.com',
        'github': 'https://github.com',
    }


class PostListView(ContextMixin, ListView):
    model = Post
    template_name = 'blog/index.html'
    context_object_name = 'posts'

    def get_queryset(self):
        return Post.objects.filter(is_published=True).order_by('date_published')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(PostListView, self).get_context_data()
        context.update(self.context)
        context['user'] = self.request.user
        return context

    def get(self, request, *args, **kwargs):
        send_message.delay('info@info.com')
        return super(PostListView, self).get(request=request)


class PostDetailView(ContextMixin, DetailView):
    model = Post
    template_name = 'blog/post.html'
    context_object_name = 'post'
    slug_url_kwarg = 'post_slug'

    def get_context_data(self, **kwargs):
        context = super(PostDetailView, self).get_context_data()
        context.update(self.context)
        context['user'] = self.request.user
        return context


class AboutTemplateView(ContextMixin, TemplateView):
    template_name = 'blog/about.html'

    def get_context_data(self, **kwargs):
        context = super(AboutTemplateView, self).get_context_data()
        context.update(self.context)
        context.update(
            {
                'about_title': _('About Very Cool Site'),
                'about_subtitle': _('Subtitle very cool'),
                'about_about': '''
Lorem ipsum dolor sit amet, consectetur adipisicing elit. Saepe nostrum ullam eveniet pariatur voluptates odit, fuga atque ea nobis sit soluta odio, adipisci quas excepturi maxime quae totam ducimus consectetur?
Lorem ipsum dolor sit amet, consectetur adipisicing elit. Eius praesentium recusandae illo eaque architecto error, repellendus iusto reprehenderit, doloribus, minus sunt. Numquam at quae voluptatum in officia voluptas voluptatibus, minus!
Lorem ipsum dolor sit amet, consectetur adipisicing elit. Aut consequuntur magnam, excepturi aliquid ex itaque esse est vero natus quae optio aperiam soluta voluptatibus corporis atque iste neque sit tempora!
                '''
            }
        )
        context['user'] = self.request.user
        return context


class ContactCreateView(ContextMixin, TemplateView):
    template_name = 'blog/contact.html'

    def get_context_data(self, **kwargs):
        context = super(ContactCreateView, self).get_context_data()
        context.update(self.context)
        context['heading'] = 'Contact :)'
        context['subheading'] = 'Please...'
        context['contact_form'] = ContactForm()
        context['user'] = self.request.user
        return context

    def post(self, request: HttpRequest):
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            send_message.delay(request.POST.get('email'))
        return self.get(request=request)

#
# class PostApiView(View):
#
#     def get(self, request: HttpRequest, post_id=None):
#         if not post_id:
#             posts = Post.objects.all().filter(is_published=True)
#             data = {}
#             for post in posts:
#                 data[str(post.id)] = {
#                     'title': post.title,
#                     'subtitle': post.subtitle,
#                     'text': post.text,
#                     'image': post.image.url,
#                     'author': post.author.username
#                 }
#             return JsonResponse(data=data)
#         else:
#             post = Post.objects.filter(pk=int(post_id))
#             if post:
#                 post = post[0]
#                 post = {
#                     'id': post.id,
#                     'title': post.title,
#                     'subtitle': post.subtitle,
#                     'text': post.text,
#                     'image': post.image.url,
#                     'author': post.author.username
#                 }
#                 return JsonResponse(data=post)
#             else:
#                 return JsonResponse(data={'status': 404, 'detail': f'post {post_id} does not exist'}, status=404)
