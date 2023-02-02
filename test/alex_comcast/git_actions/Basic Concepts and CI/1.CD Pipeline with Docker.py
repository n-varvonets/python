# https://www.youtube.com/watch?v=R8_veQiYBjI&ab_channel=TechWorldwithNana

"""What is Github Actions?"""
# Github Actions - Is platform to automate developer workflows
# CI/CD - is one of many workflows
"""What are developer workflows? Use Cases for GitHub Actions"""
# Below will be a few examples why does it need:
# 1.
# Git project can have a team(2+) who contribute their features to main logic of app to our project(pull requests).
# Situation: You as master of team which are developing some app and have got msg from user about some err.
# What you should do?: Yor organization task:
#   - is it minor/major?
#   - is it reproducible?
#   - assign to contributor(your participant of dev team)?
#   - contributor fix this err and push you a pull request
#   - you review his code on correctness
#   - is it fix?
#   - merge to master branch

# CI/CD Pipline:
# after last action of mering to master branch - here we can revoke our trigger which will:
#   - test our merged code
#   - build
#   - make deploy(including release notes and version number)

# Problem: if more team - therefore more pull requests - it take a lot of time to management the task
# and there are a lot typical cases - so it has to be automated (by CI/CD)

"""Basic Concepts of GitHub Actions: How GitHub Actions automates those workflows? GitHub Events & Actions"""
# they happens when:
#   - something happens IN or TO your repository(event):
#         - pull request was created
#         - issue created
#         - cont.joined(uor participant or team)
#         - pull request was merged
#         - other apps(apps/tools which was integrated into github response to our req as action for checking on correctness)
#   - automatic actions are executed in response

"""GitHub Actions CI/CD"""
# 1. most common workflow for yor repo:
#   - you commit the code;
#   - test;
#   - build;
#   - push;
#   - deploy;

"""Benefits of Github Actions"""
# 1) integration with other technologies is important! these all use in on project and make good communication:
#       - different languages(js,python,java,django,fastapi,node.js)
#       - different os(ubuntu,win,macos,android)
#       - different tools(docker, psql, redis)
#       - different hosts(aws, digital ocean)
# So every time you have to:
#   - install python
#   - install django
#   - install docker
#   - configure integration and plugins

"""Syntax of Workflow File"""
# 1.syntax_django.yml
"""Where does this Workflow Code run? GitHub Action Runner"""
# each job in workflow runs **in a fresh** virtual environment
"""Build Docker Image and push to private Docker Repo"""


