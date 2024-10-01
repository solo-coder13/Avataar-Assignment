# Avataar-Assignment
Analyzing the process of image generation using Stable Diffusion and ControlNet, with a focus on user-guided prompts and additional control inputs like depth and normal maps.

## Introduction

This project is focused on generating high-quality images from text prompts using Stable Diffusion (SD), guided by additional conditioning inputs such as depth maps, normal maps, and canny edges, with the help of ControlNet. The assignment aims to dissect the image generation pipeline and explore different conditioning techniques, analyze generation quality with varying aspect ratios, and optimize generation latency.

## Problem Statement

We have been provided with metadata that includes text prompts and depth maps. The task is to generate the best possible images using Stable Diffusion, and further experiment with different aspect ratios and latency reduction techniques.

### Key Deliverables:
1. **Generate the best possible output images** using the given prompts and depth maps, optionally combining depth with other conditioning like normals and canny edges.
2. **Generate images with different aspect ratios** and compare the quality against the standard 1:1 aspect ratio.
3. **Analyze generation latency**, suggest optimizations, and explore the trade-offs between latency reduction and image quality.

## Requirements

### Libraries and Dependencies
- Python 3.x
- PyTorch
- Hugging Face `diffusers` library (for Stable Diffusion)
- ControlNet (can be integrated via diffusers or ControlNet-specific library)
- OpenCV (for canny edge detection and other image processing tasks)
- NumPy (for handling `.npy` files)
- Matplotlib (for visualizing results)
