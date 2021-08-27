# Video Converter

## Description
To convert a video to show it on the ring

## Converting Process
1. crop to square and set center as origin
2. sum up every pixel
 1. Find point via polar coordinates in video
 2. Find medium of all 
     1. for_all(y+-epsilon){for_all( x -+ epsilon){medium =+ color}
     2. medium = medium/sum(square(+-epsilon) 
3. stream video to screen