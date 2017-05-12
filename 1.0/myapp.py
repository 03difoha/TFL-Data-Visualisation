from __future__ import division
import datetime
import settings
from flask import Flask
from flask import request
from flask import render_template
import mpld3
import numpy as np
import matplotlib.pyplot as plt


app = Flask(__name__)


@app.route('/')
def my_form():
    return render_template("template.html")


@app.route('/', methods=['POST', 'GET'])
def my_form_post():
    requestParams = []
    location = request.form.get('location','')
    requestParams.append(location)
    #sType = request.form.get('sType', '')
    #requestParams.append(sType)
    day = request.form.get('day','')
    requestParams.append(day)

    hour = []
    daysAvs = []

    carParkData = (settings.db.child("Car Parks").child(requestParams[0] + " (LUL)").child("Pay and Display Parking").child(
            requestParams[1]).get().val())


    for i in carParkData:
        for key, value in i.iteritems():
            hour.append(value)
        hAv = sum(hour) / len(hour)
        daysAvs.append(int(hAv))
        print daysAvs
        hour[:] = []


    colours = []

    maxCap = max(daysAvs)

    for i in daysAvs:
        p = float((i / maxCap) * 100)
        if p > 90:
            colours.append('#EE7785')
        elif p < 90 and p > 60:
            colours.append('#D68975')
        elif p < 60 and p > 30:
            colours.append('#FCD0A1')
        elif p < 30 and p > 10:
            colours.append("#67D5B5")
        elif p < 10 and p > 5:
            colours.append('#67D5B5')


    N = 24

    ind = np.arange(N)  # the x locations for the groups
    width = 1  # the width of the bars

    fig, ax = plt.subplots()
    rects = ax.bar(ind, daysAvs, width, color=colours)


    # add some text for labels, title and axes ticks
    ax.set_ylabel('Empty Car Park Spaces')
    ax.set_xlabel('Hour of the Day')
    ax.set_title('Average Car park use of ' + requestParams[0] + ' on ' + requestParams[1])
    plt.tick_params(
        axis='x',
        which='both',
        bottom='on',
        top='off',
        labelbottom='on')
    plt.axis('tight')


    times = []

    for i in range(10):
        times.append('0' + str(i) + ':00')

    for i in range(10, 24):
        times.append(str(i) + ':00')

    print (times)


    # plt.text(0.0, -2.0, '00:00', rotation=-45)
    # axis label example
    chart = mpld3.fig_to_html(fig)

    return render_template("template.html", chart=chart)


if __name__ == '__main__':
    app.debug = True
    app.run()

