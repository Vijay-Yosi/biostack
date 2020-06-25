import random


def random_params():
    EPOCHS = int(10**random.uniform(2.0, 3.0))
    parameters = {'activation': random.choice(['tanh']),
                  'batchnorm_conv': random.choice([True, False]),
                  'batchnorm_gru': random.choice([True, False]),
                  'batchnorm_mid': random.choice([True, False]),
                  'batch_size': int(10**random.uniform(1.7, 2.3)),
                  'conv_activation': random.choice(['tanh']),
                  'conv_depth': random.randint(1, 3),
                  'conv_dim_depth': int(2**random.uniform(1, 4)),
                  'conv_dim_width': int(2**random.uniform(1, 4)),
                  'conv_d_growth_factor': random.uniform(0.5, 2),
                  'conv_w_growth_factor': random.uniform(0.5, 2),
                  'do_extra_gru': random.choice([True, False]),
                  'do_vae': random.choice([True, False]),
                  'do_conv_encoder': random.choice([True, False]),
                  'epochs': EPOCHS,
                  'gru_depth': random.randint(2, 5),
                  'hg_growth_factor': random.uniform(.5, 2),
                  'hidden_dim': int(10**random.uniform(1.7, 2.0)),
                  'loss': 'categorical_crossentropy',
                  'lr': 10**random.uniform(-3.6, -2.6),
                  'middle_layer': random.randint(1, 6),
                  'momentum': random.uniform(.85, .999),
                  'optim': random.choice(['adam']),
                  'rnn_activation': random.choice(['tanh']),
                  'vae_annealer_start': random.randint(int(EPOCHS / 20), int(EPOCHS / 2)),
                  'tgru_dropout': random.uniform(.00, .25),
                  'batchnorm_vae': random.choice([True, False]),
                  'vae_activation': random.choice(['tanh']),
                  'vae_sigmoid_slope': random.uniform(0.5, 1.0),
                  'recurrent_dim': int(10**random.uniform(1.7, 2.0)),
                  'vae_weights_start': 4,
                  'val_split': 0.1,
                  'double_hg': True,
                  'repeat_vector': True,
                  'temperature': 1.00,
                  'terminal_gru': random.choice([True, False])}
    return parameters


def simple_params():
    EPOCHS = 100
    parameters = {'activation': 'tanh',
                  'batchnorm_conv': False,
                  'batchnorm_gru': False,
                  'batchnorm_mid': False,
                  'batch_size': 100,
                  'conv_activation': 'tanh',
                  'conv_depth': random.randint(1, 3),
                  'conv_dim_depth': 8,
                  'conv_dim_width': 8,
                  'conv_d_growth_factor': 1,
                  'conv_w_growth_factor': 1,
                  'do_extra_gru': False,
                  'do_vae': False,
                  'do_conv_encoder': False,
                  'epochs': EPOCHS,
                  'gru_depth': random.randint(2, 5),
                  'hg_growth_factor': 1,
                  'hidden_dim': 50,
                  'loss': 'categorical_crossentropy',
                  'lr': 0.001,
                  'middle_layer': random.randint(1, 6),
                  'momentum': 0.995,
                  'optim': random.choice(['adam']),
                  'rnn_activation': 'tanh',
                  'vae_annealer_start': random.randint(int(EPOCHS / 20), int(EPOCHS / 2)),
                  'tgru_dropout': random.uniform(.00, .25),
                  'batchnorm_vae': False,
                  'vae_activation': 'tanh',
                  'vae_sigmoid_slope': random.uniform(0.5, 1.0),
                  'recurrent_dim': int(10**random.uniform(1.7, 2.0)),
                  'vae_weights_start': 4,
                  'val_split': 0.1,
                  'double_hg': True,
                  'repeat_vector': True,
                  'temperature': 1.00,
                  'terminal_gru': False
                  }
    return parameters
