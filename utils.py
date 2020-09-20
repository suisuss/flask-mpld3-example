import numpy as np
import mpld3
import matplotlib.pyplot as plt
import random

def draw_fig1(x, y, fig_type=None, pie_labels=None, pie_fracs=None):
    if fig_type:
        fig, ax = plt.subplots()
        if fig_type == "line":
            ax.plot(x, y)
        elif fig_type == "bar":
            ax.bar(x, y)
        elif fig_type == "pie":
            ax.pie(pie_fracs, labels=pie_labels)
        elif fig_type == "scatter":
            ax.scatter(x, y)
        elif fig_type == "hist":
            ax.hist(y, 10, density=1)
        elif fig_type == "area":
            ax.plot(x, y)
            ax.fill_between(x, 0, y, alpha=0.2)
        return mpld3.fig_to_html(fig)
    else:
        return None

def draw_fig2(x, y, fig_types=None, pie_labels=None, pie_fracs=None):
    fig_types = list(filter(None, fig_types))
    if fig_types:
        fig = plt.figure()
        for i, fig_type in enumerate(fig_types): 
            axi = fig.add_subplot(2, 2, i + 1)
            if fig_type == "line":
                axi.plot(x, y)
            elif fig_type == "bar":
                axi.bar(x, y)
            elif fig_type == "pie":
                axi.pie(pie_fracs, labels=pie_labels)
            elif fig_type == "scatter":
                axi.scatter(x, y)
            elif fig_type == "hist":
                axi.hist(y, 10, density=1)
            elif fig_type == "area":
                axi.plot(x, y)
                axi.fill_between(x, 0, y, alpha=0.2)
        return mpld3.fig_to_html(fig)
    else:
        return None


def draw_fig3(x, y, fig_size=None, fig_types=None, pie_labels=None, pie_fracs=None):
    fig_types = list(filter(None, fig_types))
    if fig_types:
        fig = plt.figure()
        for i, fig_type in enumerate(fig_types): 
            axi = fig.add_subplot(2, 2, i + 1)
            if fig_type == "line":
                axi.plot(x, y)
            elif fig_type == "bar":
                axi.bar(x, y)
            elif fig_type == "pie":
                axi.pie(pie_fracs, labels=pie_labels)
            elif fig_type == "scatter":
                axi.scatter(x, y)
            elif fig_type == "hist":
                axi.hist(y, 10, density=1)
            elif fig_type == "area":
                axi.plot(x, y)
                axi.fill_between(x, 0, y, alpha=0.2)
        return mpld3.fig_to_html(fig)
    else:
        return None