import pandas as pd
import csv
from io import StringIO
import time

def main():

    path = './../../SourceData/samplearrays.csv'
    seed = './arrayseed.csv'

    loc_count = 0
    cat_count = 0
    csv_count = 0

    ave_loc = 0
    ave_csv = 0
    ave_cat = 0

    data = []
    df_loc = pd.read_csv(seed)
    df_cat = pd.read_csv(seed)
    df_csv = pd.read_csv(seed)


    # Oped the file, read the entries into the data list, then close the file.
    # Any use of the source data will be from the data object for time consistency

    with open(path, "r") as file:
        reader = csv.reader(file)

        for row in reader:
            data.append(row)
        file.close()


    # build the dataframe from source data, using .loc method
    tic = time.perf_counter()
    for row in data:
        df_loc.loc[len(df_loc)] = row
        loc_count += 1
    toc = time.perf_counter()
    loc_elapsed = toc - tic
    ave_loc = loc_elapsed / loc_count


    # build the dataframe from source data, using .loc method
    tic = time.perf_counter()
    for row in data:
        df_cat = pd.concat([df_cat, pd.DataFrame([row])], ignore_index=True)
        cat_count += 1
    toc = time.perf_counter()
    cat_elapsed = toc - tic
    ave_cat = cat_elapsed / cat_count


    # build the dataframe from the source, using
    output = StringIO()
    df_csv.to_csv(output)
    csv_writer = csv.writer(output)
    tic = time.perf_counter()
    for row in data:
        csv_writer.writerow(row)
    output.seek(0) # we need to get back to the start of the StringIO
    df_csv = pd.read_csv(output, index_col=0)
    toc = time.perf_counter()
    csv_count = len(df_csv) -1
    csv_elapsed = toc - tic
    ave_csv = csv_elapsed / csv_count


    if (csv_count == loc_count == cat_count):
        with open ("time.txt", 'a') as write:
            write.writelines(f"Run On {time.strftime("%y.%m.%d %H:%M:%S", time.gmtime())} \n Lines = {str(loc_count)} \n loc() duration = {str(loc_elapsed)} \n loc() = {str(ave_loc)} \n cat() duration = {str(cat_elapsed)} \n cat() = {str(ave_cat)} \n csv duration = {str(csv_elapsed)} \n csv = {str(ave_csv)} \n \n")
    else:
        print("Count Error!")
        print("loc_count = " + str(loc_count))
        print("cat_count = " + str(cat_count))
        print("csv_count = " + str(csv_count))


        # tic = time.perf_counter()

        # FUNCTION

        # toc = time.perf_counter()
        # elapsed = toc - tic



if __name__ == "__main__":
    main()
