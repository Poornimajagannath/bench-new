City Abbreviations {#tax-info-city-abbrevs}
===========================================

Several applications expand some commonly used city-name abbreviations, which enables the tax calculation service to correctly evaluate city names for tax purposes. The US Postal Service also maintains a list of common abbreviations. When a customer uses abbreviations not accepted by either entity, the tax calculation service might not recognize the combination of city, state, and postal code, in which case the request fails and returns a reason code of `400`.  
The following table provides a list of the abbreviations used by the tax calculation service and the US Postal Service.

| Abbreviation |  Expansion  |           Abbreviation            |   Expansion   |
|--------------|-------------|-----------------------------------|---------------|
| bch          | beach       | n                                 | north         |
| crk          | creek       | ny                                | new york      |
| cty          | city        | pk                                | park          |
| cyn          | canyon      | pkwy                              | parkway       |
| e            | east        | pt                                | point         |
| ft           | fort        | s                                 | south         |
| grdn         | garden      | sf                                | san francisco |
| hbr          | harbor      | st (only for the US country code) | saint         |
| hgts, hts    | heights     | spr                               | spring        |
| jct, jctn    | junction    | sprs                              | springs       |
| la           | los angeles | vly                               | valley        |
| mt, mtn      | mountain    | w                                 | west          |
[Expanded City Abbreviations]

