# cog-Real-ESRGAN


Web Demoe and API: 
[![Replicate](https://replicate.com/cjwbw/real-esrgan/badge)](https://replicate.com/cjwbw/real-esrgan)

An implementation of [Real-ESRGAN](https://github.com/ai-forever/Real-ESRGAN) in [Cog](https://github.com/replicate/cog), and pushing it to Replicate.


First, download the weights:

    cog run script/download-weights 

Then, you can run predictions:

    cog predict -i image=@...

Or, push to a Replicate page:

    cog push r8.im/...
