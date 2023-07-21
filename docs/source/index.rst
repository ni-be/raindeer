.. Raindeer documentation master file, created by
   sphinx-quickstart on Fri Jul 21 00:11:05 2023.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to Raindeer's documentation!
====================================

.. toctree::
   :maxdepth: 2
   :caption: Contents:
   
   modules

Raindeer
========

Analysis of weather data in Germany. 

This project is done as part of the *Research Software Engineering* course 
group project in summer 2023. 

.. contents:: Table of Contents
   :depth: 3

Problem Description
-------------------

Research Questions
~~~~~~~~~~~~~~~~~~

This project was created on the basis of answering the following research questions:

1) What is the temperature trend in germany?
2) Are there correlations between different weather parameters?
3) What will the average temperature be next year in germany?
4) Are there patterns in the weather data?
5) How can we make the weather data from the online database usable?

From these, multiple user stories were created:

User-Stories
~~~~~~~~~~~~

1. As a researcher, I want to generate a plot of temperature, precipitation, and sunshine over time so that I can see how they correlate.
2. As a researcher, I want to plot the temperature, precipitation, and sunshine duration of a federal state in a certain time frame so that I can better understand the correlations between these weather phenomenons.
3. As a researcher, I want to plot the yearly mean temperature, precipitation, or sunshine duration of different federal states so that I can have a more general understanding of the differences in climate between them.
4. As a researcher, I want to be able to save resulting plots and images so that I can easily use them in, for example, research papers.
5. As an expert researcher, I want to be able to customize a lot so that the result fits my specific research question.
6. As a researcher, I want to be able to view patterns in the weather conditions such as reoccurring events and their frequency.
7. As a climate researcher, I want to automatically download data from the German Meteorological Service so that I do not waste time doing this by hand.
8. As an expert climate researcher, I want to make a forecast of the temperature / precipitation / sunshine duration so that I know what the weather will be like in the future.
9. ...

`Here <https://gitup.uni-potsdam.de/jubruns/raindeer/-/blob/main/docs/requirements.md>`_ you can find a full list of all user stories. Some of which are not yet implemented.

How to Get Started
-------------------

After downloading this package, install it by running the following command in its root directory:

.. code-block:: bash

   $ pip install -e .

Running the Program
-------------------

The programm has two interfaces / access points. You can access some functionality through the `command-line interface <#command-line-interface>`_.
In addition, you can directly access the modules through importing it, e.g. to a Jupyter Notebook. 

Configuration and QoL
----------------------

There is a `config.yaml` file in the root directory of the project.
You can access each list using `utilities:yaml_reader(OPTION)`.

`More information <#yaml_reader>`_

Jupyter Notebook
----------------

Start the jupyter notebook from the command-line with 

.. code-block:: bash

   $ jupyter notebook

This will open a homepage in your browser containing all files in your current working directory. From here, select ``raindeer.ipynb`` and open it. Inside the notebook is the computational narrative for this software. It explains all the modules and use-cases as well as answering some interesting research questions using the data.

Authors
-------

- Nikolas Bertrand (backend developer)
- Julian Bruns (backend developer)
- Josephine Funken (backend developer / tester)
- Timo Wedding (backend developer / “client” developer)


How to get involved
-------------------

- `Contributing <https://gitup.uni-potsdam.de/jubruns/raindeer/-/blob/main/CONTRIBUTING.md>`_
- `Code of Conduct <https://gitup.uni-potsdam.de/jubruns/raindeer/-/blob/main/CONDUCT.md#contributor-covenant-code-of-conduct>`_
- `License <https://gitup.uni-potsdam.de/jubruns/raindeer/-/blob/main/LICENSE.txt>`_
- `Citation <https://gitup.uni-potsdam.de/jubruns/raindeer/-/blob/main/CITATION.cff>`_   

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
