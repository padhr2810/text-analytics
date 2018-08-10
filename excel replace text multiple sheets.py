"""
Pre-processing an Excel file containing text data. In this instance, we want to replace text 
(e.g. old_string with new_string) in an Excel file with multiple worksheets, and then save the data 
as a new Excel file with identical worksheet names.
"""

import pandas as pd

# Specify the changes you wish to make
# Dictionary Key = original text
# Dictionary Value = new text
change_dict = {'old_text': 'new',
    'worse': 'better'}
	

# Specify the file you wish to modify
file = 'old.xlsx'

# Load the Excel file
xl = pd.ExcelFile(file)

# Print the sheet names
print(xl.sheet_names)

# Specify the Excel file you wish to write to
writer = pd.ExcelWriter('new_from_df.xlsx')

# Loop through each work sheet in the original Excel file
# Replace (based on the dict)
# Write to the new Excel file
for sheet in xl.sheet_names:
    temp_df  = xl.parse(sheet, header=None)
    temp_df.replace(change_dict, value = None, inplace = True, regex=True)
    temp_df.to_excel(writer,sheet, index=None, header=None)

# Save the new Excel file
writer.save()


