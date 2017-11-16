
_ATTRIBUTES = ('bg_color',
               'bold',
               'border_color',
               'bottom',
               'bottom_color',
               'font_color',
			   'font_name',
               'font_size',
               'font_script',
               'italic',
               'left',
               'left_color',
               'num_format',
               'right',
               'right_color',
               'text_v_align',
               'text_h_align',
               'text_wrap',
               'top',
               'top_color')

_DEFAULTS = dict(align_left=1,
                 align_center=2,
                 align_right=3,
                 align_top=1,
                 align_vcenter=2,
                 align_bottom=3,
                 bg_color='#FFFFFF',
                 bold=False,
                 border=None,
                 border_color='#D9D9D9',
                 border_style_ext=5,
                 border_style_int=1,
                 font_color='#000000',
                 font_name='Arial',
                 font_size=9,
                 italic=False,
                 num_format='0',
                 num_format_count='0',
                 num_format_default='0.00',
                 num_format_pct='0%',
                 num_format_stat='0.00',
                 text_wrap=True)

cell_types = ('base',     'base_text',
			  'net',      'net_text',
			  'stat',     'stat_text',
			  'stattest', 'stattest_text',
			  'sum',   	  'sum_text',
			  'test',  	  'test_text',
			  'ubase', 	  'ubase_text',
			  'label',
			  'y')

cell_attributes = ('bg_color', 'bold', 'font_color', 'font_name', 'font_size', 'italic')

_DEFAULT_CELL = dict([item
                      for cell_type in cell_types
                      for item in [(a + '_' + cell_type, _DEFAULTS[a]) for a in cell_attributes]])

_DEFAULT_GENERAL = dict(bg_color=_DEFAULTS['bg_color'],
                        bg_color_default=_DEFAULTS['bg_color'],
                        bold=_DEFAULTS['bold'],
                        border_color=_DEFAULTS['border_color'],
                        border_color_net_top=_DEFAULTS['border_color'],
                        border_color_stat_top=_DEFAULTS['border_color'],
                        border_style_ext=_DEFAULTS['border_style_ext'],
                        border_style_int=_DEFAULTS['border_style_int'],
                        bottom=_DEFAULTS['border'],
                        bottom_color=_DEFAULTS['border_color'],
                        font_color=_DEFAULTS['font_color'],
                        font_color_str=_DEFAULTS['font_color'],
                        font_name=_DEFAULTS['font_name'],
                        font_name_str=_DEFAULTS['font_name'],
                        font_script=False,
                        font_size=_DEFAULTS['font_size'],
                        font_size_str=_DEFAULTS['font_size'],
                        font_super_test=True,
                        italic=_DEFAULTS['italic'],
                        left=_DEFAULTS['border'],
                        left_color=_DEFAULTS['border_color'],
                        num_format=_DEFAULTS['num_format'],
                        num_format_count=_DEFAULTS['num_format_count'],
                        num_format_default=_DEFAULTS['num_format_default'],
                        num_format_pct=_DEFAULTS['num_format_pct'],
                        num_format_stat=_DEFAULTS['num_format_stat'],
                        right=_DEFAULTS['border'],
                        right_color=_DEFAULTS['border_color'],
                        text_v_align=_DEFAULTS['align_vcenter'],
                        text_h_align=_DEFAULTS['align_center'],
                        text_v_align_base=_DEFAULTS['align_vcenter'],
                        text_h_align_base=_DEFAULTS['align_center'],
                        text_v_align_base_text=_DEFAULTS['align_vcenter'],
                        text_h_align_base_text=_DEFAULTS['align_right'],
                        text_v_align_label=_DEFAULTS['align_vcenter'],
                        text_h_align_label=_DEFAULTS['align_left'],
                        text_v_align_net=_DEFAULTS['align_vcenter'],
                        text_h_align_net=_DEFAULTS['align_center'],
                        text_v_align_net_text=_DEFAULTS['align_vcenter'],
                        text_h_align_net_text=_DEFAULTS['align_right'],
                        text_v_align_stat=_DEFAULTS['align_vcenter'],
                        text_h_align_stat=_DEFAULTS['align_center'],
                        text_v_align_stat_text=_DEFAULTS['align_vcenter'],
                        text_h_align_stat_text=_DEFAULTS['align_right'],
                        text_v_align_stattest=_DEFAULTS['align_vcenter'],
                        text_h_align_stattest=_DEFAULTS['align_center'],
                        text_v_align_stattest_text=_DEFAULTS['align_vcenter'],
                        text_h_align_stattest_text=_DEFAULTS['align_right'],
                        text_v_align_sum=_DEFAULTS['align_vcenter'],
                        text_h_align_sum=_DEFAULTS['align_center'],
                        text_v_align_sum_text=_DEFAULTS['align_vcenter'],
                        text_h_align_sum_text=_DEFAULTS['align_right'],
                        text_v_align_test=_DEFAULTS['align_vcenter'],
                        text_h_align_test=_DEFAULTS['align_center'],
                        text_v_align_test_text=_DEFAULTS['align_vcenter'],
                        text_h_align_test_text=_DEFAULTS['align_right'],
                        text_v_align_ubase=_DEFAULTS['align_vcenter'],
                        text_h_align_ubase=_DEFAULTS['align_center'],
                        text_v_align_ubase_text=_DEFAULTS['align_vcenter'],
                        text_h_align_ubase_text=_DEFAULTS['align_right'],
                        text_v_align_y=_DEFAULTS['align_vcenter'],
                        text_h_align_y=_DEFAULTS['align_center'],
                        text_wrap=_DEFAULTS['text_wrap'],
                        top=_DEFAULTS['border'],
                        top_color=_DEFAULTS['border_color'])

_DEFAULT_ATTRIBUTES = dict([item for item in (_DEFAULT_CELL.items() + _DEFAULT_GENERAL.items())])