<!--
{
"name" : "practices-and-workflows",
"version" : "0.1",
"title" : "Platform best practices and suggested workflows",
"description": "Work effectively with and get most out of Acquia Cloud using best practices and suggested workflows.",
"freshnessDate" : 2015-06-01,
"homepage" : "https://docs.acquia.com/cloud",
"license" : "All Rights Reserved"
}
-->

<!-- @section -->


### Learning Objectives

By the end of this module, learners will be able to understand:

* Workflows and best practices related to Code Management

* Workflows and best practices related to Configurations Management

* Workflow automation by using Cloud Hooks

* Best practices for Performance, Security and Live Deployment of a site on Acquia Cloud

<!-- @section -->

## Lesson 3.1: Code Management Workflows with Acquia Cloud

Now, you have your Cloud Dev and Local Dev environments setup and you're ready to start development.

### Adding new modules and themes

While creating a new site on Cloud Dev, you select an existing Drupal Distribution listed on Acquia Cloud. A Drupal Distribution consists of Drupal Core and several contributed modules and themes. When you clone a Cloud Dev site to your Local Dev environment, all the modules and themes included in the Distribution get copied to your Local Dev environment.  In a real life scenario, you'd need to add contributed or custom modules and / or themes to your site.

When developing with Acquia Cloud, you need to add additional modules and themes to your Local Dev environment and then push the changes to Cloud Dev.

### About the iterative process of Drupal development

Drupal development typically involves two types of activities:

* Code:  Addition of new modules or changes to existing ones.

* Configuration:  Building various site functionality using Drupal Admin UI.

In a real life project, Drupal development is an iterative activity. It is not enough to build the site functionality just once and push live, but developers need to carry out site building and deploying activities on ongoing basis. Development typically happens on  Local Dev Site.

At the same time, clients may keep on adding data to their testing environment, which is typically  Cloud Dev Site.  This results in the code and the data on both the sites going  out of sync.

Developers need to test newly added functionality on the Local Dev Site using data added by the client on Cloud Dev Site. Once they are happy with the functionality, they need to push the code (and not the data) to the Cloud Dev Site.

### The iterative development process involves

* Developing code locally

* Pushing code changes to Cloud

* Clients add data on Cloud

* Pulling Data from Cloud

* Making changes to Code locally

* Pushing Code to Cloud

### Follow the exercises in this section for a step by step guide for

* Adding new modules to your site,

* Modifying the code on Local Dev,

* Pushing new or changed code to the Cloud Dev site and

* Pulling client added data from Cloud Dev to Local Dev sites.

* Automating workflows using Acquia Cloud Hooks

<!-- @section -->

## Exercise 3.1.1 : Local development

### Scenario

At this point, you’ve synced up your online Cloud Dev Site with your local environment. You’re working on your site for the first time, adding in new code to your local dev site. We’re going to add a simple module, this will give us a chance to practice deployment.

### Step A. Add a custom module

1. Download 'Hello Cloud' module here from Google Drive. ([https://docs.google.com/file/d/0B_jmG1TM9szHUEg0SnlhakZTYWs/](https://docs.google.com/file/d/0B_jmG1TM9szHUEg0SnlhakZTYWs/))

2. Use the File > Download menu to get a zip file containing both files    ![image alt text](https://raw.githubusercontent.com/outlearn-content/assets/master/ac/image_13.png)

3. Add this module to your site:

    ```
    $ cd ~/Dev\ Desktop/mysite

    $ mkdir -p sites/all/modules/custom/hello_cloud

    $ cd sites/all/modules/custom/hello_cloud

    $ unzip ~/Downloads/hello_cloud-v1.zip
    ```

4. Go to Admin > Modules. Select the Hello Cloud module to enable and Save Configuration.

<!-- @task, "hasDeliverable" : false, "text" : "Add a custom module to your site."-->

### Step B. Test it’s working locally

Verify the module is working. This is a manual functional test.

* Visit yoursite.dev.local/hello-cloud

* In the main menu locate the new "Hello Cloud" link. Your site should look like this:

![image alt text](https://raw.githubusercontent.com/outlearn-content/assets/master/ac/image_14.png)

<!-- @task, "hasDeliverable" : false, "text" : "Test the Hello Cloud module."-->

<!-- @section -->

## Exercise 3.1.2 : Deploy on Cloud (Dev env) From Local

### Scenario

In the previous step, we cloned our Drupal site from Cloud to our local environment and added a new module (code) to our site. This has resulted in changes to our local code and database and making them out of sync with Cloud Dev.

At this point, we’ll push changes from our Local Dev Site push to our Cloud Dev Site.

![image alt text](https://raw.githubusercontent.com/outlearn-content/assets/master/ac/image_15.png)

NOTE: Copying the DB is a one-time event, mostly just for this workshop. Normally you would automate DB changes like enabling new modules.

### Step A: Syncing code - choose best option for you

### Option 1: On Mac or Windows with Acquia Dev Desktop 2

1. Open Acquia Dev Desktop, select your Cloud Dev site from the list of sites on the left column.

2. On the right side, you will see site details, at the bottom of this section, there are workflow options.

3. Select "Push to Cloud Dev" and the “Code” + “Database” checkboxes.

4. Click "Push code and database to Cloud Dev".

5. In the commit dialog, all files default to "Commit". Select any you do not want to commit yet and use the Action button to skip them.

6. Enter a descriptive commit message. For example: "Adding Hello Cloud module."

![image alt text](https://raw.githubusercontent.com/outlearn-content/assets/master/ac/image_16.png)

### Option 2: On Linux with Git and Drush on the command line

Code – via Git . This works because Acquia Cloud has an automated git deployment mechanism. Otherwise, you’d need something to deploy your code from Git onto the web servers.

Open Command prompt. cd path/to/ your repository and enter following commands.

* git pull origin master

    * Imports the latest code changes from the project Git repo.

* git status

    * Check for uncommitted local changes.

* git add .

    * Prepares new or changed files since the previous commit.

* git commit -m "Deploying initial site build"

    * Commits changes to your local repository, with a message to inform colleagues what changes were made.

* git push origin master

    * Commits your changes to the project Git repository, and (on Acquia Cloud) deploys those changes to any environment running the "master" branch.

Database (Configurations and Content) – via drush sql-sync. This will push content types and configuration - and ALL content. This step requires that you have Drush aliases set up correctly. Example:

```
$ drush sql-sync @mysite.local @mysite.dev
```

<!-- @task, "hasDeliverable" : false, "text" : "Sync your code."-->

### Step B: Check your site

1. Once the Push is successful, visit your Cloud Dev Site. You can click the "cloud site" URL in Dev Desktop.

2. You should now see that your Local Dev Site and Cloud Dev Site are in sync!

![image alt text](https://raw.githubusercontent.com/outlearn-content/assets/master/ac/image_17.png)

<!-- @task, "hasDeliverable" : false, "text" : "Verify that your Local Dev Site and Cloud Dev Site are in sync."-->

<!-- @section -->

## Exercise 3.1.3 : Iterative development

### Scenario

* At this point, both our Local Dev Site and Cloud Dev Site are in sync.

* It is likely that Cloud Dev Site will be used by testers or client to add data for testing and you will continue development on the Local Dev Site .

* This will involve adding new data to your cloud site and modifications to code on your local development environment, for example.

### Step A. Add data to Production site

We’re going to add user data to the live  production site. This is the typical kind of data which you’ll begin to collect as people use your site.

1. On Acquia Free Cloud, there is no Production environment. We’ll use the Stage environment as a pretend production environment.

2. On the Acquia Cloud UI, click the "visit" arrow next to Stage, and add a couple of users via Drupal’s People > Add User page.

![image alt text](https://raw.githubusercontent.com/outlearn-content/assets/master/ac/image_18.png)

<!-- @task, "hasDeliverable" : false, "text" : "Add a couple of users to the site."-->

### Step B. Modify the module

Now we’ll go back to your Local Dev Site and local development environment.

Open `hello_cloud.module` file, go to line number 23 and replace the function `hello_cloud_page()` with following code.  (If there is some issue with copy-pasting the following code, simply download the updated module files from the following URL, unzip and replace your existing files from `hello_cloud` folder) : [Files located here on Google Drive ](https://docs.google.com/file/d/0B_jmG1TM9szHbHJaVmtXb3lETW8/)

```js
/* code starts */function hello_cloud_page() {  $output = 'Say Hello to the Cloud!!';  $output .= hello_cloud_list_users();  return $output;}// Return an HTML table of users and email addresses for the site.function hello_cloud_list_users (){  $result = db_query("SELECT * FROM {users} where uid<>0")->fetchAll();  foreach ($result as $value) {    $account = $value->uid ? user_load($value->uid) : '';    $rows[] = array(      $value->uid ? theme('username', array('account' => $account)) : '',      $value->uid ? check_plain($account->mail) : '',    );    }  $header = array(   'Others Saying Hello!',   'Email address',  );  $output = theme('table', array('header' => $header, 'rows' => $rows));  return $output;}/* code ends */
```

Test your new code locally. You only have a single user (the admin), but that is good enough for an initial test. If you want, in the next step you can copy your Production database all the way down to your local environment.

<!-- @task, "hasDeliverable" : false, "text" : "Add the suggested code into your module."-->

### Step C. Sync up the database changes

Copy your latest Production database to your Dev environment for testing. Use the Cloud UI:

![image alt text](https://raw.githubusercontent.com/outlearn-content/assets/master/ac/image_19.png)

Optionally , you can also copy this database to your local environment for more complete testing before pushing your code changes to Cloud Dev.

**Option 1**: Use Dev Desktop to "Pull from Cloud Dev", select the Database checkbox, and press “Pull database from Cloud Dev”.

**Option 2**: Use the drush sql-sync command, if you have set up Drush aliases:

```
$ drush sql-sync @aqcloudcourse.dev @aqcloudcourse.local --no-cache --sanitize -v
```

Now verify if your functionality is working correctly with the data added from the cloud site. For this purpose, visit /hello-cloud link on the Local Dev Site, this should now reflect user data that we added on the Cloud Dev Site

<!-- @task, "hasDeliverable" : false, "text" : "Sync up your database changes."-->

### Step D. Push code from Local Dev Site to Cloud Dev Site

Once you are happy that the locally added code works well with the data from the Cloud, you will want to push the code to the Cloud. There are two options outlined below for pushing code from local to cloud. Choose the one which suits you best.

A word of caution: at this point, you may be tempted to push both, the code as well as database from Local Dev Site to Cloud Dev Site. In our current example, this won’t make any difference. However, in a real life situation, the data on the Cloud Dev Site might have changed since you last synced the databases. In real life situations, it is not recommended to copy database from Local to Cloud unless you really know what you are doing!

#### Option 1: On Mac with Acquia Dev Desktop 2

1. Open Acquia Dev Desktop, select your Cloud Dev site from the list of sites on the left column.

2. On the right side, you will see site details, at the bottom of this section, there are workflow options.

3. Select "Push to Cloud Dev", “Code” checkbox only.

4. Click "Push code to Cloud Dev".

5. You may be asked to enter a Commit message in the following window. Enter a useful commit message. For example: "Change Hello Cloud module to display all users in a table."

#### Option 2: On Linux with Git on the command line

This option involves managing code via Git.

Open the Command prompt. cd path/to/ your repository and enter following commands

* git status

* git pull

* git add .

* git commit -am "Change Hello Cloud module to display all users in a table."

* git push origin master

<!-- @task, "hasDeliverable" : false, "text" : "Push your code to the Cloud Dev site."-->

### Step E. Test it’s working

Now verify if your functionality is working correctly on the Cloud Dev Site

For this purpose, login to your Cloud Dev Site and visit /hello-cloud link. You should see results like this

![image alt text](https://raw.githubusercontent.com/outlearn-content/assets/master/ac/image_20.png)

> **NOTE:** If you do not see the changes, you may need to Clear Caches on the Cloud Dev Site. To do this, go to Admin > Configuration > Performance. Click Clear All Caches.

<!-- @task, "hasDeliverable" : false, "text" : "Verify that you can see the users on your Cloud Dev Site."-->

## Lesson 3.1 Summary

In this section, we carried out iterative development workflow with Acquia Cloud.

At the beginning of this section, we had a clone of our Cloud Dev site in our Local Dev environment. We added new module (Hello_Cloud) to our local dev. We pushed this module to Cloud Dev using Acquia Dev Desktop (or Git)

We added some data on the Cloud Dev environment and tested our code.

We made some changes to the code locally, pulled the data from Cloud Dev to test our changes.

<!-- @section -->

## Lesson 3.2: Configuration Management Workflows with Acquia Cloud

Drupal development typically involves two types of activities:

* Code : Addition of new modules

* Configuration: Building various site functionality using Drupal Admin UI

In the previous Section we saw how we can manage code while working with Acquia Cloud. In this Section, we will focus on Configurations management.

Most of Drupal site configurations are stored in the database, which makes them tedious to move between various environments of a site (from local to dev etc).

To overcome this issue, we can use a module called a features (  http://drupal.org/project/features  ) and move our key configurations to features.

Learn more about features  [https://drupal.org/node/580026](https://drupal.org/node/580026)

Follow exercises in this section to create a view, export the view to a feature, push the feature from Local Dev to Cloud Dev, modify the feature and sync changes.

<!-- @section -->

## Exercise 3.2.1 Local Development

### Scenario:

At this point you wish to add new code and configuration to your local site

### Step A. Add modules

Add contributed modules to sites/all/modules/contrib

Add **CTools, Views, Features** modules on local environment. Either download and unzip or use the drush command -

```
drush dl ctools views features
```
<!-- @task, "hasDeliverable" : false, "text" : "Add CTools, Views, Features modules on local environment."-->

### Step B. Add a View. Change your site configuration

Now we’ll build the site locally, adding a view and menu link in the view.

1.  On your Local Dev Site, go to Modules page to enable these modules:
    * Chaos Tools
    * Features
    * Views
    * View UI

2. Tip: Verify that you have Articles Content Type. This is available if the Standard Profile is selected when you installed.
    * View name: "Articles".
    * Select Show "Content" of type “Article”
    * Select "Create a menu link"
    * Keep the remaining defaults.
        ![image alt text](https://raw.githubusercontent.com/outlearn-content/assets/master/ac/image_21.png)

3. Go to Structure > Views > Add New View.

4. Click "Save & Exit".

5. Check your new page at /articles. Your site will look like this. Yes, with no content!

![image alt text](https://raw.githubusercontent.com/outlearn-content/assets/master/ac/image_22.png)

<!-- @task, "hasDeliverable" : false, "text" : "Check your changes on your site."-->

<!-- @section -->

## Exercise 3.2.2 Deploy on Cloud

### Scenario

* In the previous step, we added new modules **(code)** to our site. We also carried out a simple site building exercise to add a view **(configuration)** to our site.

* At this point, we’ll push changes from our Local Dev Site push to our Cloud Dev Site.

### Step A: Syncing code - choose best option for you

### Option 1: On Mac or Windows with Acquia Dev Desktop 2

1. Open Acquia Dev Desktop, select your cloud dev site from the list of sites on the left column.

2. On the right side, you will see site details, at the bottom of this section, there are workflow options.

3. Select "Push to Cloud Dev", “Code” and “Database” checkboxes.

4. Click "Push code and database to Cloud Dev".

5. You may be asked to enter a Commit message in the following window. Enter appropriate commit message. For example: "Deploying initial site build.

![image alt text](https://raw.githubusercontent.com/outlearn-content/assets/master/ac/image_23.png)

### Option 2: On Any system with Git and Drush

1. Code: via Git
    * Open Command prompt. cd path/to/ your repository and enter following commands
    * git status
        * This checks to see what differences there are between local and repository
    * git pull
        * This pulls down the latest from the Cloud Dev Site
    * git add .
        * This records any new files you’ve added since the lastest sync
    * git commit -am "Deploying initial site build"
        * This makes a commit message to inform colleagues what changes were made.
    * git push origin master
        * This begins the upload to the repository.

2. Database (Configurations and Content): via drush sql-sync

This will push content types and configuration - and ALL content. For the first time, there doesn’t seem to be another way.

Example

```
drush sql-sync @aqcloudcourse.loc @aqcloudcourse.prod --no-cache --sanitize -v
```

<!-- @task, "hasDeliverable" : false, "text" : "Sync your code."-->

<!-- @section -->

## Exercise 3.2.3 Featurize

### Scenario:

* At this point, both our Local Dev Site and Cloud Dev Site are in sync. Now you will come back to Local Dev Site and continue developing / building the site.

* Drupal development typically involves two types of activities:

* Code: Addition of new modules ()

* Configuration: Building various site functionality using Drupal Admin UI

* Most of Drupal site configurations are stored in the database, which makes them tedious to move between various environments of a site (from local to dev etc).

* To overcome this issue, we can use a module called a features ( [http://drupal.org/project/features](http://drupal.org/project/features) ) and move our key configurations to features.

* Learn more about features [https://drupal.org/node/580026](https://drupal.org/node/580026)

### Step A. Create an Articles Feature

For this exercise, we will create a feature from our Articles Content Type and related View that we created in the previous step.

1. Login to your Local Dev Site.

2. Go to Structure > Features > Create New Feature (admin/structure/features/create).

3. Provide a name, description for your feature

4. Select components (Content Type > Articles, Views > Articles).

5. Under "Advanced options", click “Generate Feature”.

    ![image alt text](https://raw.githubusercontent.com/outlearn-content/assets/master/ac/image_24.png)

7. Go back to Features overview page. Your feature should be listed here.

8. Select the feature, this will enable it.

9. Click "Save Settings".

<!-- @task, "hasDeliverable" : false, "text" : "Create an Articles Feature."-->

### Step B: Push Changes - Feature created on Local Dev Site to the Cloud Dev Site

Choose the options which suits you best.

### Option 1 - On Mac or Windows with Acquia Dev Desktop 2

1. Start Acquia Dev Desktop 2, select your site in the left column.
    * Select "Push to Cloud Dev"
    * Select "Code" ( only code, don't select Database )

2. In the Local workflow section on the right side:

3. Click "Push code to Cloud Dev".

    ![image alt text](https://raw.githubusercontent.com/outlearn-content/assets/master/ac/image_25.png)

### Option 2- On any system with Git commandline

Open Command prompt. cd path/to/ your repository and enter following commands

* git status
  * This checks to see what differences there are between local and repository

* git pull
  * This pulls down the latest from the Cloud Dev Site

* git add .
  * This records any new files you’ve added since the lastest sync
* git commit -am "Deploying initial site build"
  * This makes a commit message to inform colleagues what changes were made.
* git push origin master
  * This begins the upload to the repository.

### Step C: Enable feature on the Cloud Dev Site

1. Go to the Cloud Dev Site.

2. Go to Structure > Features.

3. Your newly pushed feature should be available in the list.

4. Select checkbox to Enable the feature.

5. Click "Save Settings".

<!-- @task, "hasDeliverable" : false, "text" : "Push your changes."-->

<!-- @section -->

## Exercise 3.2.4 Iterative Development

### Scenario

In a real life project, Drupal Site Building is an iterative activity. It is not enough to build the site functionality just once and push to Cloud, but developers need to carry out site building and deploying activities on ongoing basis.

* Let us see how to handle this in our current exercise

* For this purpose, we’ll come back to our Local Dev Site and make changes to the Articles View using Views UI.

### Step A. Create changes

1. On Local Dev Site, go to Structure > Views > Articles.

2. In the Articles view edit page, click on Advanced to expand to see options.

3. Under No results behaviour > Click "Add".

    ![image alt text](https://raw.githubusercontent.com/outlearn-content/assets/master/ac/image_26.png)

5. Select Global: Text Area. Click Apply.

    ![image alt text](https://raw.githubusercontent.com/outlearn-content/assets/master/ac/image_27.png)

7. Add a message like "No articles available!"

    ![image alt text](https://raw.githubusercontent.com/outlearn-content/assets/master/ac/image_28.png)

9. Save the view.

<!-- @task, "hasDeliverable" : false, "text" : "Create changes."-->

### Step B: Recreate feature

1. Go to Structure > Features.

2. On the features overview page, locate your Articles feature. It will display status as 'Overridden'. (This is because you have changed / overridden the functionality from what's stored in the Feature)

    ![image alt text](https://raw.githubusercontent.com/outlearn-content/assets/master/ac/image_29.png)

4. Click on Re-create link next to the Articles feature.

5. On the Re-create page, click to expand the Advanced Options, and click "Generate Feature"

    ![image alt text](https://raw.githubusercontent.com/outlearn-content/assets/master/ac/image_30.png)

7. This will update your feature's code with latest changes that you carried out using UI.

<!-- @task, "hasDeliverable" : false, "text" : "Recreate feature."-->

### Step C: Push code to cloud dev site

1. Now follow steps to push your code to Cloud Dev Site. Try to complete this task without checking the steps in Exercise 3, Step C.

<!-- @task, "hasDeliverable" : false, "text" : "Push code to cloud dev site."-->

### Step D: Update Feature on Cloud Dev Site

1. Visit your Cloud Dev Site, Structure > Features. The code appears as "Overridden".

    * This is because Articles View is still using old settings and is not updated with new settings from the features.

    * You need to carry out an additional step to make sure that updated Features code is "refreshed" or applied properly on the Cloud Dev Site.

2. Click on the status text (Overridden).

3. Select the component which is overridden (Views) and Click "Revert Components"

    ![image alt text](https://raw.githubusercontent.com/outlearn-content/assets/master/ac/image_31.png)

5. Go back to Features overview page and verify if the Article feature is showing Default status

6. Go to the views page (/articles) and verify if newly added empty text is visible on the page.

<!-- @task, "hasDeliverable" : false, "text" : "Update Feature on Cloud Dev Site."-->

<!-- @section -->

## Lesson 3.3: Workflow automation using Acquia Cloud API

### Scenario

In the previous step, we came across a situation where a developer needs to carry out certain steps on the Cloud Dev Site after deploying the code.

We can automate carrying out of such steps using Acquia Cloud Hooks.

In our scenario, whenever we update a feature on our Local Dev Site and deploy it on Cloud Dev Site, we need to run either Database Update Script (update.php) or revert the feature (run a drush command : drush features-revert-all).

### About Cloud hooks

A Cloud Hook is simply a script in your code repository that Acquia Cloud executes on your behalf when a triggering action occurs.

More information about Acquia Cloud Hooks - https://docs.acquia.com/cloud/manage/cloud-hooks

Samples for Cloud Hooks: https://github.com/acquia/cloud-hooks

### Step A: Create the Cloud Hook

This can be achieved by using an Acquia Cloud Hook as follows

Open Command prompt and type

```
cd path/to/repository
```

Create a file as follows using a text editor

hooks/dev/post-code-deploy/feature-update.sh

Add the following to your file feature-update.sh

```bash
#!/bin/bash

site=$1

env=$2

drush @$site.$env features-revert-all
```

<!-- @task, "hasDeliverable" : false, "text" : "Create the Cloud Hook."-->

### Step B: Push changes from local to cloud

Push your code to Cloud Dev Site.

Make changes to your feature on Local Dev Site.

Push changes to Cloud Dev Site.

<!-- @task, "hasDeliverable" : false, "text" : "Push changes from local to cloud."-->

### Step C: Verify changes

Visit the Articles View page (/articles) on your Cloud Dev Site .

Verify that changes made locally and pushed via the feature update are reflected on the Cloud Dev Site . The Features Revert step on the Cloud Dev Site is now automated via Cloud Hook.

<!-- @task, "hasDeliverable" : false, "text" : "Verify changes."-->

### More Resources

There's a lot more that you can do with Cloud Hooks! Here are a few helpful resources to explore more

* [Automating with Cloud Hooks](https://docs.acquia.com/cloud/manage/cloud-hooks) (official documentation)

* [10 Ways Acquia Cloud Hooks can help you sleep at night](https://www.acquia.com/blog/10-ways-acquia-cloud-hooks-can-help-you-sleep-night)

* [Automate tests and more with Acquia Cloud Hooks](https://www.acquia.com/blog/automate-tests-and-more-acquia-cloud-hooks)

* [Cloud Hooks Examples on Github ](https://github.com/acquia/cloud-hooks)

<!-- @section -->

## Lesson 3.4: Performance, Security and Live Deployment

Introduce learners to suggested best practices for improving site performance, securing site code and for the production deployment of a site on Acquia Cloud.

#### Topics

* Audit your site for Performance best practices using Acquia Insight

* Building a super-performant site on Acquia Cloud

* Security and compliance with Acquia Cloud

* Writing secure code (coding best practices for ensuring site security)

* Best practices for working with the file system, cron jobs, SSL, SSH and other platform components.

* Carrying out load testing on Acquia cloud.

* Deploying a site to Production on Acquia Cloud

* Monitor server health and trends using Platform Health.


## Lesson 3.4.1 Performance

Audit your site for Performance best practices using Acquia Insight ([https://docs.acquia.com/network/enhance/insight](https://docs.acquia.com/network/enhance/insight))

Building a super-performant site on Acquia Cloud  ([https://docs.acquia.com/cloud/performance](https://docs.acquia.com/cloud/performance) )

<!-- @task, "hasDeliverable" : false, "text" : "Audit your site for Performance best practices."-->

## Lesson 3.4.2. Security

Security and compliance with Acquia Cloud  ([https://docs.acquia.com/cloud/arch/security](https://docs.acquia.com/cloud/arch/security))

<!-- @task, "hasDeliverable" : false, "text" : "Review the document Security and compliance with Acquia Cloud."-->

Writing secure code (coding best practices for ensuring site security)

Best practices for working with the file system, cron jobs, SSL, SSH and other platform components.

* [https://docs.acquia.com/cloud/files](https://docs.acquia.com/cloud/files)

* [https://docs.acquia.com/cloud/ssh](https://docs.acquia.com/cloud/ssh)

## Lesson 3.4.3 Live deployment

Carrying out load testing on Acquia cloud. ([https://docs.acquia.com/cloud/load](https://docs.acquia.com/cloud/load))

<!-- @task, "hasDeliverable" : false, "text" : "Review the document Carrying out load testing on Acquia cloud."-->

Deploying a site to Production on Acquia Cloud  ([https://docs.acquia.com/cloud/manage/publish](https://docs.acquia.com/cloud/manage/publish))

Monitor server health and trends using Platform Health. ([https://docs.acquia.com/cloud/platform-health-faq](https://docs.acquia.com/cloud/platform-health-faq))
