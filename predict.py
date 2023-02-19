import torch
from PIL import Image
import numpy as np
from RealESRGAN import RealESRGAN
from cog import BasePredictor, Input, Path


class Predictor(BasePredictor):
    def setup(self):
        """Load the model into memory to make running multiple predictions efficient"""
        self.models = {}

        for scale in [2, 4, 8]:
            self.models[scale] = RealESRGAN("cuda", scale=scale)
            self.models[scale].load_weights(
                f"weights/RealESRGAN_x{scale}.pth", download=False
            )

    def predict(
        self,
        image: Path = Input(
            description="Input image",
        ),
        upscale: int = Input(
            choices=[2, 4, 8], description="Upscaling factor", default=4
        ),
    ) -> Path:
        model = self.models[upscale]
        path_to_image = "inputs/lr_image.png"
        image = Image.open(str(image)).convert("RGB")
        sr_image = model.predict(image)
        out_path = "/tmp/out.png"
        sr_image.save(out_path)
        return Path(out_path)
