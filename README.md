# Projects Template Manual

Welcome to this neat template for quickly creating an index of all projects your group is working on! We figured out how to set everything up so that **_you can effortlessly deploy it in under 5 minutes_** and have your group members (probably students) populate it with minimal knowledge or effort. It should work well for class projects, too!

[See Our Page as a Demo](https://software.phaseslab.org/){: .btn }

## How to set up? (step-by-step)

1. Follow the big green `Use this template` and select `Create a new repository` **OR** fork it if you would like to contribute in the future.
1. You will now see some mess, but don't worry! Once you populate the links, in a few minutes, it should look all good 😊.
1. You will only need to exit 2 files! The `README.md` holds all content, while `_congif.yml` holds some configuration metadata.
1. In `README.md`, replace all `<< Your Group Name >>` fields with the actual name of your group. You can do it manually (there aren't many), or, if you are editing locally on Unix (Linux/Mac) or using GitHub Codespaces (Linux), you can open do it automatically with `sed -i 's/<< Your Group Name >>/SuperNiceGroup/g' README.MD`. Do the same thing with `<< Your Group URL >>`. 
1. In `_congif.yml`, do the same as above. You should also change the `<< Your Title >>` that will show up in the top-left corner and adjust other links as needed so that they point to your resources, like the group homepage or class dashboard.
1. **You are now ready to take it online!** Simply go to `Settings > Pages > Build and deployment`, click on the `Source`'s dropdown menu, select `Actions`, and don't do anything else here. Make _any_ change to the `README.md` and push it. 
1. **Wait around 45s, and boom, done! Your site should now be online!** You should see a tan dot (still working) or green checkmark (done) next to your last commit message. If not, you may need to enable workflows under `Actions`.
1. To allow others to contribute directly, if you trust them, you should give them write access under `Settings > Collaborators`, or explain to them how to (1) fork a repository and (2) do pull requests.
1. Once the content is ready, remove these instructions by simply deleting everything above the `# << Your Group Name >> Projects` header. You have a backup at the end of this document.
1. To make further customizations, you can consult the manual for [the underlying Jekyll theme](https://just-the-docs.com/), which, as of September 2023, is actively developed and maintained. 

## How to add yourself in under a minute?

1. _(If you have write access)_ Open this repository page in developer mode by simply clicking the `.` key, and `README.md` should just pop up, ready for your changes.
1. Under **Active Group Members**, put (1) your name between `**'s, (2) replace `<< GitHub username>>` with your user name, (3) replace `<< ORCID ID number>>` with your ORCID ID (just the numbers).
1. Go to the `Source Control` icon on the left panel (third from the top, will have a blue mark if you edited anything), write a short message about what you did, and click _Commit&Push_. Done!

## How to quickly contribute a project to the list?

1. Start by using the _Legend_ to figure out where your project belongs within the page structure.
1. This part is very flexible, and you can tune it to your favorite flavor. You just create a new entry in a list with the `- ` symbol, copy-paste appropriate markers based on the _Legend_, and write out the bold name of the software / project / assignment alongside a hyperlink to the GitHub/GitLab repository `[**<< software name >>**](https://github.com/<< repo holder >>/<< repo name >>)` followed by a short description. Examples (a few taken from Phases Research Lab in September 2023) are provided and should get you started pretty quickly!
1. Under your description, you can add live badges, which will update over time! This lets you see which projects are active, well-tested, and released (e.g., on PyPI). You can also link papers this way. You can either (1) get them from a service like [shields.io](https://shields.io/) or (2) change values in URLs as appropriate. The first (broken) example shows which ones should be replaced with `<< repo holder >>`, `<< repo name >>`, `<< branch >>`, `<< docs address >>`, and `<< software name >>` to get ones like in the second example.
1. Go to the `Source Control` icon on the left panel (third from the top, will have a blue mark if you edited anything), write a short message about what you just added, and click _Commit&Push_. Done!


# << Your Group Name >> Projects
This repository serves as an index of all software projects [<< Your Group Name >>](<< Your Group URL >>) group members are working on, from small and private ones to large and open-source ones, emphasizing the latter.

**Contents:**
[**Active Development**](#active-development) ([Open](#open-) | [Staging](#staging-) | [Internal](#internal-))  &nbsp;|&nbsp;  [**Active Contributions**](#active-contributions)  &nbsp;|&nbsp;  [**Maintained**](#maintained)  &nbsp;|&nbsp;  [**Legacy**](#legacy)  &nbsp;|&nbsp;  [**Other**](#other)  &nbsp;|&nbsp;  [**Alumni Work**](#alumni-work)

**Active Group Members** (ordered by GitHub activity):   
[**John Template** <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/github.svg" width="16" height="16">](https://github.com/<< GitHub username>>) [![orcidlogo](https://info.orcid.org/wp-content/uploads/2019/11/orcid_16x16.png)](https://orcid.org/<< ORCID ID number>>)&nbsp; | &nbsp;
[**Allice Example** <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/github.svg" width="16" height="16">](https://github.com/<< GitHub username>>) [![orcidlogo](https://info.orcid.org/wp-content/uploads/2019/11/orcid_16x16.png)](https://orcid.org/<< ORCID ID number>>)&nbsp; | &nbsp;
[**Some Cool PostDoc** <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/github.svg" width="16" height="16">](https://github.com/<< GitHub username>>) [![orcidlogo](https://info.orcid.org/wp-content/uploads/2019/11/orcid_16x16.png)](https://orcid.org/<< ORCID ID number>>)&nbsp; | &nbsp;
[**Prof. Big Shot** <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/github.svg" width="16" height="16">](https://github.com/<< GitHub username>>) [![orcidlogo](https://info.orcid.org/wp-content/uploads/2019/11/orcid_16x16.png)](https://orcid.org/<< ORCID ID number>>)&nbsp; | &nbsp;


**Legend:**
- 🟢 Open Source / 🟠 Release Soon / 🔴 Internal or Private
- ✅ User-Ready / 🔬 Research-Ready / 🏗 Under Construction and Experimental / 💤 Not-Supported
- 🤏 Small Codes or Modifications

## Active Development

- _Ordered open-to-internal, ready-to-experimental, and large-to-small._
- Unless specified, the lead developer/s are active PRL members

### Open 🟢

- 🟢 ✅ [**<< software name >>**](https://github.com/<< repo holder >>/<< repo name >>) - this software is a novel tool for combinatorial exploration of perovskite chemical space 

  [![GitHub last commit (by committer)](https://img.shields.io/github/last-commit/<< repo holder >>/<< repo name >>?label=Last%20Commit)](https://github.com/<< repo holder >>/<< repo name >>)
  [![latest](https://img.shields.io/badge/Read%20The%20Docs-Latest-green)](https://<< docs address >>)
  [![codecov](https://codecov.io/gh/<< repo holder >>/<< repo name >>/branch/<< branch >>/graph/badge.svg?token=Fu7FJZeJu0)](https://codecov.io/gh/<< repo holder >>/<< repo name >>)
  [![PyPI version](https://badge.fury.io/py/<< software name >>.svg)](https://pypi.org/project/<< software name >>)

- 🟢 ✅ [**pySIPFENN**](https://github.com/PhasesResearchLab/pySIPFENN) - py(**S**tructure-**I**nformed **P**rediction of **F**ormation **E**nergy using **N**eural **N**etworks) allows for easy prediction of formation energy out-of-the-box (🟢✅) and using small-dataset ML through transfer learning-based adjustment of models to new materials (🟠) and properties (🔴).

  [![GitHub last commit (by committer)](https://img.shields.io/github/last-commit/PhasesResearchLab/pysipfenn?label=Last%20Commit)](https://github.com/PhasesResearchLab/pySIPFENN)
  [![latest](https://img.shields.io/badge/Read%20The%20Docs-Latest-green)](https://pysipfenn.readthedocs.io/en/latest/)
  [![codecov](https://codecov.io/gh/PhasesResearchLab/pySIPFENN/branch/main/graph/badge.svg?token=S2J0KR0WKQ)](https://codecov.io/gh/PhasesResearchLab/pySIPFENN)
  [![PyPI version](https://badge.fury.io/py/pysipfenn.svg)](https://pypi.org/project/pysipfenn)

- 🟢 🔬 [**fmat**](https://github.com/HUISUN24/feasibility_map) - **F**easibility of **MAT**erials mapper is a CALPHAD-based tool helping avoid the formation of undesired phases and designing optimal composition pathway to join dissimilar materials. It provides a comprehensive understanding of the phase formation process during manufacturing processes through prediction of both equilibrium and non-equilibrium phases.

  [![GitHub last commit (by committer)](https://img.shields.io/github/last-commit/HUISUN24/feasibility_map?label=Last%20Commit)](https://github.com/HUISUN24/feasibility_map)
  [![PyPI version](https://badge.fury.io/py/fmat.svg)](https://pypi.org/project/fmat)

- 🤏 🟢 ✅ [**pqam-dparamhu2021**](https://github.com/amkrajewski/pqam-dparamhu2021) - **P**y**QA**lloy-compatible **M**odel for alloy **D** **Param**eter prediction based on Yong-Jie **Hu**'s **2021** literature model (in R) which has been optimized for high-throughput and wrapped in Python.

  [![GitHub last commit (by committer)](https://img.shields.io/github/last-commit/amkrajewski/pqam-dparamhu2021?label=Last%20Commit)](https://github.com/amkrajewski/pqam-dparamhu2021)
  [![PyPI version](https://badge.fury.io/py/pqam-dparamhu2021.svg)](https://pypi.org/project/pqam-dparamhu2021)

- 🤏 🟢 🔬 [**optimade-python-tools-mpdd**](https://github.com/PhasesResearchLab/optimade-python-tools-mpdd) - fork of [**Materials-Consortia/optimade-python-tools**](https://github.com/Materials-Consortia/optimade-python-tools) by [@ml-evs](https://github.com/ml-evs); tuned to the needs of MPDD and, more generally, other very large memory IO limited materials databases.

  [![GitHub last commit (by committer)](https://img.shields.io/github/last-commit/PhasesResearchLab/optimade-python-tools-mpdd?label=Last%20Commit)](https://github.com/PhasesResearchLab/optimade-python-tools-mpdd)
  [![Static Badge](https://img.shields.io/badge/OPTIMADE_Endpoint-MPDD-purple)](http://mpddoptimade.phaseslab.com/)


### Staging 🟠

- 🟠/🟢 ✅ **MPDD** ([**server**](https://github.com/PhasesResearchLab/MPDD-server) & [**tools**](https://github.com/PhasesResearchLab/MPDD-OPTIMADE)) - **M**aterial-**P**roperty-**D**escriptor **D**atabase is an atomistic data processing infrastructure allowing decentralized featurization (calculation of descriptors) and rapid machine learning model deployment on millions of DFT-relaxed configurations. Data is openly served through [**OPTIMADE**](https://github.com/Materials-Consortia/OPTIMADE) API at [mpddoptimade.phaseslab.com](http://mpddoptimade.phaseslab.com/) (🟢), but the high-throughput API and source code for server and client are kept internal for now (🟠). 

- 🟠 🔬 [**nimplex**](https://github.com/amkrajewski/nimplex) - **NIM** sim**PLEX**  A small scientific library for providing uniform density random/grid sampling on N-dimensional simplex spaces in Nim language.

- 🟠 🏗 [[**Third Generation Pure Element with Pycalphad and ESPEI**]](https://github.com/amr8004/PureElementPRL)
Custom installations of pycalphad and ESPEI with common 3rd generation CALPHAD models as well as built in experimental Cp data fitting for model parameters.

### Internal 🔴

- 🔴 🔬 [**ULTERA**](https://github.com/PhasesResearchLab/ULTERA) - _Internal_ set of software tools developed within ULTERA projects, which will be individually released (e.g., PyQAlloy 🟢) or kept internal.

- 🔴 🏗 **PyZentropy** - Python toolset to implement the Zentropy approach ([doi.org/10.1007/s11669-022-00942-z](https://doi.org/10.1007/s11669-022-00942-z)) described in brief in [this news article](https://www.psu.edu/news/materials-research-institute/story/zentropy-and-art-creating-new-ferroelectric-materials/)
  

## Active Contributions

- 🟢 [**pymatgen**](https://github.com/amkrajewski/pymatgen): 
  - 2023: 1 enhancement and 1 bug fix, both to _pymatgen.**core**_ 
  - 2017: 1 enhancement to _pymatgen.**analysis**_ and 1 bug fix to _pymatgen.**io**_ 

- 


## Maintained

- 🟢 ✅ [**DFTTK**](https://github.com/PhasesResearchLab/dfttk) - The goal of DFTTK is to make high-throughput first-principles calculations as simple as possible.

- 🟢 ✅ [**scheil**](https://github.com/pycalphad/scheil) - A Scheil-Gulliver simulation tool using pycalphad.

- 


## Legacy

- 🟢 💤 [**nanograin**](https://github.com/PhasesResearchLab/nanograin)

- 🟢 💤 [**prlworkflows**](https://github.com/PhasesResearchLab/prlworkflows)

- 🟢 💤 [**popparsing**](https://github.com/PhasesResearchLab/popparsing)

- 



## Other

-



## Alumni Work

- 🟢 ✅ [**kawin**](https://github.com/materialsgenomefoundation/kawin) - Python implementation of the Kampmann-Wagner Numerical (KWN) model to predict precipitate nucleation and growth behavior. This package couples with pycalphad to perform thermodynamic and kinetic calculations. [**See the Docs**](https://kawin.org/)

  [![GitHub last commit (by committer)](https://img.shields.io/github/last-commit/materialsgenomefoundation/kawin?label=Last%20Commit)](https://github.com/materialsgenomefoundation/kawin)
  [![PyPI version](https://badge.fury.io/py/kawin.svg)](https://pypi.org/project/kawin)

- 

## Contributions

- Please limit the description to 3 lines of text and up to 1 of badges.
- Make sure to include links to source code if the project is open-source.
- If you are an **active << Your Group Name >> member** you should have write access to this repository by default, and you are allowed to make changes directly.
- If you are a **past << Your Group Name >> member**, you are welcome to contribute (1) the code you worked on while active to the appropriate category (please use `Legacy` if you no longer actively maintain it), as well as (2) code you created after leaving the group under `Alumni Work`. You can contribute by forking the repository and opening a pull request.
- The easiest way to contribute is to open GitHub dev environment in your browser by simply clicking `.` key. It will work on any device with a keyboard (even an iPad!). With it, **you can make a simple contribution in under a minute without any knowledge of git!**. Simply (1) edit the text in the README file, which will open automatically, (2) click on the _Source Control_ icon on the left panel (third from top), (3) write a short message about what you did, and (4) click _Commit&Push_. Done!


>## How to set up? (step-by-step)
>1. Follow the big green `Use this template` and select `Create a new repository` **OR** fork it if you would like to contribute in the future.
>1. You will now see some mess, but don't worry! Once you populate the links, in a few minutes, it should look all good 😊.
>1. You will only need to exit 2 files! The `README.md` holds all content, while `_congif.yml` holds some configuration metadata.
>1. In `README.md`, replace all `<< Your Group Name >>` fields with the actual name of your group. You can do it manually (there aren't many), or, if you are editing locally on Unix (Linux/Mac) or using GitHub Codespaces (Linux), you can open do it automatically with `sed -i 's/<< Your Group >Name >>/SuperNiceGroup/g' README.MD`. Do the same thing with `<< Your Group URL >>`. 
>1. In `_congif.yml`, do the same as above. You should also change the `<< Your Title >>` that will show up in the top-left corner and adjust other links as needed so that they point to your resources, like the group homepage or class dashboard.
>1. **You are now ready to take it online!** Simply go to `Settings > Pages > Build and deployment`, click on the `Source`'s dropdown menu, select `Actions`, and don't do anything else here. Make _any_ change to the `README.md` and push it. 
>1. **Wait around 45s, and boom, done! Your site should now be online!** You should see a tan dot (still working) or green checkmark (done) next to your last commit message. If not, you may need to enable workflows under `Actions`.
>1. To allow others to contribute directly, if you trust them, you should give them write access under `Settings > Collaborators`, or explain to them how to (1) fork a repository and (2) do pull requests.
>1. Once the content is ready, remove these instructions by simply deleting everything above the `# << Your Group Name >> Projects` header. You have a backup at the end of this document.
>1. To make further customizations, you can consult the manual for [the underlying Jekyll theme](https://just-the-docs.com/), which, as of September 2023, is actively developed and maintained. 
>## How to add yourself in under a minute?
>1. _(If you have write access)_ Open this repository page in developer mode by simply clicking the `.` key, and `README.md` should just pop up, ready for your changes.
>1. Under **Active Group Members**, put (1) your name between `**'s, (2) replace `<< GitHub username>>` with your user name, (3) replace `<< ORCID ID number>>` with your ORCID ID (just the numbers).
>1. Go to the `Source Control` icon on the left panel (third from the top, will have a blue mark if you edited anything), write a short message about what you did, and click _Commit&Push_. Done!
>## How to quickly contribute a project to the list?
>1. Start by using the _Legend_ to figure out where your project belongs within the page structure.
>1. This part is very flexible, and you can tune it to your favorite flavor. You just create a new entry in a list with the `- ` symbol, copy-paste appropriate markers based on the _Legend_, and write out the bold name of the software / project / assignment alongside a hyperlink to the GitHub/GitLab >repository `[**<< software name >>**](https://github.com/<< repo holder >>/<< repo name >>)` followed by a short description. Examples (a few taken from Phases Research Lab in September 2023) are provided and should get you started pretty quickly!
>1. Under your description, you can add live badges, which will update over time! This lets you see which projects are active, well-tested, and released (e.g., on PyPI). You can also link papers this way. You can either (1) get them from a service like [shields.io](https://shields.io/) or (2) change >values in URLs as appropriate. The first (broken) example shows which ones should be replaced with `<< repo holder >>`, `<< repo name >>`, `<< branch >>`, `<< docs address >>`, and `<< software name >>` to get ones like in the second example.
>1. Go to the `Source Control` icon on the left panel (third from the top, will have a blue mark if you edited anything), write a short message about what you just added, and click _Commit&Push_. Done!