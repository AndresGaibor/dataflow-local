---
source: https://qlik.dev/embed/foundational-knowledge/app-anatomy/generic-object-model/
last_updated: 2025-11-21T14:05:39Z
---

# Generic object

Generic objects are structures for storing and interacting with data in an app.
They are the primary type of entity through which the engine provides access to
the components of an app. When the engine retrieves an app for the API, it
converts the app to a JSON structure and returns a handle to be used for API
interactions. The component objects of the app are turned into JSON generic
objects. These generic objects are sub-objects of the app and cannot exist
without it.

The Capability APIs, the Qlik Sense .NET SDK, and the enigma.js library all use
the Qlik Engine JSON API internally, and so expose generic objects via their
classes and methods.

The generic object is considered "generic" because it is a flexible structure
that can represent many different app components, such as sheets, stories,
lists, hypercubes, slides, and bookmarks. Generic objects can contain or refer
to other generic objects, depending on their respective types. The qType
property of the generic object identifies its type (for example, some possible
values for `qType` are *sheet*, *Dimension*, *Measure*, and *GenericObject*).

## Properties and layout

The generic object has two important components that are relied on during
interactions with app data: a set of properties that defines the app's structure
and logic, and a layout that represents the engine's evaluation of the
definitions in the properties. This evaluation by the engine is referred to as *rendering*.
You can set the properties of a generic object by calling the [SetProperties method](https://qlik.dev/apis/json-rpc/qix/genericobject/#setproperties)
in the Qlik Engine JSON API. You retrieve the layout of a generic object by
calling the [GetLayout method](https://qlik.dev/apis/json-rpc/qix/genericobject/#getlayout).

## Validation states of generic objects

Unlike properties, layouts are not saved anywhere. They are calculated on the
fly so that the client has the most up-to-date view of the data when it
retrieves a layout. Because of this, the engine keeps track of data that has
changed between calls to GetLayout. The generic object can have one of three states:

- Invalid: Something relating to the object's data has changed. Either the data
  model has changed (typically because a selection has been made) or a property
  has been updated by a call to the SetProperties method.
- Validating: An object is invalid and the GetLayout method has been called. The
  validation process starts.
- Valid: The validation of the object has finished. The engine returns the
  layout requested by the GetLayout method.

When you make a call to the engine that changes the layout (for example,
filtering, or selecting data), the engine returns a field in the response called
change. This field contains the handles of the objects that have changed since
the last layout calculation. At this point, you should call GetLayout to get the
latest view of the data.

## Example: Properties and layout

Consider the following set of properties of a generic object:

```json
{
  "qInfo": {
     "qType": "simple-object",
     "qId": "12345"
  },
  "myClientProperty": "This is just a string that engine will persist in my app",
  "salesString": {
    "qStringExpression": {  // This will evaluate to a formatted string.
      "qExpr": "Sum(Sales)"
  }
  },
  "salesValue": {
    "qValueExpression": {  // Same as above but will evaluate as number.
      "qExpr": "Sum(Sales)"
    }
  }
}
```

When the client calls the GetLayout method, the engine evaluates the properties
and returns the following layout:

```json
{
  "qInfo": {
    "qId": "12345",
    "qType": "simple-object"
  },
  "qSelectionInfo": {},
  "myClientProperty": "This is just a string that engine will persist in my app",
  "salesString": "198.22",
  "salesValue": 198.221456
}
```

## Properties

Generic objects have different properties depending on what they represent.
There are two kinds of properties:

### Properties defined by the Qlik engine

These properties are validated by the engine, and some are also evaluated
(rendered) and replaced in the Qlik associative engine output (the layout) by
their calculated counterparts. In the Qlik Engine JSON API, you can set the
properties of a generic object, either when you create the object or after you
create the object, by using the SetProperties method or the ApplyPatches method.
Fixed (or static) properties are the mandatory properties of a generic object.
For example, `qInfo`, and `qExtendsId` are fixed properties inside the
GenericObjectProperties object. Dynamic properties are additional (optional)
properties that can be added to generic objects, depending on the type of app
object the generic object represents. Dynamic properties have types that are
defined in the API and known to the engine.

The properties of the generic object determine what the engine evaluates. You
set the properties in a definition object, and the engine evaluates (or renders)
the calculated results in a layout object. To evaluate the properties of a
generic object, you use the GetLayout method. For example, a qHyperCubeDef
object contains definitions for dimensions and measures. The engine evaluates
these properties and exposes them in the qHyperCube object, which contains the
calculated results. Properties defined by the engine are prefixed by the letter
'q' in the JSON of API requests and responses.

### User-defined properties (also referred to as full dynamic)

These properties are persisted in the repository, but are not used or recognized
by the engine. They can be any type you define. The engine includes them
unchanged in the layout, so your code should use them for something. To prevent
confusion, do not prefix user-defined properties by the letter 'q'.
