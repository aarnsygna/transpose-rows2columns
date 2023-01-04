import pandas as pd

# None_RCC_17-635-28_N1_30um_S1_20200920_pixel_intensities copy.csv
csv_filename = input("Enter .csv file to read: ")

#csv_df = pd.read_csv(filepath_or_buffer=csv_filename).transpose()
csv_df = pd.read_csv(filepath_or_buffer=csv_filename,
                     sep=",", header=2,
                     index_col=0
                     ).transpose()


print(csv_df.head())
