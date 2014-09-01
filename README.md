deploymate-to-pmd
=================

Generates a PMD report from a JSON generated from [**Deploymate**](http://www.deploymateapp.com).

# Usage

    /Applications/Deploymate.app/Contents/MacOS/Deploymate --cli -t TestTarget TestProject.xcodeproj -o json | python deploymate-to-pmd.py > deploymate_pmd.xml
    

Now you can use `deploymate_pmd.xml` with the [**PMD Plugin**](https://wiki.jenkins-ci.org/display/JENKINS/PMD+Plugin) on [**Jenkins**](http://jenkins-ci.org). Just add a **Publish PMD analysis result** on your post-build actions.

### Deploymate CLI

You can read more about **Deploymate CLI** on its [support page](http://www.deploymateapp.com/kb/cli/).

# Thanks

- [**Ivan Vasic**](https://twitter.com/ivanvasic) for creating Deploymate
