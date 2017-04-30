#!/usr/bin/python
# -*- coding: utf-8 -*-
from sermonapp import ma
from sermonapp.models import Category


class CategorySchema(ma.ModelSchema):
    class Meta:
        model = Category

category_schema = CategorySchema()
categories_schema = CategorySchema(many=True)