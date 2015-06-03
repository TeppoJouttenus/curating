ng_files = []
ng_generalHeader = """"homepage" : "https://docs.angularjs.org/guide",
"freshnessDate" : 2015-06-02,
"license" : "CC BY 3.0"
}
-->
"""

ng_files.append({'infile' : '/Users/teppo/Content/angular.js/docs/content/guide/introduction.ngdoc',
'outfile' : '/Users/teppo/Content/angular/modules/introduction.md',
'header' : """<!--
{
"name" : "introduction",
"version" : "0.1",
"title" : "Introduction",
"description" : "Explain the big picture of Angular.",
""" + ng_generalHeader})

ng_files.append({'infile' : '/Users/teppo/Content/angular.js/docs/content/guide/concepts.ngdoc',
'outfile' : '/Users/teppo/Content/angular/modules/concepts.md',
'header' : """<!--
{
"name" : "concepts",
"version" : "0.1",
"title" : "Conceptual Overview",
"description" : "Brief overview of all the important parts of AngularJS.",
""" + ng_generalHeader})

ng_files.append({'infile' : '/Users/teppo/Content/angular.js/docs/content/guide/databinding.ngdoc',
'outfile' : '/Users/teppo/Content/angular/modules/databinding.md',
'header' : """<!--
{
"name" : "databinding",
"version" : "0.1",
"title" : "Data Binding",
"description" : "How to synchronize data between model and view components.",
""" + ng_generalHeader})

ng_files.append({'infile' : '/Users/teppo/Content/angular.js/docs/content/guide/controller.ngdoc',
'outfile' : '/Users/teppo/Content/angular/modules/controller.md',
'header' : """<!--
{
"name" : "controller",
"version" : "0.1",
"title" : "Controllers",
"description" : "Controller is a JavaScript constructor function that is used to augment the Angular Scope.",
""" + ng_generalHeader})

ng_files.append({'infile' : '/Users/teppo/Content/angular.js/docs/content/guide/services.ngdoc',
'outfile' : '/Users/teppo/Content/angular/modules/services.md',
'header' : """<!--
{
"name" : "services",
"version" : "0.1",
"title" : "Services",
"description" : "Angular services are substitutable objects that are wired together using dependency injection.",
""" + ng_generalHeader})

ng_files.append({'infile' : '/Users/teppo/Content/angular.js/docs/content/guide/scope.ngdoc',
'outfile' : '/Users/teppo/Content/angular/modules/scope.md',
'header' : """<!--
{
"name" : "scope",
"version" : "0.1",
"title" : "Scopes",
"description" : "Scope is an object that refers to the application model.",
""" + ng_generalHeader})

ng_files.append({'infile' : '/Users/teppo/Content/angular.js/docs/content/guide/di.ngdoc',
'outfile' : '/Users/teppo/Content/angular/modules/di.md',
'header' : """<!--
{
"name" : "di",
"version" : "0.1",
"title" : "Dependency Injection",
"description" : "Software design pattern that deals with how components get hold of their dependencies.",
""" + ng_generalHeader})

ng_files.append({'infile' : '/Users/teppo/Content/angular.js/docs/content/guide/templates.ngdoc',
'outfile' : '/Users/teppo/Content/angular/modules/templates.md',
'header' : """<!--
{
"name" : "templates",
"version" : "0.1",
"title" : "Templates",
"description" : "Angular combines the template with information from the model and controller to render the dynamic view that a user sees in the browser.",
""" + ng_generalHeader})

ng_files.append({'infile' : '/Users/teppo/Content/angular.js/docs/content/guide/expression.ngdoc',
'outfile' : '/Users/teppo/Content/angular/modules/expression.md',
'header' : """<!--
{
"name" : "expression",
"version" : "0.1",
"title" : "Expressions",
"description" : "Angular expressions are JavaScript-like code snippets that are usually placed in bindings.",
""" + ng_generalHeader})

ng_files.append({'infile' : '/Users/teppo/Content/angular.js/docs/content/guide/filter.ngdoc',
'outfile' : '/Users/teppo/Content/angular/modules/filter.md',
'header' : """<!--
{
"name" : "filter",
"version" : "0.1",
"title" : "Filters",
"description" : "A filter formats the value of an expression for display to the user.",
""" + ng_generalHeader})

ng_files.append({'infile' : '/Users/teppo/Content/angular.js/docs/content/guide/forms.ngdoc',
'outfile' : '/Users/teppo/Content/angular/modules/forms.md',
'header' : """<!--
{
"name" : "forms",
"version" : "0.1",
"title" : "Forms",
"description" : "A Form is a collection of controls for the purpose of grouping related controls together.",
""" + ng_generalHeader})

ng_files.append({'infile' : '/Users/teppo/Content/angular.js/docs/content/guide/directive.ngdoc',
'outfile' : '/Users/teppo/Content/angular/modules/directive.md',
'header' : """<!--
{
"name" : "directive",
"version" : "0.1",
"title" : "Scopes",
"description" : "When should you create your own directives in your AngularJS app, and how to implement them.",
""" + ng_generalHeader})

ng_files.append({'infile' : '/Users/teppo/Content/angular.js/docs/content/guide/animations.ngdoc',
'outfile' : '/Users/teppo/Content/angular/modules/animations.md',
'header' : """<!--
{
"name" : "animations",
"version" : "0.1",
"title" : "Animations",
"description" : "Animation hooks trigger animations during the life cycle of various directives.",
""" + ng_generalHeader})

ng_files.append({'infile' : '/Users/teppo/Content/angular.js/docs/content/guide/compiler.ngdoc',
'outfile' : '/Users/teppo/Content/angular/modules/compiler.md',
'header' : """<!--
{
"name" : "compiler",
"version" : "0.1",
"title" : "HTML Compiler",
"description" : "HTML compiler allows the developer to teach the browser new HTML syntax.",
""" + ng_generalHeader})

ng_files.append({'infile' : '/Users/teppo/Content/angular.js/docs/content/guide/providers.ngdoc',
'outfile' : '/Users/teppo/Content/angular/modules/providers.md',
'header' : """<!--
{
"name" : "providers",
"version" : "0.1",
"title" : "Providers",
"description" : "Provider recipe is the most comprehensive as well as most verbose of the recipe types.",
""" + ng_generalHeader})

ng_files.append({'infile' : '/Users/teppo/Content/angular.js/docs/content/guide/bootstrap.ngdoc',
'outfile' : '/Users/teppo/Content/angular/modules/bootstrap.md',
'header' : """<!--
{
"name" : "bootstrap",
"version" : "0.1",
"title" : "Bootstrap",
"description" : "Explains the Angular initialization process.",
""" + ng_generalHeader})

ng_files.append({'infile' : '/Users/teppo/Content/angular.js/docs/content/guide/unit-testing.ngdoc',
'outfile' : '/Users/teppo/Content/angular/modules/unit-testing.md',
'header' : """<!--
{
"name" : "unit-testing",
"version" : "0.1",
"title" : "Unit Testing",
"description" : "These guidelines help you avoid creating an untestable application.",
""" + ng_generalHeader})

ng_files.append({'infile' : '/Users/teppo/Content/angular.js/docs/content/guide/e2e-testing.ngdoc',
'outfile' : '/Users/teppo/Content/angular/modules/e2e-testing.md',
'header' : """<!--
{
"name" : "e2e-testing",
"version" : "0.1",
"title" : "E2E Testing",
"description" : "Help you verify the health of your Angular application.",
""" + ng_generalHeader})

ng_files.append({'infile' : '/Users/teppo/Content/angular.js/docs/content/guide/$location.ngdoc',
'outfile' : '/Users/teppo/Content/angular/modules/$location.md',
'header' : """<!--
{
"name" : "$location",
"version" : "0.1",
"title" : "Using $location",
"description" : "The $location service parses the URL in the browser address bar and makes the URL available to your application.",
""" + ng_generalHeader})

ng_files.append({'infile' : '/Users/teppo/Content/angular.js/docs/content/guide/css-styling.ngdoc',
'outfile' : '/Users/teppo/Content/angular/modules/css-styling.md',
'header' : """<!--
{
"name" : "css-styling",
"version" : "0.1",
"title" : "Working With CSS",
"description" : "List of CSS classes set by Angular.",
""" + ng_generalHeader})

ng_files.append({'infile' : '/Users/teppo/Content/angular.js/docs/content/guide/production.ngdoc',
'outfile' : '/Users/teppo/Content/angular/modules/production.md',
'header' : """<!--
{
"name" : "production",
"version" : "0.1",
"title" : "Running in Production",
"description" : "There are a few things you might consider when running your AngularJS application in production.",
""" + ng_generalHeader})

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
