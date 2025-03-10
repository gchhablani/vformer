import torch

from vformer.models import VanillaViT

img = torch.randn(2, 3, 256, 256)


def test_VanillaViT():

    model = VanillaViT(img_size=256, patch_size=32, n_classes=10, in_channels=3)
    _ = model(img)

    model = VanillaViT(
        img_size=256,
        patch_size=32,
        n_classes=10,
        latent_dim=1024,
        decoder_config=(1024, 512),
    )
    _ = model(img)
