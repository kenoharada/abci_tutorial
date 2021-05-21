import torch
from torchvision import datasets, transforms


def set_up_data(args):
    train_kwargs = {'batch_size': args.batch_size, 'num_workers': 1,'pin_memory': True,'shuffle': True}
    test_kwargs = {'batch_size': args.test_batch_size, 'num_workers': 1,'pin_memory': True,'shuffle': False}
    transform=transforms.Compose([
        transforms.ToTensor(),
        transforms.Normalize((0.1307,), (0.3081,))
        ])
    train_dataset = datasets.MNIST('../../pytorch_examples/data', train=True, download=True,
                       transform=transform)
    test_dataset = datasets.MNIST('../../pytorch_examples/data', train=False,
                       transform=transform)
    train_loader = torch.utils.data.DataLoader(train_dataset,**train_kwargs)
    test_loader = torch.utils.data.DataLoader(test_dataset, **test_kwargs)
    return train_loader, test_loader


if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('--batch-size', type=int, default=64)
    parser.add_argument('--test-batch-size', type=int, default=64*4)
    args = parser.parse_args()
    train_loader, test_loader = set_up_data(args)
    print('train_num', len(train_loader))
    print('test_num', len(test_loader))