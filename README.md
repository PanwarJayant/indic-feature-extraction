# indic-feature-extraction

A team-project for IRE course @ IIIT Hyderabad.

## Contents

- **[models](./models/)**: This folder contains all the different state-of-the-art multi-lingual models used for the project
- **[datasets](./datasets/)**: This folder contains all the files used for generating the dataset tsv files and the finally generated tsv files as well

## Python Package Requirements

- `simpletransformers`: light-weight transformers library for running models
- `sacrebleu, jiwer, rouge_score`: dependencies for the `evaluate` library
- `evaluate`: for performing evaluations on the model predictions

Install them using the following pip command:

```python
  pip install simpletransformers sacrebleu jiwer rouge_score evaluate
```

## How to Run

- After installing the packages, go to **[models](./models/)** folder and use the README there to understand which python notebook to run.
- Change the dataset paths accordingly in the python-notebook.
- Just run the cells of the desired python-notebook sequentially.

**Note**: GPU support is required for training the models.
