---
layout: post
title: Paper Accepted at ACM CHI'21 - GestureMap 
date: 2021-02-01 15:01:35 +0300
image: '/images/chi21_logo.png'
post_url: 2021-02-01-gesturemap
---

My first paper has been accepted to the ACM CHI'21 conference. Although this work was an extension of my master thesis, it still required many iterations and additions before it was ready to be submitted to the conference. I spent many weeks working on this project and I'm incredibly relieved to see it finally being featured at CHI'21 - one of the biggest conference for human-computer-interaction. In this work I've built an interactive tool to analyse behavioral gesture data for the control of interactive systems. The key feature in this tool is the underlying generative model which I used to automatically learn feature representations for the 3D depth sensor motion training data. I've then used these representations to build a map displaying all the behavior captured in the underlying dataset. The tool also allows users to simulate new "unseen" behavior by leveraging the generative model to create new motion data points. Feel free to checkout the paper linked below for further details.

<iframe width="560" height="315" src="https://www.youtube.com/embed/IWwotWgsBFU" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>


<img src="/images/gesturemap_teaser.png" alt="Teaser figure" width="1024px"/>

**GestureMap: Supporting Visual Analytics and Quantitative Analysis of Motion Elicitation Data by Learning 2D Embedding**<br>
Hai Dang<sup>1</sup>, Daniel Buschek<sup>1</sup><br>
<sup>1</sup>University of Bayreuth<br>


<a href="https://arxiv.org/pdf/2103.00912.pdf">**Read Paper**</a> 


<p align="justify"><b>Abstract:</b> <i>This paper presents GestureMap, a visual analytics tool for gesture elicitation which directly visualises the space of gestures. Con- cretely, a Variational Autoencoder embeds gestures recorded as 3D skeletons on an interactive 2D map. GestureMap further integrates three computational capabilities to connect exploration to quan- titative measures: Leveraging DTW Barycenter Averaging (DBA), we compute average gestures to 1) represent gesture groups at a glance; 2) compute a new consensus measure (variance around average gesture); and 3) cluster gestures with k-means. We evaluate GestureMap and its concepts with eight experts and an in-depth analysis of published data. Our findings show how GestureMap facilitates exploring large datasets and helps researchers to gain a visual understanding of elicited gesture spaces. It further opens new directions, such as comparing elicitations across studies. We discuss implications for elicitation studies and research, and opportunities to extend our approach to additional tasks in gesture elicitation.
</i></p>

<iframe width="560" height="315" src="https://www.youtube.com/embed/DgIRlwZhCVQ" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>