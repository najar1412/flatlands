Where i work our bread and butter is in the production of computer generated imagery (CGI). Fully CG or partially CG images of commercial or residential buildings yet to be completed. These images are made up of 4 key aspects; composition, the scheme, lighting and assets. All with the final goal of advertising to potential buyers. Its an interesting environment to develop in, mixing code and computer generated imagery. This post is focused on the management of our assets, how an unmanaged library can be expensive and how we went about solving it.

### What's considered an asset?

When I say assets i’m mainly referring to [3D models](https://en.wikipedia.org/wiki/3D_modeling) complete with textures that can be placed into a 3d modelling environment and rendered to a high resolution realistic image. A 3d assets could be a table, car, street lamp. Honestly, anything.

### How does this work with the library?

Our library is filled to the brim of assets. This post will only be discussing the type of asset described above - but for background - other ‘types’ of asset include (but not limited to) 2d imagery, footage and light information (.ies).

We categories 3d assets by a couple of different criteria.
Asset type - is it a street lamp, a car or a table.
Asset Packs - Many 3d modelling companies offer packs of assets. 30 Kitchen utensils, or a pack of 10 winter trees.
General location - a bathroom will have the assets of a bar of soup, shower curtains and facets or an office might have work desks, phones, computers and binders.

We store all 3d assets in nested folders. 
[example image: bathroom > soap, shower curtain. Office > work desks, phones and computers]

99% of the time these assets will be imported directly into the 3d animation software. This will usually import the geometry completely with symbolic links to any related textures.

Current costs of running the library
After a bit of napkin math and some more than biased testing conditions involving a stopwatch and a list of items to find in the library. We came to the conclusion that it takes approx 6 minutes to find an object. With n amount of assets per image and a set number of images to complete per month. It worked out around ~180 hours per 5 artists were spent on finding assets per month. 
Now these numbers are guesstimates at best, but - from personal experience - aren’t that unrealistic. Unfortunately i couldn’t find any hard numbers online to compare such a niche query so I had to instead take the results as a sort of baseline. Any solutions found - at minimum - should shatter those numbers or it would be a waste of time.

### Additional library specific issues

With the underlying goal of drastically reducing that 180 hour number I wanted to get other user’s feedback on their experience of using the library. The biggest takeaways from this were as follows;

Non-ability of being able to search the library efficiently.
Missing, duplicated or edited models and textures (overwritten).
On boarding of new fulltime or freelancing artist.
Too much maintenance time.
No one really knows whats in there

Some are incredibly outdated, others are missing texture maps, or have had textures edited and saved over etc. Imagine if [Bernard Black](https://en.wikipedia.org/wiki/Black_Books) sold 3d asset.

What gives this an extra layer of complexity is all our offices are scattered around the globe. Each having their own libraries to maintain with zero standards in place.

Over the years a few people have taken it upon themselves to sort and clean the library - heroes - these attempts are never actually finished however. The next person then tries with injecting their ideas of how the library should be interacted with ultimately making it harder to navigate. 

It’s now at the point that only people whom have been here for a few years actually know where things are, or even worst make their own library inside the library...

<quote>Something that's ¼ of our deliverables shouldn't be left to die.</quote>



### Compile collected information as baseline


test
