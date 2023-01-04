import pandas as pd

# None_RCC_17-635-28_N1_30um_S1_20200920_pixel_intensities copy.csv
# Assigning csv variable name
csv_filename = input("Enter .csv file to read: ")
# Assigning header number as an int.. 2 is recommended for metaspace
column_header = int(
    input("Which column number will be your header?(from 0,1,2...): ")
    )

# Pandas to read assigned csv, header assigned, and index set to 0th column.
# Pandas tranpose feature called.
csv_df = pd.read_csv(filepath_or_buffer=csv_filename,
                     sep=",", header=column_header,
                     index_col=0
                     ).transpose().reset_index(names="mol_formula")

print(csv_df.head())

# Target function achieved of app, can now write out dataframe to .csv
csv_df.to_csv(path_or_buf= ("transposed_" +csv_filename))
