# Workflow to add a new sign

* Create an image for the traffic_sign combination (the height should be as high as needed, the width is 800px)
* Add a line to the table in parking.md that constitutes a new sign with it's tagging
* Save the .md-File in Typora and make sure to close the markdown editor
* Execute the `makeJSON.py`-File in the scripts-Folder
* Open Typora and open parking.md. Export it in `GitHub`-Style as `PDF`, overwrite the file `parking.pdf` in `export/pdf/parking.pdf`
* If everything went correct, the follwing files should show up as changed in GitHub:
	* `parking.md`
	* A new file `img/*.png`
	*  
