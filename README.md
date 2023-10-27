# Benchmarks for Cooperative verification of safety and security Properties of PLC programs
This repo is where we put the artifacts from our experiments described in our paper - Benchmarks for cooperative verification of safety and security properties of PLC programs

Welcome to the repository for cooperative verification experiments in the context of safety and security properties for Programmable Logic Controllers (PLC) programs. This repository houses the necessary artifacts and tools to reproduce the experiment's results.

## Table of Contents

- [Algorithms](#algorithms)
  - [Tool Selection Algorithm](#tool-selection-algorithm)
  - [Custom Verifier Validator](#custom-verifier-validator)
- [Running Experiments](#running-experiments)
- [Experiment Overview](#experiment-overview)
- [Experiment Workflow](#experiment-workflow)
- [Properties](#properties)

## Algorithms

### Tool Selection Algorithm

We have implemented a Python-based tool selection algorithm. Its primary purpose is to assist in selecting verification tools that best align with the unique characteristics of PLC programs. To run this algorithm, use the following command:

```bash
python3 Tool_Selection2.py
 ```
```
 Custom Verifier Validator
The custom verifier validator is a specialized CoVeriTeam program developed internally. Its function combines the three most highly recommended verification tools for conducting PLC program verification.
```

### Running Experiments
Automating the experimentation process was essential due to the substantial number of PLC programs involved (40). To execute these experiments efficiently, we have provided a bash script, which is detailed below. The PLC programs utilized in these experiments are conveniently located in this repository.

```
./runExperiments.sh
```
### Experiment Overview
Our primary objective in these experiments is to identify and select the most suitable verification tools for effectively verifying PLC programs. This selection process revolves around assessing the tools' performance and features, with a specific focus on minimizing both false positives and false negatives.

### Experiment Workflow
The experimentation workflow follows these key steps:

The Tool Selection Algorithm assists in selecting verification tools that best match the characteristics of PLC programs.
These selected tools are subsequently submitted to the Custom Verifier Validator.
In the initial round of experiments, instances of "unknowns" may arise, necessitating further evaluation.
The evaluation process concentrates on the False Positive Rate (FPR) and False Negative Rate (FNR) of the tools.
The best-performing tools, as determined by the evaluation criteria, are then utilized in a second round of experiments with additional PLC programs, especially in cases where results are inconclusive or conflicting.
Combinations of tools, as described in the paper, are considered to enhance the verification process.
Properties
To adapt Linear Temporal Logic (LTL) formulas to the specific behavior of PLC programs, we introduced the end-of-cycle (EoC) variable in the properties used in these experiments. Further details regarding this adaptation can be found in the associated paper.

For additional information on the experiments, their outcomes, and the specific tools employed, please consult the associated paper.

Thank you for your interest in our cooperative verification experiments for PLC program safety and security. Your contributions and feedback are greatly appreciated.
