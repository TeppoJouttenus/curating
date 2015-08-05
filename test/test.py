import re
from pprint import pprint
import string

files = """{"olm" : "./modules/index.md"},
    {"olm" : "./modules/introduction.md"},
    {"olm" : "./modules/concepts.md"},
    {"olm" : "./modules/databinding.md"},
    {"olm" : "./modules/controller.md"},
    {"olm" : "./modules/services.md"},
    {"olm" : "./modules/scope.md"},
    {"olm" : "./modules/di.md"},
    {"olm" : "./modules/templates.md"},
    {"olm" : "./modules/expression.md"},
    {"olm" : "./modules/filter.md"},
    {"olm" : "./modules/forms.md"},
    {"olm" : "./modules/directive.md"},
    {"olm" : "./modules/animations.md"},
    {"olm" : "./modules/module.md"},
    {"olm" : "./modules/compiler.md"},
    {"olm" : "./modules/providers.md"},
    {"olm" : "./modules/bootstrap.md"},
    {"olm" : "./modules/unit-testing.md"},
    {"olm" : "./modules/e2e-testing.md"},
    {"olm" : "./modules/$location.md"},
    {"olm" : "./modules/css-styling.md"},
    {"olm" : "./modules/i18n.md"},
    {"olm" : "./modules/security.md"},
    {"olm" : "./modules/accessibility.md"},
    {"olm" : "./modules/ie.md"},
    {"olm" : "./modules/production.md"},
    {"olm" : "./modules/migration.md"},"""

list = files.split('\n')
namesForModules = []
names = []

reNames = re.compile(r'modules/([^.]*).md')

for i in range(len(list)):
    namesForModules.append('{\"module\" : \"'+reNames.findall(list[i])[0]+'\"},')

for i in range(len(list)):
    names.append(reNames.findall(list[i])[0])

# print names

newlistForModules="\n".join(namesForModules)
newlist="\n".join(names)
print newlist
# print repr(names)
# print repr(newlist)
# pprint(newlist)
