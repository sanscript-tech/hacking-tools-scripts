### Welcome to Autumn of Open Source 2020! 🤗

**For participation, please visit** : https://aos.sanscript.tech/

**Here are some guidelines you need to follow for contributions.**

- Please **register** for the event to contribute and join our slack channel  **(_mandatory_)**. You will receive a confirmation mail and link for joining slack channel through the mail.
- Please **specify your full name** on your GitHub profile for review.
- Each participant will be assigned **2 issues (max)** at a time to work.
- Participants have **7 days** to complete issues.
- Participants have to **comment on issues** they would like to work on, and mentors will assign you.
- Issues will be assigned on a **first-come, first-serve basis.**
- Participants can also open their issues, but it needs to be verified and labelled by a mentor.
- Before opening a new issue, please check if it is already created or not.
- Issues labelled with **AOS2020** are only eligible.
- Pull requests will be merged after being reviewed by a mentor.
- Create a pull request from **a branch** not from **Main**.
- You will be **scored** based on the level of issues you have solved.
- It might take a day to review your pull request. Please have patience and be nice.
- We all are here to learn. You are allowed to make mistakes. That's how you learn, right!
- Reach out to mentors if you need help through the slack channel.

**Pull Requests review criteria:**
- Please mention parent issue no. with "**#**" in the description while sending a pull request.
- You must add your code file into the respective language folder.
- Your work must be original, written by you not copied from other resources.
- You must **comment** on your code where necessary.
- Add a **readme** file which must contain:-
  - description of your issue you have solved.
  - use case.
  - sample input and output.
  - for issues labelled with medium or high, please add relevant output images in a seperate folder.
  - please add all the images in a separate folder to make you contribution look clean.

_The Event will end on **20 November 2020**.
We will provide a **certificate** of contribution to the participant with at least **one pull request merged.**_

**Mentors/Maintainers of the project:-**
- @tejan-singh
- @yashaswibiyahut
- @balapriyac
- @SANKET7738

**_For queries regarding registration, participation, certification and rewards, reach out for help at_
help@sanscript.tech**

## Fork this repository 🚀

Fork this repository by clicking on the fork button on the top of this page.
This will create a copy of this repository in your account.

![forking](https://user-images.githubusercontent.com/56690856/96425111-453c6380-1219-11eb-80f4-f46a0371ed2e.png)

## Clone the repository 🏁

Now clone the forked repository to your machine. Go to your GitHub account, open the forked repository, click on the code button and then click the _copy to clipboard_ icon.

![cloning](https://user-images.githubusercontent.com/56690856/96425484-b24ff900-1219-11eb-9cf0-58053ee8b758.png)

Open a terminal and run the following git command:

```bash
git clone "url you just copied"
```

where "url you just copied" (without the quotation marks) is the url to this repository (your fork of this project). See the previous steps to obtain the url.

For example:

```bash
git clone https://github.com/sanscript-tech/hacking-tools-scripts
```

![cloning to local](https://user-images.githubusercontent.com/56690856/96425961-3ace9980-121a-11eb-8516-8235782e86f9.png)

## Create a branch ⚓

Change to the repository directory on your computer (if you are not already there):

```bash
cd (filename)
```

![set working directory](https://user-images.githubusercontent.com/56690856/96426111-6ea9bf00-121a-11eb-90e3-8ccc7183a6c0.png)

Now create a branch using the `git checkout` command:

```bash
git checkout -b your-new-branch-name
```

For example:

```bash
git checkout -b dev_username
```

![checking out to new branch](https://user-images.githubusercontent.com/56690856/96426659-2a6aee80-121b-11eb-81f3-d616ae00229d.png)

## Make necessary changes and commit those changes 🚏

Do the necessary changes.

If you go to the project directory and execute the command `git status`, you'll see there are changes.
![making changes](https://user-images.githubusercontent.com/56690856/96426834-6736e580-121b-11eb-9211-8b26715921ae.png)

Add those changes to the branch you just created using the `git add` command:

```bash
git add .
```

![add changes](https://user-images.githubusercontent.com/56690856/96427459-34412180-121c-11eb-9fa1-72cdaeae61f3.png)

Now commit those changes using the `git commit` command:

```bash
git commit -m "(Add your message here)"
```

replacing `<Add your message here>` with your message.

![commit changes](https://user-images.githubusercontent.com/56690856/96427464-35724e80-121c-11eb-91c2-20001f5def5a.png)

## Push changes to GitHub 🪂

Push your changes using the command `git push`:

```bash
git push origin <branch-name>
```

replacing `<branch-name>` with the name of the branch you created earlier.

![push changes](https://user-images.githubusercontent.com/56690856/96427466-360ae500-121c-11eb-9c02-e201906a0a72.png)

## Submit your changes for review 🚩

If you go to your repository on GitHub, you'll see a `Compare & pull request` button. Click on that button.
![create PR](https://user-images.githubusercontent.com/56690856/96427945-ce08ce80-121c-11eb-9223-a120c7d72541.png)

Now submit the pull request.

![submit PR](https://user-images.githubusercontent.com/56690856/96427954-cfd29200-121c-11eb-90f7-1f4ea2f8342f.png)

Soon we will be merging all your changes into the master branch of this project. You will get a notification email once the changes have been merged.
