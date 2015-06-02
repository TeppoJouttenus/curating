ng_files = []
ng_generalHeader = """"homepage" : "https://docs.angularjs.org/guide",
"freshnessDate" : 2015-06-02,
"license" : "CC BY 3.0"
}
-->
"""
ng_files.append({'infile' : '/Users/teppo/Content/angular.js/docs/content/guide/introduction.ngdoc',
'outfile' : '/Users/teppo/Content/angular/modules/introduction.md',
'header' : ''})
ng_files.append({'infile' : '/Users/teppo/Content/angular.js/docs/content/guide/concepts.ngdoc',
'outfile' : '/Users/teppo/Content/angular/modules/concepts.md',
'header' : ''})

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
