<!--
{
"name" : "orientation",
"version" : "0.1",
"title" : "Yext Orientation",
"description": "Get started at Yext.",
"freshnessDate" : 2015-06-01,
"homepage" : "https://sites.google.com/a/yext.com/engineering/orientation",
"license" : "All Rights Reserved"
}
-->

<!-- @section -->

## Machine Setup

The primary Yext code repository is cloned on your workstation:

> ~/alpha - our codebase, containing Java, Go, and Python code, development tools, configurations and binaries, managed by git [[codebase orientation](https://sites.google.com/a/yext.com/engineering/orientation/alpha)]

Many applications come set up for you to use, which you can test by checking the [Automated Machine Setup](https://sites.google.com/a/yext.com/engineering/orientation/automated-machine-setup):  

*   [Eclipse (Luna)](https://projects.eclipse.org/releases/luna), with Yext coding conventions and plugins
*   [Sublime Text](http://www.sublimetext.com) <u>3</u>, with projects for Alpha (~/Alpha.sublime-project) and Go (~/Go.sublime-project), and the GoSublime plugin (for autocomplete and import management)
*   [Sequel Pro](http://www.sequelpro.com), for manual queries against the database
*   [Git](http://git-scm.com/documentation), with a number of helpful aliases (see ~/.gitconfig)
*   [Meld](http://meldmerge.org), the open source diff/merge tool
*   [Kaleidoscope](http://www.kaleidoscopeapp.com), a proprietary diff/merge tool [[license](https://sites.google.com/a/yext.com/engineering/orientation/Yext.KaleidoscopeLicense?attredirects=0&d=1)]
*   [Homebrew](http://brew.sh), the OSX package manager
*   Aliases to build and run programs from the command line: "icbm", "play", "bplay", "brun". (installed in ~/.bash_profile)

<!-- @task, "text" : "Test some of the applications with a custom setup on your workstation." -->

_Note_: The setup is mostly automated, but you can refer to the manual process in these documents. Do not follow these steps without talking to you mentor, as repeating some of them may cause issues: [Eclipse](https://sites.google.com/a/yext.com/engineering/orientation/setup), [Go](https://docs.google.com/a/yext.com/document/d/1fkbd6tlJITHAZArgFqVbFZwTVgNJGIIYAGH3GqM2JGY/edit#heading=h.u7faqjsfa1q), [Git](https://docs.google.com/a/yext.com/document/d/1H6Slwo5uOUEbTO-B4r6wTZtKfrSjfJTnpPPgIWRfUx0/edit#heading=h.ry6fdips40dv).

### Optional

*   Syntax highlighting for Soy Templates: [https://github.com/anvie/SoyTemplate](https://github.com/anvie/SoyTemplate)
*   [Re-map Caps-Lock to Control](http://sanziro.com/2009/05/map-your-capslock-key-to-control.html) - OS X supports Emacs-style shortcuts everywhere, and this makes them easier to access. For example: Ctrl-A - beginning of line, Ctrl-E - end of line, Ctrl-P - previous line, Ctrl-N - next line


<!-- @section -->

## Build and Run some code

Begin by opening a terminal  

```bash
$ cd ~/alpha
$ bplay admin2

Navigate to http://localhost:9005/admin2/
and enter your credentials.
```

<!-- @task, "text" : "Try running \"bplay\"." -->

You should now be logged in to a local build of the Yext Admin interface, running against db-test. The "bplay" alias stands for "build and play". Yext Java web applications are almost universally written using the Play! Framework.  

<!-- @link, "url" : "https://www.playframework.com/documentation/1.2.7/home/", "text" : "Skim the Play! Framework website." -->



<!-- @section -->

## Start HAProxy

To avoid having to remember the ports of all applications, as well as to simplify the redirections between applications, developers run a [reverse proxy](http://en.wikipedia.org/wiki/Reverse_proxy) called [HAProxy](http://www.haproxy.org/). It is a program that runs on port 80 and forwards requests to your servers based on the URL. Run it as follows.

```bash
(Open a new terminal with **⌘T**)

$ cd ~/alpha
$ sudo tools/bin/haproxy_localhost.sh

Navigate to http://localhost/admin2/
(assuming admin2 is still running)
```
<!-- @task, "text" : "Start HAProxy." -->

You no longer need to remember the port of each application.  



<!-- @section -->

### Set up Eclipse workspace

We will apply the configuration suggested by the Workspace Mechanic plugin and then import project files checked into the Alpha source repository.

1.  Begin by increasing the amount of memory Eclipse is allowed to use
    1.  Open /Application/eclipse/Eclipse.app/Contents/MacOS/eclipse.ini
    2.  Update -Xmx and -Xms to 1G and 4G respectively
3. Open Eclipse
4.  A pop-up appears that says "**Workspace Mechanic found issues that need your attention**." Click through to correct all of the issues
5.  Go to **File > Import > General > Existing Projects into Workspace**
6.  Set the root directory to **~/alpha/eclipse/projects**
7.  Click through to complete the operation

Now all of the Yext Java projects appear in the left-hand project-browser, and Eclipse will automatically build all of them.  
Sometimes there are some additional tweaks if things don't work immediately:

* If source code is not found, ensure "ALPHA_HOME" is set in Classpath Variables and Linked Resources.
* Protoc may not be configured. Enable "Compile .proto files on save". In the Main tab, set the "Use protoc in:" to point to tools/icbm/protoc-darwin-x86_64\. In the Options tab, enable "Generate Java" and keep the default Java Output Directory, "src-gen".

If there are issues with any of the plugins, you may want to refer to the [Eclipse Manual Setup](https://sites.google.com/a/yext.com/engineering/orientation/setup)  

<!-- @task, "text" : "Set up your Eclipse workspace." -->


<!-- @section -->

### Debug in Eclipse

This walkthrough demonstrates how to debug a running Java server using Eclipse.  

1.   Run admin2 as described above
2.   In Eclipse, select the admin2 project and then open the Run -> Debug Configurations menu  
3.   Select "Remote Java Application" and click the "New" icon  
4.   Set the port to 8994
5.   Click "Debug"  
6.   Navigate to the controllers.Customers class in the admin2 project's app folder in Eclipse and set a breakpoint on one of the first lines of the **listCustomers()** function by double-clicking in the left-hand margin of the source line  
7.   Go to   [http://localhost:9005/admin2/](http://localhost:9005/admin2/) . Log in if you haven't logged in yet. Once logged in, Eclipse should hit your breakpoint and pause  

<!-- @task, "text" : "Try debugging in Eclipse." -->


<!-- @section -->

### Learn

Here are some references for learning about Yext technology and culture.

* Learn about Yext products by completing the Certification Course
    * [View the study materials](http://yextcertification.com/) (certify/walkthrough759)  
    * [Take the exam](http://bit.ly/yext_internal_certification)  
* Read about our [development workflow](https://sites.google.com/a/yext.com/engineering/orientation/development-workflow). Print the [Quick Start Reference](https://sites.google.com/a/yext.com/engineering/orientation/quick-start) and keep it on your desk.  
* Read about our [System Architecture](https://docs.google.com/a/yext.com/document/d/1GYDCnqPRChK6bUj1JMCF3S5us7Wk2zFsfIuomqewNcw/edit), and watch a [video](https://bluejeans.com/s/88FA) presentation on it.
* Complete the [SQL/Hibernate Self-study course](https://sites.google.com/a/yext.com/sql-hibernate-self-study-program/)
* Refer to the [Play! Framework documentation](http://www.playframework.com/documentation/1.2.7/  home) to understand how our Java web applications are structured.
*   Read about [the branching workflow for Git](https://docs.google.com/a/yext.com/document/d/1H6Slwo5uOUEbTO-B4r6wTZtKfrSjfJTnpPPgIWRfUx0/edit#heading=h.luorvj3z0gz4) for working on multiple changes simultaneously.
*   Get up to speed on Go with [these resources](https://docs.google.com/a/yext.com/document/d/1fkbd6tlJITHAZArgFqVbFZwTVgNJGIIYAGH3GqM2JGY/edit#heading=h.7iffq8mf7euw).
*   Watch "Brown bag" presentations on various Yext systems.
    *   Videos - In Finder, go to Go | Connect to Server... (⌘K), and enter "smb://storage.office.yext.com/public/Yext Systems Brown Bags".
    *   [View the slides](https://drive.google.com/a/yext.com/folderview?id=0B5HtOs07jQaNUWRRQVpoLTU4ZGc&usp=sharing).
*   How [Javascript Compilation](https://sites.google.com/a/yext.com/engineering/tech/javascript-compilation) works at Yext, and what you should do before committing JS code.
*   Refer to this [directory of the codebase](https://sites.google.com/a/yext.com/engineering/orientation/alpha) for easier navigation.


### Links

*   Okta (Single Sign On) - [https://yext.okta.com](https://yext.okta.com)
*   Email - [http://m.yext.com](http://m.yext.com)
*   Shared Files - [http://docs.yext.com](http://docs.yext.com) > [Engineering-wide folder](https://drive.google.com/a/yext.com/folderview?id=0B-Dqt-BTVaDNODc1NjBmODYtMDRmYy00ZDQwLTgwYTItMTliYzA0N2E1ZGIw&usp=sharing) (Each team also has a folder)  
*   Stash - git interface - [https://stash.office.yext.com/projects/Y/repos/alpha](https://stash.office.yext.com/projects/Y/repos/alpha)
*   Code review (Rietveld) - [http://review2/](http://review2/)
*   Job management (Khan) web interface - [http://khan.prod.yext.com/](http://khan.prod.yext.com/) - [Khan essentials (reference)](https://wiki.office.yext.com:8443/display/wiki/Khan+Essentials)
*   Continuous build - [http://jenkins03.office.yext.com:8080/](http://jenkins03.office.yext.com:8080/) [http://jenkins02.office.yext.com:8080/](http://jenkins02.office.yext.com:8080/])
*   JIRA (Scrum management, Bug tracking) - [http://jira.yext.com](http://jira.yext.com)
*   Sentry (Exception monitoring) - [http://sentry.prod.yext.com/](http://sentry.prod.yext.com/])
