datatype-names
==============

Map between keyword and label-based datatype names for ArcGIS Python toolboxes. Prior to 10.1SP1, tools
used 'labels' for names, such as 'Feature Layer'. But this was determined to hamper internationalization,
and at 10.1SP1, this was changed to keyword names, such as 'GPFeatureLayer'. This class detects the 
version of ArcGIS being used, and converts between the names so one standard can be used, but still
support unpatched 10.1 users.

    import datatype
    dt = datatype.DataType()
    
    # depending on the release of ArcGIS detected, this
    result = dt.format('Feature Layer')
    # will return 'Feature Layer' for 10.1, and 'GPFeatureLayer' for 10.1SP1 or 10.2
