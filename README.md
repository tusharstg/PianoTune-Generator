# PianoTune-Generator

![alt text](https://github.com/tusharstg/PianoTune-Generator/blob/main/image11.png?raw=true "GUI")

![alt text](https://github.com/tusharstg/PianoTune-Generator/blob/main/image3.jpg?raw=true "Neural Network")

##############################################################################
				Bidrectional LSTM RNN
##############################################################################

Our RNN works pretty well at impersonating music.  There are two ways to interact with it.
You can train a model or use an existing one to predict.

Training:
Call `python3 train.py --name <name of model to train> --songs_dir <directory containing midis>`
Optional params include:
    `--checkpoint <hdf5 file>` to resume training from a previous checkpoint.
    `--notes <pickled notes file>` to use pre-parsed notes.
    `--epochs <int>` to set the number of epochs to train for, defaults to 10

Predicting/Generating:
Call `python3 GUI.py and enter name of the model where model name is:
    - ragtime
    - rap
    - christmas
Or a custom trained model.

Note that a hdf5 and notes file must exist in their respective places with the same name to
generate a song.

Based on the tutorial found here:
https://towardsdatascience.com/how-to-generate-music-using-a-lstm-neural-network-in-keras-68786834d4c5
