# Kyle Potchka — ePortfolio

Plain HTML/CSS/JS site for the LIS 4934 Senior Capstone ePortfolio project.

## File structure

```
index.html          Home — bio, skills, resume link
projects.html        Internship + coursework projects
reflections.html    Narrative / reflections
contact.html         Contact info
assets/style.css     All site styling
assets/main.js       Mobile nav toggle
assets/Potchka_Resume.pdf   Downloadable resume
```

## Deploy to GitHub Pages (free public link, no login required)

1. Go to https://github.com and sign in (or create a free account).
2. Click the **+** in the top right → **New repository**.
   - Name it something like `eportfolio`.
   - Set it to **Public**.
   - Don't add a README (you already have one).
3. Download `kyle-potchka-eportfolio.zip` and unzip it — that gives you a folder containing all the site files. Open a terminal inside that folder and run:
   ```
   git init
   git add .
   git commit -m "Initial portfolio"
   git branch -M main
   git remote add origin https://github.com/YOUR-USERNAME/eportfolio.git
   git push -u origin main
   ```
   (Replace `YOUR-USERNAME` with your GitHub username.)
   - No git installed, or new to it? You can instead drag-and-drop all the files
     directly onto the "Add file → Upload files" button on your new repo's GitHub page —
     no command line needed.
4. In the repo, go to **Settings → Pages**.
5. Under "Build and deployment," set **Source** to `Deploy from a branch`,
   branch `main`, folder `/ (root)`. Click **Save**.
6. After a minute, your public link will appear at the top of that page —
   it will look like:
   `https://YOUR-USERNAME.github.io/eportfolio/`
7. That link works for anyone, no login required. Submit that link for your assignments.

## Updating the site throughout the semester

- Edit any `.html` file directly — the text is plain HTML, readable even if you're new to it.
- To add a new project card, copy an existing `<article class="project-card">...</article>`
  block in `projects.html` and edit the text inside it.
- To add a real photo, drop an image file into `assets/`, then in `index.html` replace
  the `<div class="portrait-frame">Photo coming soon</div>` block with
  `<img src="assets/your-photo.jpg" alt="Kyle Potchka">`.
- Look for text in `[square brackets]` — those are placeholders (mainly in
  `reflections.html` and the project reflection notes) written for you to
  replace with your own words.
- After editing locally, push your changes the same way as step 3 above
  (`git add .`, `git commit -m "update"`, `git push`) and GitHub Pages
  updates automatically within a minute or two.

## Notes

- Your phone number was left off the public pages intentionally, since this
  site has no login. It's still included in the résumé PDF only.
- Add your real LinkedIn/GitHub URLs in `contact.html` (currently placeholders).
