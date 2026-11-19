---
source: https://qlik.dev/embed/nebula/render/app-selections/
last_updated: 2026-06-02T18:15:45+01:00
---

# Current app selections

An essential part of the Qlik experience is filtering data through selections.
Most charts support selections in the data they render, which then filters out
data and affect other charts connected to the same data model.

## Current app selections bar

The current app selections bar shows you the currently active selections in the
specified app. To render this bar you first need an `HTMLElement`:

```html
<div class="curr-selections"></div>
```

You can then `mount` the selections UI into that element:

```js
const n = embed(enigmaApp);

(await n.selections()).mount(document.querySelector(".curr-selections"));
```

Without any selections it should like this:

![selections bar with no selections made](https://qlik.dev/_astro/selections-empty.CHDzJLBC.png)

As you start applying selections in the various charts, the UI is updated to
reflect the current state:

![making selections in current app](https://qlik.dev/_astro/selections-update.Cpwo3ZU4.gif)

## Multiple bars

If you are connected to multiple apps, you can show the current selections in
each one by mounting the bar into different elements:

```js
(await embed(enigmaApp).selections()).mount(
  document.querySelector(".curr-selections")
);

(await embed(anotherApp, { context: { theme: "dark" } }).selections()).mount(
  document.querySelector(".another-curr-selections")
);
```

![making selections with multiple apps](https://qlik.dev/_astro/selections-multiple.SbNWyRP4.gif)
