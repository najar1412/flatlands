<div  class="markdown-info">
 
<div  class="markdown-info-body">

This Post is currently a work in progress. If you'd like to know when its finished go ahead and add your email to the mailing list at the bottom of the page!

</div>
</div>

_Pano is an interactive panorama manager. The app is aimed at 3d/visualization professionals, but great care is being taken to allow anyone to use it._

### what?

There are a couple of different ways to do interactive panoramas. Pano is focused on the traditional technique of somehow getting a 360 degree image (whether via photography or 3d rendering), projecting it onto a sphere and placing a camera at the spheres center for the user to use to move around.

explain interactive panos
screenshots/examples

### current panorama software

The current generation of panoramas sit on the boundaries of the uncanny valley. They look good, they just they don't look *correct*.

One of the biggest culprits is [parallax](https://simple.wikipedia.org/wiki/Parallax). Parallax is the perceived change in position of an object seen from two different places. This phenomenon is the only real way for the user to judge distances within an image. 

<div  class="markdown-tip">
<div  class="markdown-tip-body">
You can see this in everyday life too, just stand at the top of a long street and look towards the other end. Take a couple of steps to the left or right. 
Can you see objects getting occluded or revealing themselves from behind foreground objects? That's Parallax.
</div>
</div>

Common optical problems are also left out of standard panorama software these may seem like problems, but to the average eye _not_ seeing these things will affect the realism. Things like chromatic aberration, lens distortion and glare.

[images: CA, LD and glare examples]

<div  class="markdown-info">
 
<div  class="markdown-info-body">
In the 3d rendering world imperfection is what makes realism. Having a surface that's super clean without the dirt and grim, without the knocks and dings of everyday life is what makes the surface look fake. It's these imperfections that'll need to be implemented to take interactive panoramas to the next level.
</div>
</div>

### what i'd  like to build

With the underlining goal of implementation parallax into traditional panorama views. I'd also like to build a management system - for the management of multiple pano's, this includes iterations of the same panorama.

Post production on already uploaded panoramas would be great too. Basic color correction, temperature and environment controls.

And finally all the other controls necessary to produce a high resolution, realistic interactive panorama.