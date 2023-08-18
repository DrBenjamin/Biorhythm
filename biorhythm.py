import streamlit as st
import datetime
import matplotlib
from matplotlib.pyplot import *
from matplotlib.figure import Figure
import matplotlib.ticker as mtick
import numpy as np # to work with numerical data efficiently




#### Main
st.title("Biorhythm")
st.subheader("Enter your birthday")
birthday = st.date_input(" ", datetime.date(1979,7,2), datetime.date(1923, 1, 1), datetime.date.today())
now = datetime.date.today()
delta = now - birthday
st.write("Your birthday is ", birthday.strftime('%d.%m.%Y'))
st.write("You are ", str(delta.days), " days old")


## Calculate biorhythm
physical = np.sin(2 * np.pi * delta.days / 23)
emotional = np.sin(2 * np.pi * delta.days / 28)
mental = np.sin(2 * np.pi * delta.days / 33)
st.write("Your physical biorhythm is at ", "{:.2%}".format(physical), " today")
st.write("Your emotional biorhythm is ", "{:.2%}".format(emotional), " today")
st.write("Your mental biorhythm is ", "{:.2%}".format(mental), " today")
t0 = birthday.toordinal()
t1 = datetime.datetime.today().toordinal()

# Range of 20 days
t = np.array(range((t1 - 10), (t1 + 10)))
y = 100 * [np.sin(2 * np.pi * (t - t0) / 23), np.sin(2 * np.pi * (t - t0) / 28), np.sin(2 * np.pi * (t - t0) / 33)]


## Matplotlib stuff
# Converting ordinals to date
label = []
for p in t:
    label.append(datetime.date.fromordinal(p))

fig = figure()
ax = fig.gca()
title('Biorhythm') 
ylim(-1, 1)
plot(label, y[0], label, y[1], label, y[2])
xlabel(now.strftime('%B %Y'))   
ylabel('Percentage')

# adding a legend
legend(['Physical', 'Emotional', 'Intellectual'])

# formatting the dates on the x axis
ax.xaxis.set_major_formatter(matplotlib.dates.DateFormatter('%d.'))
ax.yaxis.set_major_formatter(mtick.PercentFormatter(xmax = 1.0))

# Plotting
st.pyplot(fig)