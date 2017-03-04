#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django import template

register = template.Library()

def logfiles_without_para( parser, token ):
    return TagsWithoutPara()

class TagsWithoutPara( template.Node ):
    def render( self, content ):
        content['logo_src'] = '/static/images/Infinity-256X256.png'
        content['logo_blog_src'] = '/static/images/Blog-Infinity-256X256.png'
        content['logo_family_src'] = '/static/images/Family-Infinity-256X256.png'
        content['logo_research_src'] = '/static/images/Research-Infinite-256X256.png'
        return ''

register.tag('main_logo', logfiles_without_para)
