from dal import autocomplete
from dal_select2.widgets import *
from samba.geo.models import Municipio

class MunicipioAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        # Don't forget to filter out results depending on the visitor !
        if not self.request.user.is_authenticated():
            return Municipio.objects.none()

        qs = Municipio.objects.all()

        if self.q:
            qs = qs.filter(nome__istartswith=self.q)

        return qs

class Select2PtWidgetMixin(Select2WidgetMixin):
    class Media:
        """Automatically include static files for the admin."""

        css = {
            'all': (
                'autocomplete_light/vendor/select2/dist/css/select2.css',
                'autocomplete_light/select2.css',
            )
        }
        js = (
            'autocomplete_light/jquery.init.js',
            'autocomplete_light/autocomplete.init.js',
            'autocomplete_light/vendor/select2/dist/js/select2.full.js',
            'autocomplete_light/select2.js',
            # Provide an additional i18 js.
            'autocomplete_light/vendor/select2/dist/js/i18n/pt-BR.js',
        )

    def build_attrs(self, *args, **kwargs):
        attrs = super(Select2PtWidgetMixin, self).build_attrs(*args, **kwargs)
        attrs.setdefault('data-locale', 'ru')
        return attrs

class Select2Pt(Select2PtWidgetMixin, Select):
    pass


class Select2PtuMultiple(Select2PtWidgetMixin, SelectMultiple):
    pass


class ModelSelect2Pt(QuerySetSelectMixin,
                     Select2PtWidgetMixin,
                     forms.Select):
    pass

class ModelSelect2PtMultiple(QuerySetSelectMixin,
                             Select2PtWidgetMixin,
                             forms.SelectMultiple):
    pass
