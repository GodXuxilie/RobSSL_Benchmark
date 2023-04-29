# Benchmarking Robustness Transferability of Adversarial Contrastive Learning (ACL)
This repository contains the following three kinds of code:
+ Robust pre-training via various ACL methods 
+ Finetuning tools
+ Evaluation protocals

# Requirement
+ Python 3.8
+ Pytorch 1.13
+ CUDA 11.6
+ AutoAttack
+ robustbench

# Robust pre-training via ACL
We provide a unified pre-training framework to conduct robust pre-training.

```
python pretraining.py   --gpu GPU_id \
                        --experiment path_of_log_to_be_saved \
                        --pretraining pre_training_method: [ACL, AdvCL, AInfoNCE, DynACL] \
                        --dataset pretraining_dataset: [cifar10, cifar100, stl10]
                        --model type_of_backbone_network
```

# Finetuning tools
We provide a unified finetuning tools to applying the adversarially pre-trained models to downstream tasks.

### Finetuning without post-processing
```
python finetuning.py    --gpu GPU_id \
                        --experiment path_of_log_to_be_saved \
                        --pretraining  pre_training_method \
                        --model type_of_backbone_network \
                        --checkpoint path_of_pretrained_checkpoint \ 
                        --dataset downstream_dataset: [cifar10, cifar100, stl10] \ 
                        --eval_mode evalution_mode: [SLF,ALF,AFF]
```
### Finetuning with post-processing
```
python finetuning.py    --gpu GPU_id \
                        --experiment path_of_log_to_be_saved \
                        --pretraining  pre_training_method \
                        --model type_of_backbone_network \
                        --checkpoint path_of_pretrained_checkpoint \ 
                        --dataset downstream_dataset: [cifar10, cifar100, stl10] \
                        --eval_mode evalution_mode: [LP_SLF,LP_ALF,LP_AFF]
```
### Finetuning in the semi-supervised setting
```
python finetuning.py    --gpu GPU_id \
                        --experiment path_of_log_to_be_saved \
                        --pretraining  pre_training_method \
                        --model type_of_backbone_network \
                        --checkpoint path_of_pretrained_checkpoint \ 
                        --dataset downstream_dataset: [cifar10, cifar100, stl10] \
                        --eval_mode evalution_mode: [semi_AT]
```

# Evalution Protocals
We provide a unified evaluation protocals to fairly evaluate the performance of finetuned models on the downstream tasks.
```
python finetuning.py    --gpu GPU_id \
                        --experiment path_of_log_to_be_saved \
                        --pretraining  pre_training_method \
                        --model type_of_backbone_network \
                        --checkpoint path_of_pretrained_checkpoint \ 
                        --eval_mode evalution_mode: [semi_AT]
```

# Performance Benchmarking Across Tasks
Here, robust pre-training and finetuning are conducted on the same datasets.

## CIFAR-10 task




