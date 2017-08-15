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

    def test_check_content_is_correct(self):
        comments_page = self.client.get('/comments/')
        self.assertTemplateUsed(comments_page, "comments.html")
        comments_page_template_output = render_to_response("comments.html").content
        self.assertEqual(comments_page.content, comments_page_template_output)

    def setUp(self):
        super(CommentsPageTest, self).setUp()
        self.user = User.objects.create(username='newuser')
        self.user.set_password('pass')
        self.user.save()
        self.login = self.client.login(username='newuser', password='pass')
        self.assertEqual(self.login, True)


class NewCommentPageTest(TestCase):
    def test_about_us_Page_resolves(self):
        newcomment_page = resolve('/newcomment')
        self.assertEqual(newcomment_page.func, new_comment)

    def test_newcomment_page_status_code_is_ok(self):
        newcomment_page = self.client.get('/new_comment/')
        self.assertEqual(newcomment_page.status_code, 200)

    def test_check_content_is_correct(self):
        newcomment_page = self.client.get('/new_comment/')
        self.assertTemplateUsed(newcomment_page, "newcomment.html")
        newcomment_page_template_output = render_to_response("newcomment.html").content
        self.assertEqual(newcomment_page.content, newcomment_page_template_output)

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

    def test_check_content_is_correct(self):
        usercomments_page = self.client.get('/usercomments/')
        self.assertTemplateUsed(usercomments_page, "usercomments")
        usercomments_page_template_output = render_to_response("usercomments").content
        self.assertEqual(usercomments_page.content, usercomments_page_template_output)

    def setUp(self):
        super(UserCommentPageTest, self).setUp()
        self.user = User.objects.create(username='newuser')
        self.user.set_password('pass')
        self.user.save()
        self.login = self.client.login(username='newuser', password='pass')
        self.assertEqual(self.login, True)


class UserCommentsEditPageTest(TestCase):
    def test_about_us_Page_resolves(self):
        usercommentsedit_page = resolve('/edit/')
        self.assertEqual(usercommentsedit_page.func, edit_comment)

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


class DeletePageTest(TestCase):
    def test_about_us_Page_resolves(self):
        delete_page = resolve('/post/delete/')
        self.assertEqual(delete_page.func, delete_comment)

    def test_delete_page_status_code_is_ok(self):
        delete_page = self.client.get('/post/delete//')
        self.assertEqual(delete_page.status_code, 302)

    def setUp(self):
        super(DeletePageTest, self).setUp()
        self.user = User.objects.create(username='newuser')
        self.user.set_password('pass')
        self.user.save()
        self.login = self.client.login(username='newuser', password='pass')
        self.assertEqual(self.login, True)

