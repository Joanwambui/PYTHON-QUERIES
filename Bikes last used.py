import pandas as pd

result = dc_bikeshare_q1_2012.groupby('bike_number')['end_time'].max().to_frame( 'last_used').reset_index().sort_values(by='last_used', ascending=False)

# Import your libraries
import pandas as pd

# Start writing code
dc_bikeshare_q1_2012.head()

# Group by 'bike_number' and find the last 'end_time' for each bike
dc_bikeshare_q1_2012['last_used'] = dc_bikeshare_q1_2012.groupby('bike_number')['end_time'].transform('max')

# Order the results by 'last_used' in descending order
dc_bikeshare_q1_2012_sorted = dc_bikeshare_q1_2012.sort_values(by='last_used', ascending=False)

# Display the relevant columns for debugging
print(dc_bikeshare_q1_2012_sorted[['bike_number', 'last_used']])

