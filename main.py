import os
import pandas as pd


def process_files():
    # Path to the dataset
    base_path='D:\TUDO\SensorData\Dataset'
    # Get list of folders in basepath
    files_path = [x for x in os.listdir(base_path)]

    # Iterate through each folder
    for p in range (len(files_path)):
        print(files_path[p].replace("\SensorData", "\SensorData\Dataset"))
        # Extract subfolders within each folder
        sub_files_path= [x for x in os.listdir(base_path+"\\"+files_path[p])]
        print(sub_files_path)
        files_df=[]
        # Iterate through all subfolders within each folder
        for q in range(len(sub_files_path)):
            # Extract files within each subfolder
            sub_sub_files_path = [x for x in os.listdir(base_path+"\\"+files_path[p]+"\\"+sub_files_path[q])]

            # Loop through the files and push them into array of dataframes
            for r in range(len(sub_sub_files_path)):
                print(p,q,r,base_path + "\\" + files_path[p] + "\\" + sub_files_path[q] + "\\" + sub_sub_files_path[r] )
                compiled_path=base_path + "\\" + files_path[p] + "\\" + sub_files_path[q] + "\\" + sub_sub_files_path[r]
                file_data = pd.read_csv(compiled_path,sep='\t',skiprows=1, )

                # Renaming columns
                new_columns = list(file_data.columns)
                for i in range(len(new_columns)):
                    if new_columns[i] != 'SysTime':
                        new_columns[i] = new_columns[i]+"_ts"+str(r+1)
                file_data.columns = new_columns

                files_df.append(file_data)

            print(files_df[0])
            # Concatenate dfs into one df based on the SysTime Variable
            merged_df = files_df[0]
            for i in range(len(files_df) - 1):
                merged_df = pd.merge(merged_df, files_df[i + 1], on="SysTime")

            merged_df = merged_df[merged_df != 0].dropna() #dropping rows with missing values
            print(base_path.replace('Dataset','output')+'\\'+files_path[p]+'_'+sub_files_path[q]+'.csv')
            # Export the DF into a file
            merged_df.to_csv(base_path.replace('Dataset','output')+'\\'+files_path[p]+'_'+sub_files_path[q]+'.csv', index=False, sep=';',)


process_files()