import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
     # Get user input for city (chicago, new york city, washington).
    while True:
        city = input('\nWould you like to analyze Chicago, New york city or Washington?\n').lower()
        if city in ['chicago', 'new york city', 'washington']:
            break
        else:
            print('\n Wrong city, please try again.\n')


    # Get user input for month (all, january, february, ... , june).
    while True:
        month = input('\nInput the month you would like to filter the data (January-June). If you want them all, type "All"\n').title()
        if month in ['January','February','March','April','May','June','All']:
            break
        else:
            print('\nInput a month between January and June, or type "All"\n')

    # Get user input for day of week (all, monday, tuesday, ... sunday).
    while True:
        day = input('\nIntroduce the day of the week to be analyzed, type "All" if you want to analyze them all\n').title()
        if day in ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday','All']:
            break
        else:
            print('\nInput a valid day of the week or "All"\n')

    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

     # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    df['hour'] = df['Start Time'].dt.hour

    # filter by month if applicable
    if month != 'All':
        # use the index of the months list to get the corresponding int
        months = ['January', 'February', 'March', 'April', 'May', 'June']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'All':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # Display the most common month
    most_common_month = df['month'].mode()[0]
    print('\n Most common month is {}'.format(most_common_month))

    # Display the most common day of week
    most_common_day = df['day_of_week'].mode()[0]
    print('\n Most common day of the week is {}'.format(most_common_day))

    # Display the most common start hour
    most_common_hour = df['hour'].mode()[0]
    print('\n Most common start hour is {}'.format(most_common_hour))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # Display most commonly used start station
    common_start_station = df['Start Station'].value_counts().idxmax()
    print('\nMost common start station is {}'.format(common_start_station))

    # Display most commonly used end station
    common_end_station = df['End Station'].value_counts().idxmax()
    print('\nThe most common end station is {}'.format(common_end_station))

    # Display most frequent combination of start station and end station trip
    frequent_station_combination = df.groupby(['Start Station','End Station']).size().idxmax()
    print('\n Most common station combination is {}'.format(frequent_station_combination))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # Display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print('\nTotal travel time is {}'.format(total_travel_time))

    # Display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print('\nMean travel time is {}'.format(mean_travel_time))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users depending on their gender, year of birth and times used."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    count_user_types = df['User Type'].value_counts()
    print('\nCount of user types is {}'.format(count_user_types))

    # Display counts of gender (an error pops up if i´m working with the washington file, so I applied the following code)
    try:
        count_gender = df['Gender'].value_counts()
        print('\nCount of gender is {}'.format(count_gender))
    except KeyError:
        print('\nNot possible to display that information in this city.')

    # Display earliest, most recent, and most common year of birth (an error pops up if i´m working with the washington file, so I applied the following code
    try:
        earliest_year_birth = df['Birth Year'].min()
        most_recent_year_birth = df['Birth Year'].max()
        most_common_year_birth = df['Birth Year'].value_counts().idxmax()
        print("\nThe earliest year of birth is {}".format(earliest_year_birth))
        print("\nMost recent year of birth is {}".format(most_recent_year_birth))
        print("\nMost common year of birth is {}".format(most_common_year_birth))
    except KeyError:
        print('\nNot possible to display that information in this city.')


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def display_raw_data(df):
    """ Shows raw data in rows of five if user types 'yes'."""
    start_loc = 0
    view_raw_data = input('\nWould you like to see 5 rows of raw data? Please enter "yes" or "no".\n')
    while view_raw_data == 'yes':
        print(df.iloc[start_loc:start_loc+5])
        start_loc += 5
        view_keep_display = input('Do you want to keep displaying the raw data: ').lower()
        view_raw_data=view_keep_display


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_raw_data(df)
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
