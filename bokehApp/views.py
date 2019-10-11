import numpy as np
from django.shortcuts import render, render_to_response
from django.http import HttpResponse
from bokeh.models import BoxAnnotation
from bokeh.plotting import figure
from bokeh.embed import components
from bokeh.models import HoverTool

x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24]
y1 = [180, 184, 185, 184, 182, 185, 187, 189, 195, 198, 199, 196, 194, 192, 189, 189, 185, 189, 190, 188, 188, 186, 184, 185]
y0 = [175, 176, 180, 179, 180, 175, 176, 175, 177, 176, 175, 172, 175, 174, 177, 173, 174, 175, 173, 170, 174, 173, 176, 174]

def starter(request):
    plot = figure(x_range=(1, 24), y_range=(100, 225), x_axis_label='Time', y_axis_label='Water temperature', title="Water temperature over the last 48 hours")
    plot.line(x, y1, line_color="maroon", line_width=2, legend="Incoming water temp")
    plot.line(x, y0, line_color="navy", line_width=2, legend="Outgoing water temp")
    plot.legend.location = "bottom_right"
    plot.legend.background_fill_color = "gray"
    plot.legend.background_fill_alpha = 0.5
    plot.add_layout(BoxAnnotation(bottom=197, fill_alpha=0.1, fill_color='red', line_color='red'))
    script, div = components(plot)
    return render(request, 'starter.html', {'script':script, 'div':div})
