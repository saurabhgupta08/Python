# Importing the required modules
import webbrowser
import time
import requests
import pandas as pd

# Defining the url address
url = "https://www.gturesults.in/Default.aspx?ext=W2022&rof=3653"

# Opening the browser in the given url address
webbrowser.open(url)

# Waiting for the web page to load
time.sleep(10)

# Filling the details in the web page
# Assuming the details are in a dictionary called data
data = {"Enroll No.": "210200111013",}
# Looping through the data and entering it in the corresponding input fields
# Assuming the input fields have ids that match the keys of the data dictionary
for key, value in data.items():
    # Finding the input field by id
    input_field = webbrowser.find_element_by_id(key)
    # Clearing any existing text in the input field
    input_field.clear()
    # Sending the value to the input field
    input_field.send_keys(value)

# Submitting the form
# Assuming the submit button has an id of "submit"
submit_button = webbrowser.find_element_by_id("Search")
submit_button.click()

# Waiting for the next web page to load
time.sleep(10)

# Copying the details from the web site to excel sheet
# Assuming the details are in a table with an id of "details"
details_table = webbrowser.find_element_by_id("details")
# Getting the html source of the table
details_html = details_table.get_attribute("outerHTML")
# Converting the html to a pandas dataframe
details_df = pd.read_html(details_html)[0]
# Saving the dataframe to an excel sheet
details_df.to_excel("details.xlsx", index=False)
