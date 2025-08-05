FINAL ANSWER IS PART 2.

====== How to use the app ======

Download the files called part1.py and part2.py on your system locally. Ensure you have python installed on your system. 
Ensure you have images with jpg extension to test the program with.
There is a PIL dependency. So you should install it by running the following command:
pip install pillow

To run the program, run the following command:
python part2.py <absolute_image_path>

Example:
python part2.py "C:\TMMC_interview_assignment\img_1.jpg"

Do similarly for part1.py to run the part1.py program.

========= Assumption ===========

I was not sure about an assumption. Therefore, I decided to implement both the scenarios I could think of.

In the question, it says "The same line will exist on both the top half of the image and the bottom half as 
a continuous straight line." 

When we visualize the entire image as a matrix of pixels with each cell having either one of two values i.e. black and white. 

I was not sure about the following fact:
For any given vertical line, would it cross through the middle row of the image. In other words, would 
the middle row of the image have the pixel black for each vertical line.

So, divided the question into two parts.

Part 1: 

Line definitely exists on both halves.
For any given vertical line, the middle row of the image for that particular line will definitely be black.

Part 2: 

Line may not exist on the middle row of the image.
For any given vertical line, the middle row of the image for that particular line may not be black.


========== My Approach ==========

Part 1:

If we look at the middle row of the image. You could think of it as a 1d array/list. Connected/adjacent black 
cells represent one line. If there is a white cell between the two black cells, then that is a separation between two lines.
So the question comes down to counting the number of subarrays with all black cells.

Part 2:

Here, we cannot rely on the middle row of the image. Therefore, I am using BFS (Breadth First Search) Algorithm to identify different
islands of black on white background. 

I convert the image into a 2d grid of 1s and 0s. 1 representing black and 0 representing white. Then, I use BFS approach to find 
the number of islands of 1s in a sea of 0s. We only consider up, down, left, right as connected cells and diagonal cells as not connected. 
That is 4-Connectivity (No Diagonal). The answer could be extended to 8-Connectivity. However, Idid not think that was necessary since we 
are counting vertical lines and not zig-zag.


============== Note ===============

Part 1 is faster. However, it might not pass all the cases if the assumption is not true. 
Part 2 should pass all the cases.

My Final answer is Part 2.

