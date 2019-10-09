import numpy as np
from django.shortcuts import render, render_to_response
from django.http import HttpResponse
from bokeh.plotting import figure
from bokeh.embed import components
from bokeh.models import HoverTool

x = [1200, 1300, 1400, 1500]
y0 = [200, 205, 207, 201]
y1 = [190, 195, 200, 198]

def starter(request):
    plot = figure(x_axis_label='Time', y_axis_label='Water temperature', title="Water temperature for incoming and outgoing water")
    plot.circle(x, y0, size=10, color="olive", legend="Outgoing water temp")
    plot.circle(x, y1, size=10, color="navy", legend="Incoming water temp")
    plot.line(x, y1, line_color="navy")
    plot.line(x, y0, line_color="olive")
    script, div = components(plot)
    return render(request, 'starter.html', {'script':script, 'div':div})
