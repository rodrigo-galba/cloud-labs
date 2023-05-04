# Git

## How to overwrite branch

```
# overwrite master with contents of feature branch (feature > master)
git checkout feature    # source name
git merge -s ours master  # target name
git checkout master       # target name
git merge feature       # source name
```

- https://gist.github.com/ummahusla/8ccfdae6fbbe50171d77
- https://stackoverflow.com/questions/4624357/how-do-i-overwrite-rather-than-merge-a-branch-on-another-branch-in-git
