
# Proposed solution for the exercice

## Description

Make commits to a Git repository at sensible points during implementation.

- Create a Python script

- Add a function called 'get_df' that programmatically creates and returns a pandas DataFrame with the following specifications:

  - Columns 'a' and 'b' with 1000 rows.

  - Column 'a' contains random numbers in the range 0-100

  - Column 'b' contains the entries of column 'a' Modulo 10

- Start a Flask server when executing the script.

- Add a route "/data" and deliver the data from the DataFrame in JSON format.

- Add a route "/" and deliver there a HTML/JavaScript page that displays the following:

  - A bootstrap card with the title "This is the demo for JCB".

  - Within it, a Bootstrap Button with the words "Load Chart".

  - When the button is pressed, the data from '/data' is loaded asynchronously and an interactive plot (e.g. with Plotly) is rendered in the card with the values of column 'a' on the x-axis and 'b' on the y-axis.

- Upload the git repository to GitHub or send the repository to us

Optional: Use Vue.js / BootstrapVue / OpenAPI

## Implementation

The proposed solution was implemented using `flask` for the API and to serve the HTML/JavaScript files. I used the `flasgger` library to implement OpenAPI which can be accessed at the following URL [http://localhost:5000/apidocs](http://localhost:5000/apidocs).

The front-end is a SPA Vue.js app, it allows us to serve the files through the flask API and enable hot reload for development mode. It can be built for production so the server will just load the static files.

For the UI, I used [Bootstrap Vue](https://bootstrap-vue.org/).

I also used the [vue-plotly](https://github.com/David-Desmaisons/vue-plotly) library to generate the graph.

## Up & running

- Clone the GitHub repository

```bash
git clone https://github.com/JaviCT/testaufgabe.git
```

### Development

- Install font-end dependencies

```bash
cd client
yarn install or npm install
```

- Serve with hot reload at localhost:8080

```bash
yarn serve or npm serve
```

- Setup back-end

```bash
cd ../server
python3 -m venv venv
source venv/bin/activate
pip3 install -r requirements.txt
cd ..
```

- Serve back-end at localhost:5000

```bash
FLASK_ENV=development FLASK_APP=app.py flask run
```

### Production

- Install font-end dependencies

```bash
cd client
yarn install or npm install
```

- Build front-end for production

```bash
yarn build or npm build
```

- Setup back-end

```bash
cd ../server
python3 -m venv venv
source venv/bin/activate
pip3 install -r requirements.txt
cd ..
```

- Serve back-end at localhost:5000

```bash
FLASK_ENV=production FLASK_APP=app.py flask run
```
