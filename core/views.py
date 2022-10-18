"""Project core views."""
from django.views.generic import TemplateView


class HomeView(TemplateView):
    """Home page template view."""

    template_name: str = 'home.html'
