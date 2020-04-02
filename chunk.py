import pandas as pd

chunk_size = 5000
batch_no = 0

for f in pd.read_csv('IMDb movies.csv', chunksize=chunk_size):
    f.to_csv('IMDb movies.csv' + str(batch_no) + '.csv', index=False)
    batch_no += 1
