<!--
{
"name" : "platform-installation",
"version" : "0.1",
"title" : "Platform installation and tools setup",
"description": "Get going with publishing on Acquia Cloud and share your content with the world.",
"freshnessDate" : 2015-06-01,
"homepage" : "https://docs.acquia.com/cloud",
"license" : "All Rights Reserved"
}
-->

<!-- @section -->



# Module 2: Platform installation and tools setup

This Module contains hands-on exercises for creating an Acquia Cloud instance, installing a Drupal distribution on the instance and setting up local development environment to work with Acquia Cloud.

**Learning Objectives**

By the end of this module, learners will be able to:

* Create a new Acquia Cloud Free instance

* Install a Drupal Distro on the instance

* Create a local development environment by

    * Installing Acquia Dev Desktop or

    * Using their custom \*AMP Stack

* Generate Public - Private keys pair and add Public Keys to their Acquia Cloud instance.

* Install GIT on local machine (Non Dev Desktop users)

* Install Drush and setup Drush Aliases (Non Dev Desktop users)

* Synchronize Acquia Cloud based site with Local environment

    * Using Dev Desktop

    * Using Git and Drush on Non Dev Desktop environment

## Lesson 2.1: Technical Overview of the Environment

After watching introductory videos, its time to roll-up our sleeves and start hacking the code. For this purpose, we need to set up our cloud hosting environment and install a few tools locally.

To get the most out of Acquia Cloud hosting, its essential that we understand the tools and recommended practices for working with Acquia Cloud.

### What we'll do in Module 2

In the exercises to come, we'll complete the following...

#### High level steps for working with Acquia Cloud

* Setup the Cloud Environment

* Setup Local Development Environment

* Clone our Cloud Site to Local Environment

* Carryout development on Local Environment

* Push developed code from Local Environment to Cloud Environment

#### Set up the tool chain on our Local environment

* Apache / PHP / MySQL stack - for working on Drupal development locally

* Drush - for managing Drupal from command-line

* Git - for pulling and pushing code between Local Environment and Acquia Cloud

You may install these tools independently for your OS and work with Acquia Cloud, or you could use Acquia Dev Desktop - a free tool provided by Acquia to build and manage Drupal sites with ease. (For more information visit: [https://www.acquia.com/products-services/dev-desktop](https://www.acquia.com/products-services/dev-desktop)  )

Follow the exercises in this section for a step by step guide for installing tools and setting up your environments.

## Lesson 2.2: Setup Acquia Cloud Environment

## Exercise: Setup Acquia Cloud and Install Drupal

1. Sign up for Acquia Free Cloud at https://insight.acquia.com/free .

![image alt text](image_0.png)

2. Click Manage my code link when the site is provisioned

![image alt text](image_1.png)

3. From the drop down menu of Dev environment box, select Install Drupal and in the following screen, select Drupal 7 distribution.

![image alt text](image_2.png)

![image alt text](image_3.png)

![image alt text](image_4.png)

4. When the install task is done, click the orange box "Set up my site" link next to Dev to visit the site and run Drupal’s install process.

![image alt text](image_5.png)

At this point, the online development environment (Cloud Dev Site) is ready and this is now your online repository.

## Lesson 2.3: Generate and Add Public Key to Acquia Cloud Account

### Step A. Generate Public Key

You will generate a public key on your machine, unless you want to use an existing key.

#### Mac OSX :

1. Open a shell or command-line instance on your computer.

2. Ensure that you don't already have a public key saved to your computer. To do this, run the following command:

cd ~/.ssh

ls -l

3. If the directory and key file exists, run the following commands to back up the key id_rsa, as this procedure overwrites your current key if it is named id_rsa.

mkdir key_backup

mv id_rsa* key_backup

4. Generate a new public/private key pair using the keygen command:

ssh-keygen -b 4096

5. The keygen command prompts you for the directory to contain the key.

Generating public/private rsa key pair.

Enter file in which to save the key (/Users/[user_dir]/.ssh/id_rsa):

6. Press Enter to accept the default location of /.ssh/id_rsa in your user directory.

Enter passphrase (empty for no passphrase): [passphrase]

Enter same passphrase again: [passphrase]

7. Substitute [passphrase] with your own text. This is for encrypting the private key on your computer. It's possible to use a blank [passphrase], but if you do this, another user can impersonate you with a copy of the key file.

Note: Be sure to keep track of the [passphrase] since you will need to enter it when using the key.

8. The keygen command displays the following output:

Generating public/private rsa key pair.

Your identification has been saved in /Users/[user_dir]/.ssh/id_rsa.

Your public key has been saved in /Users/[user_dir]/.ssh/id_rsa.pub.

The key fingerprint is:

52:96:e9:c8:06:c2:57:26:6d:ef:2f:0c:d9:81:f4:1c username@hostname

9. Copy the key to your clipboard. Run the following code to copy the key to your clipboard:

pbcopy < ~/.ssh/id_rsa.pub

# Copies the contents of the id_rsa.pub file to your clipboard

10. Alternatively, using your favorite text editor, you can open the ~/.ssh/id_rsa.pub file and copy the contents of the file manually.

(Instructions as per  [https://docs.acquia.com/cloud/ssh/enable/key-mac-unix](https://docs.acquia.com/cloud/ssh/enable/key-mac-unix))

#### Windows:

For Windows, you need a program like Git Bash to generate a key.

1. Start Git Bash (from right-click contextual menu in Win Explorer).

2. Create key pair by typing the command:  ssh-keygen -t rsa

3. Key pair will get generated $ HOME \.ssh folder

($ HOME is the home folder for the user, typically at: C:\Users\[Your User Name])

### Step B. Add SSH key to Acquia cloud

You will add the SSH key your Acquia Cloud site via the "Users and keys" page.

Follow instructions given at:  https://docs.acquia.com/cloud/ssh/enable/add-key

## Lesson 2.4a: Create a local development environment on Windows or Mac with Dev Desktop

### Exercise

* Install Acquia Dev Desktop 2 from [https://www.acquia.com/downloads](https://www.acquia.com/downloads)

* Add your Acquia Cloud Account details to Dev Desktop

* Add location of your Private Key (Windows)

* Refresh the sites list and check if Acquia Cloud Site created in the previous exercise is listed.

* Clone the site locally.

## Lesson 2.4b: Create a local development environment on Windows with WAMP (Optional)

We strongly recommend using Acquia Dev Desktop 2 as explained in previous exercise as your local development environment. However, for some reasons if you cannot use Dev Desktop and wish to use your own WAMP / XAMP setup as local development environment, follow the steps given below to setup integration of your local environment with Acquia Cloud.

### Step A: Install WAMP or XAMPP

(We will not cover detailed steps for installing WAMP / XAMPP or any other *AMP stack that users are using for their local development environment. We are assuming that, for some reasons, users are not using Acquia Dev Desktop for local development, but are using Acquia Cloud for hosting their site.)

### Step B: Install GIT

1. Download Git for Windows from  http://git-scm.com/download/win

2. Install downloaded file, make sure to select Git GUI and Git Bash options while installing

3. Also, select the option Run Git from Windows Command prompt option

![image alt text](image_6.png)

![image alt text](image_7.png)

### Step C: Copy Git URL from Acquia Cloud

1. Login to your Acquia Cloud Account

2. Click Git URL link located at top right corner of the page![image alt text](image_8.png)

3. A pop-up window will display Git URL to be used for connecting with your Cloud Site![image alt text](image_9.png)

4. Select All and Copy this URL to your clipboard

### Step D: Clone the Cloud Codebase locally using Git

1. Open Windows Explorer

2. Navigate to your $Home\Sites folder (typically C:\Users\[Your_User_Name\Sites]

3. Right click inside the folder and click Git Bash Here from the contextual menu![image alt text](image_10.png)

4. In the Git Bash console, type the command git clone [Your_Git_URL_copied_from_Cloud]![image alt text](image_11.png)

### Step F - Install Drupal site locally

1. Open your browser

2. Open PHPMyAdmin from your local WAMP/XAMPP environment

3. Create a new blank Databases

4. In the browser, navigate to the folder where you cloned the repository in the step above inside your localhost : typically http://localhost/[your_cloned_folder]

5. Drupal installation wizard will kick-start. Provide the Database credentials created in step F-3 above.

6. Finish Drupal installation normally.

### Step G - Synchronise Database

At this stage, your Cloud Dev and Local Dev sites have exactly same codebase, but databases are NOT in sync. You need to Pull the database from Cloud Dev to Local Dev so that they are synchronized.

#### Take backup from Cloud Dev

1. Login to your Acquia Cloud Dashboard

2. Go to Databases

3. Click Backup button next to Dev environment

4. Check the status of backup request on the Workflow page

5. On the Workflow page, click Download icon from the Dev environment

6. From the pop-up list, select the most recent backup (which you had requested in #3) and click Download

7. The DB backup will be downloaded

#### Restore DB backup to Local Dev

1. Open PHPMyAdmin from your local WAMP / XAMPP environment.

2. In PhpMyAdmin, select appropriate database used for local Drupal installation (the one you had created in Step C, #7)

3. Click Import tab at the top

4. Click browse and select the backup file which you had downloaded

5. Click Go!

Your Cloud Dev and Local Dev code and databases are now in sync!

## Module 2 Summary

### In this module, we performed the following steps

* Setup Acquia Cloud environment

* Created a new site using an existing distribution in Cloud Dev Environment

* Installed software tools for local development

* Generated and added our Public Key to Acquia Cloud

* Cloned our Acquia Cloud Dev site to Local Dev environment

### At this point, our Cloud Dev site and Local Dev sites are ready and in sync!

# ![image alt text](image_12.png)

# Module 3: Platform best practices and suggested workflows

This module explains platform best practices and suggested workflows to work effectively with and get most out of Acquia Cloud.

### Learning Objectives

By the end of this module, learners will be able to understand:

* Workflows and best practices related to Code Management

* Workflows and best practices related to Configurations Management

* Workflow automation by using Cloud Hooks

* Best practices for Performance, Security and Live Deployment of a site on Acquia Cloud

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

## Exercise 3.1.1 : Local development

### Scenario

At this point, you’ve synced up your online Cloud Dev Site with your local environment. You’re working on your site for the first time, adding in new code to your local dev site. We’re going to add a simple module, this will give us a chance to practice deployment.

### Step A. Add a custom module

1. Download 'Hello Cloud' module here from Google Drive. ([https://docs.google.com/file/d/0B_jmG1TM9szHUEg0SnlhakZTYWs/](https://docs.google.com/file/d/0B_jmG1TM9szHUEg0SnlhakZTYWs/))

2. Use the File > Download menu to get a zip file containing both files![image alt text](image_13.png)

3. Add this module to your site:

$ cd ~/Dev\ Desktop/mysite

$ mkdir -p sites/all/modules/custom/hello_cloud

$ cd sites/all/modules/custom/hello_cloud

$ unzip ~/Downloads/hello_cloud-v1.zip

4. Go to Admin > Modules. Select the Hello Cloud module to enable and Save Configuration.

### Step B. Test it’s working locally

Verify the module is working. This is a manual functional test.

* Visit yoursite.dev.local/hello-cloud

* In the main menu locate the new "Hello Cloud" link. Your site should look like this:

![image alt text](image_14.png)

## Exercise 3.1.2 : Deploy on Cloud (Dev env) From Local

### Scenario

In the previous step, we cloned our Drupal site from Cloud to our local environment and added a new module (code) to our site. This has resulted in changes to our local code and database and making them out of sync with Cloud Dev.

At this point, we’ll push changes from our Local Dev Site push to our Cloud Dev Site.

![image alt text](image_15.png)

NOTE: Copying the DB is a one-time event, mostly just for this workshop. Normally you would automate DB changes like enabling new modules.

### Step A: Syncing code - choose best option for you

### Option 1: On Mac or Windows with Acquia Dev Desktop 2

1. Open Acquia Dev Desktop, select your Cloud Dev site from the list of sites on the left column.

2. On the right side, you will see site details, at the bottom of this section, there are workflow options.

3. Select "Push to Cloud Dev" and the “Code” + “Database” checkboxes.

4. Click "Push code and database to Cloud Dev".

5. In the commit dialog, all files default to "Commit". Select any you do not want to commit yet and use the Action button to skip them.

6. Enter a descriptive commit message. For example: "Adding Hello Cloud module."

![image alt text](image_16.png)

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

$ drush sql-sync @mysite.local @mysite.dev

### Step B: Check your site

1. Once the Push is successful, visit your Cloud Dev Site. You can click the "cloud site" URL in Dev Desktop.

2. You should now see that your Local Dev Site and Cloud Dev Site are in sync!

![image alt text](image_17.png)

## Exercise 3.1.3 : Iterative development

### Scenario

* At this point, both our Local Dev Site and Cloud Dev Site are in sync.

* It is likely that Cloud Dev Site will be used by testers or client to add data for testing and you will continue development on the Local Dev Site .

* This will involve adding new data to your cloud site and modifications to code on your local development environment, for example.

### Step A. Add data to Production site

We’re going to add user data to the live  production site. This is the typical kind of data which you’ll begin to collect as people use your site.

1. On Acquia Free Cloud, there is no Production environment. We’ll use the Stage environment as a pretend production environment.

2. On the Acquia Cloud UI, click the "visit" arrow next to Stage, and add a couple of users via Drupal’s People > Add User page.

![image alt text](image_18.png)



### Step B. Modify the module

Now we’ll go back to your Local Dev Site and local development environment.

Open hello_cloud.module file, go to line number 23 and replace the function hello_cloud_page() with following code.  (If there is some issue with copying -pasting the following code, simply download the updated module files from the following URL, unzip and replace your existing files from hello_cloud folder) : [Files located here on Google Drive ](https://docs.google.com/file/d/0B_jmG1TM9szHbHJaVmtXb3lETW8/)

/* code starts */function hello_cloud_page() {  $output = 'Say Hello to the Cloud!!';  $output .= hello_cloud_list_users();  return $output;}// Return an HTML table of users and email addresses for the site.function hello_cloud_list_users (){  $result = db_query("SELECT * FROM {users} where uid<>0")->fetchAll();  foreach ($result as $value) {    $account = $value->uid ? user_load($value->uid) : '';    $rows[] = array(      $value->uid ? theme('username', array('account' => $account)) : '',      $value->uid ? check_plain($account->mail) : '',    );    }  $header = array(   'Others Saying Hello!',   'Email address',  );  $output = theme('table', array('header' => $header, 'rows' => $rows));  return $output;}/* code ends */

Test your new code locally. You only have a single user (the admin), but that is good enough for an initial test. If you want, in the next step you can copy your Production database all the way down to your local environment.

### Step C. Sync up the database changes

Copy your latest Production database to your Dev environment for testing. Use the Cloud UI:

![image alt text](image_19.png)

Optionally , you can also copy this database to your local environment for more complete testing before pushing your code changes to Cloud Dev.

**Option 1**: Use Dev Desktop to "Pull from Cloud Dev", select the Database checkbox, and press “Pull database from Cloud Dev”.

**Option 2**: Use the drush sql-sync command, if you have set up Drush aliases:

$ drush sql-sync @aqcloudcourse.dev @aqcloudcourse.local --no-cache --sanitize -v

Now verify if your functionality is working correctly with the data added from the cloud site. For this purpose, visit /hello-cloud link on the Local Dev Site, this should now reflect user data that we added on the Cloud Dev Site

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

### Step E. Test it’s working

Now verify if your functionality is working correctly on the Cloud Dev Site

For this purpose, login to your Cloud Dev Site and visit /hello-cloud link. You should see results like this

![image alt text](image_20.png)

*NOTE: If you do not see the changes, you may need to Clear Caches on the Cloud Dev Site. To do this, go to Admin > Configuration > Performance. Click Clear All Caches.*

## Lesson 3.1 Summary

In this section, we carried out iterative development workflow with Acquia Cloud.

At the beginning of this section, we had a clone of our Cloud Dev site in our Local Dev environment. We added new module (Hello_Cloud) to our local dev. We pushed this module to Cloud Dev using Acquia Dev Desktop (or Git)

We added some data on the Cloud Dev environment and tested our code.

We made some changes to the code locally, pulled the data from Cloud Dev to test our changes.

## Lesson 3.2: Configuration Management Workflows with Acquia Cloud

Drupal development typically involves two types of activities:

* Code : Addition of new modules

* Configuration: Building various site functionality using Drupal Admin UI

In the previous Section we saw how we can manage code while working with Acquia Cloud. In this Section, we will focus on Configurations management.

Most of Drupal site configurations are stored in the database, which makes them tedious to move between various environments of a site (from local to dev etc).

To overcome this issue, we can use a module called a features (  http://drupal.org/project/features  ) and move our key configurations to features.

Learn more about features  [https://drupal.org/node/580026](https://drupal.org/node/580026)

Follow exercises in this section to create a view, export the view to a feature, push the feature from Local Dev to Cloud Dev, modify the feature and sync changes.

## Exercise 3.2.1 Local Development

### Scenario:

At this point you wish to add new code and configuration to your local site

### Step A. Add modules

**Add contributed modules to sites/all/modules/contrib**

Add **CTools, Views, Features** modules on local environment. Either download and unzip or use the drush command -

drush dl ctools views features

### Step B. Add a View. Change your site configuration

Now we’ll build the site locally – adding a view and menu link in the view.

1. On your Local Dev Site, go to Modules page to enable these modules:

    * Chaos Tools

    * Features

    * Views

    * View UI

2. Tip: Verify that you have Articles Content Type. This is available if the Standard Profile is selected when you installed.

    * View name: "Articles".

    * Select Show "Content" of type “Article”

    * Select "Create a menu link"

    * Keep the remaining defaults.

    * ![image alt text](image_21.png)

3. Go to Structure > Views > Add New View.

4. Click "Save & Exit".

5. Check your new page at /articles. Your site will look like this. Yes, with no content!

![image alt text](image_22.png)

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

![image alt text](image_23.png)

### Option 2: On Any system with Git and Drush

1. **Code – via Git**

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

2. **Database (Configurations and Content) – via drush sql-sync **

This will push content types and configuration - and ALL content. For the first time, there doesn’t seem to be another way.

Example

drush sql-sync @aqcloudcourse.loc @aqcloudcourse.prod --no-cache --sanitize -v

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

6. ![image alt text](image_24.png)

7. Go back to Features overview page. Your feature should be listed here.

8. Select the feature, this will enable it.

9. Click "Save Settings".

### Step B: Push Changes - Feature created on Local Dev Site to the Cloud Dev Site

Choose the options which suits you best.

### Option 1 - On Mac or Windows with Acquia Dev Desktop 2

1. Start Acquia Dev Desktop 2, select your site in the left column.

    * Select "Push to Cloud Dev"

    * Select "Code" ( only code, don't select Database )

2. In the Local workflow section on the right side:

3. Click "Push code to Cloud Dev".

4. ![image alt text](image_25.png)

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

## Exercise 3.2.4 Iterative Development

### Scenario

In a real life project, Drupal Site Building is an iterative activity. It is not enough to build the site functionality just once and push to Cloud, but developers need to carry out site building and deploying activities on ongoing basis.

* Let us see how to handle this in our current exercise

* For this purpose, we’ll come back to our Local Dev Site and make changes to the Articles View using Views UI.

### Step A. Create changes

1. On Local Dev Site, go to Structure > Views > Articles.

2. In the Articles view edit page, click on Advanced to expand to see options.

3. Under No results behaviour > Click "Add".

4. ![image alt text](image_26.png)

5. Select Global: Text Area. Click Apply.

6. ![image alt text](image_27.png)

7. Add a message like "No articles available!"

8. ![image alt text](image_28.png)

9. Save the view.

### Step B: Recreate feature

1. Go to Structure > Features.

2. On the features overview page, locate your Articles feature. It will display status as 'Overridden'. (This is because you have changed / overridden the functionality from what's stored in the Feature)

3. ![image alt text](image_29.png)

4. Click on Re-create link next to the Articles feature.

5. On the Re-create page, click to expand the Advanced Options, and click "Generate Feature"

6. ![image alt text](image_30.png)

7. This will update your feature's code with latest changes that you carried out using UI.

### Step C: Push code to cloud dev site

1. Now follow steps to push your code to Cloud Dev Site. Try to complete this task without checking the steps in Exercise 3, Step C.

### Step D: Update Feature on Cloud Dev Site

1. Visit your Cloud Dev Site, Structure > Features. The code appears as "Overridden".

    * This is because Articles View is still using old settings and is not updated with new settings from the features.

    * You need to carry out an additional step to make sure that updated Features code is "refreshed" or applied properly on the Cloud Dev Site.

2. Click on the status text (Overridden).

3. Select the component which is overridden (Views) and Click "Revert Components"

4. ![image alt text](image_31.png)

5. Go back to Features overview page and verify if the Article feature is showing Default status

6. Go to the views page (/articles) and verify if newly added empty text is visible on the page.

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

cd path/to/repository

Create a file as follows using a text editor

hooks/dev/post-code-deploy/feature-update.sh

Add the following to your file feature-update.sh

#!/bin/bash

site=$1

env=$2

drush @$site.$env features-revert-all

### Step B: Push changes from local to cloud

Push your code to Cloud Dev Site.

Make changes to your feature on Local Dev Site.

Push changes to Cloud Dev Site.

### Step C: Verify changes

Visit the Articles View page (/articles) on your Cloud Dev Site .

Verify that changes made locally and pushed via the feature update are reflected on the Cloud Dev Site . The Features Revert step on the Cloud Dev Site is now automated via Cloud Hook.

### More Resources

There's a lot more that you can do with Cloud Hooks! Here are a few helpful resources to explore more

* [Automating with Cloud Hooks](https://docs.acquia.com/cloud/manage/cloud-hooks) (official documentation)

* [10 Ways Acquia Cloud Hooks can help you sleep at night](https://www.acquia.com/blog/10-ways-acquia-cloud-hooks-can-help-you-sleep-night)

* [Automate tests and more with Acquia Cloud Hooks](https://www.acquia.com/blog/automate-tests-and-more-acquia-cloud-hooks)

* [Cloud Hooks Examples on Github ](https://github.com/acquia/cloud-hooks)

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

## Lesson 3.4.2. Security

Security and compliance with Acquia Cloud  ([https://docs.acquia.com/cloud/arch/security](https://docs.acquia.com/cloud/arch/security))

Writing secure code (coding best practices for ensuring site security)

Best practices for working with the file system, cron jobs, SSL, SSH and other platform components.

    * [https://docs.acquia.com/cloud/files](https://docs.acquia.com/cloud/files)

    * [https://docs.acquia.com/cloud/ssh](https://docs.acquia.com/cloud/ssh)

## Lesson 3.4.3 Live deployment

Carrying out load testing on Acquia cloud. ([https://docs.acquia.com/cloud/load](https://docs.acquia.com/cloud/load))

Deploying a site to Production on Acquia Cloud  ([https://docs.acquia.com/cloud/manage/publish](https://docs.acquia.com/cloud/manage/publish))

Monitor server health and trends using Platform Health. ([https://docs.acquia.com/cloud/platform-health-faq](https://docs.acquia.com/cloud/platform-health-faq))

Annexure 1 - Videos Wish List

# Module 1

* What is Acquia Cloud : [https://www.youtube.com/watch?v=3R5uSuqIei4](https://www.youtube.com/watch?v=3R5uSuqIei4)

* Tour of Acquia Cloud interface: ([video script](https://docs.google.com/a/acquia.com/presentation/d/1b8dljtVIYF1rRgSt7et0vfrpA53ev5o5HbVj1MDPeMM/edit#slide=id.p)) ([existing version](https://www.youtube.com/watch?t=158&v=ozKOdWFavgQ))

* How Acquia Cloud is different compared to other popular hosting providers ([video script](https://docs.google.com/a/acquia.com/presentation/d/1kbE8dKvf5Mzjm1e6H5Yxc_jpnfeCAb7aMwWF6s-AP1o/edit#slide=id.p))

* Overview Acquia Cloud Architecture (brief video explaining the documentation at : [https://docs.acquia.com/cloud/arch](https://docs.acquia.com/cloud/arch) )

# Module 2

* Sign up for Acquia Cloud Free account and install a Drupal 7 site. (Prasad created a raw recording)

* Local tools setup on Windows  (Prasad created a raw recording)

* Clone a Cloud Site Locally, Add Modules Locally, Push Changes to Cloud. (Prasad created a raw recording)

# Module 3

* Audit your site for Performance best practices using Acquia Insight ([https://www.youtube.com/watch?v=wqEmL-ba1Ok](https://www.youtube.com/watch?v=wqEmL-ba1Ok) )(Cooper no longer at Acquia)

* Monitor server health and trends using Platform Health.

* Identify site bottlenecks using New Relic, TraceView or xhprof.

* Building a super-performance site on Acquia Cloud (using multiple caching layers)

* Carrying out load testing on Acquia cloud.
