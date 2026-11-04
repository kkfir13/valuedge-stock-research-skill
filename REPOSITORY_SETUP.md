# Publish as an independent buffett-brain repository

**Prepared code:** branch `buffett-brain-standalone` of https://github.com/kkfir13/valuedge-stock-research-skill .

The connected GitHub app cannot create or rename a repository, or set its topics. The owner must create an **empty public** repository named `buffett-brain` at https://github.com/new (do not prefill README, License or .gitignore). To transfer the prepared code using Git:

```bash
git clone --single-branch -b buffett-brain-standalone https://github.com/kkfir13/valuedge-stock-research-skill.git buffett-brain
cd buffett-brain
git remote set-url origin https://github.com/kkfir13/buffett-brain.git
git branch -m main
git push -u origin main
```

Then edit the **About → gear** metadata to enter the description and GitHub topics listed in README. GitHub Pages optional: Settings → Pages → deploy from branch `main`, root folder. The static app is already rooted at index.html and reads the local source atlas. Confirm actual public rendering and Google indexation separately.

After creating the dedicated repository, update any README placeholders and inbound links from the original project.
