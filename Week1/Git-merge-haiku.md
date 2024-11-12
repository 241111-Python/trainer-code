# Git Fundamentals: Git Exercise

## How To Complete This Activity

### Preparatory steps: :triangular_flag_on_post:

1. Nominate a repo owner.  The repo owner should share their screen as they go through the next couple steps so all collaborators can see what's going on.

2. Repo owner adds all members of the group as collaborators on the repo. (Settings -> Collaborators and Teams)

3. The repo owner should initialize the exercise by cloning the repo, and creating two files (`haiku.md` and `one-line-test.md`) on a local branch. **(Repo owner should share their screen as they're doing this).**

* `haiku.md` should have a one line introduction (`"Hello World!"` or similar) on line one, and a goodbye line (`"Goodbye!"`) however, **the important part is to leave three blank lines for each member of the group**. In a three person group, line 1 will say `"Hello world!"`, lines 2-10 will be blank, and line 11 will have a goodbye message. Like this:
```
Hello World!










Goodbye!
```

* `one-line-test.md` should have a `"Hello world!"` message on line one, and a single line of text on line 2 (`"Replace me!"`). Like this:
```
Hello World!
Replace me!
```

* The repo owner should save these files and `git push` them to a **new separate remote branch**, then create a pull request from the new branch to the main branch. Another member of the group should review it and approve it!
> How do you create a separate branch?
> In your local terminal environment, run:
> `git checkout -b <branch-name>` Create a new branch and check it out
> `git push origin <branch-name>` Push the new branch to the remote repo
> In your browser, on GitHub:
> Then create a pull request (Pull requests -> New Pull Request).
> Your teammates must review, approve, and merge your branch to main.


### Round 1 Now the fun begins...

1. Each group member should clone the repo (or `git pull` a fresh copy if they have already cloned the repo).

2. The repo owner assigns each group member a block of three empty lines to work on (2-4, 5-7, 8-10).

3. Each group member then creates their own branch and write a haiku on their assigned three lines between the hello world message and goodbye world message.

> A [haiku](https://en.wikipedia.org/wiki/Haiku) is a three line Japanese poetry form, with five syllables on the first line, seven on the second, and five on the final line.

> If your creative energies ebb, you can always google for Haiku generators online, or just use [this one](http://www.everypoet.com/haiku/default.htm).

4. Once each group member has penned their masterpiece, they should save, add, and commit it and `git push` it to the remote repo.

5. Everyone should create pull requests all at once - This simulates the worst possible case of four people trying to alter the same file at the same time.

6. Once the pull requests have been created, each group member should take it in turn to review the merge requests.

- As you will see while merging, github can automatically merge each and every request, without issue, because it can detect that the file changes aren't deleting anything, and they aren't overwriting anything that has been committed since the pull request was created.

* **But beware, this is the best case scenario for merge conflicts - the reason that you should pull and merge master copies on the local branch prior to pushing commits is that most merge conflicts involve people deleting or altering the work of others.**

7. Resolve all merge requests until every member's work is included in the document.


### Round 2 Sometimes conflict is a good thing...
The second round begins in the same way. This time, the group works on the one-line-test.md file at the same time.

1. Each group member should pull the updated main, and overwrite line 2 with something - anything - that comes to mind.

2. Save changes and push to the remote origin custom branch, and then create simultaneous pull requests. Do not start to merge the branches until everyone in the group has created their pull request.

* As you take turns to merge another person's pull request with the main branch, you'll note that the first merge is fine - github has no problem with people overwriting files!

* The second attempt to merge another person's pull request will, however, cause an error. Github will instruct you that it cannot automatically merge the request, and that you will need to solve the problem on your local branch.

> This is because github sees four pull requests, attempting to compare to one main/master file (Let's call it M), but the moment the first pull request is merged, M ceases to exist - replaced by an updated one-line-test.md file that we'll call M1.
> The second pull request expects to be compared to M, but that doesn't exist anymore, and github can tell that it is attempting to overwrite a line.
> In a computer program, this could cause a serious error, since the person creating the second pull request might have no idea that they were attempting to overwrite M1, instead of M.

3. Now each team member is going to have to pull the new main down to their local main branch, merge the main with their local branch, and push the result.

* **This process will keep repeating! As you will see, it could take four people almost ten minutes to resolve the issues from attempting to write one line at the same time.**

### Hopefully after this, you will understand why ***it is important to check the most up to date main branch before pushing to a remote branch, and creating a pull request to the main branch.***

4. You can run this test a second time, with each person waiting to pull the updated main, overwrite it in their local branch, and pushing to a remote branch to create a pull request to the main. As you will see, a little communication and co-ordination goes a long way!

