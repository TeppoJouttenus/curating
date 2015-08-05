ng_files = []
ng_generalHeader = """"homepage" : "https://docs.angularjs.org/guide",
"freshnessDate" : 2015-06-02,
"license" : "CC BY 3.0"
}
-->
"""

ng_files.append({'infile' : '/Users/teppo/Content/angular.js/docs/content/guide/index.ngdoc',
'outfile' : '/Users/teppo/Content/angular/modules/index.md',
'header' : """<!--
{
"name" : "index",
"version" : "0.1",
"title" : "Guide to AngularJS Documentation",
"description" : "All you ever wanted to know about angular",
"canonicalSource" : "https://docs.angularjs.org/guide",
""" + ng_generalHeader})

ng_files.append({'infile' : '/Users/teppo/Content/angular.js/docs/content/guide/introduction.ngdoc',
'outfile' : '/Users/teppo/Content/angular/modules/introduction.md',
'header' : """<!--
{
"name" : "introduction",
"version" : "0.1",
"title" : "Introduction",
"description" : "Explain the big picture of Angular.",
"canonicalSource" : "https://docs.angularjs.org/guide/introduction",
""" + ng_generalHeader})

ng_files.append({'infile' : '/Users/teppo/Content/angular.js/docs/content/guide/concepts.ngdoc',
'outfile' : '/Users/teppo/Content/angular/modules/concepts.md',
'header' : """<!--
{
"name" : "concepts",
"version" : "0.1",
"title" : "Conceptual Overview",
"description" : "Brief overview of all the important parts of AngularJS.",
"canonicalSource" : "https://docs.angularjs.org/guide/concepts",
""" + ng_generalHeader})

ng_files.append({'infile' : '/Users/teppo/Content/angular.js/docs/content/guide/databinding.ngdoc',
'outfile' : '/Users/teppo/Content/angular/modules/databinding.md',
'header' : """<!--
{
"name" : "databinding",
"version" : "0.1",
"title" : "Data Binding",
"description" : "How to synchronize data between model and view components.",
"canonicalSource" : "https://docs.angularjs.org/guide/databinding",
""" + ng_generalHeader})

ng_files.append({'infile' : '/Users/teppo/Content/angular.js/docs/content/guide/controller.ngdoc',
'outfile' : '/Users/teppo/Content/angular/modules/controller.md',
'header' : """<!--
{
"name" : "controller",
"version" : "0.1",
"title" : "Controllers",
"description" : "Controller is a JavaScript constructor function that is used to augment the Angular Scope.",
"canonicalSource" : "https://docs.angularjs.org/guide/controller",
""" + ng_generalHeader})

ng_files.append({'infile' : '/Users/teppo/Content/angular.js/docs/content/guide/services.ngdoc',
'outfile' : '/Users/teppo/Content/angular/modules/services.md',
'header' : """<!--
{
"name" : "services",
"version" : "0.1",
"title" : "Services",
"description" : "Angular services are substitutable objects that are wired together using dependency injection.",
"canonicalSource" : "https://docs.angularjs.org/guide/services",
""" + ng_generalHeader})

ng_files.append({'infile' : '/Users/teppo/Content/angular.js/docs/content/guide/scope.ngdoc',
'outfile' : '/Users/teppo/Content/angular/modules/scope.md',
'header' : """<!--
{
"name" : "scope",
"version" : "0.1",
"title" : "Scopes",
"description" : "Scope is an object that refers to the application model.",
"canonicalSource" : "https://docs.angularjs.org/guide/scope",
""" + ng_generalHeader})

ng_files.append({'infile' : '/Users/teppo/Content/angular.js/docs/content/guide/di.ngdoc',
'outfile' : '/Users/teppo/Content/angular/modules/di.md',
'header' : """<!--
{
"name" : "di",
"version" : "0.1",
"title" : "Dependency Injection",
"description" : "Software design pattern that deals with how components get hold of their dependencies.",
"canonicalSource" : "https://docs.angularjs.org/guide/di",
""" + ng_generalHeader})

ng_files.append({'infile' : '/Users/teppo/Content/angular.js/docs/content/guide/templates.ngdoc',
'outfile' : '/Users/teppo/Content/angular/modules/templates.md',
'header' : """<!--
{
"name" : "templates",
"version" : "0.1",
"title" : "Templates",
"description" : "Angular combines the template with information from the model and controller to render the dynamic view that a user sees in the browser.",
"canonicalSource" : "https://docs.angularjs.org/guide/templates",
""" + ng_generalHeader})

ng_files.append({'infile' : '/Users/teppo/Content/angular.js/docs/content/guide/expression.ngdoc',
'outfile' : '/Users/teppo/Content/angular/modules/expression.md',
'header' : """<!--
{
"name" : "expression",
"version" : "0.1",
"title" : "Expressions",
"description" : "Angular expressions are JavaScript-like code snippets that are usually placed in bindings.",
"canonicalSource" : "https://docs.angularjs.org/guide/expression",
""" + ng_generalHeader})

ng_files.append({'infile' : '/Users/teppo/Content/angular.js/docs/content/guide/filter.ngdoc',
'outfile' : '/Users/teppo/Content/angular/modules/filter.md',
'header' : """<!--
{
"name" : "filter",
"version" : "0.1",
"title" : "Filters",
"description" : "A filter formats the value of an expression for display to the user.",
"canonicalSource" : "https://docs.angularjs.org/guide/filter",
""" + ng_generalHeader})

ng_files.append({'infile' : '/Users/teppo/Content/angular.js/docs/content/guide/forms.ngdoc',
'outfile' : '/Users/teppo/Content/angular/modules/forms.md',
'header' : """<!--
{
"name" : "forms",
"version" : "0.1",
"title" : "Forms",
"description" : "A Form is a collection of controls for the purpose of grouping related controls together.",
"canonicalSource" : "https://docs.angularjs.org/guide/forms",
""" + ng_generalHeader})

ng_files.append({'infile' : '/Users/teppo/Content/angular.js/docs/content/guide/directive.ngdoc',
'outfile' : '/Users/teppo/Content/angular/modules/directive.md',
'header' : """<!--
{
"name" : "directive",
"version" : "0.1",
"title" : "Directives",
"description" : "When should you create your own directives in your AngularJS app, and how to implement them.",
"canonicalSource" : "https://docs.angularjs.org/guide/directive",
""" + ng_generalHeader})

ng_files.append({'infile' : '/Users/teppo/Content/angular.js/docs/content/guide/animations.ngdoc',
'outfile' : '/Users/teppo/Content/angular/modules/animations.md',
'header' : """<!--
{
"name" : "animations",
"version" : "0.1",
"title" : "Animations",
"description" : "Animation hooks trigger animations during the life cycle of various directives.",
"canonicalSource" : "https://docs.angularjs.org/guide/animations",
""" + ng_generalHeader})

ng_files.append({'infile' : '/Users/teppo/Content/angular.js/docs/content/guide/module.ngdoc',
'outfile' : '/Users/teppo/Content/angular/modules/module.md',
'header' : """<!--
{
"name" : "module",
"version" : "0.1",
"title" : "Modules",
"description" : "You can think of a module as a container for the different parts of your app - controllers, services, filters, directives, etc.",
"canonicalSource" : "https://docs.angularjs.org/guide/module",
""" + ng_generalHeader})

ng_files.append({'infile' : '/Users/teppo/Content/angular.js/docs/content/guide/compiler.ngdoc',
'outfile' : '/Users/teppo/Content/angular/modules/compiler.md',
'header' : """<!--
{
"name" : "compiler",
"version" : "0.1",
"title" : "HTML Compiler",
"description" : "HTML compiler allows the developer to teach the browser new HTML syntax.",
"canonicalSource" : "https://docs.angularjs.org/guide/compiler",
""" + ng_generalHeader})

ng_files.append({'infile' : '/Users/teppo/Content/angular.js/docs/content/guide/providers.ngdoc',
'outfile' : '/Users/teppo/Content/angular/modules/providers.md',
'header' : """<!--
{
"name" : "providers",
"version" : "0.1",
"title" : "Providers",
"description" : "Provider recipe is the most comprehensive as well as most verbose of the recipe types.",
"canonicalSource" : "https://docs.angularjs.org/guide/providers",
""" + ng_generalHeader})

ng_files.append({'infile' : '/Users/teppo/Content/angular.js/docs/content/guide/bootstrap.ngdoc',
'outfile' : '/Users/teppo/Content/angular/modules/bootstrap.md',
'header' : """<!--
{
"name" : "bootstrap",
"version" : "0.1",
"title" : "Bootstrap",
"description" : "Explains the Angular initialization process.",
"canonicalSource" : "https://docs.angularjs.org/guide/bootstrap",
""" + ng_generalHeader})

ng_files.append({'infile' : '/Users/teppo/Content/angular.js/docs/content/guide/unit-testing.ngdoc',
'outfile' : '/Users/teppo/Content/angular/modules/unit-testing.md',
'header' : """<!--
{
"name" : "unit-testing",
"version" : "0.1",
"title" : "Unit Testing",
"description" : "These guidelines help you avoid creating an untestable application.",
"canonicalSource" : "https://docs.angularjs.org/guide/unit-testing",
""" + ng_generalHeader})

ng_files.append({'infile' : '/Users/teppo/Content/angular.js/docs/content/guide/e2e-testing.ngdoc',
'outfile' : '/Users/teppo/Content/angular/modules/e2e-testing.md',
'header' : """<!--
{
"name" : "e2e-testing",
"version" : "0.1",
"title" : "E2E Testing",
"description" : "Help you verify the health of your Angular application.",
"canonicalSource" : "https://docs.angularjs.org/guide/e2e-testing",
""" + ng_generalHeader})

ng_files.append({'infile' : '/Users/teppo/Content/angular.js/docs/content/guide/$location.ngdoc',
'outfile' : '/Users/teppo/Content/angular/modules/$location.md',
'header' : """<!--
{
"name" : "location",
"version" : "0.1",
"title" : "Using $location",
"description" : "The $location service parses the URL in the browser address bar and makes the URL available to your application.",
"canonicalSource" : "https://docs.angularjs.org/guide/$location",
""" + ng_generalHeader})

ng_files.append({'infile' : '/Users/teppo/Content/angular.js/docs/content/guide/css-styling.ngdoc',
'outfile' : '/Users/teppo/Content/angular/modules/css-styling.md',
'header' : """<!--
{
"name" : "css-styling",
"version" : "0.1",
"title" : "Working With CSS",
"description" : "List of CSS classes set by Angular.",
"canonicalSource" : "https://docs.angularjs.org/guide/css-styling",
""" + ng_generalHeader})

ng_files.append({'infile' : '/Users/teppo/Content/angular.js/docs/content/guide/i18n.ngdoc',
'outfile' : '/Users/teppo/Content/angular/modules/i18n.md',
'header' : """<!--
{
"name" : "i18n",
"version" : "0.1",
"title" : "i18n and l10n",
"description" : "Internationalization (i18n) is the process of developing products in such a way that they can be localized for languages and cultures easily. Localization (l10n), is the process of adapting applications and text to enable their usability in a particular cultural or linguistic market. .",
"canonicalSource" : "https://docs.angularjs.org/guide/i18n",
""" + ng_generalHeader})

ng_files.append({'infile' : '/Users/teppo/Content/angular.js/docs/content/guide/security.ngdoc',
'outfile' : '/Users/teppo/Content/angular/modules/security.md',
'header' : """<!--
{
"name" : "security",
"version" : "0.1",
"title" : "Security",
"description" : "This document explains some of AngularJS's security features and best practices that you should keep in mind as you build your application.",
"canonicalSource" : "https://docs.angularjs.org/guide/security",
""" + ng_generalHeader})

ng_files.append({'infile' : '/Users/teppo/Content/angular.js/docs/content/guide/accessibility.ngdoc',
'outfile' : '/Users/teppo/Content/angular/modules/accessibility.md',
'header' : """<!--
{
"name" : "accessibility",
"version" : "0.1",
"title" : "Accessibility with ngAria",
"description" : "The goal of ngAria is to improve Angular's default accessibility by enabling common ARIA attributes that convey state or semantic information for assistive technologies used by persons with disabilities.",
"canonicalSource" : "https://docs.angularjs.org/guide/accessibility",
""" + ng_generalHeader})

ng_files.append({'infile' : '/Users/teppo/Content/angular.js/docs/content/guide/ie.ngdoc',
'outfile' : '/Users/teppo/Content/angular/modules/ie.md',
'header' : """<!--
{
"name" : "ie",
"version" : "0.1",
"title" : "Internet Explorer Compatibility",
"description" : "This document describes the Internet Explorer (IE) idiosyncrasies when dealing with custom HTML attributes and tags.",
"canonicalSource" : "https://docs.angularjs.org/guide/ie",
""" + ng_generalHeader})

ng_files.append({'infile' : '/Users/teppo/Content/angular.js/docs/content/guide/production.ngdoc',
'outfile' : '/Users/teppo/Content/angular/modules/production.md',
'header' : """<!--
{
"name" : "production",
"version" : "0.1",
"title" : "Running in Production",
"description" : "There are a few things you might consider when running your AngularJS application in production.",
"canonicalSource" : "https://docs.angularjs.org/guide/production",
""" + ng_generalHeader})

ng_files.append({'infile' : '/Users/teppo/Content/angular.js/docs/content/guide/migration.ngdoc',
'outfile' : '/Users/teppo/Content/angular/modules/migration.md',
'header' : """<!--
{
"name" : "migration",
"version" : "0.1",
"title" : "Migrating from Previous Versions",
"description" : "Minor version releases in AngularJS introduce several breaking changes that may require changes to your application's source code; for instance from 1.0 to 1.2 and from 1.2 to 1.3.",
"canonicalSource" : "https://docs.angularjs.org/guide/migration",
""" + ng_generalHeader})

ng_tutorial_files = []

ng_tutorial_files.append({'infile' : '/Users/teppo/Content/angular.js/docs/content/tutorial/index.ngdoc',
'outfile' : '/Users/teppo/Content/angular/sections/index.md', 'header' : ''})

indices = ['00','01','02','03','04','05','06','07','08','09','10','11','12']
for index in indices:
    ng_tutorial_files.append({'infile' : '/Users/teppo/Content/angular.js/docs/content/tutorial/step_'+index+'.ngdoc',
    'outfile' : '/Users/teppo/Content/angular/sections/step_'+index+'.md', 'header' : ''})

ng_tutorial_files.append({'infile' : '/Users/teppo/Content/angular.js/docs/content/tutorial/the_end.ngdoc',
'outfile' : '/Users/teppo/Content/angular/sections/the_end.md','header' : ''})



mdn_files = []
mdn_files.append({'infile' : '/Users/teppo/Content/mdn/modules/re-introduction-raw.md',
'outfile' : '/Users/teppo/Content/mdn/modules/re-introduction.md',
'header' : ''})

nicholaszakas_files = []
nicholaszakas_files.append({'infile' : '/Users/teppo/Content/understandinges6/manuscript/01-The-Basics.md',
'outfile' : '/Users/teppo/Content/nicholaszakas/modules/01-The-Basics.md',
'header' : ''})


basho_generalHeader = """"homepage" : "http://docs.basho.com/riak/latest/dev/taste-of-riak/",
"freshnessDate" : 2015-05-18,
"license" : "CC Attribution 3.0"
}
-->
"""
basho_files = []
basho_files.append({'infile' : './theory/why-riak.md',
'outfile' : '/Users/teppo/Content/basho/modules/why-riak.md',
'header' : """<!--
{
"name" : "why-riak",
"version" : "0.1",
"title" : "Why Riak",
"description" : "Explain what Riak is and what problems it is designed to solve.",
""" + basho_generalHeader})
basho_files.append({'infile' : './quickstart.md',
'outfile' : '/Users/teppo/Content/basho/modules/quickstart.md',
'header' : """<!--
{
"name" : "quickstart",
"version" : "0.1",
"title" : "Riak Environment Setup",
"description" : "Get learners set up with their own local Riak environment.",
""" + basho_generalHeader})
basho_files.append({'infile' : './dev/taste-of-riak/python.md',
'outfile' : '/Users/teppo/Content/basho/modules/python.md',
'header' : """<!--
{
"name" : "python",
"version" : "0.1",
"title" : "Riak CRUD Operations in Python",
"description" : "Walk learners through basic CRUD operations.",
""" + basho_generalHeader})
basho_files.append({'infile' : './dev/taste-of-riak/querying.md',
'outfile' : '/Users/teppo/Content/basho/modules/querying.md',
'header' : ''})
basho_files.append({'infile' : './dev/taste-of-riak/querying-python.md',
'outfile' : '/Users/teppo/Content/basho/modules/querying-python.md',
'header' : ''})
basho_files.append({'infile' : './dev/taste-of-riak/object-modeling.md',
'outfile' : '/Users/teppo/Content/basho/modules/object-modeling.md',
'header' : ''})
basho_files.append({'infile' : './dev/taste-of-riak/object-modeling-python.md',
'outfile' : '/Users/teppo/Content/basho/modules/object-modeling-python.md',
'header' : ''})
basho_files.append({'infile' : './dev/references/http/get-bucket-props.md',
'outfile' : '/Users/teppo/Content/basho/modules/get-bucket-props.md',
'header' : ''})
basho_files.append({'infile' : './dev/references/http/set-bucket-props.md',
'outfile' : '/Users/teppo/Content/basho/modules/set-bucket-props.md',
'header' : ''})
basho_files.append({'infile' : './dev/references/http/reset-bucket-props.md',
'outfile' : '/Users/teppo/Content/basho/modules/reset-bucket-props.md',
'header' : ''})
basho_files.append({'infile' : './dev/references/http/list-buckets.md',
'outfile' : '/Users/teppo/Content/basho/modules/list-buckets.md',
'header' : ''})
basho_files.append({'infile' : './dev/references/http/list-keys.md',
'outfile' : '/Users/teppo/Content/basho/modules/list-keys.md',
'header' : ''})
basho_files.append({'infile' : './dev/references/http/fetch-object.md',
'outfile' : '/Users/teppo/Content/basho/modules/fetch-object.md',
'header' : ''})
basho_files.append({'infile' : './dev/references/http/store-object.md',
'outfile' : '/Users/teppo/Content/basho/modules/store-object.md',
'header' : ''})
basho_files.append({'infile' : './dev/references/http/delete-object.md',
'outfile' : '/Users/teppo/Content/basho/modules/delete-object.md',
'header' : ''})
basho_files.append({'infile' : './dev/references/http/mapreduce.md',
'outfile' : '/Users/teppo/Content/basho/modules/mapreduce.md',
'header' : ''})
basho_files.append({'infile' : './dev/references/http/secondary-indexes.md',
'outfile' : '/Users/teppo/Content/basho/modules/secondary-indexes.md',
'header' : ''})
basho_files.append({'infile' : './dev/references/http/ping.md',
'outfile' : '/Users/teppo/Content/basho/modules/ping.md',
'header' : ''})
basho_files.append({'infile' : './dev/references/http/status.md',
'outfile' : '/Users/teppo/Content/basho/modules/status.md',
'header' : ''})
basho_files.append({'infile' : './dev/references/http/list-resources.md',
'outfile' : '/Users/teppo/Content/basho/modules/list-resources.md',
'header' : ''})
basho_files.append({'infile' : './dev/references/http/search-query.md',
'outfile' : '/Users/teppo/Content/basho/modules/search-query.md',
'header' : ''})
basho_files.append({'infile' : './dev/references/http/search-index-info.md',
'outfile' : '/Users/teppo/Content/basho/modules/search-index-info.md',
'header' : ''})
basho_files.append({'infile' : './dev/references/http/fetch-search-index.md',
'outfile' : '/Users/teppo/Content/basho/modules/fetch-search-index.md',
'header' : ''})
basho_files.append({'infile' : './dev/references/http/store-search-index.md',
'outfile' : '/Users/teppo/Content/basho/modules/store-search-index.md',
'header' : ''})
basho_files.append({'infile' : './dev/references/http/delete-search-index.md',
'outfile' : '/Users/teppo/Content/basho/modules/delete-search-index.md',
'header' : ''})
basho_files.append({'infile' : './dev/references/http/fetch-search-schema.md',
'outfile' : '/Users/teppo/Content/basho/modules/fetch-search-schema.md',
'header' : ''})
basho_files.append({'infile' : './dev/references/http/store-search-schema.md',
'outfile' : '/Users/teppo/Content/basho/modules/store-search-schema.md',
'header' : ''})
basho_files.append({'infile' : './dev/taste-of-riak/clojure.md',
'outfile' : '/Users/teppo/Content/basho/modules/clojure.md',
'header' : """<!--
{
"name" : "clojure",
"version" : "0.1",
"title" : "Riak with Clojure",
"description" : "Get learners using Riak with Clojure.",
""" + basho_generalHeader})
