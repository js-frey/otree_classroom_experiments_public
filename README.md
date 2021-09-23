<h1>Overview</h1>

This is a collection of standard behavioural economics / psychology experiments. 
Currently the following experiments are available:
* Base Rate vs Similarity: Is Steve a librarian or a farmer?
* Conjunction fallacy: The Linda task
* Base rate fallacy: Medical Test
* Anchoring: Percentage of African countries in the UN
* Availability Heuristic: English words ending in “ing” vs “\_n\_ ”
* Loss Aversion: Cruise ship in a storm
* Lotteries: Allais Paradox


<h1>Usage</h1>
You can configure which sessions you want to use by clicking on “configure session” in the sessions tab or in the SESSION_CONFIGS in the settings.py file.
Once you have created a session you can view the results by clicking on “report” in the session menu.
Click the “Go” button to fetch new results. Only results of participants who have completed all questions will be displayed.
A demo version of the experiment can be found here: https://classroom-experiments-demo.herokuapp.com/demo.
This demo uses all available experiments and it is not configurable.
Please do not use the demo in an actual class, the server is not meant to handle more than a few subjects. To learn how to install oTree and set up your own server to use the classroom experiments, you can check out the official documentation (https://otree.readthedocs.io/en/latest/) or this video tutorials: https://youtu.be/OzkFvVhoHr0 .


<h1>The Experiments</h1>
<h2>The Steve Task</h2>
In this experiment subjects get a description of Steve, an introvert person with an attention for detail. They are shown potential professions and are asked to rank how likely it is that Steve has these professions. Of particular interest are the options "librarian" and "farmer" many subjects  choose librarian over farmer, despite the fact that there are many more farmers than librarians. This highlights that people neglect base rates and judge by similarity. In the version of the task implemented here, halve of the subjects are asked to rank to professions by similarity rather than probability to show that there is little difference between these ratings.  
Reference: Tversky, A.; Kahneman, D. (1982). "Judgment under uncertainty: Heuristics and biases". In Kahneman, D.; Slovic, P.; Tversky, A. (eds.). Judgment under uncertainty: Heuristics and biases. Cambridge, UK: Cambridge University Press

<h2>The Linda Task</h2>
In the Linda task, subjects get a description of Linda, who is a progressive young woman. They are asked to rank a few statements based on the probability that these statements apply to Linda. The crucial statements are "Linda is a Bank Teller" and "Linda is a bank teller and is active in the feminist movement". The first statement must be more likely, than the second, because if Linda is a bank teller and is active in the feminist movement, she is also a Bank Teller, but it may be possible that Linda is a bank teller and not active in the feminist movement. However, because Linda is more representative of a feminist than of a bank teller, many people judge the second statement to be more likely. This is known as the "conjunction fallacy". 

Reference: Tversky, A.; Kahneman, D. (1982). "Judgments of and by representativeness". In Kahneman, D.; Slovic, P.; Tversky, A. (eds.). Judgment under uncertainty: Heuristics and biases. Cambridge, UK: Cambridge University Press


<h2>The Medical Test Tasks</h2>
In this task subjects are told that there is a disease that 1 in 1000 people have. There is a test that is always positive for patients who have the disease, but is also positive for 5% of healthy patients. Subjects are asked how likely it is that the subject has the disease given that she is tested positive. A large share of subjects ignore the base rate and give high answers.

Reference: Casscells, W., Schoenberger, A., & Grayboys, T. Interpretation by physicians of clinical laboratory results. New England Journal of Medicine, 1978, 299, 999-1000. (10, 18)

<h2>Africa in the UN</h2>
In this task subjects are first asked if the share of African countries in the UN is above or below a certain percentage. There are two treatments, one with a high and one with a low percentage. In a next step they are asked to guess the percentage of African countries in the UN. Due to anchoring and insufficient adjustment the first question influences the second. The subjects who saw the high percentage generally give higher estimates than those who saw the low percentage. 

Reference:  Judgment under Uncertainty: Heuristics and Biases Amos Tversky; Daniel Kahneman Science, New Series, Vol. 185, No. 4157. (Sep. 27, 1974), pp. 1124-1131.

<h2>English words ending in “ing” vs “\_n\_</h2>
In this question subjects are divided into two treatments and have to guess the percentage of words in the English language ending in in "_n_" and "ing" respectively. Despite the fact that all words ending in "ing" also end in "_n_" the guess is generally higher in the second treatment due to availability bias. 

Based on a similar task in: Tversky, A.; Kahneman, D. (1982). "Availability: A heuristic for judging frequency and probability". In Kahneman, D.; Slovic, P.; Tversky, A. (eds.). Judgment under uncertainty: Heuristics and biases. Cambridge, UK: Cambridge University Press

<h2>Cruise ship in a storm</h2>
In this task subjects are told that a cruise ship has come into a storm and the passengers need to be rescued. They need to decide between two plans, one of which saves a subset of the passengers with certainty and the other either saves all or no passengers with a certain probability. There are two treatments one which is framed in terms of lives saved and one which is framed in terms of lives lost. In "save" frame most people choose the safe option and in the "loss" frame most people choose the risky option, which can be explained by loss aversion.

Based on the "Asian Disease Problem" in Tversky, A., & Kahneman, D. (1981). The framing of decisions and the psychology of choice. Science, 211(4481), 453–458.

<h2> Lotteries: Allais Paradox</h2>
In this task there are two treatments in which subjects need to choose between two lotteries A and B. The lotteries have 3 states. State 3 is the same for Lottery A and B within a treatment but varies between treatments. It can be either positive or zero. Even though state 3 is the same for lottery A and B, varying the payoff of it changes subjects’ preferences for the lotteries, which violates the independence axiom of expected utility theory. A possible explanation for this is the certainty effect. People seem to prefer a safe payoff and in the treatment where state 3 has a payoff Lottery B offers a safe payoff, whereas in the treatment where the payoff in state 3 is zero neither lottery provides a safe payoff.

Reference: Allais, M. (1953). Le Comportement de l’Homme Rationnel devant le Risque: Critique des Postulats et Axiomes de l’Ecole Americaine. Econometrica, 21(4), 503–546
