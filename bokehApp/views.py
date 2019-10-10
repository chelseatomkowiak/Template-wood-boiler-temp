import numpy as np
from django.shortcuts import render, render_to_response
from django.http import HttpResponse
from bokeh.models import BoxAnnotation
from bokeh.plotting import figure
from bokeh.embed import components
from bokeh.models import HoverTool

x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18]
y0 = [200, 205, 207, 201, 199, 198, 197, 200, 199, 203, 196, 196, 200, 204, 206, 208, 208, 209]
y1 = [194, 195, 200, 198, 197, 196, 199, 197, 199, 196, 197, 199, 200, 203, 204, 205, 203, 206]

def starter(request):
    plot = figure(x_axis_label='Time', y_axis_label='Water temperature', title="Water temperature over the last 48 hours")
#    plot.circle(x, y0, size=10, color="navy", legend="Outgoing water temp")
#    plot.circle(x, y1, size=10, color="maroon", legend="Incoming water temp")
    plot.line(x, y1, line_color="maroon", line_width=2, legend="Incoming water temp")
    plot.line(x, y0, line_color="navy", line_width=2, legend="Outgoing water temp")
    plot.legend.location = "bottom_right"
    plot.legend.background_fill_color = "gray"
    plot.legend.background_fill_alpha = 0.5
    plot.add_layout(BoxAnnotation(bottom=208, fill_alpha=0.1, fill_color='red', line_color='red'))
    plot.add_layout(BoxAnnotation(top=194, fill_alpha=0.1, fill_color='red', line_color='red'))
    script, div = components(plot)
    return render(request, 'starter.html', {'script':script, 'div':div})
