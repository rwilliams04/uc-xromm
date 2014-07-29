# Packaging

Initial ideas for packaging study and trial data.  See [datapackages](http://data.okfn.org/doc/data-package) for an outline of the suggested spec.


## Studies

Sample file layout for storing XROMM **study** data and associated metadata:


    /project/uc-xromm/studies/
      monkey-feeding/
        README.md
        study.json
        models/
        trials/
      lizard-locomotion/
        README.md
        study.json
        models/
        trials/
      alligator-coracoid/         # example used below
        README.md
        study.json                # see below
        models/
          all-markers.zip
          coracoid.zip
        trials/
          markerless.zip
          single-marker.zip
          double-marker.zip
          all-markers.zip



#### `study.json`

Here's an example `study.json` file for the [`alligator-coracoid`](http://xmaportal.org/sandbox/larequest.php?request=explorePublicStudy&StudyID=6&instit=SANDBOX1) example study.  Note that many of the resources associated with a study might also be [datapackages](http://data.okfn.org/doc/data-package) with their own `package.json` containing metadata for the file(s) comprising that resource.

```json
{
  "name": "alligator-coracoid",
  "title": "Alligator Coracoid Example Data",
  "description": "Data for markerless XROMM short-course tutorial",
  "version": "1.0",
  "license": "PDDL-1.0",
  "investigators": "Brainerd, Beth",
  "study_leader": "Camp, Ariel",
  "last_updated": "2007-10-31",
  "resources": [
    {
      "file": "trials/markerless.zip",
      "name": "Markerless Trial",
      "format": "trialpackage",
      "mediatype": "application/zip",
      "description": "isolated coracoid bone with no markers"
    },
    {
      "file": "trials/single-marker.zip",
      "name": "Single Marker Trial",
      "format": "trialpackage",
      "mediatype": "application/zip",
      "description": "isolated coracoid bone with marker 1"
    },
    {
      "file": "trials/double-marker.zip",
      "name": "Double Marker Trial",
      "format": "trialpackage",
      "mediatype": "application/zip",
      "description": "isolated coracoid bone with markers 1 and 4"
    },
    {
      "file": "trials/all-markers.zip",
      "name": "All Markers Trial",
      "format": "trialpackage",
      "mediatype": "application/zip",
      "description": "isolated coracoid bone with all 4 markers"
    },
    {
      "file": "trials/calibration.zip",
      "name": "Calibration",
      "format": "trialpackage",
      "mediatype": "application/zip",
      "description": "calibration data for these trials"
    },
    {
      "file": "models/coracoid.zip",
      "name": "Coracoid Bone Model",
      "format": "datapackage",
      "mediatype": "application/zip",
      "description": "Polygonal mesh models of coracoid bone"
    },
    {
      "file": "models/all-markers.zip",
      "name": "4 Marker Model",
      "format": "datapackage",
      "mediatype": "application/zip",
      "description": "Polygonal mesh models of all 4 markers"
    }
  ]
}
```
