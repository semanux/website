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
8. `bundle exec jekyll serve`

## Third-party content
- jekyll-polyglot <https://github.com/untra/polyglot>
- jekyll-assets <https://github.com/envygeeks/jekyll-assets>
- Inter Font <https://rsms.me/inter/>
- Feather Icons <https://github.com/feathericons/feather>

## TODO
- Finish contents
- Style images in blog posts: <https://www.xaprb.com/blog/how-to-style-images-with-markdown>
- Use Jekyll Assets to convert images to a certain format? Like jpg or webp?
- Minify output of Jekyll (there is no Jekyll plugin available)
- Schedule a call “button” on the Web page
- Visitor tracker
- Use `CSS.supports("backdrop-filter", "blur(10px)");` to decide about using blurry backgrounds