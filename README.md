# The-Invisible-Cloak
Implementation of program that behave in a manner to imtate the invisibility cloak of Harry Potter!

This technique is opposite to the Green Screening. In green screening, we remove background but here we will remove the foreground frame.
1. Capture and store the background frame
2. Detect the defined color using color detection and segmentation algorithm.
3. Segment out the defined colored part by generating a mask.
4. Generate the final augmented output to create a magical effect. [ output.avi ]