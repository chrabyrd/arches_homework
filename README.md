This is a template project for the Farallon Arches new hire homework assignment.  

In this exercise you will deploy Arches software in an environment of your choosing, upload this "project and package" into the software, and then build a custom [Arches function](https://arches.readthedocs.io/en/stable/functions-widgets-datatypes/?highlight=functions#functions) that saves spatial information denoting a place or address into a field within a simple Arches resource model.

As part of this homework, please do the following:

1. Fork this repo into your own github account
2. Install all relevant [dependencies](https://arches.readthedocs.io/en/stable/requirements-and-dependencies/) in your own environment
3. Clone the master branch of [Arches](https://github.com/archesproject/arches)
4. Use pip to install Arches from your [git clone](https://arches.readthedocs.io/en/stable/creating-a-development-environment/#creating-a-development-environment). Note: you do not need to create your own a project and package.
5. Clone this project and load the arches package within it (arches_homework/pkg) using the load_package command
6. Write a custom function that populates spatial data (a geojson feature collection) into the geometry node of the provided resource model

Resources:
Arches documentation: https://arches.readthedocs.io/en/stable/
Mapbox geocoding service: https://docs.mapbox.com/api/search/

Expectations:
We expect this exercise to take 4 to 8 hours. We understand that this is not a simple task, so if you find yourself spinning wheels, it's ok. We are here to help. Becuase Farallon developers function as a unit, we are just as interested in your ability to manage time and reach out for help in a productive manner as we are in assessing your coding chops.  
