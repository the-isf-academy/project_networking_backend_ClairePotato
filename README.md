# Project Networking


> **Don't forget to edit this `README.md` file**
>
> If you're interested in how to format markdown, click [here](https://www.markdownguide.org/basic-syntax/#images-1)

## API Overview
- *how can people use it?*
This API can be used to search for biology concepts and to discuss them with other users.
- *who is it intended for?*
This API is intended for grade 10 IB biology students studying at ISF, but isn't limited to only ISF students.

### Model
My Biology model allows users to...
* post a biology concept
* view all biology concepts
* view one specific concept giving the ID
* find existing concepts by searching for related keywords
* archive concepts that they want to go back to
* view all archived concepts
* mark a concept as confused
* view all concepts in order of most to least confused
* ask and answer questions about each concept

### Endpoints
| Endpoint | Get/Post | Description | Arguments|
| :---| :---  | :---| :---|
| /new | Post | post a new concept | concept (str), related_keywords (str), discussion (str)
| /all | Get | returns all concepts in a JSON format | -
| /one | Get | returns one concept based on given ID | ID (int)
| /archive | Post | archives a single concept | ID (int)
| /all_archive | Get | returns all concepts that are archived | -
| /search | Get | returns all concepts containing the given keyword in any of the fileds | keyword (str)
| /confused | Post | allows user to mark a concept as 'confused' | ID (int)
| /confused_ranked | Get | returns a list of all concepts with only their 'confused' percentage ranked in order of most to least confusing | -
| /confused_ranked | Get | returns a list of all concepts with only their 'confused' percentage ranked in order of most to least confusing | -
| /add_to_discussion | Post | allows user to add or answer a question about the concept | ID (int), discussion (str)

---

## Setup

### Contents

Here's what is included:
- `\app`
    - `models.py` - `Fortune` model
    - `views.py` - endpoints
- `database.sqlite`  
- `README.md` 

**To start a Banjo server:** `banjo` 
- [Banjo Documentation](https://the-isf-academy.github.io/banjo_docs/)



