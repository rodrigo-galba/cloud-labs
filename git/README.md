# Git

## How to overwrite branch

```
# overwrite master with contents of feature branch (feature > master)
git checkout feature    # source name
git merge -s ours master  # target name
git checkout master       # target name
git merge feature       # source name
```

## Git crypt

Transparent file encryption in git 

### Using git-crypt


Generate GPG keys based in the current user:
```
sudo apt install git-crypt #linux
sudo apt-get install haveged rng-tools
gpg --gen-key

# input your Git username
# Input yout Git email
# Input a password to unlock Git
```

```
cd repo
git-crypt init
```

Specify files to encrypt by creating a .gitattributes file:
```
*.tfvar* filter=git-crypt diff=git-crypt
*.key filter=git-crypt diff=git-crypt
env/** filter=git-crypt diff=git-crypt
.env.* filter=git-crypt diff=git-crypt
```

Add your user to the project:
```
git-crypt add-gpg-user YOUR_GITUSER_EMAIL
```

Export the key to unlock files:
```
git-crypt export-key GPG_KEY_FILE
# Ignore keyfile in the .gitignore
```

Check the status of current settings:
```
git-crypt status
```

### Decrypting git files

```
git-crypt unlock $UNLOCK_KEY
```



- https://github.com/AGWA/git-crypt
- https://gist.github.com/ummahusla/8ccfdae6fbbe50171d77
- https://stackoverflow.com/questions/4624357/how-do-i-overwrite-rather-than-merge-a-branch-on-another-branch-in-git
