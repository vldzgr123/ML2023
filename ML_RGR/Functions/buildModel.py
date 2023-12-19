import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split, GridSearchCV
import numpy as np
from collections import Counter
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from imblearn.under_sampling import NearMiss