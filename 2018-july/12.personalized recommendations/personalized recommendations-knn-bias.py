import os
import surprise
from surprise import model_selection 
import pandas as pd
import csv
   
def read_train_data(path):
    file_path = os.path.normpath(path)
    reader = surprise.Reader(line_format='timestamp user item rating', sep=',')
    data = surprise.Dataset.load_from_file(file_path, reader=reader)
    return data

movie_train = read_train_data('E:/train_v2.csv')
print(movie_train.raw_ratings)

knn_estimator = surprise.KNNWithMeans()
knn_grid = {'k': [10, 20],
              'sim_options': {'name': ['cosine'],
                              'min_support': [1, 5],
                              'user_based': [False]
                              }
              }
knn_grid_estimator = model_selection.GridSearchCV(knn_estimator, knn_grid, measures=['rmse'], cv=3)
#do grid search using cv strategy
knn_grid_estimator.fit(movie_train)
print(knn_grid_estimator.best_score['rmse'])
print(knn_grid_estimator.best_params['rmse'])
results_df = pd.DataFrame.from_dict(knn_grid_estimator.cv_results)
final_model = knn_grid_estimator.best_estimator['rmse']

#build final model using best parameters from grid search
trainSet = movie_train.build_full_trainset()
final_model.fit(trainSet)

rows = csv.reader(open('F:/test_v2.csv'))
rows = list(rows)
rows.pop(0)
f = open('F:/submission.csv', 'w',newline='')
writer = csv.writer(f)
writer.writerow(['ID', 'rating'])
count = 0
for row in rows:
  count = count + 1
  pred = final_model.predict(row[1], row[2])
  print(pred)
  writer.writerow([row[0], pred[3]])
f.close()
print(count)

