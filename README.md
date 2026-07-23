# aclut2ets2lut
## A LUT to ETS2 LUT generator/converter
### Requirements
- [Python 3](https://www.python.org/downloads/) (click on the latest version)<br>**!! When installing Python, make sure to enable "Add Python to environment variables" !!**
- LUT file [(tutorial between 0:37-2:07)](https://www.youtube.com/watch?v=o8ycizazdgk&t=37)
### How to use this script?
#### Convert LUT file
Put your LUT file into the directory.<br>
Open CMD/Terminal and go to the directory (`cd aclut2ets2lut`)<br>
Run: `python aclut2ets2lut.py <lutfile>` where `<lutfile>` is your LUT file.<br>
After converting, it will put a file called `ffb_lut.sii` in the same directory you're in.<br>

You can proceed to installing automatically using the guide underneath, or install manually using [this guide.](https://modding.scssoft.com/wiki/Documentation/Engine/Advanced_input_configuration/Force_feedback_LUT#Usage)
#### Automatic install
Run: `python install_lut.py`.<br>
It will ask you the following questions:

Where your home directory is located (mostly at C:\Users\user\Documents\Euro Truck Simulator 2 or American Truck Simulator),<br>
What your game profile name is,<br>
And how does the game get saved with (Steam Cloud or Local Save).<br>

If done correctly, it should install to your ETS2/ATS documents folder.

#### Check if the LUT has been loaded correctly
When you load your specific profile with the LUT file, in the main menu, open the Console and click on Custom. Search for `lut`. If you see in the console: `[ffb_lut] Custom force feedback lookup table loaded and configured!`, it has installed correctly. 

You can also see if it loaded by going to your force feedback overall gain settings and seeing a red exclamation mark (see beneath picture).

![Exclamation mark picture](https://github.com/Ardaninho/aclut2ets2lut/blob/main/res/exclmark.png?raw=true)
### Complete
Now your LUT file should be working. Your FFB will feel smoother than normally (or like in Assetto Corsa).<br> 
Happy trucking!

### Credits
[iRacing for their WheelCheck program](https://www.iracing.com/)<br>
[Anis on Overtake.gg for the LUT generator](https://www.overtake.gg/downloads/lut-generator-for-ac.9740/)<br>
[SCS Software about LUT usage in ETS2/ATS](https://modding.scssoft.com/wiki/Documentation/Engine/Advanced_input_configuration/Force_feedback_LUT#Usage)<br>
[Antozzy Gaming for the LUT generation tutorial](https://www.youtube.com/@antozzygaming)