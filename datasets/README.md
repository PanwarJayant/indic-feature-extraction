# datasets

- This folder contains all the files used for generating the dataset tsv files and the finally generated tsv files as well
- There are a total of 4 folders because of working with two different versions for each of Hindi and Telugu
- The original folders have only _train.tsv_ and _test.tsv_ files but the **<>-dash** folders have three files:
  - **dash_train.tsv**: for training the models with samanantar-dash dataset
  - **dash_test.tsv**: for evaluating the model predictions with samanantar-dash type targets
  - **orig_test.tsv**: for evaluating the model predictions with correct language script targets

## Samanantar

- The project uses Samananthar dataset as the baseline, and
- For the baseline++ approach, we use Samananthar-Dash dataset

## Samanantar-Dash

- Samananthar-Dash dataset is like Samananthar dataset but the indic language words (in our case Hindi and Telugu) are expanded by appendind their matras' swaras at the end of the word
- So a word like **आस्ट्रेलिया** becomes **आस्ट्रेलियाएइआ**

## Folders

- **[hi-en](./hi-en/)**: contains the training and testing files for Hindi-English Samanantar original models
- **[hi-en-dash](./hi-en-dash/)**: contains the training and testing files for Hindi-English Samanantar-Dash models
- **[te-en](./te-en/)**: contains the training and testing files for Telugu-English Samanantar original models
- **[te-en-dash](./te-en-dash/)**: contains the training and testing files for Telugu-English Samanantar-Dash models

## Code

- **[extract](./extract.py)**: python script for extracting valid sentence pairs from Samanantar
- **[split](./split.py)**: python script for splitting extracted dataset into training and testing for both language-pairs
- **[dataprep](./dataprep.ipynb)**: python notebook for converting txt files into trainable tsv format
- **[sam_dash_hindi](./sam_dash_hindi.py)**: python script for converting Samanantar Hindi text to Samanantar-Dash Hindi text
