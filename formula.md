## Descriptions
xl = pillar left
xr = pillar right
xm = pillar middle
px = plate (x = 1-5, five being the biggest)

# Formula

## Stuff I learned

number of plates -2 (top & bottom plate) == numbers of towers that need to be built to move the bottom plate.

On a even number of plates the first pillar needs to be the pillar that the plate does't need to move to
On a UNEVEN (%" != 0") number on the pillar that you want your bottom plate to move to.

HOW TO BUILD TOWERS IN BETWEEN?


## Calculate how many steps to solve this are needed
As it turns out (after trying stuff and looking at values for a few minutes) all of the plates have a binary value. Yeah, it's that easy.
![](./images/value_of_layers.png)
Meaning, that if you have 1 plate, you need one step, with two you need 3, with 4 you need 15 and so on.
