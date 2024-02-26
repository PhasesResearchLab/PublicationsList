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
