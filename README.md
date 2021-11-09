# Explore US Bikeshare Data
Made use of Python to explore data related to bike share systems for three major cities in the United States—Chicago, New York City, and Washington. Wrote code to import the data and search for insights by computing descriptive statistics.
###### 08/11/2021
![Bycicle sharing system in New York City](https://thecityfix.com/wp-content/uploads/2013/05/by-shinya_lr.jpg)

### Description
Bicycle-sharing systems puts at the disposal of a group of users a series of bicycles to be used temporarily as a means of transport. Nowadays, this alternative way of transport has become more common among citizens, and being able to find patterns and understand them has turned into an asset for managing public bycicle share systems.
Wrote Python code to import the chosen city CSV with data related to the bike share system. The script takes raw input from the user to create an interactive experience in the terminal to compute and present illustrative information.

### The Datasets
The data was provided by [Motivate](https://www.motivateco.com/), a bike share system provider for many major cities in the United States, to uncover bike share usage patterns.

Randomly selected data for the first six months of 2017 are provided for all three cities. All three of the data files contain the same core six (6) columns:

* Start Time (e.g., 2017-01-01 00:07:57)
* End Time (e.g., 2017-01-01 00:20:53)
* Trip Duration (in seconds - e.g., 776)
* Start Station (e.g., Broadway & Barry Ave)
* End Station (e.g., Sedgwick St & North Ave)
* User Type (Subscriber or Customer)

The Chicago and New York City files also have the following two columns:

* Gender
* Birth Year

![Data sample from New York City dataset](https://video.udacity-data.com/topher/2018/March/5aa771dc_nyc-data/nyc-data.png)

The original files are much larger and messier, and you don't need to download them, but they can be accessed here if you'd like to see them ([Chicago](https://www.divvybikes.com/system-data), [New York City](https://www.citibikenyc.com/system-data), [Washington](https://www.capitalbikeshare.com/system-data)). These files had more columns and they differed in format in many cases. Some data wrangling has been performed to condense these files to the above core six columns.

### Statistics Computed
* Popular times of travel
  * Most common month
  * Most common day of week
  * Most common hour of day

* Popular stations and trip
  * Most common start station
  * Most common end station
  * Most common trip from start to end

* Trip duration
  * Total travel time
  * Average travel time

* User info
  * Counts of each user type
  * Counts of each gender (only available for NYC and Chicago)
  * Earliest, most recent, most common year of birth (only available for NYC and Chicago)

### Software Needs
* You should have Python, NumPy and Pandas installed with [Anaconda](https://www.anaconda.com/products/individual#windows).
* A text editor, like Atom or Sublime Text.
* A terminal application (Terminal on Mac and Linux or Cygwin on Windows).

### Credits
Credits to [Full Stack Python](https://www.fullstackpython.com/) for the tips given and acknowledgement to the Udacity Knowledge Team for supporting and helping throughout the course.



