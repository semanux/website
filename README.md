# Website of the Semanux Project

New Website using Jekyll 4. Under construction.

## Local Setup

1. Install Ruby on your system: <https://www.ruby-lang.org/en/documentation/installation>
2. Open Command Line / PowerShell / Bash / zsh
3. Install the [bundler gem](https://bundler.io) for managing dependencies with `gem install bundler`
4. `cd directory/to/place/repo`
5. `git clone https://github.com/semanux/website.git semanux-website`
6. `cd semanux-website`
7. `bundle install --path vendor`
8. `bundle exec jekyll serve --livereload`

## Third-party content
- jekyll-polyglot <https://github.com/untra/polyglot>
- jekyll-file-exists <https://github.com/Wolfr/jekyll_file_exists>
- Inter Font <https://rsms.me/inter/>
- Feather Icons <https://github.com/feathericons/feather>

## TODO
1. Style blog posts <https://www.xaprb.com/blog/how-to-style-images-with-markdown>
1. Visitor tracker
1. Imprint
1. Actually write news
1. Social media links
1. Redirect of semanux.de to semanux.com/de (similar to approach in Hugo version)
1. Create Email addresses as listed on the page
1. Integrate Matomo
1. CI script is both in main and in jekyll branch. Still confusing which one is actually used by GitHub
1. SASS: "cards" are highly similar, maybe let them share rules?

## Ideas
- List our relevant publications?
- Show gazetheweb? (or at least something about proved technology)
- Have authors of blog posts?
- Minify output of Jekyll (there is no Jekyll plugin available)
- Use jekyll-assets to generate thumbnails?

## Tipps
- Use double quotes (") to surround any relative link in HTML code (e.g., `<a href="/imprint">Imprint</a>`). Otherwise, localization of the relative link does not work.
