# Requirements

## Functional Requirements:

**Must:**

As a researcher, I want to be able to look at specific time periods in the data without much hassle.

As a researcher, I want to generate a plot of temperature, precipitation, and sunshine over time so that I can see how they correlate.

As a researcher, I want to plot/print the temperature, precipitation, and sunshine duration of a federal state in a certain time frame so that I can better understand the correlations between these weather phenomenons. 

As a researcher, I want to plot/print the yearly mean temperature, precipitation, or sunshine duration of different federal states so that I can have a more general understanding of the differences in climate between them.

As a researcher, I want to be able to save resulting plots and images so that I can easily use them in, for example, research papers. 

As an expert researcher, I want to be able to customize a lot so that the result fits my specific research question.

As a researcher, I want to be able to view patterns in the weather conditions such as reoccurring events and their frequency.


**Should**:

As a researcher, I want to receive results as a text (file) so that I can easily copy (import) it to other systems.

As a climate researcher, I want to automatically download data from the German Meteorological Service so that I do not waste time doing this by hand.

As a researcher from the US, I want to be able to get values in the United States customary system so that I intuitively know their significance.

As an expert climate researcher, I want to make a forecast of the temperature / precipitation / sunshine duration so that I know what the weather will be linke in the future.

As a researcher, I want to plot/print the temperature, precipitation, or sunshine duration of different federal states in a certain time frame so that I can be better compare them and understand their differences. 


**Could**:

As a vertical farming startup founder, I want to know in what region I will get the most consistent rain throughout the year so that I can reuse rain water and use solar energy to make the production more resource efficient.

As a researcher, I want to generate a plot of the German map with the average measures for different places so that I have a nice plot for my next presentation.

As an expert climate researcher, I want to plot the ordered temperature, precipitation, or sunshine values with a logarithmic scale, so that I can check if Zipf's Law holds for the given data set too.


**Won't:**


## Non-Functional Requirements:

The system should run on Linux and MacOs.

The system should run on Python 3.10.

The system should have a command-line interface.

The project should come with a computational narrative. 

The system should respond in less than 2 seconds.

The system should be *fault-tolerant*, e.g. it should be able to replace missing values in data sets to avoid errors or wrong calculations.

The system should be *user-friendly* to researchers with basic knowledge of the command line.

The system should have a *detailed explanation* of its functionality so that beginner researchers can use it.

The system should be *secure*, meaning it should not delete or override data which is not explicitly ordered by the user.

The system should be *maintainable*. It should be relatively easy to add or remove features later on.