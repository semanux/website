# Website of Semanux

This is the repository of the Semanux Website. We are using [Jekyll](https://jekyllrb.com) for generating the site, [Node.js](https://nodejs.org/en) for processing the code and the generated site, and [Github Actions](https://github.com/features/actions) for automatic deployment of the site. All changes on the site originate from changes in this code repository. Please see the [license file](./LICENSE) for details about the licensing of our code.

## Local Setup

1. Install Ruby on your system: <https://www.ruby-lang.org/en/documentation/installation>.
1. Open the Command Line / PowerShell / Bash / zsh on your system.
1. Install the [bundler gem](https://bundler.io) for managing dependencies with `gem install bundler`.
1. Go to the directory where the repository should be cloned to with `cd directory/to/place/repo`.
1. Clone the repository with `git clone https://github.com/semanux/website.git semanux-website`.
1. Go into the directory of the repository with `cd semanux-website`.
1. Install the dependencies into a local `vendor` directory with `bundle install --path vendor`.
1. Generate and serve the Website with `bundle exec jekyll serve --livereload`.
1. Go to <http://localhost:4000> in the Web browser of your choice to view the generated site.

### Optional

1. Install Node.js on your system: <https://nodejs.org/en/download>.
1. Run `npm install` to install the required node modules (currently tools for tools for code autoformatting, possible more in the future).
1. Run `npm run check` to check the code formatting, run `npm run format` to automatically format the code.
1. Additionally, you may use `npm run serve` to start live Jekyll serving (which is just an alias to the the above `bundle ...` command).
1. Run `npm run clean` to remove all Jekyll generated files.

## Structure

The repository is structured as following:
- `_data`: Localized texts on the pages - posts are localized separately.
- `_includes`: Files that can be included with Jekyll.
- `_layouts`: Templates for the pages.
- `_plugins`: Plugins that are not available as gem.
- `_posts`: Posts of the blog.
- `_sass`: Files that can be included in sass/scss.
- `static`: Assets for the site.

## Contribution

Before contribution, please read following guide about CSS grids: <https://css-tricks.com/snippets/css/complete-guide-grid>

## Guidelines

- In German translation, use "Imperativ" (without "du" or "Sie").
- For `padding` and `margin`, either use the shorthand form (`padding`) or the subproperties (`padding-top`, `padding-right`, `padding-bottom`, and `padding-left`). Do not mix them, as then the ordering of properties influences the visuals.
- To be discussed: "Web site" or "web site?" (glossar would be preferable in general).

## Third-party content

- jekyll-polyglot, used as gem: <https://github.com/untra/polyglot>
- jekyll-file-exists, see `_plugins` directory: <https://github.com/Wolfr/jekyll_file_exists>
- jekyll-readtime, see `_plugins` directory: <https://gist.github.com/tohuw/cbcc8653321b9a3fb230>
- Inter Font, see `static` directory: <https://rsms.me/inter/>
- Phosphor Icons, see `static` directory: <https://github.com/phosphor-icons/phosphor-icons>

## Issues

1. CI script is both in main and in jekyll branch. Still confusing which one is actually used by GitHub (will be resolved when this is on main branch?)

## Ideas

- List our relevant publications?
- Minify the generated site.
- Process png and jpg images in `static` to webp?

## Tipps

- Use double quotes (") to surround any relative link in HTML code (e.g., `<a href="/imprint">Imprint</a>`). Otherwise, localization of the relative link does not work.