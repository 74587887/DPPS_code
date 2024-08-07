# Diffusion Posterior Proximal Sampling for Image Restoration
## 📖[**Paper**](https://arxiv.org/pdf/2402.16907)|🖼️[**Project Page**](https://dpps.pages.dev/)

Official PyTorch implementation of the ACM Multimedia 2024 paper "[Diffusion Posterior Proximal Sampling for Image Restoration](https://dpps.pages.dev/)". 
Our implementation is based on the [DPS](https://github.com/DPS2022/diffusion-posterior-sampling) codebase.



**Diffusion Posterior Proximal Sampling for Image Restoration**<br>
[Hongjie Wu*](https://hongjie-wu.pages.dev/), Linchao He*, Mingqin Zhang, Dongdong Chen, Kunming Luo, Mengting Luo, Ji-Zhe Zhou, Hu Chen and Jiancheng Lv <br>
*ACM Multimedia 2024 Oral*


<img src="https://dpps.pages.dev/static/images/cover1.jpg" alt="concept" width="100%">



## Abstract

Diffusion models have demonstrated remarkable efficacy in generating high-quality samples.
Existing diffusion-based image restoration algorithms exploit pre-trained diffusion models to leverage data priors, yet they still preserve elements inherited from the unconditional generation paradigm.
These strategies initiate the denoising process with pure white noise and incorporate random noise at each generative step, leading to over-smoothed results.
In this paper, we present a refined paradigm for diffusion-based image restoration. Specifically, we opt for a sample consistent with the measurement identity at each generative step, exploiting the sampling selection as an avenue for output stability and enhancement. The number of candidate samples used for selection is adaptively determined based on the signal-to-noise ratio of the timestep.
Additionally, we start the restoration process with an initialization combined with the measurement signal, providing supplementary information to better align the generative process.
Extensive experimental results and analyses validate that our proposed method significantly enhances image restoration performance while consuming negligible additional computational resources.

<img src="https://dpps.pages.dev/static/images/proposed.jpg" alt="concept" width="100%">

## Getting started 

### 1) Clone the repository

```
git clone  https://github.com/74587887/DPPS_code DPPS
cd DPPS
```


### 2) Download pretrained checkpoint

Download the [checkpoints](https://drive.google.com/drive/folders/1jElnRoFv7b31fG0v6pTSQkelbSX3xGZh) (from [DPS](https://github.com/DPS2022/diffusion-posterior-sampling)) and put them into `DPPS/models/`.

```
https://drive.google.com/drive/folders/1jElnRoFv7b31fG0v6pTSQkelbSX3xGZh
```


### 3) Set environment

Install required dependencies

```
pip install -r requirements.txt
```

And git the external codes for motion-blurring.

```
git clone https://github.com/LeviBorodenko/motionblur motionblur
```

### 4) Inference

```
python3 sample_condition.py \
--model_config={model_config} \
--diffusion_config=configs/diffusion_config.yaml \
--task_config={task_config};
```
### 5) Possible task and model configurations

```
# model configs
- configs/model_config.yaml  # for FFHQ dataset
- configs/imagenet_model_config.yaml  # for ImageNet dataset

# task configs
- configs/super_resolution_config.yaml  
- configs/gaussian_deblur_config.yaml
- configs/motion_deblur_config.yaml
- configs/inpainting_config.yaml
```


## Citation
If you find our code useful, please kindly consider citing our paper

```
@article{wu2024diffusion,
  title={Diffusion Posterior Proximal Sampling for Image Restoration},
  author={Wu, Hongjie and He, Linchao and Zhang, Mingqin and Chen, Dongdong and Luo, Kunming and Luo, Mengting and Zhou, Ji-Zhe and Chen, Hu and Lv, Jiancheng},
  journal={arXiv preprint arXiv:2402.16907},
  year={2024}
}
```
