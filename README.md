This is a Flask webapp that I plan to use for running challenges in CTF workshops.
It acts as a self hosted system which I will run through a CloudFlare tunnel to get an ip for it.

## Adding Challenges:
* In the python file flags.py, all you need to do to add challenges to the self host is edit the flags dictionary to allign with your challenges. File upload is currently not supported though I am working on it. The category feild in the Challenges class will automatically sort challenges on the challenges page into their correct categories. This will be adjusted later to also include a points system using another ordering method to order by points in their respective categories.

## Running the App:
* Simply use pip to ensure flask is installed, and use the command python app.py. I will add a requirements.txt if the project gets more complicated.

## Future Plans:
* Add a page for workshops where challenges can be stored for specific workshops. Workshops store challenges that can be toggled on or off for fast access and expandability.
* I might also add a register sort of page to track points easier, though this would be a basic system that would reset every workshop. Might be an idea to make this a togglable feature too.

I did use ChatGPT for quick templating and css which was later edited and refined.
