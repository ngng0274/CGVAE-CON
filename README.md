# Constrained Graph Variational Autoencoders with Constrastive Learning for Molecule Design

This repository  contains CGVAE-CON that uses contrastive learning through augmentation of latent space of molecular graphs based on  [Constrained Graph Variational Autoencoders for Molecule Design](https://arxiv.org/abs/1805.09076) (CGVAE). 

# Requirements

This code was tested in Python 3.5 with Tensorflow 1.3. `conda`, `docopt` and `rdkit` are also necessary. A Bash script is provided to install all these requirements.

```
source ./install.sh
```

To evaluate SAS scores, use `get_sascorer.sh` to download the SAS implementation from [rdkit](https://github.com/rdkit/rdkit/tree/master/Contrib/SA_Score)

# Data Extraction

Two datasets (QM9 and ZINC) are in use.

For downloading QM9 and ZINC, please go to `data` directory and run `get_qm9.py` and `get_zinc.py`, respectively.

```
python get_qm9.py

python get_zinc.py
```

# Running CGVAE-CON

We provide two settings of CGVAE-CON. The first setting samples one breadth first search path for each molecule. The second setting samples transitions from multiple breadth first search paths for each molecule. 

To train and generate molecules using the first setting, use

```
python CGVAE.py --dataset qm9|zinc
```

To avoid training and generate molecules with a pretrained model, use

```
python CGVAE.py --dataset qm9|zinc --restore pretrained_model --config '{"generation": true}'
```

To train and generate molecules using the second setting, use

```
python CGVAE.py --dataset qm9|zinc --config '{"sample_transition": true, "multi_bfs_path": true, "path_random_order": true}'
```

To use optimization in the latent space, set `optimization_step` to a positive number

```
python CGVAE.py --dataset qm9|zinc --restore pretrained_model --config '{"generation": true, "optimization_step": 50}'
```

More configurations can be found at function `default_params` in `CGVAE.py`

# Evaluation

To evaluate the generated molecules, use

```
python evaluate.py --dataset qm9|zinc
python test.py
```


# Pretrained Models and Generated Molecules

<!--
We provide pretrained models and generated molecules for both settings. The following files are pretrained models

```
pretrained/qm9_setting1
pretrained/qm9_setting2
pretrained/zinc_setting1
pretrained/zinc_setting2
```

The following files are generated molecules

```
molecules/generated_smiles_qm9_setting1
molecules/generated_smiles_qm9_setting2
molecules/generated_smiles_zinc_setting1
molecules/generated_smiles_zinc_setting2
```

-->

Generated molecules can be obtained upon request.

A program in folder `molecules` is provided to read and visualize the molecules

```
python visualize.py molecule_file output_file
```
