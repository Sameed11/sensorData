The code follows the following algorithm to get values from all the sensors and synchronise them into a single CSV file

```
Extract all the folders within the mentioned basePath
    for each folder:
        extract all the subfolders
            for each subfolder:
                extract all files and convert it into CSV
                merge all CSVs into one based on SysTime
                Write the final CSV back into the outputFile
```
,..