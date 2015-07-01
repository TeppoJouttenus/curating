<!--
{
"name" : "platform-installation",
"version" : "0.1",
"title" : "Platform installation and tools setup",
"description": "Get ready with all that you need for publishing on Acquia Cloud using hands-on exercises",
"freshnessDate" : 2015-06-01,
"homepage" : "https://docs.acquia.com/cloud",
"license" : "All Rights Reserved"
}
-->

<!-- @section -->

# Learning Objectives

This Module contains hands-on exercises for creating an Acquia Cloud instance, installing a Drupal distribution on the instance and setting up local development environment to work with Acquia Cloud.

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

<!-- @section -->

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

<!-- @section -->

## Lesson 2.2: Setup Acquia Cloud Environment

## Exercise: Setup Acquia Cloud and Install Drupal

<!-- @link, "url" : "https://insight.acquia.com/free", "text": "Sign up for Acquia Free Cloud. " -->

![image alt text](https://raw.githubusercontent.com/outlearn-content/assets/master/ac/image_0.png)

Click Manage my code link when the site is provisioned

![image alt text](https://raw.githubusercontent.com/outlearn-content/assets/master/ac/https://raw.githubusercontent.com/outlearn-content/assets/master/ac/image_1.png)

From the drop down menu of Dev environment box, select Install Drupal and in the following screen, select Drupal 7 distribution.

![image alt text](https://raw.githubusercontent.com/outlearn-content/assets/master/ac/https://raw.githubusercontent.com/outlearn-content/assets/master/ac/image_2.png)

![image alt text](https://raw.githubusercontent.com/outlearn-content/assets/master/ac/https://raw.githubusercontent.com/outlearn-content/assets/master/ac/image_3.png)

![image alt text](https://raw.githubusercontent.com/outlearn-content/assets/master/ac/https://raw.githubusercontent.com/outlearn-content/assets/master/ac/image_4.png)

When the install task is done, click the orange box "Set up my site" link next to Dev to visit the site and run Drupal’s install process.

<!-- @task, "hasDeliverable" : false, "text" : "Run Drupal’s install process."-->

![image alt text](https://raw.githubusercontent.com/outlearn-content/assets/master/ac/https://raw.githubusercontent.com/outlearn-content/assets/master/ac/image_5.png)

At this point, the online development environment (Cloud Dev Site) is ready and this is now your online repository.

<!-- @section -->

## Lesson 2.3: Generate and Add Public Key to Acquia Cloud Account

### Step A. Generate Public Key

You will generate a public key on your machine, unless you want to use an existing key.

#### Mac OSX :

1. Open a shell or command-line instance on your computer.

2. Ensure that you don't already have a public key saved to your computer. To do this, run the following command:

    ```
    cd ~/.ssh
    ls -l
    ```

3. If the directory and key file exists, run the following commands to back up the key `id_rsa`, as this procedure overwrites your current key if it is named `id_rsa`.

    ```
    mkdir key_backup
    mv id_rsa* key_backup
    ```

4. Generate a new public/private key pair using the keygen command:

    ```
    ssh-keygen -b 4096
    ```

5. The keygen command prompts you for the directory to contain the key.

    ```
    Generating public/private rsa key pair.

    Enter file in which to save the key (/Users/[user_dir]/.ssh/id_rsa):
    ```

6. Press Enter to accept the default location of /.ssh/id_rsa in your user directory.

    ```
    Enter passphrase (empty for no passphrase): [passphrase]

    Enter same passphrase again: [passphrase]
    ```

7. Substitute [passphrase] with your own text. This is for encrypting the private key on your computer. It's possible to use a blank [passphrase], but if you do this, another user can impersonate you with a copy of the key file.

    ```
    Note: Be sure to keep track of the [passphrase] since you will need to enter it when using the key.
    ```

8. The keygen command displays the following output:

    ```
    Generating public/private rsa key pair.

    Your identification has been saved in /Users/[user_dir]/.ssh/id_rsa.

    Your public key has been saved in /Users/[user_dir]/.ssh/id_rsa.pub.

    The key fingerprint is:

    52:96:e9:c8:06:c2:57:26:6d:ef:2f:0c:d9:81:f4:1c username@hostname
    ```

9. Copy the key to your clipboard. Run the following code to copy the key to your clipboard:

    ```
    pbcopy < ~/.ssh/id_rsa.pub

    Copies the contents of the id_rsa.pub file to your clipboard
    ```

10. Alternatively, using your favorite text editor, you can open the ~/.ssh/id_rsa.pub file and copy the contents of the file manually.

(Instructions as per  [https://docs.acquia.com/cloud/ssh/enable/key-mac-unix](https://docs.acquia.com/cloud/ssh/enable/key-mac-unix))

#### Windows:

For Windows, you need a program like Git Bash to generate a key.

1. Start Git Bash (from right-click contextual menu in Win Explorer).

2. Create key pair by typing the command:  ssh-keygen -t rsa

3. Key pair will get generated $ HOME \.ssh folder

($ HOME is the home folder for the user, typically at: C:\Users\[Your User Name])

<!-- @task, "hasDeliverable" : false, "text" : "Generate a public key."-->

### Step B. Add SSH key to Acquia cloud

You will add the SSH key your Acquia Cloud site via the "Users and keys" page.

<!-- @link, "url" : "https://docs.acquia.com/cloud/ssh/enable/add-key", "text": "Follow the instructions to add the SSH key to Acquia Cloud. " -->


<!-- @section -->

## Lesson 2.4a: Create a local development environment on Windows or Mac with Dev Desktop

### Exercise

* Install Acquia Dev Desktop 2 from [https://www.acquia.com/downloads](https://www.acquia.com/downloads)

* Add your Acquia Cloud Account details to Dev Desktop

* Add location of your Private Key (Windows)

* Refresh the sites list and check if Acquia Cloud Site created in the previous exercise is listed.

* Clone the site locally.

<!-- @task, "hasDeliverable" : false, "text" : "Complete the exercise to create a local development environment."-->

## Lesson 2.4b: Create a local development environment on Windows with WAMP (Optional)

We strongly recommend using Acquia Dev Desktop 2 as explained in previous exercise as your local development environment. However, for some reasons if you cannot use Dev Desktop and wish to use your own WAMP / XAMP setup as local development environment, follow the steps given below to setup integration of your local environment with Acquia Cloud.

### Step A: Install WAMP or XAMPP

(We will not cover detailed steps for installing WAMP / XAMPP or any other \*AMP stack that users are using for their local development environment. We are assuming that, for some reasons, users are not using Acquia Dev Desktop for local development, but are using Acquia Cloud for hosting their site.)

<!-- @task, "hasDeliverable" : false, "text" : "Install WAMP or XAMPP."-->

### Step B: Install GIT

1. Download Git for Windows from  http://git-scm.com/download/win

2. Install downloaded file, make sure to select Git GUI and Git Bash options while installing

3. Also, select the option Run Git from Windows Command prompt option

![image alt text](https://raw.githubusercontent.com/outlearn-content/assets/master/ac/https://raw.githubusercontent.com/outlearn-content/assets/master/ac/image_6.png)

![image alt text](https://raw.githubusercontent.com/outlearn-content/assets/master/ac/image_7.png)

<!-- @task, "hasDeliverable" : false, "text" : "Install Git."-->

### Step C: Copy Git URL from Acquia Cloud

1. Login to your Acquia Cloud Account

2. Click Git URL link located at top right corner of the page    ![image alt text](https://raw.githubusercontent.com/outlearn-content/assets/master/ac/image_8.png)

3. A pop-up window will display Git URL to be used for connecting with your Cloud Site    ![image alt text](https://raw.githubusercontent.com/outlearn-content/assets/master/ac/image_9.png)

4. Select All and Copy this URL to your clipboard

<!-- @task, "hasDeliverable" : false, "text" : "Copy Git URL from Acquia Cloud."-->

### Step D: Clone the Cloud Codebase locally using Git

1. Open Windows Explorer

2. Navigate to your $Home\Sites folder (typically `C:\Users\[Your_User_Name\Sites`]

3. Right click inside the folder and click Git Bash Here from the contextual menu    ![image alt text](https://raw.githubusercontent.com/outlearn-content/assets/master/ac/image_10.png)

4. In the Git Bash console, type the command git clone [Your-Git-URL-copied-from-Cloud]    ![image alt text](https://raw.githubusercontent.com/outlearn-content/assets/master/ac/image_11.png)

<!-- @task, "hasDeliverable" : false, "text" : "Clone the Cloud Codebase locally using Git."-->

### Step F - Install Drupal site locally

1. Open your browser

2. Open PHPMyAdmin from your local WAMP/XAMPP environment

3. Create a new blank Databases

4. In the browser, navigate to the folder where you cloned the repository in the step above inside your localhost : typically `http://localhost/[your_cloned_folder]`

5. Drupal installation wizard will kick-start. Provide the Database credentials created in step F-3 above.

6. Finish Drupal installation normally.

<!-- @task, "hasDeliverable" : false, "text" : "Install Drupal site locally."-->

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

<!-- @task, "hasDeliverable" : false, "text" : "Synchronize database."-->

<!-- @section -->

## Module 2 Summary

### In this module, we performed the following steps

* Setup Acquia Cloud environment

* Created a new site using an existing distribution in Cloud Dev Environment

* Installed software tools for local development

* Generated and added our Public Key to Acquia Cloud

* Cloned our Acquia Cloud Dev site to Local Dev environment

### At this point, our Cloud Dev site and Local Dev sites are ready and in sync!

# ![image alt text](https://raw.githubusercontent.com/outlearn-content/assets/master/ac/image_12.png)
