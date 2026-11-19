---
source: https://qlik.dev/embed/reports/reporting-api-samples/
last_updated: 2026-04-20T13:34:03+01:00
---

# Generate reports using Reporting API

## Introduction

This tutorial shows how to generate PNG and PDF reports consuming Reporting API.

Reporting APIs are asynchronous: you'll request a report generation and this
request will be enqueued and processed asynchronously.

Each request has a status which can be either `queued`, `visiting`, `processing`, `done` or `failed`.

You'll need to poll the request status to verify when it's `done` or `failed`.

![Async API flow](https://qlik.dev/_astro/reporting-async-api-flow.e5pGs2N_.png)

Async API flow with client polling:

1. The client sends a `POST /reports` request and receives an `HTTP 202 Accepted` response with a `Location` header.
   The `Location` header is the URL the client should poll for the report status.
2. The client sends a GET request to the `Location` header and receives a `HTTP 200 OK` response with the report status.
3. When the status is `done` the report will be available at the `location` specified in the status response payload.
   The client sends a GET request to that location to get the generated report.

Alternatively you can use an HTTP callback and get the report status once the callback has been received.

> **Note:** Requests cannot be modified and they have a limited lifetime.

Prerequisites:

- An access token or API key. For more information, see [Authentication](https://qlik.dev/authenticate).

## API usage examples

> **Note:** For full endpoint definitions and parameter details, see the [Reports API reference](https://qlik.dev/apis/rest/reports).

### Export a single visualization as PNG

You can request the generation of a single visualization as PNG with the following request:

```http
POST /api/v1/reports HTTP/1.1
Host: your-tenant.us.qlikcloud.com
content-type: application/json
origin: your-tenant.us.qlikcloud.com
Authorization: Bearer <API_KEY>

{
  "type": "sense-image-1.0",
  "senseImageTemplate": {
    "appId": "9eecdd74-cc10-43c4-a69a-eaa1e69d837e",
    "visualization": {
      "id": "qZPdytp",
      "type": "visualization",
      "widthPx": 345,
      "heightPx": 648
    },
    "selectionsByState": {}
  },
  "output": {
    "outputId": "my-report-id",
    "type": "image",
    "imageOutput": {
      "outZoom": 1,
      "outDpi": 96,
      "outFormat": "png"
    }
  }
}
```

where `<API_KEY>` is your API key.

Note that the `outputId` will be the name of the generated report. It's
recommended to choose a unique identifier for it.

### Export a single visualization as PDF

You can request the generation of a single visualization as PDF with the following request:

```http
POST /api/v1/reports HTTP/1.1
Host: your-tenant.us.qlikcloud.com
content-type: application/json
origin: your-tenant.us.qlikcloud.com
Authorization: Bearer <API_KEY>

{
  "type": "sense-image-1.0",
  "senseImageTemplate": {
    "appId": "2e5bbece-bb8a-4243-bb2d-083b6ffd24f5",
    "visualization": {
      "id": "UgeGF",
      "type": "visualization",
      "widthPx": 854,
      "heightPx": 414
    },
    "selectionsByState": {}
  },
  "output": {
    "outputId": "my-report-id",
    "type": "pdf",
    "pdfOutput": {
      "size": "A4",
      "orientation": "L",
      "imageRenderingDpi": 200,
      "resizeType": "fit",
      "resizeData": {
        "fit": "27.7cmx19cm"
      },
      "align": {
        "horizontal": "center",
        "vertical": "middle"
      }
    }
  }
}

```

where `<API_KEY>` is your api key.

PDF output options are covered in this [paragraph](#pdf-output-options).

### Export a sheet as PDF with default sheet size

You can request the generation of a single sheet as PDF with the following request:

```http
POST /api/v1/reports HTTP/1.1
Host: your-tenant.us.qlikcloud.com
content-type: application/json
origin: your-tenant.us.qlikcloud.com
Authorization: Bearer <API_KEY>

{
  "type": "sense-sheet-1.0",
  "senseSheetTemplate": {
    "appId": "2e5bbece-bb8a-4243-bb2d-083b6ffd24f5",
    "selectionsByState": {},
    "sheet": {
      "id": "7d6f59d6-4d76-4d9d-a735-80179bf92edd"
    }
  },
  "output": {
    "outputId": "my-report-id",
    "type": "pdf",
    "pdfOutput": {
      "size": "A4",
      "orientation": "A",
      "imageRenderingDpi": 200,
      "resizeType": "autofit",
      "align": {
        "horizontal": "center",
        "vertical": "middle"
      }
    }
  }
}
```

where `<API_KEY>` is your API key.

PDF output options are covered in this [paragraph](#pdf-output-options).

For sheet exports, `widthPx` and `heightPx` are optional parameters.
If not specified, as in the previous payload sample, *default* values will be applied
depending on the actual size and layout properties of the Sense Sheet object.

The `widthPx` default value is 1920 pixels.

The `heightPx` default value is:

- 1280 pixels for *regular* sheets and *custom* sheets where width >= height
- 2880 pixels for *extended* sheets and *custom* sheets where width \< height

### Export a sheet as PDF with custom sheet size

You can request the generation of a single sheet as PDF with the following request:

```http
POST /api/v1/reports HTTP/1.1
Host: your-tenant.us.qlikcloud.com
content-type: application/json
origin: your-tenant.us.qlikcloud.com
Authorization: Bearer <API_KEY>

{
  "type": "sense-sheet-1.0",
  "senseSheetTemplate": {
    "appId": "d9c987ab-af43-4ab2-ad02-6acc4b333101",
    "sheet": {
      "id": "89bd1bad-9ac7-46d4-828e-f1730a918dba",
      "widthPx": 1216,
      "heightPx": 757
    },
    "selectionsByState": {}
  },
  "output": {
    "outputId": "my-report-id",
    "type": "pdf",
    "pdfOutput": {
      "size": "A4",
      "orientation": "A",
      "imageRenderingDpi": 200,
      "resizeType": "autofit",
      "align": {
        "horizontal": "center",
        "vertical": "middle"
      }
    }
  }
}
```

where `<API_KEY>` is your API key.

PDF output options are covered in this [paragraph](#pdf-output-options).

In the previous payload sample a custom sheet size is requested:
`widthPx` is set to 1216 and `heightPx` is set to 757.

### Export a composition of sheets as PDF

You can generate a single PDF report that includes multiple sheets.
You can use a common `selectionsByState` definition to be applied in different
sheets, with the `selectionsByStateDef` clause.

For each sheet you must specify an output.
Sheets can have different output settings (for example size, resizeType, and orientation).

```http
POST /api/v1/reports HTTP/1.1
Host: your-tenant.us.qlikcloud.com
content-type: application/json
origin: your-tenant.us.qlikcloud.com
Authorization: Bearer <API_KEY>

{
    "type": "composition-1.0",
    "definitions": {
        "selectionsByState": {
            "selDef1": {
                "$": [
                    {
                        "fieldName": "CategoryName",
                        "values": [
                            {
                                "text": "Sportwear",
                                "isNumeric": false
                            }
                        ],
                        "defaultIsNumeric": false
                    }
                ]
            }
        }
    },
    "compositionTemplates": [
        {
            "type": "sense-sheet-1.0",
            "senseSheetTemplate": {
                "selectionsByStateDef": "selDef1",
                "appId": "efe39f64-ea3a-4cda-baa7-26dca8eaed0b",
                "sheet": {
                    "id": "JsCeVm"
                }
            }
        },
        {
            "type": "sense-sheet-1.0",
            "senseSheetTemplate": {
                "selectionsByStateDef": "selDef1",
                "appId": "efe39f64-ea3a-4cda-baa7-26dca8eaed0b",
                "sheet": {
                    "id": "FaQeFa"
                }
            }
        }
    ],
    "output": {
        "outputId": "my-report-id",
        "type": "pdfcomposition",
        "pdfCompositionOutput": {
            "pdfOutputs": [
                {
                    "size": "A4",
                    "orientation": "A",
                    "resizeType": "autofit",
                    "align": {
                        "horizontal": "center",
                        "vertical": "middle"
                    }
                },
                {
                    "size": "A3",
                    "orientation": "A",
                    "resizeType": "autofit",
                    "align": {
                        "horizontal": "center",
                        "vertical": "middle"
                    }
                }
            ]
        }
    }
}
```

where `<API_KEY>` is your API key.

PDF output options are covered in this [paragraph](#pdf-output-options).

As for single sheet PDF export, `widthPx` and `heightPx` of sheets are optional.
Where not specified, as in the previous payload sample, *default* values are applied
depending on the actual size and layout properties of the Sense Sheet object.

The `widthPx` default value is 1920 pixels.

The `heightPx` default value is:

- 1280 pixels for *regular* sheets and *custom* sheets where width >= height
- 2880 pixels for *extended* sheets and *custom* sheets where width \< height

## Selections

### Select a text field

This is a sample payload for exporting a single visualization with a text field selection:

```json
{
  "type": "sense-image-1.0",
  "senseImageTemplate": {
    "appId": "9eecdd74-cc10-43c4-a69a-eaa1e69d837e",
    "visualization": {
      "id": "qZPdytp",
      "type": "visualization",
      "widthPx": 345,
      "heightPx": 648
    },
    "selectionStrategy": "ignoreErrorsNoDetails",
    "selectionsByState": {
      "$": [
        {
          "fieldName": "Product Sub Group Desc",
          "values": [
            {
              "text": "Coffee",
              "isNumeric": false
            },
            {
              "text": "Hot Dogs",
              "isNumeric": false
            }
          ],
          "defaultIsNumeric": false
        }
      ]
    }
  },
  "output": {
    "outputId": "my-report-id",
    "type": "image",
    "imageOutput": {
      "outZoom": 1,
      "outDpi": 96,
      "outFormat": "png"
    }
  }
}
```

where `Product Sub Group Desc` is a text field.

The `$` sign in the `selectionsByState` map refers to the *default* state.

### Select a numeric field

```json
{
  "type": "sense-image-1.0",
  "senseImageTemplate": {
    "appId": "9eecdd74-cc10-43c4-a69a-eaa1e69d837e",
    "visualization": {
      "id": "qZPdytp",
      "type": "visualization",
      "widthPx": 345,
      "heightPx": 648
    },
    "selectionStrategy": "ignoreErrorsNoDetails",
    "selectionsByState": {
      "$": [
        {
          "fieldName": "Rank",
          "values": [
            {
              "number": 1,
              "isNumeric": true
            },
            {
              "number": 2,
              "isNumeric": true
            }
          ],
          "defaultIsNumeric": true
        }
      ]
    }
  },
  "output": {
    "outputId": "my-report-id",
    "type": "image",
    "imageOutput": {
      "outZoom": 1,
      "outDpi": 96,
      "outFormat": "png"
    }
  }
}
```

where `Rank` field is a numeric field.

The `$` sign in the `selectionsByState` map refers to the *default* state.

### Select a date field

```json
{
  "type": "sense-image-1.0",
  "senseImageTemplate": {
    "appId": "9eecdd74-cc10-43c4-a69a-eaa1e69d837e",
    "visualization": {
      "id": "qZPdytp",
      "type": "visualization",
      "widthPx": 345,
      "heightPx": 648
    },
    "selectionStrategy": "ignoreErrorsNoDetails",
    "selectionsByState": {
      "$": [
        {
          "fieldName": "Delivery Date",
          "values": [
            {
              "number": 38007,
              "isNumeric": true
            },
            {
              "number": 38028,
              "isNumeric": true
            }
          ],
          "defaultIsNumeric": true
        }
      ]
    }
  },
  "output": {
    "outputId": "my-report-id",
    "type": "image",
    "imageOutput": {
      "outZoom": 1,
      "outDpi": 96,
      "outFormat": "png"
    }
  }
}
```

Note that `Delivery Date` is a date time field:

- `38028` value refers to date `2/11/2004`
- `38028` value refers to date `1/21/2004`

The `$` sign in the `selectionsByState` map refers to the *default* state.

### Select a drill-down dimension

To select a drill-down dimension you need to pass all the fields that are included in it.
For instance, to select the following `Claim Type Drill Down`

![Drill-down dimension](https://qlik.dev/_astro/drill-down.Dolfbvs9.png)

you need to send the following payload:

```json
{
  "type": "sense-image-1.0",
  "senseImageTemplate": {
    "appId": "9eecdd74-cc10-43c4-a69a-eaa1e69d837e",
    "visualization": {
      "id": "qZPdytp",
      "type": "visualization",
      "widthPx": 345,
      "heightPx": 648
    },
    "selectionStrategy": "ignoreErrorsNoDetails",
    "selectionsByState": {
      "$": [
        {
          "fieldName": "Claim Type",
          "values": [
            {
              "text": "Windscreen",
              "isNumeric": false
            }
          ],
          "defaultIsNumeric": false
        },
        {
          "fieldName": "Claim Sub-Type",
          "values": [
            {
              "text": "Glass",
              "isNumeric": false
            }
          ],
          "defaultIsNumeric": false
        }
      ]
    }
  },
  "output": {
    "outputId": "my-report-id",
    "type": "image",
    "imageOutput": {
      "outZoom": 1,
      "outDpi": 96,
      "outFormat": "png"
    }
  }
}
```

where both fields `Claim Type` and `Claim Sub-Type` are included.

The `$` sign in the `selectionsByState` map refers to the *default* state.

### Selections with Always One Selected field

If your app has an [AOS](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/DataSource/select-single-value.htm)
field, then it needs to be included as *first* selection in the `selectionsByState` array.

Otherwise the final report could show incorrect data.

Suppose you have the following Always One Selected field named `Currency`

![Always One Selected field](https://qlik.dev/_astro/AOS.paYVW5Pj.png)

and you want to export a single visualization with selections `Currency` and `Department`,
where `Currency` is an Always One Selected field,
the correct payload would be

```json
{
  "type": "sense-image-1.0",
  "senseImageTemplate": {
    "appId": "9eecdd74-cc10-43c4-a69a-eaa1e69d837e",
    "visualization": {
      "id": "qZPdytp",
      "type": "visualization",
      "widthPx": 345,
      "heightPx": 648
    },
    "selectionStrategy": "ignoreErrorsNoDetails",
    "selectionsByState": {
      "$": [
        {
          "fieldName": "Currency",
          "values": [
            {
              "text": "CHF",
              "isNumeric": false
            }
          ],
          "defaultIsNumeric": false
        },
        {
          "fieldName": "Department",
          "values": [
            {
              "text": "HR",
              "isNumeric": false
            }
          ],
          "defaultIsNumeric": false
        }
      ]
    }
  },
  "output": {
    "outputId": "my-report-id",
    "type": "image",
    "imageOutput": {
      "outZoom": 1,
      "outDpi": 96,
      "outFormat": "png"
    }
  }
}
```

Note that `Currency` is the first element of the `selectionsByState` array.

The `$` sign in the `selectionsByState` map refers to the *default* state.

### Selection strategy

Selection strategy can be:

- `failOnErrors`: if selections fail to apply the report will fail
- `ignoreErrorsReturnDetails`: if selections fail to apply the report won't fail.
  Details about the failure will be included in the report status
- `ignoreErrorsNoDetails` if selections fail to apply the report won't fail and no details will be included in the
  status

Default is `ignoreErrorsReturnDetails`.

## Get the report status

The `POST /api/v1/reports` response should be `202 Accepted` with a `Location` header to be called to get the report
status.

This is a sample of a `Location` header:
`https://your-tenant.us.qlikcloud.com/api/v1/reports/1234/status`

where `1234` is the identifier of the report request.

`GET /api/v1/reports/1234/status` returns the report status, for example:

```json
{
  "reasons": [],
  "resolutionAttempts": 1,
  "results": [],
  "status": "processing",
  "statusLocation": "/reports/75a277fd-4e75-47dd-9de0-c1d4830438c3/status"
}
```

or, in case of a failure:

```json
{
  "reasons": [
    {
      "error": {
        "code": 500,
        "message": "internal server error"
      },
      "exportErrors": [
        {
          "code": "REP-500000",
          "title": "internal server error"
        }
      ]
    }
  ],
  "resolutionAttempts": 1,
  "results": [],
  "status": "failed",
  "statusLocation": "/reports/75a277fd-4e75-47dd-9de0-c1d4830438c3/status"
}
```

or, once the report is successfully done:

```json
{
  "reasons": [],
  "resolutionAttempts": 1,
  "results": [
    {
      "location": "https://your-tenant.us.qlikcloud.com:443/api/v1/temp-contents/61cdb9cebc201e00011339b8?inline=1",
      "outputId": "Sheet_pdf"
    }
  ],
  "status": "done",
  "statusLocation": "/reports/75a277fd-4e75-47dd-9de0-c1d4830438c3/status"
}
```

Then you can retrieve the raw file:

`GET https://your-tenant.us.qlikcloud.com:443/api/v1/temp-contents/61cdb9cebc201e00011339b8`

Note that the file has a default expiration time of one hour.

This can be overridden by setting a custom `outputTtl` in the `meta` option of the report request.

## PDF Output options

Note that the `outputId` will be the name of the generated report. It's recommended to choose a unique identifier for
it.

PDF output `resizeType` can be:

- `fit` fits the visualization or sheet into the area specified in `resizeData`.
  The content will be rescaled to fit in that area.
- `autofit`: automatically fits the visualization or sheet into the output size (that is, A4, A3 etc.).
  Any provided `resizeData` parameter will be ignored for this configuration.
- `none`: used to export a visualization or sheet as is (for example normal size). This may result in cropping.

PDF output `orientation` can be:

- `L` for landscape
- `P` for portrait
- `A` for auto. It sets the orientation depending on the content width and height proportions.
  If content width is greater than height the orientation is automatically set to `L` (Landscape), `P` (Portrait)
  otherwise.

PDF output `size` can be:

- `A1`
- `A2`
- `A3`
- `A4`
- `A5`
- `A6`
- `Letter`
- `Legal`
- `Tabloid`

PDF output `size` is set to `A4` by default, if not specified.

`resizeData` has a `fit` parameter which is the size of the area in the
format `"{width}{cm|mm}x{height}{cm|mm}"` (for example "297mmx210mm").
Note that PDF page orientation (landscape or portrait) should match the width and height set for this field
(for example, "297mmx210mm" for landscape and "210mmx297mm" for portrait).

If you don't have any particular output requirements you can choose:

- `A` as `orientation`
- `autofit` as `resizeType`
- omit the `resizeData` option

as in the following output sample:

```json
{
  "output": {
    "outputId": "my-report-id",
    "type": "pdf",
    "pdfOutput": {
      "size": "A4",
      "orientation": "A",
      "imageRenderingDpi": 200,
      "resizeType": "autofit",
      "align": {
        "horizontal": "center",
        "vertical": "middle"
      }
    }
  }
}
```

Output sample to fit the PDF content in a A4 with 2cm of padding with Landscape orientation:

```json
  {
    "output": {
    "outputId": "my-report-id",
    "type": "pdf",
    "pdfOutput": {
      "size": "A4",
      "orientation": "L",
      "imageRenderingDpi": 200,
      "resizeType": "fit",
      "resizeData": {
        "fit": "27.7cmx19cm"
      },
      "align": {
        "horizontal": "center",
        "vertical": "middle"
      }
    }
  }
```

where `"27.7cmx19cm"` is the size of a Landscape A4 (`"29.7cmx21cm"`) minus 2cm of padding.

Output sample to fit the PDF content in a A4 with 2cm of padding with Portrait orientation:

```json
  {
    "output": {
    "outputId": "my-report-id",
    "type": "pdf",
    "pdfOutput": {
      "size": "A4",
      "orientation": "P",
      "imageRenderingDpi": 200,
      "resizeType": "fit",
      "resizeData": {
        "fit": "19cmx27.7cm"
      },
      "align": {
        "horizontal": "center",
        "vertical": "middle"
      }
    }
  }
```

where `"19cmx27.7cm"` is the size of a Portrait A4 (`"21cmx29.7cm"`) minus 2cm of padding.

## Export deadline

In the `POST /reports` payload there's an optional parameter
that can be specified as export deadline.

The export deadline is the maximum interval, starting from the time the API
request is received, within which a report must be produced. Past this interval
the report generation fails.

The default value is 10 minutes, the maximum allowed value is 2 hours.

The following payload has an export deadline of 2 minutes
meaning that if the report generation takes more than 2 minutes
it will fail with an *export deadline exceeded* error.

```json
{
  "meta": {
    "exportDeadline": "P0Y0M0DT0H2M0S"
  },
  "type": "sense-image-1.0",
  "senseImageTemplate": {
    "appId": "2e5bbece-bb8a-4243-bb2d-083b6ffd24f5",
    "visualization": {
      "id": "UgeGF",
      "type": "visualization",
      "widthPx": 593,
      "heightPx": 365
    },
    "selectionsByState": {}
  },
  "output": {
    "outputId": "Chart_image",
    "type": "image",
    "imageOutput": {
      "outZoom": 1,
      "outDpi": 96,
      "outFormat": "png"
    }
  }
}
```

where `exportDeadline` is 2 minutes: `"P0Y0M0DT0H2M0S"`.
Note that the only accepted format is ISO8601.

If the deadline is passed, the report status will result in

```json
{
  "reasons": [
    {
      "error": {
        "code": 429,
        "message": "export deadline exceeded"
      },
      "exportErrors": [
        {
          "code": "REP-429014",
          "meta": {},
          "title": "export deadline exceeded"
        }
      ]
    }
  ],
  "resolutionAttempts": 1,
  "results": [],
  "status": "failed",
  "statusLocation": "/reports/9e2e7fe5-0ca9-460c-bbe7-f69243158975/status"
}
```

with error code `429` and `exportError` code `REP-429014`.

## HTTP callback

In some cases it might be better to use an HTTP callback instead of keep polling
for the report status once `done` or `failed`.

In the `POST /reports` payload an HTTP callback can be specified.
The API server will send an HTTP request to the specified URI once the
report status is `done` or `failed`.

Payload sample:

```json
{
  "type": "sense-image-1.0",
  "senseImageTemplate": {
    "appId": "2e5bbece-bb8a-4243-bb2d-083b6ffd24f5",
    "visualization": {
      "id": "UgeGF",
      "type": "visualization",
      "widthPx": 593,
      "heightPx": 365
    },
    "selectionsByState": {}
  },
  "output": {
    "outputId": "Chart_image",
    "type": "image",
    "imageOutput": {
      "outZoom": 1,
      "outDpi": 96,
      "outFormat": "png"
    },
    "callBackAction": {
      "httpRequest": {
        "uri": "http://sample.server.com/sample"
      }
    }
  }
}
```

where `"http://sample.server.com/sample"` is the URI the API server will call
once the report is done or failed.
