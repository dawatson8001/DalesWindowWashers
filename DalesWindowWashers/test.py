# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase
from django.core.urlresolvers import resolve
from views import index, aboutus
from django.shortcuts import render_to_response
from Accounts_app.models import User


class HomePageTest(TestCase):
    def test_home_Page_resolves(self):
        home_page = resolve('/')
        self.assertEqual(home_page.func, index)

    def test_home_page_status_code_is_ok(self):
        home_page = self.client.get('/')
        self.assertEqual(home_page.status_code, 200)

    def test_check_content_is_correct(self):
        home_page = self.client.get('/')
        self.assertTemplateUsed(home_page, "base.html", "index.html")
        home_page_template_output = render_to_response("index.html").content
        self.assertEqual(home_page.content, home_page_template_output)

    def setUp(self):
        super(HomePageTest, self).setUp()
        self.user = User.objects.create(username='newuser')
        self.user.set_password('pass')
        self.user.save()
        self.login = self.client.login(username='newuser', password='pass')
        self.assertEqual(self.login, True)


class AboutUsPageTest(TestCase):
    def test_about_us_Page_resolves(self):
        aboutus_page = resolve('/AboutUs')
        self.assertEqual(aboutus_page.func, aboutus)

    def test_home_page_status_code_is_ok(self):
        aboutus_page = self.client.get('/AboutUs')
        self.assertEqual(aboutus_page.status_code, 200)

    def test_check_content_is_correct(self):
        aboutus_page = self.client.get('/AboutUs')
        self.assertTemplateUsed(aboutus_page, "AboutUs.html")
        aboutus_page_template_output = render_to_response("AboutUs.html").content
        self.assertEqual(aboutus_page.content, aboutus_page_template_output)

    def setUp(self):
        super(AboutUsPageTest, self).setUp()
        self.user = User.objects.create(username='newuser')
        self.user.set_password('pass')
        self.user.save()
        self.login = self.client.login(username='newuser', password='pass')
        self.assertEqual(self.login, True)
