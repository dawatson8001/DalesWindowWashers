# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase
from django.core.urlresolvers import resolve
from views import register, login, logout, account_details
from Accounts_app.models import User


class RegisterPageTest(TestCase):
    def test_register_Page_resolves(self):
        register_page = resolve('/register/')
        self.assertEqual(register_page.func, register)

    def test_register_page_status_code_is_ok(self):
        register_page = self.client.get('/register/')
        self.assertEqual(register_page.status_code, 200)


class LoginPageTest(TestCase):
    def test_login_Page_resolves(self):
        login_page = resolve('/login/')
        self.assertEqual(login_page.func, login)

    def test_login_page_status_code_is_ok(self):
        login_page = self.client.get('/login/')
        self.assertEqual(login_page.status_code, 200)


class LogoutPageTest(TestCase):
    def test_logout_Page_resolves(self):
        logout_page = resolve('/logout/')
        self.assertEqual(logout_page.func, logout)

    def test_logout_page_status_code_is_ok(self):
        logout_page = self.client.get('/logout/')
        self.assertEqual(logout_page.status_code, 302)


class AccountPageTest(TestCase):
    def test_account_Page_resolves(self):
        account_page = resolve('/account/')
        self.assertEqual(account_page.func, account_details)

    def test_account_page_status_code_is_ok(self):
        account_page = self.client.get('/account/')
        self.assertEqual(account_page.status_code, 200)

    def setUp(self):
        super(AccountPageTest, self).setUp()
        self.user = User.objects.create(username='newuser')
        self.user.set_password('pass')
        self.user.save()
        self.login = self.client.login(username='newuser', password='pass')
        self.assertEqual(self.login, True)