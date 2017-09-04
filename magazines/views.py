# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Magazine

# Create your views here.

@login_required(login_url="/login/")
def show_magazines(request):
    mags = Magazine.objects.all()
    return render(request, "magazines/magazines.html", {"magazines": mags})
