# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase
from django.core.urlresolvers import resolve
from django.shortcuts import render_to_response
from .views import all_products

# Create your tests here.
class ProductsPageTest(TestCase):
    def test_products_page_resolves(self):
        products_page = resolve("/products/")
        self.assertEqual(products_page.func, all_products)


    def test_products_page_status_code_ok(self):
        products_page = self.client.get("/products/")
        self.assertEqual(products_page.status_code, 200)
    

    def test_products_page_content_is_correct(self):
        products_page = self.client.get("/products/")
        self.assertTemplateUsed(products_page, "products/products.html")
        products_page_template_output = render_to_response("products/products.html").content
        self.assertEqual(products_page.content, products_page_template_output)
