# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase
from django.core.urlresolvers import resolve
from views import post_user_list, post_list, new_comment, edit_comment, delete_comment
from django.shortcuts import render_to_response
from Accounts_app.models import User


class CommentsPageTest(TestCase):
    def test_home_Page_resolves(self):
        comments_page = resolve('/comments/')
        self.assertEqual(comments_page.func, post_list)

    def test_comments_page_status_code_is_ok(self):
        comments_page = self.client.get('/comments/')
        self.assertEqual(comments_page.status_code, 200)

    def setUp(self):
        super(CommentsPageTest, self).setUp()
        self.user = User.objects.create(username='newuser')
        self.user.set_password('pass')
        self.user.save()
        self.login = self.client.login(username='newuser', password='pass')
        self.assertEqual(self.login, True)


class NewCommentPageTest(TestCase):
    def test_newcomment_page_status_code_is_ok(self):
        newcomment_page = self.client.get('/new_comment/')
        self.assertEqual(newcomment_page.status_code, 200)

    def setUp(self):
        super(NewCommentPageTest, self).setUp()
        self.user = User.objects.create(username='newuser')
        self.user.set_password('pass')
        self.user.save()
        self.login = self.client.login(username='newuser', password='pass')
        self.assertEqual(self.login, True)


class UserCommentPageTest(TestCase):
    def test_usercomments_Page_resolves(self):
        usercomments_page = resolve('/usercomments/')
        self.assertEqual(usercomments_page.func, post_user_list)

    def test_usercomments_page_status_code_is_ok(self):
        usercomments_page = self.client.get('/usercomments/')
        self.assertEqual(usercomments_page.status_code, 200)

    def setUp(self):
        super(UserCommentPageTest, self).setUp()
        self.user = User.objects.create(username='newuser')
        self.user.set_password('pass')
        self.user.save()
        self.login = self.client.login(username='newuser', password='pass')
        self.assertEqual(self.login, True)


class UserCommentsEditPageTest(TestCase):
    def test_usercommentsedit_page_status_code_is_ok(self):
        usercommentsedit_page = self.client.get('/usercomments/')
        self.assertEqual(usercommentsedit_page.status_code, 200)

    def setUp(self):
        super(UserCommentsEditPageTest, self).setUp()
        self.user = User.objects.create(username='newuser')
        self.user.set_password('pass')
        self.user.save()
        self.login = self.client.login(username='newuser', password='pass')
        self.assertEqual(self.login, True)