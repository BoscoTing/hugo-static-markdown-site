## Usage

### Create a new site

```sh
brew install hugo
```

```sh
hugo new site mysite
```

```sh
cd ./mysite
```

Choose a theme on [hugo themes](https://themes.gohugo.io/) and run this command:

```sh
hugo new theme <your-theme-name>
```

Configure your theme in ```hugo.toml```

```sh
theme = '<your-theme-name>'
```

### Create a Post

This command will generate a ```.md``` file in the /content folder

```sh
hugo new posts/hello.md
```

### Public to GithubPage

Run these commands to generate or update the /public folder:

```sh
hugo
```

```sh
hugo server -D --renderStaticToDisk --baseURL=your-guthub-pages-url --appendPort=false``` 
```

The actual content to host a static site will be in ```/public``` folder, so you need to push the content inside it on your [**GitHub Pages**](https://pages.github.com/) repo.

```sh
cd /public
git init
git remote add your-githubpage-repo-url
git add .
git push origin main
```

Check your page on https://your-github-name.github.io
