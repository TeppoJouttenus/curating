<!--
{
"name" : "development-workflow",
"version" : "0.1",
"title" : "Yext Development Workflow",
"description": "Learn how we work together.",
"freshnessDate" : 2015-06-01,
"homepage" : "https://sites.google.com/a/yext.com/engineering/orientation/development-workflow",
"license" : "All Rights Reserved"
}
-->

<!-- @section -->

# Teams

Yext Engineering is organized into 3-8 person teams.  [Here is a current list of teams, along with their focus area](https://sites.google.com/a/yext.com/engineering/teams).

<!-- @section -->

# Scrum

Each team organizes its work using the Scrum methodology.

* Teams take work from a prioritized backlog of "User Stories", maintained in JIRA by the Team Lead in collaboration with the engineering team members and the product team.  "User Stories" are so named because they are user-visible pieces of functionality.
* Work is done in "Sprints", which are 2-week periods.
* To begin a sprint, the team has a planning meeting where they go over the upcoming user stories to (a) understand what they entail and (b) determine how big the task is, in "story points".  With historical information on how many story points were completed, the team knows roughly how much work to accept for the sprint.
* Subsequently, the team writes out the tasks for each user story and creates the sprint's "scrum board".  The scrum board describes progress on each task and serves to keep everyone on the same page with respect to sprint progress.
* Daily, teams meet for a 5-10 minute "standup", where each person says (1) what they did yesterday, (2) what they are planning to do today, and (3) if they are blocked on anything.
* On the last day of the sprint, the teams prepare and give a 20 minute demo to their stakeholders.  The demo is meant to be an interesting and useful demonstration of the work completed during the sprint that keeps stakeholders abreast of changes to their system (and impressed with the engineering and product team's productivity).
* To conclude the sprint, the team meets for a "Retrospective", where they discuss feelings about how the sprint went.  They discuss what went well (and they should keep doing / do more of) and what didn't go well (what to stop doing / problems to address).  They use those two discussions as input to decide on action items, or changes to the team process, workflow, technology, etc.

<!-- @section -->

# Technical Operations

Urgent bugs and feature requests that need to be addressed before the next sprint are tracked in Zendesk at [http://techops.yext.com/](http://techops.yext.com/).

Tickets make their way through the following workflow:

1. A Yext employee sends an email to techops@yext.com.
2. New tickets are assigned to the "L3: Tech Ops" group.
3. A member of team Fido triages the ticket, determining which team owns the product in question.
4. Fido assigns the ticket to the appropriate "L3: Tech Ops - [Team]" group.
5. An engineer on the relevant team assigns to the ticket to their Team account and adds a comment to the ticket letting the requester know that work has begun and **who that engineer is**.

**Non-urgent tickets**: If a ticket can be put off until a future sprint, it is a reasonable resolution for the team lead or product owner to create a JIRA issue, leave a Zendesk comment giving the requester a link to the JIRA issue, and close the Zendesk ticket. Tickets should not languish in Zendesk for longer than a month.

View pending tech ops tickets:

* [Unsolved tickets in my groups](http://www.google.com/url?q=http%3A%2F%2Ftechops.yext.com%2Frules%2F22493702&sa=D&sntz=1&usg=AFrqEzfxAjbKY1Wfz6kVcrGICvmi5CvN_w)
* [Open tech ops tickets](http://www.google.com/url?q=http%3A%2F%2Ftechops.yext.com%2Frules%2F33747236&sa=D&sntz=1&usg=AFrqEzfgYkTFkRsZg3KsUoZ1X44JDKWF0A)

<!-- @task, "text" : "Review some tickets." -->

To receive email about all tickets, sign up for one of the Google Groups:

* [techops-new](https://groups.google.com/a/yext.com/d/forum/techops-new-pub) - notification of all new tech ops tickets
* [techops-all](https://groups.google.com/a/yext.com/d/forum/techops-all-pub) - notification of all updates to tech ops tickets

<!-- @section -->

# Code Review Process

Yext Engineering requires pre-commit code reviews. This enables knowledge sharing among developers and increases quality of the resulting software.  The development process works as follows:

* Decide that you have reached a good milestone and are ready to send your work for review
* Decide on a code reviewer. A good reviewer is knowledgeable about the relevant code, system, or technology. This can be a peer or your team lead.
* Use the "upload.py" tool to upload a patch containing your change to the Review server and email your reviewer.
* To continue working while a code review is outstanding, use your version control system to save the state of that task (e.g. create a new branch).  


Good code reviews are 50-250 lines of code, encompass a day of work, and implement a small self-contained improvement (perhaps with unit tests).  Often tasks will be larger, and it is then the engineer's responsibility to break their work into reviewable pieces.  

Here is a checklist for deciding if your changelist is ready for review.

My changelist:

* is not too big
* is an atomic improvement
* is complete / ready to check in
* has been self-reviewed
* has been tested

<!-- @task, "hasDeliverable" : true, "text" : "Find an earlier code submission and check if it fulfils the changelist criteria. Write short comments about the changelist and submit them here."-->


The code reviewer **should** address the following points

1. Correctness: Does the code do what it claims to do? Is the code correct in both the nominal case and the boundary cases? As a reviewer, this is your opportunity to point out edge conditions of which the original developer may not have been aware.
2. Complexity: Does the code accomplish its task in a reasonably straightforward way? If you can point out simpler approaches that do not compromise the correctness or performance of the code, you should.
3. Consistency: Does the code achieve its basic goals in a way that is consistent with how similar code in our codebase achieves those goals? Is it re-using the available libraries and utility classes? Where possible, has code been refactored for re-use instead of just copying and pasting?
4. Maintainability: Could the code be extended by another developer on the team with a reasonable amount of effort? More than any item on the list, this is the karma investment you make by doing code reviews - the code you review today may be the code you have to update tomorrow, so taking the time to make sure it's maintainable by others pays itself back to you.
5. Scalability: Will the code be performant at the expected volumes? It is important that this question always be asked in the context of expected volumes. When building a new product in an untested market, it is fine to write code that works for 1000 users but not 10,000; if the product should be that successful, we will profile, optimize, and, when necessary, re-write the critical bits. The corollary is that we should not spend time optimizing code when the market demand is unproven.
6. Style: Does the code match the team style guide? This should rarely be controversial.

<!-- @task, "hasDeliverable" : true, "text" : "Write a short code review for the submission you chose in the previous task and submit the review here."-->

The code reviewer **should not** address the following:

1. Scope or mission feedback: "I don't think you should be doing this project" is almost never a useful comment for a code review. If you think the team is embarking on projects that are not worthwhile, that is great feedback to share, but not in the context of a code review. The exception here is if someone is introducing a new way of doing something that is already well-handled in some other way.
2. Design review: A code review is not the time to evaluate the overall design of a project. For example, "I don't think you should be using the DB to store this data" is not useful. Of course it is incumbent upon the developer to have their designs reviewed before implementation, and there will be scenarios in which the fundamental design is questioned during the implementation, but for a project that has been through a design review, let the results of that design stand.
3. Personal preference: "I would rather you do it my way" is an invitation to an unproductive debate. If you have a way that is demonstrably better, you should always argue for it, but if you find yourself trading hypothetical scenarios in which your solution is better than the one already implemented, with no way of determining the likelihood of said scenarios, the default is to use what the developer has already written.
