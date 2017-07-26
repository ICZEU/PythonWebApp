#!/usr/bin/python
# -*- coding: utf-8 -*-
from sermonapp import ma
from sermonapp.models import Category
from sermonapp.models import Series


class CategorySchema(ma.ModelSchema):
    class Meta:
        model = Category


class SeriesSchema(ma.ModelSchema):
    class Meta:
        model = Series


category_schema = CategorySchema()
categories_schema = CategorySchema(many=True)
series_schema = SeriesSchema()
series_list_schema = SeriesSchema(many=True)