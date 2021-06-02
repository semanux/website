# frozen_string_literal: true

source 'https://rubygems.org'

git_source(:github) { |repo_name| 'https://github.com/#{repo_name}' }

# gem 'rails'
gem 'jekyll', '~> 4.2'
gem 'wdm', '>= 0.1.0' if Gem.win_platform? # recommendation by Jekyll
gem 'eventmachine', # for livereload
    '1.2.7',
    git: 'https://github.com/eventmachine/eventmachine.git',
    tag: 'v1.2.7'
group :jekyll_plugins do
  gem 'jekyll-polyglot', '~> 1.4'
end
