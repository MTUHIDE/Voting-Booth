#Database Documentation

###How to set up
After pulling the project from GitHub, follow these steps:
1. Open a terminal in the project directory (in PyCharm you can click on the terminal tab at the bottom).
2. Create the migrations using `python manage.py makemigrations admin_back`
3. Apply the migrations using `python manage.py migrate`

This should create a migrations folder in `admin_back/`.  It should be ignored by Git automatically if you got the
 `.gitignore` from pulling the project.
 
###How to enter sample data
Creating entries in the Django database can be done through Django's interactive shell.
This is opened by running `python manage.py shell`

This opens an interactive python terminal that has Django's libraries.  Here is an example of how to add a survey entry:

```
>>> from admin_back.models import Survey
>>> survey = Survey(title="some survey name")
>>> survey.save()
```

If you set up the database properly, there should be no errors.  If you wanted to add a question, it may look something
like this:

```
>>> from admin_back.models import Question, QuestionTypes
>>> question = Question(survey=survey, text="What is 2+2?")
>>> question.save()
```

In general, you can see the attributes a table has in `models.py` or by looking at the table schemas here

##Database Schema
The following is a list of the tables in the database and their schemas.  The comments serve to show the purpose of the
various attributes of the tables.

####Survey
| Attribute | Field Type | Comments                 |
|-----------|------------|--------------------------|
| title     | string     | Title/name of the survey |
| state     | integer     | Whether the survey is active or not |

####Question
| Attribute | Field Type    | Properties     | Comments                                          |
|-----------|---------------|----------------|---------------------------------------------------|
| survey    | Survey        | Foreign Key    | The survey this question belongs to               |
| text      | String        | max_length=300 | The text of the question                          |
| yes       | Integer       | default=0      | How many "yes" votes received                       |
| votes     | Integer       | default=0      | How many total votes received                         |
| state     | QuestionState | default=ACTIVE | Whether the question is active in a survey or not |
| no        | Integer       | default=0      | How many "no" votes received
####Taken
| Attribute | Field Type | Properties    | Comments                                             |
|-----------|------------|---------------|------------------------------------------------------|
| survey    | Survey     | Foreign Key   | The survey that was taken                            |
| student   | String     | max_length=20 | The email of the student that has taken this survey. |

##Nearby changes/updates
* Since recently USG told us we only need to support yes/no questions, the need for a choice table is gone.
Instead, the question table can store the data of how many total and yes votes is received, since the choice is binary.
The amount of no votes can be calculated by `total - yes`.

* USG also mentioned that they only intend for one survey to be active at a time, and that should soon be reflected
in the survey table through some type of `state` attribute similar to the one questions have.