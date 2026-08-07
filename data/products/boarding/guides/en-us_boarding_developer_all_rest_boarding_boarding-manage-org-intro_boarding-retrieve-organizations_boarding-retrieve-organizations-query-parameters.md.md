Using Query Parameters to Filter Results {#boarding-retrieve-organizations-query-parameters}
============================================================================================

When you request the list of organizations for your account, you can use URL-encoded query parameters to narrow the list.

hierarchyQuery
:
See [Using the hierarchyQuery Parameter](#boarding-retrieve-organizations-query-parameters_hierarchyQuery "")

filters
:
Specify API field values using Lucene syntax. Keyword matching is supported. AND is the supported operator. For example, `type:"TRANSACTING" AND businessInformation.country:"US"` will return transacting organizations in the US.

fields
:
This will allow you to limit the response payload. Pass the payload attributes you want and the response will only contain those values:

    ```
      {
          organizationId,
          businessInformation:{
            phoneNumber
          }
      }
    ```

offset
:
The number specified in this parameter excludes that many items from the response. The default is `0`

limit
:
The number specified in this parameter limits how many items to include in the response. When combined with offset, limits the items returned to a specific number of items starting from a specific item. The default is `10`.

sort
:
The order in which you would like your results sorted. For example, `type:desc,entityName:asc`.

Using the hierarchyQuery Parameter {#boarding-retrieve-organizations-query-parameters_hierarchyQuery}
-----------------------------------------------------------------------------------------------------

The hierarchy query allows you to query relationships and explore your parents and children. This is a type of graph, so there is a defined language syntax that is flexible enough for you to explore this hierarchy in a natural way. The structure of the query is:  
`organizationId.direction.distance`

* `organizationId` indicates the organizationId.
* `direction` specifies hierarchical relationships. Values can be `descendents` or `ancestors`.
* `distance` indicates levels of hierarchy. You can provide a whole number to specify the number levels of hierarchy to return. You can also use the asterisk `*` to include all levels.

**Examples:**

* `org1.descendents.*` - This will retrieve all descendents.
* `org1.ancestors.*` - This will retrieve all ancestors.
* `revent1234.descendents.1` - This will retrieve all direct children.

