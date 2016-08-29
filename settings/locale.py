from django.utils.translation import ugettext_lazy as _

from settings.base import rel


TIME_ZONE = 'UTC'

LANGUAGES = (
	('uk', _('Ukrainian')),
    ('en', _('English')),
    ('ru', _('Russian')),

)

LANGUAGE_CODE = 'uk-UA'

USE_I18N = True

USE_L10N = True

USE_TZ = True

LOCALE_PATHS = (
    rel('locale'),
)
