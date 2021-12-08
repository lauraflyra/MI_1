import math
import numpy as np
import itertools
from tabulate import tabulate
import matplotlib.pyplot as plt
import time
import random
from numpy import linalg as LA

import tensorflow as tf
from keras.datasets import mnist

(X_train, y_train),(X_test, y_test) = mnist.load_data()

