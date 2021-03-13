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
1. Links are not correctly localized (at least on Mac, maybe issue only there?)
1. News on front
1. Style blog posts <https://www.xaprb.com/blog/how-to-style-images-with-markdown>
1. Style blog overview
1. Visitor tracker
1. Imprint
1. Idea on front
1. Team on front
1. Schedule a call “button” on front
1. Actually write news
1. Deploy page to Web server

## Ideas
- List our relevant publications?
- Show gazetheweb? (or at least something about proved technology)
- Have authors of blog posts?
- Minify output of Jekyll (there is no Jekyll plugin available)
- Use jekyll-assets to generate thumbnails?