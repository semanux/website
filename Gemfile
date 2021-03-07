# frozen_string_literal: true

source "https://rubygems.org"

git_source(:github) {|repo_name| "https://github.com/#{repo_name}" }

# gem "rails"
gem "jekyll", "~> 4.2"
group :jekyll_plugins do
  gem "jekyll-polyglot", "~> 1.4"
  gem "jekyll-assets", "~> 1.0"
  gem 'wdm', '>= 0.1.0' if Gem.win_platform? # recommendation by Jekyll
end
