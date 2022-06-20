## SCPE: Simple Constructive for Packet Embedding

This repository contains the code for our paper [SimCSE for Encrypted Traffic Classification and Zero-Day Attack Detection](https://XXXX).


## Quick Links

  - [Requirements](#requirements)
  - [Getting Started](#getting-started)
  - [Extract Hexadecimal Representation](#extract-hexadecimal-representation)
  - [Train SCPE](#train-SCPE)
    - [Pre-Processing](#pre-processing)
    - [Training](#training)
    - [Predicting](#predicting)

## Requirements
```bash
!pip install transformers
!pip install scapy
```

## Getting Started

To install this package, clone this repository and then run:

```bash
pip install -e .
```
Note that for enabling GPU encoding, you should install the correct version of PyTorch that supports CUDA.
 
## Extract Hexadecimal Representation

For binary classification, create two folders containing the PCAP files. 
The input: path for the folder that contains the PCAP files, and the target is the label of the files—for example, 0 for benign files and 1 for malware.

```bash
path= r"<PATH TO THE PCAP FILES FOLDER>"
target=0
extract_hex=pack2hex(path, target)
df_benign= extract_hex.extract()
```

## Train SCPE

### Pre-Processing
```bash
from sklearn.model_selection import train_test_split

# Load the dataset
data = pd.read_csv (r'<PATH TO THE CSV FILE') 

# Extract the relevant series
sentences= data['hex']
y_target=data['target'].to_numpy()

# Split to Train-Test
X_train, X_test, y_train, y_test = train_test_split(sentences, y_target, test_size=0.2)

# Convert to the proper object
X_train=X_train.to_list()
X_test=X_test.to_list()
```

### Training
```bash
# create SCPE class
model=SCPE()

# Train the SCPE
epocs=1
model.train(X_train,y_train,epocs)
```

### Predicting
```bash
y_pred=model.predict(X_test)
```


inproceedings{gao2021simcse,
   title={{SimCSE}: Simple Contrastive Learning of Sentence Embeddings},
   author={Gao, Tianyu and Yao, Xingcheng and Chen, Danqi},
   booktitle={Empirical Methods in Natural Language Processing (EMNLP)},
   year={2021}
}
