---
layout: post
title: 48h Makeathon Project by TUM.ai
date: 2021-11-20 15:01:35 +0300
image: '/images/48h_makeathon.png'
post_url: 2021-02-01-48h-makeathon
---


This past weekend I had the opportunity to participate in the 48-hour Makeathon event, which was organized by[TUM.ai](https://www.tum-ai.com) - the largest student initiative in Germany focusing on democratizing AI. Out of the [four available tracks](https://www.tum-ai.com/makeathon) I joined the infrastructure and city services track because I, for one, have never done a project in that field before. I was excited to explore the types of problems this industry faces. It was a lot of fun collaborating with my teammates. We interviewed an industry expert and conceptualized an interactive application to support floor plan searching by drawing a shape or uploading an existing floor plan.

Here is short preview of the system.
<img src="images/makeathon2021_final_demo.gif">


**Interview: Opportunity to reuse floor plans**

We interviewed an industry expert who specialized in residential and office buildings to better understand where there are potential areas for improvement. Many cities are experiencing the same problem: The number of people moving to the town exceeds available housing. During the interview, we discovered that the real estate industry is currently trying to cope with this challenge by reusing existing floor plans as a foundation to design new buildings.

However, most floor plans, although being created digitally, are shared as analog copies. This makes it difficult to reuse them or search for them digitally. Furthermore, even if there was a shared database with digitalized floor plans, it would still be challenging to describe a floor plan exactly. One option would involve searching by meta-information such as the number of rooms, size of rooms, etc. However, this solution does not address the floor plan's visual aspects, such as the rooms' shape and layout on the plane. The alternative, creating a floor plan from scratch, is often very time-consuming and cost-intensive.

We, therefore, proposed an interactive search machine to enable architects to search for matching floor plans by simply drawing its shape. The most significant value of experienced architects is that they can quickly envision a targeted scenario based on the experience they have had in past projects. It would be easy for them to sketch out the outline of such a plan to search a database and start planning with similar floor plans.

**Dataset**
I found the following data set called [CubiCasa5k](https://github.com/CubiCasa/CubiCasa5k) online.  It consists of around 5000-floor plans available in different data formats into 80 categories. First, I converted all images to a greyscale, removed noise, and kept only the bold border line of the floor plan images. Finally, I cropped the images to be all the same size.

<div>
<img src="images/make2021_orig_sample1.jpeg" width="100">
<img src="images/make2021_pp_sample1.jpeg" width="100">
<img src="images/make2021_orig_sample2.jpeg" width="100">
<img src="images/make2021_pp_sample2.jpeg" width="100">
</div>


**Technical outline**

I conceptualized and built the prototype. Initially, I skimmed through research papers to find potential solutions to the problem but quickly gave up the hope of finding something simple. Many of the introduced systems used complex graph-based modeling techniques. For the demo, I tried to simplify the approach as much as possible to have a running prototype that conveyed the basic idea. Given the severe time constraints, I decided to implement two search input methods:
User Drawing. I manually clustered the dataset for the demo into four simple categories: L-shaped, Rectangle-Horizontal, Rectangle-Vertical, and Z-Shaped. Each class was then mapped to a number ranging from 0 to 3. I then trained a **Convolutional NN** to classify user-drawn shapes. I drew 100 shapes per category on a Tablet computer and labeled the dataset from 0 to 3.

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

*User Template Upload*. The user could also upload a template of an existing floor plan and search for similar ones. I trained a **Convolutional Autoencoder** to learn an embedding for each image. I then used the **K-Nearest-Neighbor Search** to retrieve the k closest matches from the database.


**Conclusion**

I had a lot of fun thinking about the problem and hacking this interactive prototype in these 48 hours. We presented the project to the challenge-setting company, and they really liked the interactive search feature. I was incredibly thankful to have had the opportunity to peek behind the curtains of the building industry and learn about the problems they are trying to solve. This challenge further highlights the potential of human-centered artificial intelligence to improve processes and user experiences across different industries.