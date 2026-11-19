---
source: https://qlik.dev/embed/foundational-knowledge/app-anatomy/list-object-model/
last_updated: 2025-07-08T16:09:30Z
---

# List object

A list object is a type of Qlik Sense object that consists of exactly one
dimension and no measures. List objects provide some additional capability
for some special cases compared with hypercubes. In particular, list objects
can return information regarding elements that are excluded by the current
set of selections, and therefore enable a more comprehensive selection of
dimension values. When you receive the layout of a list object, all values
are rendered. If selections are applied, selected values are displayed
along with the excluded and optional values.

The following table shows the methods that apply to list objects.

List object methods

| Method                      | Description                                                                                       |
| --------------------------- | ------------------------------------------------------------------------------------------------- |
| AbortListObjectSearch       | Abort the results of a search in a list object.                                                   |
| AcceptListObjectSearch      | Accept the results of a search in a list object. The search results become selected in the field. |
| GetListObjectData           | Get the values of a list object.                                                                  |
| ListObject                  | Renders the properties of a list object.                                                          |
| ListObjectDef               | Define your list object.                                                                          |
| SearchListObjectFor         | Search for a string in a list object.                                                             |
| SelectListObjectAll         | Selects all values of a field.                                                                    |
| SelectListObjectAlternative | Selects all the alternative values of a list object.                                              |
| SelectListObjectExcluded    | Selects all the excluded values of a list object.                                                 |
| SelectListObjectPossible    | Selects all possible values of a list object.                                                     |
| SelectListObjectValues      | Selects some values in a list object.                                                             |
