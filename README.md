# Diffusion Posterior Proximal Sampling for Image Restoration
## 📖[**Paper**](https://arxiv.org/pdf/2402.16907)|🖼️[**Project Page**](https://dpps.pages.dev/)

Official PyTorch implementation of the ACM Multimedia 2024 paper "[Diffusion Posterior Proximal Sampling for Image Restoration](https://dpps.pages.dev/)". 
Our implementation is based on the [DPS](https://github.com/DPS2022/diffusion-posterior-sampling) codebase.



**Diffusion Posterior Proximal Sampling for Image Restoration**<br>
[Hongjie Wu](https://hongjie-wu.pages.dev/), Linchao He, Mingqin Zhang, Dongdong Chen, Kunming Luo, Mengting Luo, Ji-Zhe Zhou, Hu Chen and Jiancheng Lv <br>
*ACM Multimedia 2024 Oral*


<img src="https://dpps.pages.dev/static/images/cover1.jpg" alt="concept" width="80%">



## Abstract

Diffusion models have demonstrated remarkable efficacy in generating high-quality samples.
Existing diffusion-based image restoration algorithms exploit pre-trained diffusion models to leverage data priors, yet they still preserve elements inherited from the unconditional generation paradigm.
These strategies initiate the denoising process with pure white noise and incorporate random noise at each generative step, leading to over-smoothed results.
In this paper, we present a refined paradigm for diffusion-based image restoration. Specifically, we opt for a sample consistent with the measurement identity at each generative step, exploiting the sampling selection as an avenue for output stability and enhancement. The number of candidate samples used for selection is adaptively determined based on the signal-to-noise ratio of the timestep.
Additionally, we start the restoration process with an initialization combined with the measurement signal, providing supplementary information to better align the generative process.
Extensive experimental results and analyses validate that our proposed method significantly enhances image restoration performance while consuming negligible additional computational resources.

<img src="https://dpps.pages.dev/static/images/proposed.jpg" alt="concept" width="90%">



## Citation
If you find our work interesting, please consider citing

```
@article{wu2024diffusion,
  title={Diffusion Posterior Proximal Sampling for Image Restoration},
  author={Wu, Hongjie and He, Linchao and Zhang, Mingqin and Chen, Dongdong and Luo, Kunming and Luo, Mengting and Zhou, Ji-Zhe and Chen, Hu and Lv, Jiancheng},
  journal={arXiv preprint arXiv:2402.16907},
  year={2024}
}
```
