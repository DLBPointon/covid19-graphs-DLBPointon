# Instructions

## Introduction

The world is currently experiencing an outbreak of a respiratory disease caused 
by a novel (new) coronavirus that was first detected in Wuhan City, China.

https://www.who.int/emergencies/diseases/novel-coronavirus-2019 


Following the disease outbreak through simple graphs and mapping has the potential 
to help people understand what is going on and may contribute to avoid panic and 
misunderstanding.

A great [interactive tool](https://arcg.is/0fHmTX)
to display the latest available data has been developed by 
[John Hopkins University CSSE](https://systems.jhu.edu/).
As part of this work they make the latest data available at
https://github.com/CSSEGISandData/COVID-19

Simple graphics can be useful in visualizing the data. 
For instance, the Guardian Newspaper published two graphs on 16 Feb:

![Guardian Covid-19 graphs](
https://aru-bioinf-ibds.github.io/images/guardian_graph_for_coursework.png)
> From https://www.theguardian.com/world/2020/feb/17/coronavirus-causes-mild-disease-in-four-in-five-patients-says-who

Your task for this coursework is to develop a tool to automatically produce up-to-date custom
CSV files, graphs or other useful graphics for our customer Alice of the TheDailyWeasel 
newsgroup. You will be working with Oliver who is the 
"Product Owner" and will talk to Alice. You can get advice and help from a senior developer `osmart` who is very busy and must be contacted via GitHub as he works remotely from his cottage on 
island of [Muck](https://en.wikipedia.org/wiki/Muck,_Scotland).

## customer Alice's initial wish list

Oliver (PO) took these notes from a conversation with the customer Alice.
* We really need an automatic way to get data from the CSSEGISandData repository as 
  manually downloading and processing the CSV is a real pain. We want a command-line 
  script that Jane can run and download and process the data to produce ~~a 
  single CSV file~~ CSV file(s) with summary data
  so we can load into Excel and produce graphs like the Guardian ones above.

  > **Clarification 06 March: We do not mind if you produce a single CSV file or separate CSV files for 'Confirmed' 'Deaths' and 'Recovered'
  > As long as the filenames and the title rows clearly show the what is what.**
  > see https://canvas.anglia.ac.uk/courses/14266/discussion_topics/135698


  The dates should be down the page. This is an absolute priority.
  * *The tool needs to download the latest data from the repository with no manual intervention*
* Then we would like the CSV file to be extended to provide analysis of
  * Total
  * Mainland China
  * Diamond Princess
  * Asia (excluding Mainland China & Diamond Princess)
  * Europe
  * The UK
  * The Americas
* Once you have got the CSV file script to us then we would like the tool to have an option
  to produce graphs for our blog pages:
  * The option should produce a new directory of a given name with all the graphics in it.
  * Graphs should be in either PNG or SVG format. 
  * Filenames should include the date like `2020_02_16_confirmed_china_other.png`
  * Must produce graphs like the Guardian Ones above
  * But as you are Data Scientists then please produce the most informative plots you can.
* It would be great if you could work out a way of making the graphs/CSV data available on 
  a web page we can access without running the script ourselves.
* If you can sort this all our then please make suggestions for improvements. 
* The deadline for the project to be completed is 2pm on 20th March.

Please note that Alice can change her mind. Oliver has promised we are an Agile organization
so remember the 2nd Agile Manifesto Principle:

> Welcome changing requirements, even late in development. 
> Agile processes harness change for the customer’s competitive advantage.

* there will be an additional feature request posted before 8th March. 

>
> Please note the additional feature request 
> was posted on 05 March at https://canvas.anglia.ac.uk/courses/14266/discussion_topics/135617 

## Senior developer `osmart` rules.

`osmart` is a grumpy fellow but you need to work with him. So please try to keep to his rules.
Working with difficult colleagues is all part of the game.

* `osmart` has already produced a proof of concept 
  * Please see Jupyter NoteBook that downloads the Covid-19 dataset:
    [customers_proof_of_concept.ipynb](customers_proof_of_concept.ipynb)    
  * It produces a graph like
    ![POC graph](https://aru-bioinf-ibds.github.io/images/proof_of_concept_graph.png)
* `osmart` will provide you with starting code including a script within 2 working days of 
  you starting work on the report. 
* Please make sure you frequently pull changes from the repo in case `osmart`
  has made any commits. You should push your changes at least once per day. 
  Broken code can be committed.
* `osmart` wants you to use GitHub issues and a GitHub Project Simple Kanban board 
  for the project. He will show you how to setup a GitHub Project Simple Kanban board
* issues should have initial tasks lists if appropriate.
* every commit message should include an issue number. If you forget then add a comment to the issue page. 
* `osmart` comes down to ARU from Muck every Monday 
  and can be seen in person particularly to discuss Kanban board.  
  Please open a GitHub issue with the help tag asking for a slot and assign it to `osmart`
* `osmart` will not look at any code that has not been committed and will not look at emails.
* You must use issue pages to get help. `osmart` will respond to help requests with 4 
  working days and will then offer help in person / via zoom.  
  No help requests are to be posted from
  after Sunday 15th March. **Do not leave it until the last minute to do the work**
* Initial work to satisfy Alice's initial absolute requirement should be done in the master 
  branch. 
* All subsequent work for additional requirements should be done in separate feature branch(es). 
  Do not merge work back to master unless `osmart` agrees
* `osmart` wants you to use a class structure for the work that he will provide for you. 
* Although you can discuss the project with other apprentices you should not share code or
  documentation with each other.
  The final check list for the project that must be submitted via TurnItIn will 
  include 'This is my own work' declaration..
  Plagiarism checks will be conducted. Please review 
  [2019/20 Information about Assessment Offenses](https://canvas.anglia.ac.uk/courses/14266/pages/2019-slash-20-information-about-assessment-offences).
  You can reuse code that you have written provided the commit message clearly states
  where this is sourced from.

## Marking Scheme 

Please see Assignment Canvas page https://canvas.anglia.ac.uk/courses/14266/assignments/84677

