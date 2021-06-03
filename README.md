# Website of the Semanux

This is the repository of Semanux. We are using the Jekyll page generator, node.js, and Github Actions for automatic deployment. All changes on the Web site originate from changes in this code repository. Please see the [license file](./LICENSE) for details about the licensing of our code.

## Local Setup

1. Install Ruby on your system: <https://www.ruby-lang.org/en/documentation/installation>.
1. Open the Command Line / PowerShell / Bash / zsh on your system.
1. Install the [bundler gem](https://bundler.io) for managing dependencies with `gem install bundler`.
1. Go to the directory where the repository should be cloned to with `cd directory/to/place/repo`.
1. Clone the repository with `git clone https://github.com/semanux/website.git semanux-website`.
1. Go into the directory of the repository with `cd semanux-website`.
1. Install the dependencies into a local `vendor` directory with `bundle install --path vendor`.
1. Generate and serve the Web site with `bundle exec jekyll serve --livereload`.

### Optional
1. Install Node.js on your system: <https://nodejs.org/en/download>.
1. Run `npm install` to install node modules (currently tools for tools for code autoformatting, possible more in the future).
1. Run `npm run check` to check the code formatting, run `npm run format` to automatically format the code.
1. Additionally, you may use `npm run serve` to start live Jekyll serving (which is just an alias to the the above `bundle ...` command).
1. Run `npm run clean` to remove all Jekyll generated files.

## Third-party content
- jekyll-polyglot <https://github.com/untra/polyglot>
- jekyll-file-exists <https://github.com/Wolfr/jekyll_file_exists>
- Inter Font <https://rsms.me/inter/>
- Feather Icons <https://github.com/feathericons/feather>

## TODO
1. Style posts <https://www.xaprb.com/blog/how-to-style-images-with-markdown>
1. Visitor tracker (with respect to privacy laws)
1. Imprint
1. Social media links
1. Redirect of semanux.de to semanux.com/de (similar to approach in Hugo version)
1. Create Email addresses as listed on the page
1. CI script is both in main and in jekyll branch. Still confusing which one is actually used by GitHub (will be resolved when this is on main branch?)

## Ideas
- List our relevant publications?
- Show gazetheweb? (or at least something about proved technology)
- Have authors of posts?
- Minify output of Jekyll (there is no Jekyll plugin available), maybe use Node.js?
- Use jekyll-assets to generate thumbnails? (will probably collide with polyglot)

## Tipps
- Use double quotes (") to surround any relative link in HTML code (e.g., `<a href="/imprint">Imprint</a>`). Otherwise, localization of the relative link does not work.
