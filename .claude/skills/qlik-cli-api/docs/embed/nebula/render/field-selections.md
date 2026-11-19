---
source: https://qlik.dev/embed/nebula/render/field-selections/
last_updated: 2026-06-02T18:15:45+01:00
---

# Field selections

While making selections in charts to filter your data often is a more direct
experience, it can also be useful to see individual fields in an ordered
manner. Classically called a listbox or filterpane in QlikView and Qlik Sense,
nebula.js exposes simple access to listing and making selections in a field.

## Field selections listbox

The listbox show a list of values in a field while highlighting selections.
To render this bar you first need an `HTMLElement`:

```html
<div class="listbox" style="height: 400px"></div>
```

You can then `mount` the selections UI into that element for a given field:

```js
const n = embed(enigmaApp);

const fieldName = 'MyField'; // Should refer to a field in your app
const options = {
  title: "Custom title" // Overrides fieldname to set a custom title
},

(await n.field(fieldName)).mount(document.querySelector('.listbox'), options);
```

This should give you a box looking like this:

![Listbox empty selections](https://qlik.dev/_astro/listbox-empty.Min9Clip.png)
