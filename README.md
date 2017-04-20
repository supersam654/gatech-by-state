# Georgia Tech Students by State (Normalized)

While at Georgia Tech, there always seemed to be an inordinate number of students from Florida (after Georgia of course because it's a public school). I've constantly heard people mention that there are _soooo_ many people from Florida that it finally dawned on me to investigate further. At first, I attributed this to a combination of Florida being geographically close to Georgia. However, it always bothered me that Florida is a populous state and they should naturally be overrepresented compared with other states.

## Question: Are there an excessive number of Floridians at Georgia Tech?

TL;DR: **No**.

### Setup

To answer this question, I needed:

* The number of students at GT by state
* The number of people in the US by state
* A way to read all of this data (preferably in Python)
* A basic understanding of fractions

Georgia Tech publishes a Fact Book which contains a lot of really neat stuff about all things related to Geogia Tech. In particular, I was interested in the [enrollment of students by state](http://factbook.gatech.edu/admissions-and-enrollment/enrollment-by-state-table-4-12/). Note that this data is from 2015.

I found lots of information on [state populations on Wikipedia](https://en.wikipedia.org/wiki/List_of_U.S._states_and_territories_by_population). I chose to use the estimated 2016 statistics as opposed to the 2010 census data because I was only interested in percentages of people living in each state and I figured recent estimated figures were better than known, old figures.

### Technical stuff

I didn't feel like manually extracting the data from either webpage and I didn't feel like directly parsing the HTML and extracting the table data automatically. Instead, I [extracted the tables with Google Sheets](https://opendata.stackexchange.com/a/828) and exported them as CSVs. I also had to do a small amount of cleaning. In particular, I unbolded the line for "Georgia" on the GT data and deleted a couple of weird lines in both datasets.

Then I made a little python script (`normalize.py`) which reads by CSVs, figures out what percentage of the population lives in each state, compares that to the percentage of students enrolled from each state, and prints out a pretty table. (I actually needed to run `pip install tabulate` to create the pretty table).

Note that Wikipedia includes a more complete list of "state-like-things" like territories. I ended up deleting a couple of territories from each CSV if the other CSV didn't have that territory in it.

You can run the script yourself with:

    python normalize.py > table.txt

## Findings

First and foremost, I was unsurprised that Georgians are vastly overrepresented at GT. It's a fantastic state school and, if I was paying in-state tuition, I couldn't imagine going to any other engineering school without a huge scholarship.

At the bottom of the list, we can see that California, Texas, and New York are underrepresented at the school. All three of those states have huge populations potentially many other in-state schools to pick from. California in particular has many wonderful in-state universities which would be very hard to refuse compared with out-of-state tuition at GT.

And finally, we get to Florida. From the data, we can see that Florida is (I assume statistically insignificantly) slightly underrepresented at GT. At first glance, this would imply that Florida is appropriately represented on campus.

Unfortunately, this goes directly against a consensus of public opinions. Why do people think there are so many Floridians when there really aren't? After looking at the data a bit, something looked a bit weird. Other really populous states (CA, NY, TX) are underrepresented on campus which makes them appear more in line with less populous states. However, Floridians ignore that trend and flock to GT. Why? Probably a combination of geography and lack of good universities in Florida. Looking at what percentage of students go to out-of-state schools would be enlightening (although I have a hunch economic prosperity will be a stronger indicator than school choice). All of this culminates in Floridians being the second largest group on campus by a long shot.

## Raw Data

Below is a table of all of the interesting fields in the CSVs I extracted. The `Difference` column is just `GT Percent - US Percent` as a percentage. For even raw-er data, check out the two CSVs directly.

    State                   GT Pop    US Pop    GT Percent    US Percent  Difference
    --------------------  --------  --------  ------------  ------------  ------------
    Georgia                   9045  10310371   0.678443      0.0315473    64%
    New Jersey                 290   8944469   0.0217522     0.027368     0%
    Virginia                   258   8411808   0.0193519     0.0257382    0%
    Tennessee                  176   6651194   0.0132013     0.0203511    0%
    Maryland                   212   6016447   0.0159016     0.0184089    0%
    South Carolina             108   4961119   0.00810081    0.0151799    0%
    Alabama                    102   4863300   0.00765077    0.0148806    0%
    Kentucky                    51   4436974   0.00382538    0.0135761    0%
    Connecticut                 94   3576452   0.00705071    0.0109431    0%
    Puerto Rico                 42   3411307   0.00315032    0.0104378    0%
    Iowa                         6   3134693   0.000450045   0.00959142   0%
    Utah                         2   3051217   0.000150015   0.00933601   0%
    Mississippi                 17   2988726   0.00127513    0.0091448    0%
    Arkansas                    17   2988248   0.00127513    0.00914334   0%
    Nevada                      11   2940058   0.000825083   0.00899589   0%
    Kansas                      13   2907289   0.000975098   0.00889562   0%
    New Mexico                   6   2081015   0.000450045   0.00636742   0%
    Nebraska                    12   1907116   0.00090009    0.00583533   0%
    West Virginia                6   1831102   0.000450045   0.00560274   0%
    Idaho                        6   1683140   0.000450045   0.00515001   0%
    Hawaii                       3   1428557   0.000225023   0.00437105   0%
    New Hampshire               29   1334795   0.00217522    0.00408416   0%
    Maine                       12   1331479   0.00090009    0.00407401   0%
    Rhode Island                 7   1056426   0.000525053   0.00323242   0%
    Montana                      0   1042520   0             0.00318987   0%
    Delaware                    26    952065   0.0019502     0.0029131    0%
    South Dakota                 3    865454   0.000225023   0.00264809   0%
    North Dakota                 4    757952   0.00030003    0.00231916   0%
    Alaska                       5    741894   0.000375038   0.00227002   0%
    District of Columbia        12    681170   0.00090009    0.00208422   0%
    Vermont                     12    624594   0.00090009    0.00191111   0%
    Wyoming                      2    585501   0.000150015   0.0017915    0%
    Guam                         4    161785   0.00030003    0.000495024  0%
    U.S. Virgin Islands          2    103574   0.000150015   0.000316912  0%
    Florida                    658  20612439   0.0493549     0.0630692    -1%
    North Carolina             277  10146788   0.0207771     0.0310468    -1%
    Washington                  44   7288000   0.00330033    0.0222996    -1%
    Arizona                     47   6931071   0.00352535    0.0212075    -1%
    Massachusetts              137   6811779   0.010276      0.0208424    -1%
    Indiana                     18   6633053   0.00135014    0.0202956    -1%
    Missouri                    53   6093000   0.0039754     0.0186431    -1%
    Wisconsin                   28   5778708   0.00210021    0.0176815    -1%
    Colorado                    64   5540545   0.00480048    0.0169528    -1%
    Minnesota                   31   5519952   0.00232523    0.0168898    -1%
    Louisiana                   48   4681666   0.00360036    0.0143248    -1%
    Oregon                      27   4093465   0.0020252     0.012525     -1%
    Oklahoma                    12   3923561   0.00090009    0.0120052    -1%
    Pennsylvania               217  12802503   0.0162766     0.0391727    -2%
    Illinois                   166  12801539   0.0124512     0.0391697    -2%
    Ohio                       109  11614373   0.00817582    0.0355373    -2%
    Michigan                    27   9928301   0.0020252     0.0303783    -2%
    New York                   222  19745289   0.0166517     0.0604159    -4%
    Texas                      276  27862596   0.0207021     0.085253     -6%
    California                 276  39250017   0.0207021     0.120096     -9%


# License

The code is licensed under the MIT license. Georgia Tech probably holds the copyright on their student data. I'm not entirely sure who owns the US census data because things published by the government are frequently in the public domain because the public paid for them.
