# IASS2024 - Building Information Modelling with COMPAS

**Location**
* ETH Hönggerberg Campus, Building HIB, Floor E, E11

**Date**
* Sunday 25th August 2024

**Time**
* 📝 8:00 - Registration
* 🌅 8:30 to 12:30 - Morning Session
* 🍽️ 12:30 to 13:30 - Lunch
* 🌇 13:30 to 17:30 - Afternoon Session

**Documentation**
* [📃 COMPAS docs](https://compas.dev)


:exclamation: **Attention: Please install all requirements, before the workshop** :exclamation:
* [Part 1 - Requirements](#part-1---requirements)
* [Part 2 - Conda Environment](#part-2---conda-environment)
* [Part 3 - Visual Studio Code](#part-3---visual-studio-code)
* [Part 4 - Rhino and Blender](#part-4---rhino-and-blender)

**Slack**
* :loudspeaker: If you need help, please post a note on the workshop Slack channel: [Join Slack](https://join.slack.com/t/iass2024/invite/enQtNzQ4NjM2NzgxNjExOC0xMDFkNTc3MzIwYjUwMjg2ZTBjMzNlNjY0NzY4MzUxMzZhNTdhMDhhNmExZWU1MjViMThlNWMyYjdlMWViZWNk?x=x-p7478427615159-7492983888418-7490099579333)

**Presentation**
* [**Installation Slides**](https://docs.google.com/presentation/d/16EuhLaW2rxKc8An3LFzQjU9iB8ruaGXISeOHUOhu5rw/edit#slide=id.g2f4bba232ed_1_43)
* [IASS 2024 - Building Information Modelling with COMPAS](https://docs.google.com/presentation/d/1jFXqqwnK6FNqnpAwlR4I0-DgS6SMbqrILT1w2i2q2XQ/edit?pli=1#slide=id.p)

## Part 1 - Requirements

* Minimum OS: Windows 10 Pro or Mac OS Sierra 10.12
* [Anaconda 3](https://www.anaconda.com/), or miniconda if you prefer...
* [Git](https://git-scm.com/)
* [Visual Studio Code](https://code.visualstudio.com/) with the `Python` and `Pylance` extensions from Microsoft.
* [Rhino 8](https://www.rhino3d.com/download) 
* [Blender 4.0](https://download.blender.org/release/Blender4.0/)

<div align="center">
  <video src="https://github.com/user-attachments/assets/74884b1b-3bac-4080-9275-eb9bcdff3209" controls>
    Your browser does not support the video tag.
  </video>
</div>

## Part 2 - Conda Environment

> **IMPORTANT**: If you're on Windows, all commands below have to be executed in the *Anaconda Prompt* (NOT the *Command Prompt*)

We use `conda` to make sure we have clean, isolated environment for dependencies.

Download workshop files by cloning the GitHub repository:

    git clone https://github.com/compas-Workshops/IASS2024.git

Then create the workshop environment and install the dependencies:

    conda env create -f env.yml


[comment]: <> ( Incase mistakes were made, remove the current environment and try again: ```conda deactivate && conda env remove -n iass2024 && conda clean --all``` )

### Verify installation

Activate the environment

    conda activate iass2024

> **NOTE**: You should see that your prompt changed from `(base)` to `(iass2024)`

Run the verification command `python -m compas`:

    (iass2024) python -m compas

    Yay! COMPAS is installed correctly!

    COMPAS: 2.3.0
    Python: 3.10.0 (CPython)
    Extensions: ['compas', 'compas-notebook', 'compas-occ', 'compas-ifc', 'compas-viewer', 'compas-fd', 'compas-model']


<div align="center">
  <video src="https://github.com/user-attachments/assets/17b311f6-9dcf-4598-afd8-3f3c2a53e9f8" controls>
    Your browser does not support the video tag.
  </video>
</div>

## Part 3 - Visual Studio Code

We will run the Python examples in Visual-Studio-Code editor.
When you open Visual-Studio-Code:
* select the right conda environment by "ctrl+shift+p". 
* click on "Python: Select Interpreter" 
* click on "Python 3.10 ('iass2024')"
* be sure that the terminal shows 'iass2024' else type again conda activate 'iass2024'

<div align="center">
  <video src="https://github.com/user-attachments/assets/0423c780-c774-47f8-8c4c-17e2b394fc94" controls>
    Your browser does not support the video tag.
  </video>
</div>

## Part 4 - Rhino and Blender

Compas, compas-Fofin, compas_ifc in CAD python editors have to be installed using the following workflow :
* Rhino installation: https://compas.dev/compas/latest/userguide/cad.rhino8.html
* Blender installation: https://compas.dev/compas/latest/userguide/cad.blender.html

<div align="center">
  <video src="https://github.com/user-attachments/assets/c8db40a8-1e14-4165-8a02-0eccf571bb18" controls>
    Your browser does not support the video tag.
  </video>
</div>






