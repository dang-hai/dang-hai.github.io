---
layout: post
title: ACM CHI'22 - GANSlider
date: 2022-02-01 15:01:35 +0300
image: '/images/ganslider_thumbnail.png'
post_url: 2022-02-01-ganslider
---

**GANSlider: How Users Control Generative Models for Images using Multiple Sliders with and without Feedforward Information**<br>
Hai Dang<sup>1</sup>, Lukas Mecke<sup>2,3</sup>, Daniel Buschek<sup>1</sup><br>
<sup>1</sup>University of Bayreuth, <sup>2</sup>Bundeswehr University Munich, <sup>3</sup>LMU Munich<br>

<p align="justify"><b>Paper Link:</b> 
<a href="https://arxiv.org/pdf/2202.00965.pdf">Arxiv</a>, 
<a href="https://dl.acm.org/doi/abs/10.1145/3491102.3502141">ACM Library</a>

<iframe width="560" height="315" src="https://www.youtube.com/embed/uhQPxD1tyf8" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

I am happy to announce that my second full paper was accepted for CHI'22 in New Orleans. While there is an increasing interest in generative tools, we still lack an in-depth understanding of how users perceive and interact with them. 

<img src="/images/reconstructions.gif" alt="Reconstructions" width="1024px"/>

Today's research and commercial applications [1] often provide a slider interface to control generative models. Each slider therein manipulates a particular attribute of the image, for example, to control semantic facial expressions such as smiling or frowning or changing the hair color (Figure 1). 

<img src="/images/ganspace.jpeg" alt="slider interface" width="1024px"/>

In many situations, clear dimensions (i.e., smiling or hair color) are not available or only so with additional optimization effort. More often, the sliders may affect multiple aspects of the image simultaneously. In these situations, it is up to the user to make sense of and interpret the individual control dimensions (Figure 2). 

<img src="/images/ganspace_unknown.png" alt="Teaser figure" width="1024px"/>

Instead,  we introduced Filmstrip-like sliders (Figure 3) to support users to make more informed interactions by showing previews of the different states along each control dimension. Participants in our user study were asked to reconstruct a target image by manipulating a set of sliders. One of the findings demonstrated that users made more unnecessary interactions when using regular sliders without the preview. Furthermore, in the absence of any feedback on the individual control dimensions, the only way for users to learn about individual sliders is to interact with them, adding to the total number of unnecessary interactions. On the other hand, the Filmstrip slider allowed users to make more strategic interaction decisions. Please refer to our paper if you want to know more about how we quantified and evaluated our user study.

<img src="/images/ganslider_teaser.png" alt="Reconstructions" width="1024px"/>

Although slider interfaces are frequently used, there is still room for improvement. The Filmstrip slider is one step in that direction. In addition, we may also have to rethink to what degree current UI elements are still suitable when working with new generative systems.


