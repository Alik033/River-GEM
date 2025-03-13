import torch
import torch.nn as nn

def bicubic_downsample(x, scale_factor=0.5):
    """
    Downsamples a batch of images using bicubic interpolation in PyTorch.
    """
    target_height = int(x.size(2) * scale_factor)
    target_width = int(x.size(3) * scale_factor)
    return torch.nn.functional.interpolate(x, size=(target_height, target_width), mode='bicubic', align_corners=False)

def bicubic_upsample(x, scale_factor=2.0):
    """
    Upsamples a batch of images using bicubic interpolation in PyTorch.
    """
    target_height = int(x.size(2) * scale_factor)
    target_width = int(x.size(3) * scale_factor)
    return torch.nn.functional.interpolate(x, size=(target_height, target_width), mode='bicubic', align_corners=False)

class Downsample(nn.Module):
    def __init__(self, n_feat):
        super(Downsample, self).__init__()

        self.body = nn.Sequential(nn.Conv2d(n_feat, n_feat//2, kernel_size=3, stride=1, padding=1, bias=False),
                                  nn.PixelUnshuffle(2))

    def forward(self, x):
        return self.body(x)

class Upsample(nn.Module):
    def __init__(self, n_feat):
        super(Upsample, self).__init__()

        self.body = nn.Sequential(nn.Conv2d(n_feat, n_feat*2, kernel_size=3, stride=1, padding=1, bias=False),
                                  nn.PixelShuffle(2))

    def forward(self, x):
        return self.body(x)
