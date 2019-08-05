import numpy as np
import os
import tensorflow as tf
from tensorflow.python.estimator.export.export import build_raw_serving_input_receiver_fn
from tensorflow.python.estimator.export.export_output import PredictOutput

INPUT_TENSOR_NAME = "inputs"
SIGNATURE_NAME = "serving_default"
LEARNING_RATE = 0.001


def keras_model_fn(hyperparameters):
    model = Sequential()
    
    model.add(Bidirectional(LSTM(32, activation = 'relu', dropout = 0.1, recurrent_dropout = 0.1, return_sequences = True), input_shape = (None,train_data.shape[-1])), name = 'inputs')
    model.add(Bidirectional(LSTM(16, activation = 'relu', dropout = 0.1, recurrent_dropout = 0.1))) 
    model.add(layers.Dense(1))

    model.compile(optimizer = Adam(lr = hyperparameters['learning_rate'],beta_1 = 0.9, beta_2 = 0.999, epsilon = None, decay = hyperparameters['decay'], amsgrad = False), loss = 'mae')
    return model



hyperparameters = {"learning_rate": 1e-4, "decay": 1e-6}

def train_input_fn(training_dir, hyperparameters):
    return _input_fn(training_dir, 'abalone_train.csv')


def eval_input_fn(training_dir, hyperparameters):
    return _input_fn(training_dir, 'abalone_test.csv')


def _input_fn(training_dir, training_filename):
    training_set = tf.contrib.learn.datasets.base.load_csv_without_header(
        filename=os.path.join(training_dir, training_filename), target_dtype=np.int, features_dtype=np.float32)

    return tf.estimator.inputs.numpy_input_fn(
        x={INPUT_TENSOR_NAME: np.array(training_set.data)},
        y=np.array(training_set.target),
        num_epochs=None,
        shuffle=True)()