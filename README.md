<h1>Overview</h1>

This is a collection of standard behavioural economics / psychology experiments. 
Currently the following experiments are available:
* Base Rate vs Similarity: Is Steve a librarian or a farmer?
* Conjunction fallacy: The Linda task
* Base rate fallacy: Medical Test
* Anchoring: Percentage of African countries in the UN
* Availability Heuristic: English words ending in “ing” vs “\_n\_ ”
* Loss Aversion: Cruise ship in a storm
* Allais Paradox


<h1>Usage</h1>
You can configure which sessions you want to use by clicking on “configure session” in the sessions tab or in the SESSION_CONFIGS in the settings.py file.
Once you have created a session you can view the results by clicking on “report” in the session menu.
Click the “Go” button to fetch new results. Only results of participants who have completed all questions will be displayed.
A demo version of the experiment can be found here: https://classroom-experiments-demo.herokuapp.com/demo.
This demo uses all available experiments and it is not configurable.
Please do not use the demo in an actual class, the server is not meant to handle more than a few subjects. To learn how to install oTree and set up your own server to use the classroom experiments, you can check out the officical documentation (https://otree.readthedocs.io/en/latest/) or this video tutorials: https://youtu.be/OzkFvVhoHr0 .


<h1>The Experiments</h1>
<h2>The Steve task</h2>
In this experiment subjects get a description of Steve, an introvert person with an attention for detail. They are shown potential professions and are asked to rank how likely it is that Steve has these professions. Of particular interest are the options "librarian" and "farmer" many subejcts choose librarian over farmer, despite the fact that there are many more farmers than librarians. This highlights that people neglect base rates and judge by simiarity. In the version of the task implemented here, halve of the subejcts are asked to rank to professions by similarity rather than probability to show that there is little difference between these ratings.  

<h2>The Linda task</h2>

<h2>The Linda task</h2>
In the linda task, subjects get a description of Linda, who is a progressive young woman. They are asked to rank a few statements based on the probability that these statements apply to Linda. The crucial statements are "Linda is a Bank Teller" and "Linda is a bank teller and is active in the feminist movement". The first statement must be more linkely, than the second, because if Linda is a bank teller and is active in the feminist movement she is also a Bank Teller, but it may be possible that Linda is a bank teller and not aktive in the feminist movement. However, because Linda is more representative of a feminist than of a bank teller, many people judge the second statement to be more likely. This si known as the "conjunciton fallacy". 

Source: Tversky, A.; Kahneman, D. (1982). "Judgments of and by representativeness". In Kahneman, D.; Slovic, P.; Tversky, A. (eds.). Judgment under uncertainty: Heuristics and biases. Cambridge, UK: Cambridge University Press
