<!--
{
"name": "modules",
"version" : "0.1",
"title" : "Finding and Reviewing Links",
"description" : "Outlearn's master plan for finding all the awesomeness out there.",
"freshnessDate" : 2015-10-06,
"license" : "All Rights Reserved"
}
-->

<!-- @section -->

# What Makes a Good Module

Best learning is customized based on the needs of individuals and teams. Current learning solutions make that much harder than it should be. Outlearn unleashes customization through Modules that any developer or manager can assemble to Learning Paths. You are right now viewing a Module called "Finding and Reviewing Links" and you may be seeing it on its own or as part of a Path. This is a native Module where all the content is hosted on Outlearn so it can contain enrichments like sections and tasks.

Outlearn also supports "Link Modules" which are created from links submitted to the platform. They pull some key information from the link target and add in a screenshot to make it easy to see what the link is all about. We expect that early on there will be much more Link Modules than native Modules. However, we want to make Outlearn such an attractive publishing platform that longer term lots of developer authors want to publish natively here.

As an expert in your topic area, you have a natural sense of what makes a resource awesome for professional developers. That's the number one criteria for you to follow when deciding what to include. We want all the best resources for a given topic to be included in our topic streams. When evaluating a link, please consider whether it has:

* Accurate and up-to-date content
* Relevant topic for developers

In addition to all the best stuff, we want to have a comprehensive collection of good resources around the web. These good links will point to stuff that may not be polished or unusually insightful but will still be helpful for developers. This applies especially to content that is unique so that there isn't any better version of the same information available somewhere else. Because we target professional developers who have more detailed and specialized learning needs than beginners, there are usually fewer competing resources available. If a piece of content is the best resource available for a given need, we should include it even if it has some shortcomings.

If a piece of content is so poorly written that it's painful to read or it contains clear inaccuracies, then we do not want it at Outlearn. We also do not want redundant content that is equivalent to what we already have.

It's not enough for us to fill the Outlearn catalog with high quality stuff. That quality must also be obvious to the users. One of the fastest ways to demonstrate quality is to include well-recognized content. We should include all the relevant posts and resources from the official teams developing Angular, Docker, etc. We also want to include as many resources as possible from respected thought leaders who talk at conferences, write well-known blogs, teach online courses, etc. You can read in the Review Links section below about how we feature Modules. Please feature all the content from teams and individuals with big brands.

Potential targets for Outlearn Link Modules include:

* **Tutorials**. We are especially interested in advanced tutorials for very specific needs, such as how to combine two technologies together, how to use something at scale, how to deploy a tool in production etc.
* **Blog posts**. These could be about trends or news in the topic area or related technologies and tools. Opinionated and well argued posts about best practices or common mistakes are super valuable. When someone shares the mistakes they made or how they overcame a challenge, that will be gold to a developer in a similar situation. News can be about the general topic such as Node.js or a specific package as long as the package is interesting.
* **Videos**. Learning from videos is less flexible than reading because it's harder to scan and skip around. But conference talks and other presentations can still be invaluable and there are also other good video resources like tutorials or interviews with thought leaders.
* **Software libraries or packages**. Staying up-to-date on the latest libraries, gems, packages, etc. can be hard work and we can help by including high-quality ones in the catalog.
* **Tools**. Developers are passionate about their tools so links to Atom or Sublime Text packages, build tools, testing frameworks, etc. are great additions to the Outlearn catalog.
* **Anything else valuable**. The list above certainly misses some solid resources that should be included so feel free to add other valuable stuff.

We are currently staying focused on technical resources so we will not include discussions about how it is to work for a startup or cool movies that developers love. For borderline cases, we can discuss what should go in via [Slack](https://outlearn.slack.com/messages/curators/).

<!-- @section -->

# Review Links

When reviewing links, the main consideration is the quality of the original resource as described in the section What Makes a Good Module. In addition, please also check that our platform turned the link into an Outlearn module correctly so that the title, description, and screenshot are reasonable. Out end goal is to have new content appear in the catalog as quickly after publication as possible. We would love for you to review links several times a week.

In this Learning Path we will often use words link and Module interchangeable because each submitted link is turned into a module that either gets accepted or rejected. So reviewing links or Modules means the same thing.

You should have received login information from Outlearn for the admin panel that lets you review submitted links. Go ahead and log in and you will see the screen below:

![Curator Navigation](https://raw.githubusercontent.com/outlearn-content/assets/master/cc/navigate.png)

Click on Content Catalog and Review Module. Note that Review Module is just a convenient shortcut to a filtered view of the Links page so feel free to use whichever works for you.

You will see all the links to be reviewed as shown below:

![Curator Link List](https://raw.githubusercontent.com/outlearn-content/assets/master/cc/link-list.png)

Below is a suggested workflow for link review. Feel free to suggest improvements in Slack.

* Use Suggested Tags filter to find links with tags relevant to your Topic Stream. For example, you can filter with suggested tags containing _docker_ to find links with tags _docker_, _docker-compose_, etc.
* Open up a handful of links in separate tabs by clicking Review at the end of the line.
* Go to the first new tab to review the link. If you make the browser window wide enough, you can see the Module preview next to the controls. You may want to zoom out to see more of the screenshot without scrolling. See a sample below:
    ![Curator Link Review](https://raw.githubusercontent.com/outlearn-content/assets/master/cc/review.png)
* Look at the preview and check that the title, description, and the screenshot all look ok. If any of them are missing, misformatted, or otherwise weird, click Escalate. Escalation should be used whether the content is good or not. It keeps broken Modules away from the catalog. Outlearn staff will review all escalated Modules to see how we can improve our code that creates the Modules. We will try to recreate the Module in better condition so that it can be reviewed again for content quality.
* If the preview looks good, click on the Generating Link to go to the original content and to review if it should be included in the catalog.
* If the link content is not good enough, go ahead and Reject it.
* If the content is good, check the suggested tags. We allow up to five tags per Module. Make sure that the most important tags are included. The section below talks more about tagging.
* Decide if you want to Feature the item. Featured items have a bright background color in the catalog. See an example below. As a rule of thumb, you can aim to feature about 10-20% of the Modules. You should Feature anything that you consider to be a "must-read". These items will be promoted in our newsletters and in other ways.
    ![Feature](https://raw.githubusercontent.com/outlearn-content/assets/master/cc/feature.png)
* Accept the content and close the tab. Opening several tabs at once and closing them after review is much faster than using one tab to load link after link.
* Repeat the review steps for all the Modules with suggested tags that match your Topic Stream.
* Suggested tags are not completely reliable so please also look through the rest of the Modules to find others that fit your Topic Stream.

We have a set of keyboard shortcuts to make your life easier:

```
t = focus tag field
f = toggle featured
ctl-a = approve
ctl-r = reject
ctl-e = escalate
```

If you made a mistake in tagging or accepting, rejecting, or escalating a Module, you can re-review it. Just choose the correct state in the filters such as rejected to find the module and then click Review again.

Note that all curators see all Modules no matter what their subject is. There is no easy way to change that because we do not always know which tags are correct for a submitted link. Feel free to review any Modules where you have the required expertise. If you feel uncertain, just leave the Module in pending_review state and another curator will deal with it.

<!-- @section -->

# Tagging

Outlearn uses tags to include Modules and Paths in the right Topic Streams so getting them right matters a lot. We automatically fill in suggested tags based on the content but you should make sure that you use the most relevant tags. As you update the tags you can see into which Topic Streams the Module will go. Some Modules should go to several Topic Streams, such as something tagged with `es6` (Pro JS) and `angularjs` (AngularJS).

As you start typing in tags, the page suggest autocompletions. They are ordered based on how often each tag is used in our catalog. Below is a list of most relevant tags that we want to use canonically. They are mostly borrowed from Stack Overflow's canonical tags. If you ever have a question about a canonical tag, you can check what Stack Overflow uses. The tags are always lowercase, always one word with occasional multiword tags hyphenated:

```
angularjs
node.js
tips-and-tricks (use for best practices as well)
common-mistakes
continuous-integration
continuous-delivery
debugging
logging
design-patterns
```

### Miscellaneous Notes About Tagging

* If you review a resource about AngularJS or Node.js that would also benefit people interested in JavaScript in general, go ahead and add the javascript tag.

<!-- @section -->

# Submit Links

The workflow for submitting links is the same for users and curators. You have to be logged in on outlearn.com to submit a link. Go to our [Contribute a Link](https://www.outlearn.com/links/contribute) page, paste in a link and optionally add suggested tags. We have a bookmarklet to submit links easily and are considering additional ways to submit such as a Chrome plugin, etc. If you have opinions on how to make link submissions as easy as possible, please share them in Slack.

We aim to automate as much of the link submission as possible with foragers that go through pre-selected web resources and submit links automatically for review. What we ask you to do is to find things that the foragers are missing and give us feedback so that we improve the sources and filters used in the foragers. You can take a look at the individual Topic Stream on outlearn.com to see what's missing. You can also use the admin panel to view all links and search by URL for links or websites that are already represented on the platform.
