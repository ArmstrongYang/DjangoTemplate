#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django import template

register = template.Library()

RESOURCE_isCDN = False

def do_tags_without_para( parser, token ):
    return TagsWithoutPara()

def do_tags_with_para( parser, token ):
    paras = token.split_contents()
    if len( paras ) != 6:
        raise template.TemplateSyntaxError("this tag takes exactly five arguments")
 
    return TagsWithPara(paras)
 
class TagsWithoutPara( template.Node ):
    def render( self, content ):
        content['resource_isCDN'] = RESOURCE_isCDN
        if RESOURCE_isCDN:
            content['modernizr_js'] = '//cdn.bootcss.com/modernizr/2.8.3/modernizr.min.js'
            content['respond_js'] = '//cdn.bootcss.com/respond.js/1.4.2/respond.min.js'

        else:
            content['bootstrap_css'] = '/static/opensource/css/bootstrap.min.css'    
            content['font_awesome'] = '/static/opensource/css/font-awesome.min.css'    
            content['animate_css'] = '/static/opensource/css/animate.min.css'    
            content['custom_home_css'] = '/static/custom/home-style.css'
            content['jquery'] = '/static/opensource/js/jquery.min.js'
            content['bootstrap_js'] =  '/static/opensource/js/bootstrap.js'    
        return ''
 
class TagsWithPara( template.Node ):
    def __init__( self, paras ):
        self.paras = paras
 
    def render( self, context ):
        context['paras_0'] = self.paras[0]
        context['paras_1'] = self.paras[1]
        context['paras_2'] = self.paras[2]
        context['paras_3'] = self.paras[3]
        context['paras_4'] = self.paras[4]
        context['paras_5'] = self.paras[5]
        return ''

register.tag('open_source', do_tags_without_para)
register.tag('custom_tags_without_para', do_tags_without_para)
register.tag('custom_tags_with_para', do_tags_with_para)