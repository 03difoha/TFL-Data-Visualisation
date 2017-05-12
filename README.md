# TFL-Data-Visualisation
Visualising Car Park data with MatPlotLib

This ongoing project intends to use MatPlotLib to visualise car park data available from the TFL API.

The number of free car park spaces at avaiable locations was recorded each hour over the period of a month and stored on firebase.

The code supplied will allow you to record your own data, and also display it via a Flask web app + MatPlotLib.

The current version can be found here http://03difoha.pythonanywhere.com/


Known Bugs:
As some car parks do not have disabled parking, if you loop through the list containing the space 'type' you will receive a Nontype error. Future solution: use Jquery to hide the disabled option of the dropdown when you select a car park without disabled bays.

