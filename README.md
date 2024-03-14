# NAPOTD

## NASA Astronomy Picture of the Day

An API to get the current picture from NASA's astronomy picture of the day website.

-----

Every Day NASA posts a new astronomy-related image on https://apod.nasa.gov/apod/

Unfortunately, that image URL changes, so I cannot point to a single URL and get the current image of the day.

This is my solution.  I created a python web API that returns a 302, redirecting you to the image URL by parsing the
code of the website to find the `img` tag.

I am using it to update the background of my phone every day with Tasker.  It's nice.

For convenience, I also dockerized it.