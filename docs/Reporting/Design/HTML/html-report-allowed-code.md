---
title: "Allowlist for code in HTML templates"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Reporting/Design/HTML/html-report-allowed-code.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Reporting from Qlik Cloud Analytics", "In-application reporting with Qlik Cloud Analytics", "Designing report templates", "Designing HTML report templates", "Adding content to your HTML report template"]
---

# Allowlist for code in HTML templates

For security and compatibility, your HTML report template is automatically sanitized as needed when you save it. If the template contains tags that are not allowed, you are notified and can choose whether to allow automatic removal or manually remove them yourself.

An HTML template cannot be saved if it contains any content that is not listed on this page. When prohibited content is present in the template, you must first sanitize the contents, either automatically or by manually removing non-compliant code, before saving.

## Tags allowed by default

a, abbr, acronym, address, area, article, aside, b, bdi, big, blockquote, body, br, button, caption, center, cite, code, col, colgroup, data, datalist, dd, del, details, dfn, dir, div, dl, dt, em, fieldset, figcaption, figure, font, footer, form, h1, h2, h3, h4, h5, h6, head, header, hr, html, i, img, input, ins, kbd, keygen, label, legend, li, main, map, mark, menu, menuitem, meter, nav, ol, optgroup, option, output, p, pre, progress, q, rp, rt, ruby, s, samp, section, select, small, span, strike, strong, style, sub, summary, sup, table, tbody, td, textarea, tfoot, th, thead, time, title, tr, tt, u, ul, var, wbr.

## Attributes allowed by default

abbr, accept-charset, accept, accesskey, action, align, alt, autocomplete, autosave, axis, bgcolor, border, cellpadding, cellspacing, challenge, char, charoff, charset, checked, cite, class, clear, color, cols, colspan, compact, contenteditable, coords, datetime, dir, disabled, draggable, dropzone, enctype, for, frame, headers, height, high, href, hreflang, hspace, ismap, keytype, label, lang, list, longdesc, low, max, maxlength, media, method, min, multiple, name, nohref, noshade, novalidate, nowrap, open, optimum, pattern, placeholder, prompt, pubdate, radiogroup, readonly, rel, required, rev, reversed, rows, rowspan, rules, scope, selected, shape, size, span, spellcheck, src, start, step, style, summary, tabindex, target, title, type, usemap, valign, value, vspace, width, wrap.

## CSS properties allowed by default

align-content, align-items, align-self, all, animation, animation-delay, animation-direction, animation-duration, animation-fill-mode, animation-iteration-count, animation-name, animation-play-state, animation-timing-function, backface-visibility, background, background-attachment, background-blend-mode, background-clip, background-color, background-image, background-origin, background-position, background-position-x, background-position-y, background-repeat, background-repeat-x, background-repeat-y, background-size, border, border-bottom, border-bottom-color, border-bottom-left-radius, border-bottom-right-radius, border-bottom-style, border-bottom-width, border-collapse, border-color, border-image, border-image-outset, border-image-repeat, border-image-slice, border-image-source, border-image-width, border-left, border-left-color, border-left-style, border-left-width, border-radius, border-right, border-right-color, border-right-style, border-right-width, border-spacing, border-style, border-top, border-top-color, border-top-left-radius, border-top-right-radius, border-top-style, border-top-width, border-width, bottom, box-decoration-break, box-shadow, box-sizing, break-after, break-before, break-inside, caption-side, caret-color, clear, clip, color, column-count, column-fill, column-gap, column-rule, column-rule-color, column-rule-style, column-rule-width, column-span, column-width, columns, content, counter-increment, counter-reset, cursor, direction, display, empty-cells, filter, flex, flex-basis, flex-direction, flex-flow, flex-grow, flex-shrink, flex-wrap, float, font, font-family, font-feature-settings, font-kerning, font-language-override, font-size, font-size-adjust, font-stretch, font-style, font-synthesis, font-variant, font-variant-alternates, font-variant-caps, font-variant-east-asian, font-variant-ligatures, font-variant-numeric, font-variant-position, font-weight, gap, grid, grid-area, grid-auto-columns, grid-auto-flow, grid-auto-rows, grid-column, grid-column-end, grid-column-gap, grid-column-start, grid-gap, grid-row, grid-row-end, grid-row-gap, grid-row-start, grid-template, grid-template-areas, grid-template-columns, grid-template-rows, hanging-punctuation, height, hyphens, image-rendering, isolation, justify-content, left, letter-spacing, line-break, line-height, list-style, list-style-image, list-style-position, list-style-type, margin, margin-bottom, margin-left, margin-right, margin-top, mask, mask-clip, mask-composite, mask-image, mask-mode, mask-origin, mask-position, mask-repeat, mask-size, mask-type, max-height, max-width, min-height, min-width, mix-blend-mode, object-fit, object-position, opacity, order, orphans, outline, outline-color, outline-offset, outline-style, outline-width, overflow, overflow-wrap, overflow-x, overflow-y, padding, padding-bottom, padding-left, padding-right, padding-top, page-break-after, page-break-before, page-break-inside, perspective, perspective-origin, pointer-events, position, quotes, resize, right, row-gap, scroll-behavior, tab-size, table-layout, text-align, text-align-last, text-combine-upright, text-decoration, text-decoration-color, text-decoration-line, text-decoration-skip, text-decoration-style, text-indent, text-justify, text-orientation, text-overflow, text-shadow, text-transform, text-underline-position, top, transform, transform-origin, transform-style, transition, transition-delay, transition-duration, transition-property, transition-timing-function, unicode-bidi, user-select, vertical-align, visibility, white-space, widows, width, word-break, word-spacing, word-wrap, writing-mode, z-index.

## CSS at-rules allowed by default

namespace, style.

## URI schemes allowed by default

data, http, https, mailto.

## Default attributes that contain URIs

action, background, dynsrc, href, lowsrc, src.

## HTML and CSS comments

For developer convenience, HTML comments are allowed in HTML templates. However, they are removed in generated HTML reports.

CSS comments are removed in both HTML templates and generated HTML reports.

## Sanitization example

The following HTML code requires sanitization because it contains a script element. The script tag is not included in [*Tags allowed by default*](#Tags).

```
<html><head>
  <style>h2 { color: red }</style>
  <script>Window.alert('Hi!')</script>
  <title>Sanitization example</title>
  </head>
  <body>
    <h2>This is your chart</h2>

</body></html>
```

When you add this code and try to save your template, you are prompted to do one of the following:

- Allow automatic sanitization of your code by clicking Save anyway.
- Return to the editor to fix the code yourself by clicking Close and continue editing.

With automatic sanitization, the resulting code in the template will be:

```
<html><head>
  <style>h2 { color: #FF0000 }</style>

  <title>Sanitization example</title>
  </head>
  <body>
    <h2>This is your chart</h2>

</body></html>
```
