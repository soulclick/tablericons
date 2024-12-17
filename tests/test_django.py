from __future__ import annotations

from typing import Any

import django
from django.conf import settings
from django.template import Context
from django.template import Template

settings.configure(
    ROOT_URLCONF=__name__,  # Make this module the urlconf
    SECRET_KEY="insecure",
    TEMPLATES=[
        {
            "BACKEND": "django.template.backends.django.DjangoTemplates",
            "APP_DIRS": False,
        },
    ],
    INSTALLED_APPS=["tablericons"],
)
urlpatterns: list[Any] = []
django.setup()


def test_success_outline_simple():
    template = Template('{% load tablericons %}{% tablericon_outline "school" %}')

    result = template.render(Context())

    assert result == (
        # fmt: off
        '<svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">\n  <path d="M22 9l-10 -4l-10 4l10 4l10 -4v6" />\n  <path d="M6 10.6v5.4a6 3 0 0 0 12 0v-5.4" />\n</svg>'
        # fmt: on
    )


def test_success_outline_path_attr():
    template = Template(
        "{% load tablericons %}"
        + '{% tablericon_outline "school" stroke_linecap="butt" %}'
    )

    result = template.render(Context())

    assert result == (
        # fmt: off
        '<svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">\n  <path d="M22 9l-10 -4l-10 4l10 4l10 -4v6" stroke-linecap="butt" />\n  <path d="M6 10.6v5.4a6 3 0 0 0 12 0v-5.4" stroke-linecap="butt" />\n</svg>'
        # fmt: on
    )


def test_success_outline_complete():
    template = Template(
        "{% load tablericons %}"
        + '{% tablericon_outline "school" size=48 class="h-4 w-4" '
        + 'data_test="a < 2" %}'
    )

    result = template.render(Context())

    assert result == (
        # fmt: off
        '<svg width="48" height="48" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="h-4 w-4" data-test="a &lt; 2">\n  <path d="M22 9l-10 -4l-10 4l10 4l10 -4v6" />\n  <path d="M6 10.6v5.4a6 3 0 0 0 12 0v-5.4" />\n</svg>'
        # fmt: on
    )


def test_success_outline_size_none():
    template = Template(
        "{% load tablericons %}" + '{% tablericon_outline "school" size=None %}'
    )

    result = template.render(Context())

    assert result == (
        # fmt: off
        '<svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">\n  <path d="M22 9l-10 -4l-10 4l10 4l10 -4v6" />\n  <path d="M6 10.6v5.4a6 3 0 0 0 12 0v-5.4" />\n</svg>'
        # fmt: on
    )


def test_success_filled():
    template = Template(
        "{% load tablericons %}"
        + '{% tablericon_filled "egg" size=40 class="h-4 w-4 inline" %}'
    )

    result = template.render(Context())

    assert result == (
        # fmt: off
        '<svg width="40" height="40" viewBox="0 0 24 24" fill="currentColor" class="h-4 w-4 inline">\n  <path d="M12.002 2c-4.173 -.008 -8.002 6.058 -8.002 12.083c0 4.708 3.25 7.917 8 7.917c4.727 -.206 8 -3.328 8 -7.917c0 -6.02 -3.825 -12.075 -7.998 -12.083z" />\n</svg>'
        # fmt: on
    )
