# The code is modified from the code of DynACL <>.
import os
import argparse
import torch
import torch.nn.functional as F
import torch.backends.cudnn as cudnn
import numpy as np
from utils import train_loop, get_loader, get_model,setup_hyperparameter, eval_test_nat, runAA, logger, eval_test_OOD


parser = argparse.ArgumentParser(
    description='Finetuning (SLF, ALF, AFF) and Evaluation')
parser.add_argument('--experiment', type=str,
                    help='location for saving trained models,\
                    we recommend to specify it as a subdirectory of the pretraining export path',
                    required=True)

parser.add_argument('--model', type=str, default='r18')
parser.add_argument('--data', type=str, default='../data',
                    help='location of the data')
parser.add_argument('--dataset', default='cifar10', type=str,
                    help='dataset to be used (cifar10 or cifar100)')
parser.add_argument('--resize', type=int, default=32,
                    help='location of the data')

parser.add_argument('--batch-size', type=int, default=512, metavar='N',
                    help='input batch size for training (default: 512)')
parser.add_argument('--test-batch-size', type=int, default=512, metavar='N',
                    help='input batch size for testing (default: 512)')

parser.add_argument('--epochs', type=int, default=25, metavar='N',
                    help='number of epochs to train')
parser.add_argument('--weight-decay', '--wd', default=2e-4,
                    type=float, metavar='W')
parser.add_argument('--lr', type=float, default=0.01, metavar='LR',
                    help='learning rate')
parser.add_argument('--momentum', type=float, default=0.9, metavar='M',
                    help='SGD momentum')

parser.add_argument('--epsilon', type=float, default=8. / 255.,
                    help='perturbation')
parser.add_argument('--step-size', type=float, default=2. / 255.,
                    help='perturb step size')
parser.add_argument('--num-steps-train', type=int, default=10,
                    help='perturb number of steps')
parser.add_argument('--num-steps-test', type=int, default=20,
                    help='perturb number of steps')

parser.add_argument('--eval-only', action='store_true',
                    help='if specified, eval the loaded model')
parser.add_argument('--eval-AA', action='store_true',
                    help='if specified, eval the loaded model')
parser.add_argument('--eval-OOD', action='store_true',
                    help='if specified, eval the loaded model')
parser.add_argument('--checkpoint', default='', type=str,
                    help='path to pretrained model')

parser.add_argument('--resume', action='store_true',
                    help='if resume training')
parser.add_argument('--start-epoch', default=0, type=int,
                    help='the start epoch number')

parser.add_argument('--decreasing_lr', default='10,20',
                    help='decreasing strategy')
parser.add_argument('--cvt_state_dict', action='store_true',
                    help='Need to be specified if pseudo-label finetune is not implemented')

parser.add_argument('--bnNameCnt', default=1, type=int)
parser.add_argument('--mode', type=str, default='SLF',
                    help='Ensemble, SLF, ALF, AFF')
parser.add_argument('--pretraining', type=str, default='ACL',
                    help='Ensemble, SLF, ALF, AFF')

parser.add_argument('--test_frequency', type=int, default=0,
                    help='validation frequency during finetuning, 0 for no evaluation')   

parser.add_argument('--gpu', type=str, default='0', help='Set up the GPU id')
args = parser.parse_args()

# settings
os.environ['CUDA_VISIBLE_DEVICES'] = args.gpu
model_dir = os.path.join('checkpoints', args.experiment)
print(model_dir)
if not os.path.exists(model_dir):
    os.makedirs(model_dir)
log = logger(os.path.join(model_dir))
log.info(str(args))
device = 'cuda'
cudnn.benchmark = True


if args.eval_only:
    common_corrup_dir = 'checkpoints/' + args.experiment + '/common_corruptions'
    if not os.path.exists(common_corrup_dir):
        os.makedirs(common_corrup_dir)
    common_corrup_log = logger(os.path.join(common_corrup_dir))

    result_log = 'checkpoints/' + args.experiment + '/result/'
    if not os.path.exists(result_log):
        os.makedirs(result_log)
    result_log = logger(os.path.join(result_log))
    result_log.info('test checkpoint: {}'.format(args.checkpoint))

    mode = 'eval'
    train_loader, vali_loader, test_loader, num_classes = get_loader(args)
    model, optimizer, scheduler = get_model(args, num_classes, mode, log, device=device)
    model.eval()

    # eval natural accuracy
    nat_acc = eval_test_nat(model, test_loader, device, advFlag=None)
    log.info('standard acc: {:.2f}'.format(nat_acc * 100))

    # eval robustness against adversarial attacks
    if args.eval_AA:
        AA_log = 'checkpoints/' + args.experiment + '/result/AA_details.txt'
        AA_acc = runAA(model, test_loader, AA_log, advFlag=None)
        log.info('robust acc: {:.2f}'.format(AA_acc * 100))

    # eval robustness againt common corruptions
    if args.eval_OOD:
        common_corrup_dir = os.path.join(model_dir, 'common_corruptions')
        common_corrup_log = logger(os.path.join(common_corrup_dir))
        ood_acc_list, ood_acc_mean = eval_test_OOD(model, args.dataset, common_corrup_log, device, advFlag=None)
        log.info('mean corruption acc: {:.2f}'.format(ood_acc_mean * 100))
        for i in range(5):
            log.info('corruption severity-{} acc: {:.2f}'.format(i+1, ood_acc_list[i] * 100))
    
else:
    result_log = 'checkpoints/' + args.experiment + '/result/'
    if not os.path.exists(result_log):
        os.makedirs(result_log)
    result_log = logger(os.path.join(result_log))

    common_corrup_dir = 'checkpoints/' + args.experiment + '/common_corruptions'
    if not os.path.exists(common_corrup_dir):
        os.makedirs(common_corrup_dir)
    common_corrup_log = logger(os.path.join(common_corrup_dir))

    if args.mode == 'Ensemble' or args.mode == 'SLF':
        mode = 'SLF'
        log.info('Finetuning mode: SLF')
        # SLF finetuning
        args = setup_hyperparameter(args)
        train_loader, vali_loader, test_loader, num_classes = get_loader(args)
        model, optimizer, scheduler = get_model(args, num_classes, mode, log, device=device)
        train_loop(args, model, optimizer, scheduler, train_loader, test_loader, mode, device, log, model_dir)
        
        # eval natural accuracy
        SLF_nat_acc = eval_test_nat(model, test_loader, device, advFlag=None)
        result_log.info('{} standard acc: {:.2f}'.format(mode, SLF_nat_acc * 100))

        # eval robustness against adversarial attacks
        if args.eval_AA:
            AA_log = 'checkpoints/' + args.experiment + '/result/AA_details.txt'
            SLF_AA_acc = runAA(model, test_loader, AA_log, advFlag=None)
            result_log.info('{} robust acc: {:.2f}'.format(mode, SLF_AA_acc * 100))

        # eval robustness againt common corruptions
        if args.eval_OOD:
            SLF_ood_acc_list, SLF_ood_acc_mean = eval_test_OOD(model, args.dataset, common_corrup_log, device, advFlag=None)
            result_log.info('{} mean corruption acc: {:.2f}'.format(mode, SLF_ood_acc_mean * 100))
            for i in range(5):
                result_log.info('{} corruption severity-{} acc: {:.2f}'.format(mode, i+1, SLF_ood_acc_list[i] * 100))

    if args.mode == 'Ensemble' or args.mode == 'ALF':
        mode = 'ALF'
        args = setup_hyperparameter(args)
        train_loader, vali_loader, test_loader, num_classes = get_loader(args)
        model, optimizer, scheduler = get_model(args, num_classes, mode, log, device=device)
        train_loop(args, model, optimizer, scheduler, train_loader, test_loader, mode, device, log, model_dir)

        # eval natural accuracy
        ALF_nat_acc = eval_test_nat(model, test_loader, device, advFlag=None)
        result_log.info('{} standard acc: {:.2f}'.format(mode, ALF_nat_acc * 100))

        # eval robustness against adversarial attacks
        if args.eval_AA:
            AA_log = 'checkpoints/' + args.experiment + '/result/AA_details.txt'
            ALF_AA_acc = runAA(model, test_loader, AA_log, advFlag=None)
            result_log.info('{} robust acc: {:.2f}'.format(mode, ALF_AA_acc * 100))

        # eval robustness againt common corruptions
        if args.eval_OOD:
            ALF_ood_acc_list, ALF_ood_acc_mean = eval_test_OOD(model, args.dataset, common_corrup_log, device, advFlag=None)
            result_log.info('{} mean corruption acc: {:.2f}'.format(mode, ALF_ood_acc_mean * 100))
            for i in range(5):
                log.info('{} corruption severity-{} acc: {:.2f}'.format(mode, i+1, ALF_ood_acc_list[i] * 100))

    if args.mode == 'Ensemble' or args.mode == 'AFF':
        mode = 'AFF'
        args = setup_hyperparameter(args)
        train_loader, vali_loader, test_loader, num_classes = get_loader(args)
        model, optimizer, scheduler = get_model(args, num_classes, mode, log, device=device)
        train_loop(args, model, optimizer, scheduler, train_loader, test_loader, mode, device, log, model_dir)

        # eval natural accuracy
        AFF_nat_acc = eval_test_nat(model, test_loader, device, advFlag='pgd')
        result_log.info('{} standard acc: {:.2f}'.format(mode, AFF_nat_acc * 100))
        AFF_nat_acc = eval_test_nat(model, test_loader, device, advFlag=None)
        result_log.info('{} standard acc: {:.2f}'.format(mode, AFF_nat_acc * 100))

        # eval robustness against adversarial attacks
        if args.eval_AA:
            AA_log = 'checkpoints/' + args.experiment + '/result/AA_details.txt'
            AFF_AA_acc = runAA(model, test_loader, AA_log, advFlag='pgd')
            result_log.info('{} robust acc: {:.2f}'.format(mode, AFF_AA_acc * 100))

        # eval robustness againt common corruptions
        if args.eval_OOD:
            AFF_ood_acc_list, AFF_ood_acc_mean = eval_test_OOD(model, args.dataset, common_corrup_log, device, advFlag='pgd')
            result_log.info('{} mean corruption acc: {:.2f}'.format(mode, AFF_ood_acc_mean * 100))
            for i in range(5):
                result_log.info('{} corruption severity-{} acc: {:.2f}'.format(mode, i+1, AFF_ood_acc_list[i] * 100))

    if args.mode == 'Ensemble':
        result_log.info('mean robust accuracy: {:.2f}'.format(np.mean([SLF_AA_acc * 100, ALF_AA_acc * 100, AFF_AA_acc * 100])))
        if args.eval_AA:
            result_log.info('mean standard accuracy: {:.2f}'.format(np.mean([SLF_nat_acc * 100, ALF_nat_acc * 100, AFF_nat_acc * 100])))
        if args.eval_OOD:
            result_log.info('mean corruption accuracy: {:.2f}'.format(np.mean([SLF_ood_acc_mean * 100, ALF_ood_acc_mean * 100, AFF_ood_acc_mean * 100])))