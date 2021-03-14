import csv

import pandas as pd

# # gathers all the genres into one list
# csv_file = open("movies.csv")
# read_csv = csv.reader(csv_file)
# lst_genres = []
# for row in read_csv:
#     genres = row[2]
#     lst = genres.split('|')
#     for i in lst:
#         if i not in lst_genres:
#             lst_genres.append(i)
# lst_genres.sort()
# print(lst_genres)

# # creates new csv file to format we desire where the genres are in their own column
# with open('movies_ordered.csv', 'w', newline='') as csvfile:
#     csv_writer = csv.writer(csvfile, delimiter=',')
#     csv_writer.writerow(['movieId', 'title', '(no genres listed)', 'Action', 'Adventure', 'Animation', 
#     'Children', 'Comedy', 'Crime', 'Documentary', 'Drama', 'Fantasy', 'Film-Noir', 'Horror', 
#     'IMAX', 'Musical', 'Mystery', 'Romance', 'Sci-Fi', 'Thriller', 'War', 'Western'])
    
#     csv_file = open("movies.csv")
#     read_csv = csv.reader(csv_file)
#     for row in read_csv:
#         nRow = []
#         nRow.append(row[0])
#         nRow.append(row[1])

#         col = row[2]
#         genres = col.split('|')
#         for lst_genre in lst_genres:
#             if lst_genre in genres:
#                 nRow.append('1')
#             else:
#                 nRow.append('0')
#         csv_writer.writerow(nRow)

# opened file in pandas and it worked
data = pd.read_csv("movies_ordered.csv") 
head = data.head()
print(head)

# for future, want to figure out what to do precisely with dataframes
# can add dimension for ratings but we felt that categories mattered more for the time being
# other datasets seemed not super useful
# could also webscrape directors or head actors