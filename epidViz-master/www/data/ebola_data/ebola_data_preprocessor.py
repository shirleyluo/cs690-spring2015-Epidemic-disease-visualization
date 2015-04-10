import sys
import os
import pandas as pd

class Ebola_data_preprocessor(object):
    def __init__(self, folder):
        self.folder = folder


    def extract_csv(self):
        files = [os.path.join(os.path.abspath(self.folder), f) for f in os.listdir(self.folder) if f.endswith('csv') if os.path.isfile(os.path.join(os.path.abspath(self.folder), f))]
        output_csv = 'latest_ebola_data.csv'
        for i, f in enumerate(files):
            df = pd.read_csv(f)
            df.drop(['Ebola measure', 'Indicator type', 'Display Value', 'Low', 'High', 'Comments'], inplace=True, axis=1)
            df = df[df['Epi week'] == '02 to 08 March 2015']
            df = df[df['Case definition'] == 'Confirmed']
            df = df[df['Ebola data source'] == 'Situation report']
            df = df[df['Numeric'] != 0]

            if i == 0:
                df.to_csv(output_csv, mode='w', index=False, header=True)
            else:
                df.to_csv(output_csv, mode='a', index=False, header=False)


if __name__ =='__main__':
    folder = sys.argv[1]
    viz_data = Ebola_data_preprocessor(folder)
    viz_data.extract_csv()


