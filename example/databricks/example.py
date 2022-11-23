# Databricks notebook source
# MAGIC %md
# MAGIC <img align="left" src="https://ithaka-labs.s3.amazonaws.com/static-files/images/tdm/tdmdocs/tapi-logo-small.png" />
# MAGIC 
# MAGIC This notebook free for educational reuse under [Creative Commons CC BY License](https://creativecommons.org/licenses/by/4.0/).
# MAGIC 
# MAGIC Created by [Firstname Lastname](https://) for the 2022 Text Analysis Pedagogy Institute, with support from the [National Endowment for the Humanities](https://neh.gov), [JSTOR Labs](https://labs.jstor.org/), and [University of Arizona Libraries](https://new.library.arizona.edu/).
# MAGIC 
# MAGIC For questions/comments/improvements, email author@email.address.<br />
# MAGIC ____

# COMMAND ----------
# MAGIC %md
# MAGIC # `Introduction to Pandas` `1`
# MAGIC 
# MAGIC This is lesson `1` of 3 in the educational series on `TOPIC`. This notebook is intended `to teach XXX and introduce the concepts of XXXX`. 
# MAGIC 
# MAGIC **Audience:** `Teachers` / `Learners` / `Researchers`
# MAGIC 
# MAGIC **Use case:** `Tutorial` / `How-To` / `Reference` / `Explanation` 
# MAGIC 
# MAGIC `Include the use case definition from [here](https://constellate.org/docs/documentation-categories)`
# MAGIC 
# MAGIC **Difficulty:** `Beginner` / `Intermediate` / `Advanced`
# MAGIC 
# MAGIC `Beginner assumes users are relatively new to Python and Jupyter Notebooks. The user is helped step-by-step with lots of explanatory text.`
# MAGIC `Intermediate assumes users are familiar with Python and have been programming for 6+ months. Code makes up a larger part of the notebook and basic concepts related to Python are not explained.`
# MAGIC `Advanced assumes users are very familiar with Python and have been programming for years, but they may not be familiar with the process being explained.`
# MAGIC 
# MAGIC **Completion time:** `90 minutes`
# MAGIC 
# MAGIC **Knowledge Required:** 
# MAGIC ```
# MAGIC * Python basics (variables, flow control, functions, lists, dictionaries)
# MAGIC * Object-oriented programming (classes, instances, inheritance)
# MAGIC 
# MAGIC These should be general skills but can mention a particular library
# MAGIC ```
# MAGIC 
# MAGIC **Knowledge Recommended:**
# MAGIC ```
# MAGIC * Basic file operations (open, close, read, write)
# MAGIC ```
# MAGIC 
# MAGIC **Learning Objectives:**
# MAGIC After this lesson, learners will be able to:
# MAGIC ```
# MAGIC 1. Understanding of What Pandas is
# MAGIC 2. Understanding of Why Pandas is useful
# MAGIC 3. Understanding that Pandas is not a replacement for Excel
# MAGIC 4. Understanding of how to install and import pandas
# MAGIC 5. Understanding of the DataFrame, what it is, and how to use it
# MAGIC ```
# MAGIC ___

# COMMAND ----------
# MAGIC %md
# MAGIC # Required Python Libraries
# MAGIC `List out any libraries used and what they are used for`
# MAGIC * Pandas
# MAGIC 
# MAGIC ## Install Required Libraries

# COMMAND ----------
### Install Libraries ###

# Using !pip installs
!pip install pandas

# COMMAND ----------
# MAGIC %md
# MAGIC # Introduction
# MAGIC 
# MAGIC ```
# MAGIC Pandas is a Python library in Python that allows for you to easily work with tabular data that is often stored in Excel files or .csv files. It is often considered one of the most vital Python libraries for data analysis because of its ease of use. There are other Python libraries that allow you to work with Excel data, such as XLSX and XLRD, which are leveraged by Pandas on the back end to interact with Excel spreadsheets. However, most tabular data is stored in .csv files, or Comma Separated Values files. There are other variations of this same structure (such as .tsv), but they all work the same. They use a special character to denote movement in the table to the next cell.
# MAGIC ```

# COMMAND ----------
# MAGIC %md
# MAGIC <center><img src="https://upload.wikimedia.org/wikipedia/commons/thumb/e/ed/Pandas_logo.svg/1200px-Pandas_logo.svg.png" width="500"></center>

# COMMAND ----------
# MAGIC %md
# MAGIC ## Why use Pandas?

# COMMAND ----------
# MAGIC %md
# MAGIC If you work with data at all or plan to in the future, becoming comfortable with Pandas early on will make your life a lot easier. There are other Python libraries that allow you to work with .csv files, such as CSV, but these are not the same as Pandas. Pandas has one large advantage over CSV. It not only allows you to input .csv files into Python, it allows you to easily load them as DataFrames.
# MAGIC 
# MAGIC **DataFrames** are special data structures that contain not only the raw data in a table, but preserve the structure and hierarchy of that table. By loading .csv files as a DataFrame, Pandas not only allows you easy access to your data, but a powerful way to analyze it within a script. In addition to that, Pandas also has robust built-in features that we will explore throughout this textbook.
# MAGIC 
# MAGIC Finally, many MANY!! libraries for data analysis are built on top of Pandas. If you plan to understand how certain libraries work or how to get data to specific classes or functions correctly as a Pandas DataFrame, then you must be familiar with the Pandas library.
# MAGIC 
# MAGIC So, why use Pandas? Because it is the best library for importing and working with tabular data. It allows you to easily read files as DataFrames. And, it is a required library for most data analysis libraries.

# COMMAND ----------
# MAGIC %md
# MAGIC ## How to Install Pandas

# COMMAND ----------
# MAGIC %md
# MAGIC Installing pandas is as easy as installing any other Python library. If you are working within a Jupyter notebook like this one, you can execute the following command within a cell:

# COMMAND ----------
!pip install pandas

# COMMAND ----------
# MAGIC %md
# MAGIC In Jupyter notebooks the ! indicates that you want to perform a command in the terminal. We then specify what command we want to run. In this case, pip install. Finally, we specify the library we want to install, pandas. If you are not working within a Jupyter notebook, you can do the same thing by opening up your terminal, such as Command Prompt on Windows, and executing the same command.

# COMMAND ----------
# MAGIC %md
# MAGIC ## How to Import Pandas

# COMMAND ----------
# MAGIC %md
# MAGIC Once you have installed Pandas, it is time to import it. It is Pythonic, or good Python practice, to import pandas as pd. By importing a library as something, you give it that specific variable as a name. This has a few benefits. First, it makes Pandas easier to call in your script, because you can call the library with "pd" rather than "pandas". Second, all... yes. ALL. Pandas tutorials and posts on Stackoverflow will use "pd".

# COMMAND ----------
import pandas as pd

# COMMAND ----------
# MAGIC %md
# MAGIC After executing the above command, you will have successfully imported pandas into your Python script. In the next notebook, we will start working with Pandas

# COMMAND ----------
# MAGIC %md
# MAGIC ## Video

# COMMAND ----------
%%HTML
<center>
<iframe width="560" height="315" src="https://www.youtube.com/embed/dMoXe8DUQ7E" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</center>

# COMMAND ----------
# MAGIC %md
# MAGIC # Working with Pandas and the DataFrame

# COMMAND ----------
# MAGIC %md
# MAGIC With pandas imported above, we can begin to work with the library. Normally, you will create a Pandas DataFrame from a CSV or some external data file. We will see examples of that below. To begin, though, let's start with the basics. Below we have a dictionary. A good way to think of this dictionary is as an Excel Spreadsheet. Each key in the dictionary is a column and its value is a list which contains each cell in that column. We will see an example of a two-column dataset below, but for now let's work with the single column dataset, "names". In this column, we have a list of 6 names.

# COMMAND ----------
names_dict = {"names":
        [
            "Tom",
            "Mary",
            "Jeff",
            "Rose",
            "Stephanie",
            "Rodger"
        ]}

# COMMAND ----------
# MAGIC %md
# MAGIC Normally in Python, we would work with this data as an object. I could do something like the following to get the value of names:

# COMMAND ----------
print (names_dict["names"])

# COMMAND ----------
# MAGIC %md
# MAGIC But this is a textbook on Pandas and DataFrames. We want to do more! We want to work strictly with our data as a DataFrame. In order to do this, we need to convert the data into a Pandas DataFrame. To do that, we can use the line of code below. The pd.DataFrame can take numerous arguments. We won't get into all of them right now. For now, understand that there is one essential argument that you must pass: the data that you wish to convert into a DataFrame. In our case, we will be converting the single-column dictionary into a DataFrame, so we pass that object as the only argument. We can see this in the code below.

# COMMAND ----------
df = pd.DataFrame(names_dict)

# COMMAND ----------
# MAGIC %md
# MAGIC ## How to Display a DataFrame

# COMMAND ----------
# MAGIC %md
# MAGIC Loading the data as DataFrame is not the end of our work. It is often times essential to view that data in a Jupyter notebook or terminal. To see what it looks like, you can use the following command.

# COMMAND ----------
df

# COMMAND ----------
# MAGIC %md
# MAGIC Note that we are not printing off the data. This is because we are working within a Jupyter notebook. Were we working within an IDE, such as Atom, we would need to use the following command:

# COMMAND ----------
print (df)

# COMMAND ----------
# MAGIC %md
# MAGIC Notice, however, that the formatting of the data in the output is a bit different. When we print off a DataFrame, we do not see the nice formatting, such as the row highlighting and column header emboldening. It is for these reasons, that I recommend using the command "df" rather than print (df)

# COMMAND ----------
# MAGIC %md
# MAGIC ## How to Save DataFrame to CSV

# COMMAND ----------
# MAGIC %md
# MAGIC Often times when you convert your data into a DataFrame, you will process it and then ultimately save it to disk. To do this, we have a few different options, such as CSV and JSON. We will meet this process with JSON a bit later. For now, let's focus on one file type: CSV, or comma separated value. To save your DataFrame to a CSV file, you can write the following command

# COMMAND ----------
df.to_csv("data/names.csv")

# COMMAND ----------
# MAGIC %md
# MAGIC As we will see a little later, there are different arguments that you can pass here (and should!) For now, let's focus on that single argument that we used: a string. This string should correspond to the file that you want to create. In this case, we are putting it into the data subfolder under the name "names.csv".

# COMMAND ----------
# MAGIC %md
# MAGIC ## How to Read DataFrame from CSV

# COMMAND ----------
# MAGIC %md
# MAGIC Now that we have the data saved to a CSV file, let's create a new DataFrame, df2, and read that data. We can do this with the command pd.read_csv(). As with to_csv, we can pass multiple arguments here, but for now, we will stick with the one mandatory one, a string of the file that we wish to open. In this case, it is the same file we just created. Let's open it and print it off.

# COMMAND ----------
df2 = pd.read_csv("data/names.csv")

# COMMAND ----------
df2

# COMMAND ----------
# MAGIC %md
# MAGIC This doesn't look right. Notice that this DataFrame looks a bit off from what we saved to disk. Why is that? It is because of *how* we saved the file. If we don't specify an index, Pandas will automatically create one for us. In order to correctly save our file, we need to pass an extra keyword argument, specifically index=False. Let's try and save this file again under a different name: "names_no_index.csv".

# COMMAND ----------
df.to_csv("data/names_no_index.csv", index=False)

# COMMAND ----------
# MAGIC %md
# MAGIC Let's create a new DataFrame, df3, and reopen and print off the data.

# COMMAND ----------
df3 = pd.read_csv("data/names_no_index.csv")

# COMMAND ----------
df3

# COMMAND ----------
# MAGIC %md
# MAGIC Like magic, now we have a DataFrame that represents our original data.

# COMMAND ----------
# MAGIC %md
# MAGIC ## How to Save DataFrame to JSON

# COMMAND ----------
# MAGIC %md
# MAGIC In Pandas, we are not limited to CSV files, we can do this same process with JSON files, which are JavaScript Object Notation files. These are a bit different from CSV files and are used to store more complex data, specifically data that is used on the web because all browsers can interpret JSON data off-the-shelf. To save our data to a JSON file, we can use the to_json(). Note that we are not passing the index argument here. When our data is stored as a JSON file this is not necessary.

# COMMAND ----------
df3.to_json("data/names.json")

# COMMAND ----------
# MAGIC %md
# MAGIC Now, let's open that same data as a new DataFrame, df4. We can do the same thing as we did with the CSV file, except use read_json() and then print it off.

# COMMAND ----------
df4 = pd.read_json("data/names.json")

# COMMAND ----------
df4

# COMMAND ----------
# MAGIC %md
# MAGIC ## How to Add a Column to the DataFrame

# COMMAND ----------
# MAGIC %md
# MAGIC When working with DataFrames, you will almost always need to manipulate the data in some way. This means adding columns, deleting columns, performing permutations on data in columns, etc. We are going to cover all these things throughout this textbook. For now, let's start with the basics. Imagine we got the names of individuals from one source and their ages from another. We now need to add those ages into our DataFrame. We can approach the DataFrame as something like a dictionary here. We can add a column by creating it with df4\["ages"\]. This allows us to make that equal to the new data. The command below essentially adds a column to our DataFrame. Let's execute the command and print it off.

# COMMAND ----------
df4["ages"] = [20, 26, 20, 18, 52, 40]

# COMMAND ----------
df4

# COMMAND ----------
# MAGIC %md
# MAGIC Notice that we now have our second column. I want to stress right now, that to do this we needed data that matched the length of the names. If we tried to do this same act, but with 5 ages, rather than 6, we would have received an error.

# COMMAND ----------
# MAGIC %md
# MAGIC ## How to Grab a Specific Column

# COMMAND ----------
# MAGIC %md
# MAGIC When working with a DataFrame, you will often need to grab a single column of data. To do that, we can navigate the column data rather like a Python Class. Let's create a new object, names, and grab just the names column by stating df4.names. This command tells Pandas to grab the "names" column. Note, this is case sensitive. After we grab it, let's print it off too.

# COMMAND ----------
names = df4.names

# COMMAND ----------
print (names)

# COMMAND ----------
# MAGIC %md
# MAGIC Notice that we have a lot of data here about our names. We have their index (left column of integers). At the bottom, we have the type of data that it is. Don't worry about this extra data at the bottom for now. Let's try and grab the ages column now.

# COMMAND ----------
ages = df4.ages

# COMMAND ----------
ages

# COMMAND ----------
# MAGIC %md
# MAGIC ## How to Convert a Column to a List

# COMMAND ----------
# MAGIC %md
# MAGIC When you are working with a DataFame, you will often times need to work with that data not as a column, rather as a list. To do this, you will want to convert that data into a list. You can do this, by calling the method .tolist() after the data in question. Let's try it with ages and print off a list of ages.

# COMMAND ----------
ages_list = df4.ages.tolist()

# COMMAND ----------
print (ages_list)

# COMMAND ----------
# MAGIC %md
# MAGIC While this may not seem necessary on the surface, it is. One of the main reasons that this is essential is for processing large quantities of data. It is often times computationally less expensive to work with that data as a list or, better yet, as a NumPy array.

# COMMAND ----------
# MAGIC %md
# MAGIC ## How to Grab a Specific Row of a DataFrame

# COMMAND ----------
# MAGIC %md
# MAGIC It will often times be necessary to grab a DataFrame by row, not column. We have a lot of different ways to grab a row, but for now let's imagine we want to just grab a specific row by index. (We can grab all rows that have a certain value in a certain column also, but we will see that a bit later.) To grab a row by index, you can use the iloc command. This stands for Index Location. Index Location can be indexed rather like a list, as in the code below. The index you choose should correspond to the row index (starting with 0).

# COMMAND ----------
row1 = df4.iloc[1]

# COMMAND ----------
row1

# COMMAND ----------
