# Auto-Image-Map-Segmentation
In HTML, the <map> tag defines an image-map. An image-map is an image with clickable areas. The idea behind the image map is you should be able to perform different actions depending on where in the image you click.  To create an image map you need an image and a map containing some rules that describe the clickable areas.  Traditionally, users have to define coordinates themselves to  be able to place the clickable areas onto the image.  However, depending on the size of the image and the number of areas a user needs, this can be a time-consuming exercise. By using the skimage library, some of that work can be automated.  By supplying an image to the 'image' variable and specifying  the number of segments needed in the 'num_segments' variable and the 'compactness' variables,  the coordinates of the image countours can be extracted and the subsequent HTML map co-ordinates produced automatically.

To run the code, you need to have a .jpg file that you want to segment into an HTML image map.

Save the 'Africa.jpg' and 'Image Map Example.html' files to your desktop. 
Run the Python code.
An 'Image Map Coords.txt' will be produced containing your image map coorindates.
Open the 'Image Map Example.html' in a text editor, and replace the <<image map boiler plate>> text with the output from the Image Map        Coords.txt
Save the html file.
Open the html file with any browser to see how successful the automatic segmentation is. You will likely have to tweak the 'num_segments'   and 'compactness' variables to get the best map.
  
You can change the href value for each map segment to link to another webpage.

