---
layout: post
title: 48h Makeathon Project by TUM.ai
date: 2021-11-20 15:01:35 +0300
image: '/images/48h_makeathon.png'
post_url: 2021-02-01-48h-makeathon
---


This past weekend I had the opportunity to participate in the 48 hour Makeathon event which was organised by [TUM.ai](https://www.tum-ai.com) - the largest student initiative in Germany focusing on democratising AI. Out of the [four available tracks](https://www.tum-ai.com/makeathon) I joined the infrastructure and city services track, because I, for one, have never done a project in that field before, and I was really excited to explore the types of problems this industry is currently facing. It was a lot of fun collaborating with my team mates. We interviewed an industry expert and conceptualized an interactive application to support floor plan searching by either *drawing a shape* or by *uploading an existing floor plan*.

Here is short preview of the system.
<img src="images/makeathon2021_final_demo.gif">


**Interview: Opportunity to reuse floor plans**

We conducted an interview with an industry expert who specilized in residential and office buildings to better understand where there are potential areas for improvements. Many cities are currently experiencing the same problem: The number of people moving to the city is larger than there is available housing. During the interview we have discovered that one way the real estate industry is currently trying to cope with this challenge is by reusing existing floor plans as a foundation to design new buildings.

However, most floor plans, although being created digitally, are shared as analog copies. This makes it difficult to reuse them or  search them digitally. Even if there was a shared data base with digitalized floor plans it would be still difficult to describe a floor plan exactly. One option would involve searching by meta information such as number of rooms, size of rooms, etc. This solution, however, does not address visual aspects of the floor plan such as the shape of the rooms and their layout on the plane. The alternative, creating a floor plan from scratch, is often very time-consuming and cost-intensive. 

We therefore proposed an interactive search machine to enable architects to search for matching floor plans by simply drawing its shape. The biggest value of an experienced architects is that they can quickly envision a target plan based on the experience they have made in past projects. It would be easy for them to sketch out the outline of such a plan to search a database and start planning with existing similar floor plans.

**Dataset**
I found the following data set called [CubiCasa5k](https://github.com/CubiCasa/CubiCasa5k) online. It consists of around 5000 floor plans available in different data formats into 80 categories. I converted all images to grey scale, removed noise and kept only the bold border line of the floor plan images. Finally I cropped the images to be all the same size.

<div>
<img src="images/make2021_orig_sample1.jpeg" width="100">
<img src="images/make2021_pp_sample1.jpeg" width="100">
<img src="images/make2021_orig_sample2.jpeg" width="100">
<img src="images/make2021_pp_sample2.jpeg" width="100">
</div>


**Technical outline**

I was in charge of implementing the prototype. Initially, I was skimming through research papers to find potential solutions to the problem, but quickly gave up the hope of finding something simple enough, many of the introduced systems used complex graph based modelling techniques. For the demo I tried to simplify the approach as much as possible witht the goal to have a running prototype that conveys the basic idea. Given the severe time constraints, I decided to implement two sarch input methods:

*User Drawing*. For the demo I manually clustered the dataset into four simple categories: L-shaped, Rectangle-Horizontal, Rectangle-Vertical, Z-Shaped. Each category was then mapped to a number ranging from 0-3. I then trained a **Convolutional NN** to classify user drawn shapes. I drew 100 shapes per category on a Tabletcomputer and also labeled the dataset from 0-3.

<div>
<img src="images/make2021_shapel.jpeg" width="100">
<img src="images/make2021_orig_shapel.jpeg" width="100">
<img src="images/make2021_shape_hor.jpeg" width="100">
<img src="images/make2021_orig_shape_hor.jpeg" width="100">
<img src="images/make2021_shape_vert.jpeg" width="100">
<img src="images/make2021_orig_shape_vert.jpeg" width="100">
<img src="images/make2021_shapez-11.jpeg" width="100">
<img src="images/make2021_orig_shapez-11.jpeg" width="100">
</div>

*User Template Upload*. The user could also upload a template of an existing floor plan and search for similar ones. Here, I trained a **Convolutional Autoencoder** to learn an embedding for each image. I then used the **K-Nearest-Neighbor Search** to retrieve the k closest matches from the data base.




**Conclusion**

I had a lot fun thinking about the problem and hacking this interactive prototype in these 48 hours. We presented the project to the challenge setting company and they really liked interactive search feature. I was incredibly thankful to have had the opportunity to peak behind the curtains of the buildung industry and learn about the types of problems they are trying to solve. This challenge further highlights the potential of human centered artifical intelligence to improve proceses and user experiences across different industries.