## Contrastive Learning for PCAP

This repository contains the code for our paper:
[SimCSE for Encrypted Traffic Detection and Zero-Day Attack Detection](https://ieeexplore.ieee.org/document/9780135)

## Quick Links

  - [Requirements](#requirements)
  - [Getting Started](#getting-started)
  - [Load the model](#load-the-model)
    - [Fit](#fit)
    - [Transform](#transform)
    - [Fit and Transform](#fit-and-transform)

## Requirements
```bash
!pip install transformers
!pip install contrastive_learning_for_pcap
```

## Getting Started

Import the package:
```bash
from contrastive_learning_for_pcap.contrastive_learning_for_pcap import contrastive_learning_for_pcap
```
 
## Load the model

```bash
PATH= "PATH TO FOLDER THAT CONTAINS PCAP FILES"
model=contrastive_learning_for_pcap(PATH)
``` 
## Fit

```bash
epoc_num=1
model.fit_transform(epoc_num)
``` 
## Transform

```bash
vectors=model.transform()
``` 
## Fit and Transform

```bash
epoc_num=1
vectors=model.fit_transform(epoc_num)
```

## Citation
```
@article{bar2022simcse,
  title={Simcse for encrypted traffic detection and zero-day attack detection},
  author={Bar, Rotem and Hajaj, Chen},
  journal={IEEE Access},
  volume={10},
  pages={56952--56960},
  year={2022},
  publisher={IEEE}
}

```

