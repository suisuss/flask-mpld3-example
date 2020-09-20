from flask import Flask, render_template, request
import numpy as np
import mpld3
import matplotlib.pyplot as plt
import matplotlib
import random
from utils import draw_fig1, draw_fig2, draw_fig3

matplotlib.use('Agg')
plt.ioff()

matplotlib_config = {
  "lines.linewidth": 2.0,
  "axes.edgecolor": "#bcbcbc",
  "patch.linewidth": 0.5,
  "legend.fancybox": True,
  "axes.facecolor": "#eeeeee",
  "axes.labelsize": "large",
  "axes.grid": True,
  "grid.color":"white",
  "grid.linestyle":"solid",
  "patch.edgecolor": "#eeeeee",
  "axes.titlesize": "x-large"
}
matplotlib.rcParams.update(matplotlib_config)

app = Flask(__name__)

fig_type_options=[{'fig_type':'line'}, {'fig_type':'area'}, {'fig_type':'bar'}, {'fig_type':'pie'}]
fig_size_options=[{'fig_size':111 }, {'fig_size':222}, {'fig_size':333}]

@app.route('/', methods=['GET', 'POST'])
def flask_mpld3_example():
    return render_template('index.html')

@app.route('/one', methods=['GET', 'POST'])
def example_one():
    fig_type_selection = request.form.get('fig_type1')
    x = list(range(100))
    y = [a * 2 + random.randint(-20, 20) for a in x]

    pie_fracs = [20, 30, 40, 10]
    pie_labels = ["A", "B", "C", "D"]

    plot = draw_fig1(x, y, fig_type=fig_type_selection, pie_labels=pie_labels, pie_fracs=pie_fracs)
    return render_template('one.html', x=x, y=y, fig_type_options=fig_type_options, fig_type_selection=fig_type_selection, plot=plot)


@app.route('/two', methods=['GET', 'POST'])
def example_two():
    fig_types_selection = [request.form.get('fig_type1'), request.form.get('fig_type2'), request.form.get('fig_type3'), request.form.get('fig_type4')]
    x = list(range(100))
    y = [a * 2 + random.randint(-20, 20) for a in x]

    pie_fracs = [20, 30, 40, 10]
    pie_labels = ["A", "B", "C", "D"]

    plot = draw_fig2(x, y, fig_types=fig_types_selection)
    return render_template('two.html', fig_type_options=fig_type_options, fig_types_selection=fig_types_selection, x=x, y=y, plot=plot)



@app.route('/three', methods=['GET', 'POST'])
def example_three():
    fig_size =  request.form.get('fig_size')

    x = list(range(100))
    y = [a * 2 + random.randint(-20, 20) for a in x]

    pie_fracs = [20, 30, 40, 10]
    pie_labels = ["A", "B", "C", "D"]

    return render_template('three.html', x=x, y=y, fig_size_options=fig_size_options)


if __name__ == '__main__':
    app.run(debug=True)
