# CIFAR-10 task
nohup python finetuning_eval.py --gpu 0 --experiment ACL_cifar10_r18_cifar10 --dataset cifar10 --pretraining ACL --model r18 --checkpoint ./checkpoints/ACL_DS.pt --mode Ensemble --eval-AA --eval-OOD &
nohup python finetuning_eval.py --gpu 2 --experiment DynACL_cifar10_r18_cifar10 --dataset cifar10 --pretraining DynACL --model r18 --checkpoint ./checkpoints/DynACL.pt --mode Ensemble --eval-AA --eval-OOD &
nohup python finetuning_eval.py --gpu 0 --experiment AdvCL_cifar10_r18_cifar10 --dataset cifar10 --pretraining AdvCL --model r18 --checkpoint ./checkpoints/AdvCL.pt --mode Ensemble --eval-AA --eval-OOD &
nohup python finetuning_eval.py --gpu 2 --experiment AInfoNCE_cifar10_r18_cifar10 --dataset cifar10 --pretraining A-InfoNCE --model r18 --checkpoint ./checkpoints/AInfoNCE.pt --mode Ensemble --eval-AA --eval-OOD &
nohup python finetuning_eval.py --gpu 2 --experiment DeACL_cifar10_r18_cifar10 --dataset cifar10 --pretraining DeACL --model r18 --checkpoint ./checkpoints/DeACL.pt --mode Ensemble --eval-AA --eval-OOD &
nohup python finetuning_eval.py --gpu 2 --experiment DynACL_plus_cifar10_r18_cifar10 --dataset cifar10 --pretraining DynACL --model r18 --checkpoint ./checkpoints/DynACL++.pt --mode Ensemble --eval-AA --eval-OOD &
nohup python finetuning_eval.py --gpu 2 --experiment DynACL_IR_cifar10_r18_cifar10 --dataset cifar10 --pretraining DynACL_IR --model r18 --checkpoint ./checkpoints/DynACL_IR.pt --mode Ensemble --eval-AA --eval-OOD &
nohup python finetuning_eval.py --gpu 2 --experiment DynACL_IR_plus_cifar10_r18_cifar10 --dataset cifar10 --pretraining DynACL_IR_plus --model r18 --checkpoint ./checkpoints/DynACL_IR_plus.pt --mode Ensemble --eval-AA --eval-OOD &

# CIFAR-100 task
nohup python finetuning_eval.py --gpu 1 --experiment ACL_cifar100_r18_cifar100 --dataset cifar100 --pretraining ACL --model r18 --checkpoint ./checkpoints/ACL_DS_CIFAR100.pt  --mode Ensemble --eval-AA --eval-OOD &
nohup python finetuning_eval.py --gpu 3 --experiment DynACL_cifar100_r18_cifar100 --dataset cifar100 --pretraining DynACL --model r18 --checkpoint ./checkpoints/DynACL_CIFAR100.pt  --mode Ensemble --eval-AA --eval-OOD &
nohup python finetuning_eval.py --gpu 0 --experiment AdvCL_cifar100_r18_cifar100 --dataset cifar100 --pretraining AdvCL --model r18 --checkpoint ./checkpoints/AdvCL_CIFAR100.pt --mode Ensemble --eval-AA --eval-OOD &
nohup python finetuning_eval.py --gpu 2 --experiment AInfoNCE_cifar100_r18_cifar100 --dataset cifar100 --pretraining A-InfoNCE --model r18 --checkpoint ./checkpoints/AInfoNCE_CIFAR100.pt --mode Ensemble --eval-AA --eval-OOD &
nohup python finetuning_eval.py --gpu 2 --experiment DynACL_plus_cifar100_r18_cifar100 --dataset cifar100 --pretraining DynACL --model r18 --checkpoint ./checkpoints/DynACL++_CIFAR100.pt --mode Ensemble --eval-AA --eval-OOD &
nohup python finetuning_eval.py --gpu 2 --experiment DynACL_IR_cifar100_r18_cifar100 --dataset cifar100 --pretraining DynACL_IR --model r18 --checkpoint ./checkpoints/DynACL_IR_CIFAR100.pt --mode Ensemble --eval-AA --eval-OOD &
nohup python finetuning_eval.py --gpu 2 --experiment DynACL_IR_plus_cifar100_r18_cifar100 --dataset cifar100 --pretraining DynACL_IR_plus --model r18 --checkpoint ./checkpoints/DynACL_IR_plus_CIFAR100.pt --mode Ensemble --eval-AA --eval-OOD &

# STL10 task
nohup python finetuning_eval.py --gpu 1 --experiment ACL_stl10_r18_stl10 --dataset stl10 --pretraining ACL --model r18 --checkpoint ./checkpoints/ACL_DS_STL10.pt  --mode Ensemble --eval-AA &
nohup python finetuning_eval.py --gpu 3 --experiment DynACL_stl10_r18_stl10 --dataset stl10 --pretraining DynACL --model r18 --checkpoint ./checkpoints/DynACL_STL10.pt  --mode Ensemble --eval-AA &
nohup python finetuning_eval.py --gpu 2 --experiment DynACL_plus_stl10_r18_stl10 --dataset stl10 --pretraining DynACL --model r18 --checkpoint ./checkpoints/DynACL++_STL10.pt --mode Ensemble --eval-AA &
nohup python finetuning_eval.py --gpu 2 --experiment DynACL_IR_stl10_r18_stl10 --dataset stl10 --pretraining DynACL_IR --model r18 --checkpoint ./checkpoints/DynACL_IR_STL10.pt --mode Ensemble --eval-AA &
nohup python finetuning_eval.py --gpu 2 --experiment DynACL_IR_plus_stl10_r18_stl10 --dataset stl10 --pretraining DynACL_IR_plus --model r18 --checkpoint ./checkpoints/DynACL_IR_plus_STL10.pt --mode Ensemble --eval-AA &

# transferability from CIFAR-10 to STL10
nohup python finetuning_eval.py --gpu 0 --experiment ACL_cifar10_r18_stl10 --dataset stl10 --pretraining ACL --model r18 --checkpoint ./checkpoints/ACL_DS.pt --mode Ensemble --eval-AA &
nohup python finetuning_eval.py --gpu 2 --experiment DynACL_cifar10_r18_stl10 --dataset stl10 --pretraining DynACL --model r18 --checkpoint ./checkpoints/DynACL.pt --mode Ensemble --eval-AA &
nohup python finetuning_eval.py --gpu 0 --experiment AdvCL_cifar10_r18_stl10 --dataset stl10 --pretraining AdvCL --model r18 --checkpoint ./checkpoints/AdvCL.pt --mode Ensemble --eval-AA &
nohup python finetuning_eval.py --gpu 2 --experiment AInfoNCE_cifar10_r18_stl10 --dataset stl10 --pretraining A-InfoNCE --model r18 --checkpoint ./checkpoints/AInfoNCE.pt --mode Ensemble --eval-AA &
nohup python finetuning_eval.py --gpu 2 --experiment DeACL_cifar10_r18_stl10 --dataset stl10 --pretraining DeACL --model r18 --checkpoint ./checkpoints/DeACL.pt --mode Ensemble --eval-AA &
nohup python finetuning_eval.py --gpu 2 --experiment DynACL_IR_cifar10_r18_stl10 --dataset stl10 --pretraining DynACL_IR --model r18 --checkpoint ./checkpoints/DynACL_IR.pt --mode Ensemble --eval-AA &

# transferability from CIFAR-100 to STL10
nohup python finetuning_eval.py --gpu 1 --experiment ACL_cifar100_r18_stl10 --dataset stl10 --pretraining ACL --model r18 --checkpoint ./checkpoints/ACL_DS_CIFAR100.pt  --mode Ensemble --eval-AA &
nohup python finetuning_eval.py --gpu 3 --experiment DynACL_cifar100_r18_stl10 --dataset stl10 --pretraining DynACL --model r18 --checkpoint ./checkpoints/DynACL_CIFAR100.pt  --mode Ensemble  --eval-AA &
nohup python finetuning_eval.py --gpu 0 --experiment AdvCL_cifar100_r18_stl10 --dataset stl10 --pretraining AdvCL --model r18 --checkpoint ./checkpoints/AdvCL_CIFAR100.pt --mode Ensemble --eval-AA  &
nohup python finetuning_eval.py --gpu 2 --experiment AInfoNCE_cifar100_r18_stl10 --dataset stl10 --pretraining A-InfoNCE --model r18 --checkpoint ./checkpoints/AInfoNCE_CIFAR100.pt --mode Ensemble --eval-AA  &
nohup python finetuning_eval.py --gpu 3 --experiment DynACL_IR_cifar100_r18_stl10 --dataset stl10 --pretraining DynACL_IR --model r18 --checkpoint ./checkpoints/DynACL_IR_CIFAR100.pt  --mode Ensemble --eval-AA &
