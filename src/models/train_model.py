import numpy as np
import os
import tensorflow as tf
from tensorflow.python.estimator.export.export import build_raw_serving_input_receiver_fn
from tensorflow.python.estimator.export.export_output import PredictOutput
from tensorflow.python.keras.preprocessing.sequence import TimeseriesGenerator
from tensorflow.python.keras import Sequential
import logging


from tensorflow.python.keras.models import Sequential
from tensorflow.python.keras import layers
from tensorflow.python.keras.optimizers import Adam
from tensorflow.python.keras.models import Sequential
from tensorflow.python.keras.layers import LSTM
from tensorflow.python.keras.layers import Dense
from tensorflow.python.keras.layers import TimeDistributed
from tensorflow.python.keras.layers import Bidirectional


INPUT_TENSOR_NAME = "inputs_input" # Watch out, it needs to match the name of the first layer + "_input"
SIGNATURE_NAME = "serving_default"
DECAY = 1e-6
LEARNING_RATE = 1e-4
N_INPUTS = 128
BATCH_SIZE = 2000
TEST_BATCH_SIZE = 1
DAYS_IN_FUTURE = 1
SIMPLIFY = 1
hyperparameters = {"learning_rate": LEARNING_RATE, "decay": DECAY}
counter = 0

def keras_model_fn(hyperparameters):
    logging.debug('Initializing Keras Model....')
    model = Sequential()    
    model.add(LSTM(32, activation = 'relu', dropout = 0.0, recurrent_dropout = 0.0, return_sequences = True, input_shape = (None, 19), name = 'inputs'))
    model.add(LSTM(8, activation = 'relu', dropout = 0.0, recurrent_dropout = 0.0)) 
    model.add(layers.Dense(1))

    model.compile(optimizer = Adam(lr = 0.0005, beta_1 = 0.9, beta_2 = 0.999, epsilon = None, decay = 0.000001, amsgrad = False), loss = 'mae')
    return model


def create_sequences(data, targets, lookback, delay, min_index, max_index, shuffle = False, batch_size = 32, step = 1):
    '''Create sequence based on a specified len'''
    global counter
    counter += 1
    print('STEP::', counter,' / CREATE SEQUENCE DATA INPUT SHAPE:',data.shape, ' / CREATE SEQUENCE TARGETS INPUT SHAPE:',targets.shape)
    
    
    if max_index is None:
        max_index = len(data) - delay - 1
    i = min_index + lookback
    
    while 1:
        if shuffle:
            rows = np.random.randint(min_index + lookback, max_index, size = batch_size)
        else:
            if i + batch_size >= max_index:
                i = min_index + lookback
            rows = np.arange(i, min(i + batch_size, max_index))
            i += len(rows)
        
        samples = np.zeros((len(rows), lookback // step, data.shape[-1]))
        labels = np.zeros((len(rows),))
        
        for j, row in enumerate(rows):
            #print('DATA SHAPE', data.shape)
            #print('TARGETS SHAPE', targets.shape)
            indices = range(rows[j] - lookback, rows[j], step)
            samples[j] = data[indices]
            labels[j] = targets[rows[j] + delay]
        yield samples, labels


def serving_input_fn(hyperparameters):
    print('IMPORTANT LOG: Initializing serving_input_fn ...')
    # Here it concerns the inference case where we just need a placeholder to store
    # the incoming information ...    
    tensor = tf.placeholder(tf.float32, shape = [None,1, 19])
    inputs = {INPUT_TENSOR_NAME: tensor}
    return tf.estimator.export.ServingInputReceiver(inputs, inputs)


def train_input_fn(training_dir, hyperparameters):
    print('IMPORTANT LOG: Initializing train input function.....')
    print('IMPORTANT LOG: train_dir:: {}'.format(training_dir))
    return _input_fn(tf.estimator.ModeKeys.TRAIN, batch_size = BATCH_SIZE, data_dir = training_dir, training_filename = 'train.csv')


def eval_input_fn(training_dir, hyperparameters):
    print('User Message: Initializing eval input function.....')
    return _input_fn(tf.estimator.ModeKeys.EVAL, batch_size = BATCH_SIZE, data_dir = training_dir, training_filename = 'train.csv')


def _input_fn(mode, batch_size, data_dir, training_filename):
    print('IMPORTANT LOG: initializing input function.....')
    print('IMPORTANT LOG: train_dir:: {}'.format(data_dir))
    
    assert os.path.exists(data_dir), ("Unable to find data for input, are you sure you downloaded them ?")

    train_data = tf.contrib.learn.datasets.base.load_csv_without_header(filename = os.path.join(data_dir, training_filename), target_dtype = np.float32, features_dtype = np.float32)
    
    print('IMPORTANT SHAPE', train_data.data.shape, '\n')
    print('IMPORTANT SHAPE', train_data.target.shape)
    print('.....................................................................................................................' )

    
    if mode == tf.estimator.ModeKeys.TRAIN:
        datagen = create_sequences(data = train_data.data,
                                   targets = train_data.target,
                                   min_index = 0,
                                   max_index = 2000,
                                   shuffle = False,
                                   batch_size = BATCH_SIZE,
                                   step = SIMPLIFY,
                                   lookback = N_INPUTS,
                                   delay = DAYS_IN_FUTURE)
        
        print('COMPLETED TRAIN DATA GENERATION...')
    
    else:
        datagen = create_sequences(data = train_data.data,
                                   targets = train_data.target,
                                   min_index = 2001,
                                   max_index = 2500,
                                   shuffle = False,
                                   batch_size = TEST_BATCH_SIZE,
                                   step = SIMPLIFY,
                                   lookback = N_INPUTS,
                                   delay = DAYS_IN_FUTURE)
        print('COMPLETED EVAL DATA GENERATION...')
    
    
    
    x, y = datagen.next()
    print('DONE DATA GENERATION...')
    

    print('IMPORTANT LOG SAMPLE::', x)
    print('IMPORTANT LOG TRAIN::', y)

    return {INPUT_TENSOR_NAME: x}, y