"""
Purpose: Explore and experiment with Python's statistics module

Author: Solomon Stevens

Use statistics module to generate descriptive statistics about
made up data regarding the milage of a fully-charged electric car

All scripts in this repository use only the standard library.

@ uses statistics module for descriptive stats

"""
#Logger Setup
#
# import setup_logger function from instructor-generated module
from util_logger import setup_logger
#
# setup the logger using the current file name (a built-in variable)
logger, logname = setup_logger(__file__)
#

#Import statistics module
import statistics

#Insert "data"
#-> According to Google, the average distance an electric car can go
#   is between 100 and 400 miles on a full charge. So to accumulate
#   this "data", I asked for random numbers between 100 and 400.
miles_per_charge = [345, 371, 138, 372, 288, 129, 182, 261, 380, 381, 
                    146, 391, 376, 240, 329, 141, 220, 360, 324, 370, 
                    284, 110, 337, 359, 396, 309, 304, 208, 279, 113, 
                    126, 319, 392, 184, 349, 369, 215, 199, 298, 305, 
                    148, 225, 214, 264, 397, 290]

#Run statistics on "data"
#-> Mean
avg = statistics.mean(miles_per_charge)
avg = round(avg, 2)

#-> Median
med = statistics.median(miles_per_charge)
med = round(med, 2)

#-> Min
lowest = min(miles_per_charge)

#-> Max
highest = max(miles_per_charge)

#-> Range
range_ = highest - lowest

#-> Variance
vary = statistics.variance(miles_per_charge)
vary = round(vary, 2)


#Log findings
logger.info(f"The average cars got {avg} miles per full charge.")
logger.info(f"But the median of milage is {med} miles per full charge.")
logger.info(f"The best cars achieved {highest} miles per full charge.")
logger.info(f"The worst cars got only {lowest} miles per full charge.")
logger.info(f"This list of cars has a variance of {vary} miles per full charge.")