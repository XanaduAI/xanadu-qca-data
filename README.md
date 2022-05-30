# Quantum-advantage data
This repository contains a reference to the data showcased in [our Nature paper on quantum computational advantage](https://www.nature.com/articles/s41586-022-04725-x). Data is publicly hosted in an s3 bucket and can be downloaded via the `download_data.py` python utility.

## Directories

The manuscript presents a set of different GBS instances, each one of them benchmarked in a different way to provide evidence of quantum-computational advantage. Each folder in this bucket corresponds to one of these GBS instances:

 - `fig2/`: A 16-mode GBS instance used to sample outcome probabilities and compute their TVD to the ground-truth distribution. Displayed in Fig. 2 of the manuscript and Figs. S4 and S5 of the Supplementary Information.
 - `fig3a/`: A 216-mode GBS instance with low squeezing used to compute the cross entropy. Displayed in Fig. 3a of the manuscript.
 - `fig3b/`: A 72-mode GBS instance with used to compute the Bayesian log average. Displayed in Fig. 3b of the manuscript.
 - `fig4/`: A 216-mode GBS instance with high squeezing used to compute the photon-number distribution, second-order correlations and an estimation of simulation times. Displayed in Fig. 4 of the manuscript.
 - `figS15/`: A 288-mode GBS instance with high squeezing used to demonstrate scalability, compute the photon-number distribution, second-order correlations and an estimation of simulation times. Displayed in Fig. S15 of the Supplementary Information.

## Folder contents

Each of the folder contains the following files:

### `program_params.json`

This dictionary contains all the instructions required to _define_ the respective GBS instance. In particular, the entries are:

 - `r`: the squeezing values of the computational modes.
 - `phi_0`, `phi_1`, `phi_2`: the arguments of the three phase modulators associated to the respective loops
 - `alpha_0`, `alpha_1`, `alpha_2`: the arguments of the three beamsplitters associated to the respective loops; note that the transmission values of the beamsplitters are obtained by $T = \text{cos}^2 \alpha$.
 - `loop_phases`: the round-trip phases as picked up by a mode that travels through the first, second or third delay line, respectively.
 - `common_efficiency`: the optical efficiency experienced by a mode that bypasses all three delay lines and is detected by the most efficient detector channel.
 - `loop_efficiencies`: the optical efficiency picked up by a mode that travels through the first, second or third delay line, respectively.
 - `relative_mode_efficiencies`: the relative efficiencies of the 16 detector channels; these efficiencies are cyclic in the sense that temporal mode $i$ will experience the same detection efficiency as mode as mode $i+16$.
 - `crop`: the number of time bins acquired before arrival of the first optical pulse at the detectors; these time bins are discarded from the `samples.npy`, `T.npy`, and `U.npy`.

### `U.npy`

A complex matrix of shape $M \times M$ where $M$ is the number of computational modes. It is the unitary matrix applied by Borealis.

### `T.npy`

A complex matrix of shape $M \times M$ where $M$ is the number of computational modes. It is the transfer matrix applied by Borealis (equivalent to the unitary, only with loss taken into account). The transfer matrix $T$ and the squeezing array $\vec{r}$ form the ground truth that our experimental samples are benchmarked against.


### `r.npy`

The vector of squeezing values $\vec{r}$ that the circuit acts upon. The transfer matrix $T$ and the squeezing array $\vec{r}$ form the ground truth that our experimental samples are benchmarked against.

### `samples.npy`

An array containing the experimental photon-number samples acquired by Borealis. It is of the shape $n \times 1 \times M$ where $n$ is the number of repetitions (also referred to as shots or acquisition cycles) and $M$ is the number of computational modes.

