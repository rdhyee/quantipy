"""
Excel cell formats
"""

from quantipy.core.tools.qp_decorators import lazy_property

from excel_formats_constants import _ATTRIBUTES, _DEFAULT_ATTRIBUTES


class _Format(dict):

    __attributes__ = _ATTRIBUTES
    __slots__ = __attributes__

    def __init__(self, **kwargs):
        for name in self.__attributes__:
            if name in kwargs.keys():
                self[name] = kwargs[name]
        for name in kwargs:
            if name not in self.__attributes__:
                raise Exception(name)

    def __hash__(self):
        return hash(repr(self))


class _ExcelFormats(object):

    __default_attributes__ = _DEFAULT_ATTRIBUTES.keys()
    __slots__ = __default_attributes__

    def __init__(self, **kwargs):
        for name in self.__default_attributes__:
            value_or_default = kwargs.get(name, _DEFAULT_ATTRIBUTES[name]) 
            setattr(self, name, value_or_default)


class ExcelFormats(_ExcelFormats):

    __slots__ = ('_lazy__background',
                 '_lazy__base',
                 '_lazy__bottom',
                 '_lazy_cell_details', 
                 '_lazy__count',
                 '_lazy__interior',
                 '_lazy__left',
                 '_lazy__net',
                 '_lazy__pct',
                 '_lazy__right',
                 '_lazy__stat',
                 '_lazy__sum',
                 '_lazy_template',
                 '_lazy__test',
                 '_lazy__top',
                 '_lazy__ubase',
                 '_lazy_x_label',
                 '_lazy_x_right',
                 '_lazy_x_base',
                 '_lazy_x_bold',
                 '_lazy_x_italic',
                 '_lazy_x_net',
                 '_lazy_x_stat',
                 '_lazy_x_test',
                 '_lazy_x_ubase',
                 '_lazy_y')

    def __init__(self, **kwargs):
        super(ExcelFormats, self).__init__(**kwargs)
                # updates = getattr(self, '_' + part)()


    def __getattr__(self, name):
        if name.startswith('x_') and name not in dir(self):
            return self.x_right
        return self.__getattribute__(name)

    def __getitem__(self, name):
        try:
            return getattr(self, name)
        except AttributeError:
            format_ = self.template
            
            parts = name.split('_no_')
            name, no = parts[0], parts[1:]

            for part in name.split('_'):
                if part == 'dummy':
                    for attr in ('top', 'top_color'):
                        try:
                            format_.pop(attr)
                        except KeyError:
                            pass
                    continue
                updates = getattr(self, '_' + part)
                if ('left' in name) and (part == 'right'):
                    updates = {k: v for k, v in updates.iteritems() 
                               if k != 'left'}
                format_.update(updates)

            for attr in no:
                try:
                    format_.pop(attr)
                except KeyError:
                    pass

            return _Format(**format_)

    @property
    def template(self):
        return dict([(a, getattr(self, a)) for a in _Format.__attributes__])
            
    @lazy_property
    def cell_details(self):
        format_ = self.template

        format_.update(dict(font_name=self.font_name_test, text_h_align=1))

        return _Format(**format_)

    @lazy_property
    def y(self):
        format_ = self.template
        
        format_.update(dict(left=self.border_style_ext,
                            top=self.border_style_ext,
                            right=self.border_style_ext,
                            bottom=self.border_style_ext,
                            bold=self.bold_y,
                            bg_color=self.bg_color_y,
                            font_color=self.font_color_y,
                            font_name=self.font_name_y,
                            font_size=self.font_size_y,
                            italic=self.italic_y,
                            text_v_align=self.text_v_align_y,
                            text_h_align=self.text_h_align_y,
                            ))

        return _Format(**format_)

    @lazy_property
    def test(self):
        format_ = self.template

        format_.update(dict(font_name=self.font_name_test,
                            font_size=self.font_size_test,
                            font_color=self.font_color_test,
                            bold=self.bold_y,
                            left=self.border_style_ext,
                            top=self.border_style_ext,
                            right=self.border_style_ext,
                            bottom=self.border_style_ext))

        return _Format(**format_)

    @lazy_property
    def x_label(self):
        format_ = self.template

        format_.update(dict(bold=self.bold_label,
                            bg_color=self.bg_color_label,
                            font_color=self.font_color_label,
                            font_name=self.font_name_label,
                            font_size=self.font_size_label,
                            italic=self.italic_label,
                            text_v_align=self.text_v_align_label,
                            text_h_align=self.text_h_align_label,
                           ))

        return _Format(**format_)

    @lazy_property
    def x_right(self):
        format_ = self.template

        format_.update(dict(text_h_align=3))
        
        return _Format(**format_)

    @lazy_property
    def x_bold(self):
        format_ = self.template

        format_.update(dict(bold=True, text_h_align=3))
                            
        return _Format(**format_)

    @lazy_property
    def x_italic(self):
        format_ = self.template

        format_.update(dict(italic=True, text_h_align=3))

        return _Format(**format_)

    @lazy_property
    def x_net(self):
        format_ = self.template

        format_.update(dict(bold=self.bold_net_text,
                            bg_color=self.bg_color_net_text,
                            font_color=self.font_color_net_text,
                            font_name=self.font_name_net_text,
                            font_size=self.font_size_net_text,
                            italic=self.italic_net_text,
                            text_v_align=self.text_v_align_net_text,
                            text_h_align=self.text_h_align_net_text))
                            
        return _Format(**format_)

    @lazy_property
    def x_stat(self):
        format_ = self.template

        format_.update(dict(font_name=self.font_name_stat,
                            font_size=self.font_size_stat,
                            font_color=self.font_color_stat,
                            bold=self.bold_stat,
                            text_h_align=3))

        return _Format(**format_)

    @lazy_property
    def x_test(self):
        format_ = self.template

        format_.update(dict(font_name=self.font_name_test,
                            font_size=self.font_size_test,
                            font_color=self.font_color_test,
                            font_script=self.font_super_test,
                            bold=self.bold_test,
                            text_h_align=3,
                            num_format='0.00'))

        return _Format(**format_)

    @lazy_property
    def x_base(self):
        format_ = self.template

        format_.update(dict(bold=self.bold_base_text,
                            bg_color=self.bg_color_base_text,
                            font_color=self.font_color_base_text,
                            font_name=self.font_name_base_text,
                            font_size=self.font_size_base_text,
                            italic=self.italic_base_text,
                            text_v_align=self.text_v_align_base_text,
                            text_h_align=self.text_h_align_base_text))
                            
        return _Format(**format_)

    @lazy_property
    def x_ubase(self):
        format_ = self.template

        format_.update(dict(bold=self.bold_ubase_text,
                            bg_color=self.bg_color_ubase_text,
                            font_color=self.font_color_ubase_text,
                            font_name=self.font_name_ubase_text,
                            font_size=self.font_size_ubase_text,
                            italic=self.italic_ubase_text,
                            text_v_align=self.text_v_align_ubase_text,
                            text_h_align=self.text_h_align_ubase_text))
                            
        return _Format(**format_)

    @lazy_property
    def _left(self):
        return dict(left=self.border_style_ext)

    @lazy_property
    def _right(self):
        return dict(left=self.border_style_int,
                    right=self.border_style_ext)

    @lazy_property
    def _top(self):
        return dict(top=self.border_style_ext)

    @lazy_property
    def _bottom(self):
        return dict(bottom=self.border_style_ext)

    @lazy_property
    def _interior(self):
        return dict(left=self.border_style_int)

    @lazy_property
    def _base(self):
        return dict(font_color=self.font_color_base,
                    bold=self.bold_base,
                    bottom=self.border_style_int)

    @lazy_property
    def _base(self):
        return dict(bottom=self.border_style_int, 
                    bold=self.bold_base,
                    bg_color=self.bg_color_base,
                    font_color=self.font_color_base,
                    font_name=self.font_name_base,
                    font_size=self.font_size_base,
                    italic=self.italic_base,
                    text_v_align=self.text_v_align_base,
                    text_h_align=self.text_h_align_base)

    @lazy_property
    def _ubase(self):
        return dict(bottom=self.border_style_int, 
                    bold=self.bold_ubase,
                    bg_color=self.bg_color_ubase,
                    font_color=self.font_color_ubase,
                    font_name=self.font_name_ubase,
                    font_size=self.font_size_ubase,
                    italic=self.italic_ubase,
                    text_v_align=self.text_v_align_ubase,
                    text_h_align=self.text_h_align_ubase)

    @lazy_property
    def _count(self):
        return dict(num_format=self.num_format_count,
                    bg_color=self.bg_color_default) 

    @lazy_property
    def _pct(self):
        return dict(num_format=self.num_format_pct, 
                    bg_color=self.bg_color_default) 

    @lazy_property
    def _net(self):
        return dict(top=self.border_style_int, 
                    top_color=self.border_color_net_top,
                    bold=self.bold_net,
                    bg_color=self.bg_color_net,
                    font_color=self.font_color_net,
                    font_name=self.font_name_net,
                    font_size=self.font_size_net,
                    italic=self.italic_net,
                    text_v_align=self.text_v_align_net,
                    text_h_align=self.text_h_align_net)

    @lazy_property
    def _stat(self):
        return dict(top=self.border_style_int,
                    border_color=self.border_color_stat_top,
                    font_name=self.font_name_stat,
                    font_size=self.font_size_stat,
                    font_color=self.font_color_stat,
                    bold=self.bold_stat,
                    num_format=self.num_format_stat,
                    bg_color=self.bg_color_stat)

    @lazy_property
    def _test(self):
        return dict(font_name=self.font_name_test,
                    font_size=self.font_size_test,
                    font_color=self.font_color_test,
                    bold=self.bold_test,
                    font_script=self.font_super_test,
                    bg_color=self.bg_color_test)

    @lazy_property
    def _sum(self):
        return dict(top=self.border_style_int)

