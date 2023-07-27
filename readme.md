### Cracktechproject

A dynamic web-based platform that allows users to manage profiles and interact with various questions.

## Pre-requisites:

- [Python 3](https://www.python.org/downloads/)
- [pip](https://pip.pypa.io/en/stable/installing/)
- [virtualenv](https://virtualenv.pypa.io/en/latest/installation.html) (Recommended)

## Quick Start:

### 1. Clone the repository:

```bash
git clone https://github.com/mominfaruk/Cracktechproject.git
cd cracktechproject
```


### 2. (Recommended) Set up a virtual environment:

This helps in isolating the project dependencies.

<pre><div class="bg-black rounded-md mb-4"><div class="flex items-center relative text-gray-200 bg-gray-800 px-4 py-2 text-xs font-sans justify-between rounded-t-md"><span>bash</span></div></div></pre>

<pre><div class="bg-black rounded-md mb-4"><div class="p-4 overflow-y-auto"><code class="!whitespace-pre hljs language-bash">virtualenv venv
source venv/bin/activate  # On Windows, use: `venv\Scripts\activate`
</code></div></div></pre>

### 3. Install project dependencies:

<pre><div class="bg-black rounded-md mb-4"><div class="flex items-center relative text-gray-200 bg-gray-800 px-4 py-2 text-xs font-sans justify-between rounded-t-md"><span>bash</span></div></div></pre>

<pre><div class="bg-black rounded-md mb-4"><div class="p-4 overflow-y-auto"><code class="!whitespace-pre hljs language-bash">pip install -r requirements.txt
</code></div></div></pre>

### 4. Run migrations:

This step sets up the database schema based on the project models.

<pre><div class="bg-black rounded-md mb-4"><div class="flex items-center relative text-gray-200 bg-gray-800 px-4 py-2 text-xs font-sans justify-between rounded-t-md"><span>bash</span></div></div></pre>

<pre><div class="bg-black rounded-md mb-4"><div class="p-4 overflow-y-auto"><code class="!whitespace-pre hljs language-bash">python manage.py migrate
</code></div></div></pre>

### 5. Start the development server:

<pre><div class="bg-black rounded-md mb-4"><div class="flex items-center relative text-gray-200 bg-gray-800 px-4 py-2 text-xs font-sans justify-between rounded-t-md"><span>bash</span></div></div></pre>

<pre><div class="bg-black rounded-md mb-4"><div class="p-4 overflow-y-auto"><code class="!whitespace-pre hljs language-bash">python manage.py runserver
</code></div></div></pre>

Now, the application should be accessible at: [http://127.0.0.1:8000/](http://127.0.0.1:8000/).

## Populating the Database:

For initial data setup, you can utilize the Django admin panel:

1. run python manage.py generate_data
2. Access the Django admin site by navigating to [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/) and log in using the admin credentials.Through the admin dashboard, you can manage (add/edit) records for User, Question, FavoriteQuestion, and ReadQuestion.

## Running Tests:

Ensure all functionalities are working as expected:

<pre><div class="bg-black rounded-md mb-4"><div class="flex items-center relative text-gray-200 bg-gray-800 px-4 py-2 text-xs font-sans justify-between rounded-t-md"><span>bash</span></div></div></pre>

<pre><div class="bg-black rounded-md mb-4"><div class="p-4 overflow-y-auto"><code class="!whitespace-pre hljs language-bash">python manage.py test functionality
</code></div></div></pre>

This will execute tests from the `functionality` app and output the results.
