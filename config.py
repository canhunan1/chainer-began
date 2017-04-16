import argparse


def validate_args(args):
    k_0 = args.k_0
    gamma = args.gamma

    assert(0 <= k_0 and k_0 <= 1.0)
    assert(0 <= gamma and gamma <= 1.0)

    return args


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--gpu', type=int, default=-1)

    # CelebA dataset specific
    parser.add_argument('--celeba-root', type=str,
                        default='/home/test/datasets/celeba_aligned/CelebA')
    parser.add_argument('--celeba-scale', type=int, default=64,
                        help='Width and height dimension of images')

    # General
    parser.add_argument('--dataset', type=str, default='celeba')
    parser.add_argument('--iterations', type=int, default=500000)
    parser.add_argument('--batch-size', type=int, default=16)
    parser.add_argument('--out-dir', type=str, default='result')

    # Hyperparameters
    parser.add_argument('--n-z', type=int, default=64,
                        help='Size of generator noise')
    parser.add_argument('--n-h', type=int, default=64,
                        help='Size of hidden state')
    parser.add_argument('--gamma', type=float, default=0.5,
                        help='Diversity ratio. Lower values lead to lower \
                             image diversity')
    parser.add_argument('--k-0', type=float, default=0)
    parser.add_argument('--lambda-k', type=float, default=0.001)
    parser.add_argument('--g-lr', type=float, default=5e-5)
    parser.add_argument('--d-lr', type=float, default=5e-5)
    parser.add_argument('--g-lr-decay-interval', type=int, default=100000)
    parser.add_argument('--d-lr-decay-interval', type=int, default=100000)
    parser.add_argument('--g-n', type=int, default=16)
    parser.add_argument('--d-n', type=int, default=16)
    parser.add_argument('--g-block-size', type=int, default=2)
    parser.add_argument('--d-block-size', type=int, default=2)
    parser.add_argument('--g-embed-size', type=int, default=8)
    parser.add_argument('--d-embed-size', type=int, default=8)

    # Other
    parser.add_argument('--loss-norm', type=int, default=1,
                        help='Pixel-wise loss norm, 1 or 2')

    return validate_args(parser.parse_args())
