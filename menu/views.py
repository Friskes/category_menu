from django.views.generic.base import TemplateView

from menu.models import Category

# Create your views here.


class MenuView(TemplateView):

    template_name = 'menu/menus.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)

        categories = Category.objects.all().select_related('menu')

        menus_categories = {}
        for category in categories:

            if category.menu in menus_categories:
                menus_categories[category.menu].append(category)
            else:
                menus_categories[category.menu] = [category]

        context.update({'menus_categories': menus_categories})

        return context
