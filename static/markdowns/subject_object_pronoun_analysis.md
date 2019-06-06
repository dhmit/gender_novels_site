# Basic Subject vs Object Pronoun Frequency Analysis

**This markdown file contains data from an analysis of feminine
and masculine subject pronouns vs object pronouns.**

The code used for this analysis can be found in 
gender\_pronoun\_freq\_analysis.py

Two analyses were conducted on this subject. The first compares
how often each gender's pronouns were used in the subject within
their gender, i.e., what portion of female pronouns are subject pronouns
and what portion of male pronouns are subject pronouns. The 
second analysis compares the frequency of masculine and 
feminine pronouns in subject pronouns, ie, what portion of 
subject pronouns are masculine vs feminine.

## First Analysis
This analysis first separated the pronouns into masculine 
and feminine pronouns and compared frequencies within these
categories.

### Overall
These frequencies are the portion of pronouns of a certain
gender that are subject pronouns. Thus, on average, approximately 72% of 
masculine pronouns in a given novel are subject pronouns while approximately 
45% of feminine pronouns are subject pronouns.

Male: 
0.72

Female: 
0.45

### Binned
The following are averages of the same frequency but binned 
over author gender, date published, and location.

#### Female pronouns:
The following are frequencies of female pronouns that are
 subject pronouns.

By author gender: 

Male author: 0.44

Female author: 0.46

By date: (`NaN` means no novels from this range available)

To 1810 : 0.41

1810 to 1819 : 0.45

1820 to 1829 : `NaN`

1830 to 1839 : 0.35

1840 to 1849 : 0.42

1850 to 1859 : 0.39 

1860 to 1869 : 0.48 

1870 to 1879 : 0.48 

1880 to 1889 : 0.42 

1890 to 1899 : `NaN`

1900 on : 0.47

By location:

England: 0.44 

United States: 0.45 

Other: 0.43

####Male Pronouns

By author gender:

Male author: 0.73
 
Female author: 0.72
 
By date:

To 1810: 0.71

1810 to 1819: 0.70 

1820 to 1829: `NaN`

1830 to 1839: 0.70 

1840 to 1849: 0.69 

1850 to 1859: 0.70 

1860 to 1869: 0.73 

1870 to 1879: 0.73 

1880 to 1889: 0.73 

1890 to 1899: `NaN`

1900 on: 0.73

By location:

England: 0.72

US: 0.73

Other: 0.72
 
### Thoughts
We noticed no trends in the binning for this analysis. 
It did seem notable that about 72% of all male pronouns were
subject pronouns while only about 45% of female pronouns
were subject pronouns.

## Analysis 2

This analysis looked at the percentage of subject pronouns
that were male verses female. The following frequencies are
the portion of subject pronouns that are female.

### Overall
Overall: 0.32

Thus, on average, about 32% of the subject pronouns in a given 
novel were feminine.

### Binned

#### By author gender:

Male author: 0.24

Female author: 0.43

#### By date:

To 1810: 0.45

1810 to 1819: 0.42

1820 to 1829: `NaN`

1830 to 1839: 0.10

1840 to 1849: 0.32

1850 to 1859: 0.39

1860 to 1869: 0.43

1870 to 1879: 0.38

1880 to 1889: 0.22

1890 to 1899: `NaN` 

1900 on: 0.31

#### By location:

England: 0.30

US: 0.34

Other: 0.30

### Thoughts
For this analysis, we found the overall comparison and the
comparison by author gender most noteworthy. We noticed no
trends in the date binning, though there is a strange deviancy
from the norm in the 1830's. We noticed no trend based on location.

## Overall Thoughts
Analysis #1 is probably the most useful of the two. The results
observed in analysis #2 are likely due to just the frequency of
male vs female pronoun use in general as observed in an earlier
analysis (see he\_she\_freq\_data.md).
