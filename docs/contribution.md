# Contribution
Any contribution is encouraged, e.g., bug report, question answer, and submit pull-request.

Before moving your hands, we highly recommend reading the [doc](docs) and see 
the [test](tests) example code. They will often save lots of time to find 
proper usage methods.

**Every feature MUST have test cases.**


## Bug and Questions

Please use [Github Issues](https://github.com/yeasy/hyperledger-py/issues).


## Contribution

* Fork the project as your own, e.g., `github_user/hyperledger-py`, then 
clone locally and setup necessary user info.
```sh
$ git clone git@github.com:github_user/hyperledger-py.git
$ cd hyperledger-py
$ git config user.name "your name"
$ git config user.email "your email"
```

* Make some change (may need to update the [change log](docs/change_log.md)). Make sure to run tox and pass all test cases, then commit and push to your forked project.
```sh
$ #do some change on the content
$ tox
$ git commit -am "Fix issue #1: change helo to hello"
$ git push
```

* At the github webpage, open a pull request.

* Remember to frequently sync your forked copy with the official repo if you 
want the latest version.
```sh
$ git remote add upstream https://github.com/yeasy/hyperledger-py
$ git fetch upstream
$ git checkout master
$ git rebase upstream/master
$ git push -f origin master
```
